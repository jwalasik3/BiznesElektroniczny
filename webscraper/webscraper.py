import time
import re
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import requests
import pandas as pd
import concurrent.futures
import shutil

"""
Instrukcja obsługi xd:
1. Wszystkie zdjecia zapisuja sie bezposrednio w all_images, zeby latwiej sie kopiowalo
2. Zdjecia sa rowniez ladnie zapisane w folderach w folderze images
3. Jesli masz dobry internet, to ustaw wiecej watkow w kodzie nizej, zeby szybciej dzialalo

"""
base_img_url = 'http://localhost:8080/img/p/'
"""
Do zmiennej powyzej wpisz sciezke do zdjec, z ktorej presta bedzie kopiowac zdjecia w czasie importu
"""


products_df = pd.DataFrame(columns=['Name', 'Categories', 'Price', 'Long desc', 'Short desc', 'Image URLs'])
all_images_dir = 'all_images'
os.makedirs(all_images_dir, exist_ok=True)

def make_valid_directory_name(input_string):
    valid_name = input_string.replace(' ', '')
    valid_name = re.sub(r'[-–<>:_+"/\\|?*]', '', valid_name)
    valid_name = valid_name.strip()

    return valid_name

# Function to download a single image with retries and timeout settings
def download_single_image(img_url, img_path, retries=10, timeout=15):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for attempt in range(retries):
        try:
            response = requests.get(img_url, headers=headers, stream=True, timeout=timeout)
            if response.status_code == 200:
                try:
                    with open(img_path, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    shutil.copy(img_path, all_images_dir)
                    return
                except FileNotFoundError as e:
                    print(f"File not found error: {e}")
                except PermissionError as e:
                    print(f"Permission error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
            else:
                print(f"Failed to download {img_url}, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {img_url}: {e}")
            time.sleep(2)
    print(f"Failed to download {img_url} after {retries} attempts")

# Function to download multiple images concurrently
def download_images(images, imgs_dir, product_name):
    image_urls = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i, img in enumerate(images):
            img_url = img.get_attribute('src')
            img_name = f'{make_valid_directory_name(product_name)}_{i + 1}.jpg'
            img_path = os.path.join(imgs_dir, img_name)
            image_urls.append(base_img_url  + img_name)
            futures.append(executor.submit(download_single_image, img_url, img_path))
        concurrent.futures.wait(futures)
    return image_urls

def scrape_images(images_dir, driver, product_name):
    big_imgs_dir = os.path.join(images_dir, 'full_size')
    os.makedirs(big_imgs_dir, exist_ok=True)
    big_img_urls = []
    min_img_urls = []
    if product_name == 'Themed Crochet Kit Bundle – Dinosaur + Cactus + Whale Beginner Crochet Kits':
        print('sprawdzmy to !')
    try:
        images = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'figure'))
        ).find_elements(By.TAG_NAME, 'img')

        if not images:
            print(f"No images found for {images_dir}")
            raise RuntimeError(f"Failed to find images for {images_dir}")
        else:
            big_img_urls = download_images(images, big_imgs_dir, product_name)

    except Exception:
        print(f"No images found for {images_dir}")
        raise RuntimeError(f"Failed to find images for {images_dir}")

    """try:
        WebDriverWait(driver, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//ol[@class="flex-control-nav flex-control-thumbs"]//img'))
        )

        min_imgs_dir = os.path.join(images_dir, 'miniatures')
        os.makedirs(min_imgs_dir, exist_ok=True)

        miniatures = driver.find_elements(By.XPATH, '//ol[@class="flex-control-nav flex-control-thumbs"]//img')
        if miniatures:
            min_img_urls = download_images(miniatures, min_imgs_dir, product_name + 'mini')
    except TimeoutException:
        pass"""

    if not os.listdir(big_imgs_dir):
        print(f"Warning: {images_dir} is empty after scraping. product name: {product_name}")
        raise RuntimeError(f"No images downloaded for {images_dir}")

    return big_img_urls + min_img_urls



def scrape_data(product_name, driver):
    try:
        price = driver.find_element(By.XPATH, '//div[@class="product-title-container"]/p/span/bdi').text
        price = float(price.replace("$", ""))
    except NoSuchElementException:
        try:
            price = driver.find_element(By.XPATH, '//div[@id="open-atc-options"]/span[last()]').text.strip()
            price = float(price.replace("$", ""))
        except NoSuchElementException:
            price = None

    try:
        description1 = driver.find_element(By.XPATH, '//div[@class="woocommerce-product-details__short-description"]').text.rstrip('/n')
    except NoSuchElementException:
        try:
            description1 = driver.find_element(By.XPATH, '//div[@class="product-long-desc"]').text.rstrip('/n')
        except NoSuchElementException:
            description1 = None
    try:
        description2 = driver.find_element(By.ID, "tab-description").text.rstrip('/n')
    except NoSuchElementException:
        description2 = None

    product_data = {'Name': product_name,
                    'Price': price,
                    'Long desc': description1,
                    'Short desc': description2 }

    return product_data

def scrape_product_page(url, product_dir, driver, product_name, category_name):
    try:
        driver.get(url)
        os.makedirs(product_dir, exist_ok=True)
        img_urls = scrape_images(product_dir, driver, product_name)
        product_data = scrape_data(product_name, driver)
        product_data['Image URLs'] = "|".join(img_urls)
        product_data['Categories'] = category_name
        products_df.loc[len(products_df)] = product_data
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def scrape_products_from_current_page(driver, images_dir, category_name):
    products = driver.find_elements(By.XPATH,
                                    '//ul[@class="shop-item-list"]//li[@class="shop-item"]//a[@class="product-title"]')
    product_names = []
    dir_names = []
    product_urls = []
    for product in products:
        product_name = product.find_element(By.TAG_NAME, 'p').text
        product_names.append(product_name)
        product_urls.append(product.get_attribute('href'))
        dir_names.append(make_valid_directory_name(product_name))

    for i, url in enumerate(product_urls):
        product_dir = os.path.join(images_dir, dir_names[i])
        scrape_product_page(url, product_dir, driver, product_names[i], category_name)

def scrape_single_page(page_url, images_dir, category_name):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(page_url)
        scrape_products_from_current_page(driver, images_dir, category_name)
    except Exception as e:
        print(f"Error scraping {page_url}: {e}")
    finally:
        driver.quit()

def scrape_all_pages_concurrently(page_urls, images_dir, category_name):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: # set 3 with poor internet
        futures = []
        for page_url in page_urls:
            futures.append(executor.submit(scrape_single_page, page_url, images_dir, category_name))
        concurrent.futures.wait(futures)

def scrape_one_category(category_url, category_dir_name, category_name):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(category_url)

    page_urls = []
    while True:
        try:
            # Add current page URL to the list
            page_urls.append(driver.current_url)

            # Find the "Next" button and get the next page URL
            next_page = driver.find_element(By.XPATH, '//a[@class="next page-numbers"]')
            next_page_url = next_page.get_attribute("href")

            # Navigate to the next page
            driver.get(next_page_url)
        except Exception:
            if len(page_urls) == 1:
                scrape_products_from_current_page(driver, category_dir_name, category_name)
            break  # No more pages, stop gathering URLs

    driver.quit()

    if len(page_urls) > 1:
        scrape_all_pages_concurrently(page_urls, category_dir_name, category_name)

def scrape_categories(images_dir):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://clubcrochet.com/shop/category/kits/")

    categories = driver.find_elements(By.XPATH, '//ul[@id="menu-1-be8201d"]/li/a')
    category_urls = []
    category_names = []

    for category in categories:
        category_urls.append(category.get_attribute('href'))
        category_names.append(category.text)

    driver.quit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor: # set 1 with poor internet
        futures = []
        for i, url in enumerate(category_urls):
            category_dir_name = os.path.join(images_dir,make_valid_directory_name(category_names[i]))
            os.makedirs(category_dir_name, exist_ok=True)
            futures.append(executor.submit(scrape_one_category, category_urls[i], category_dir_name, category_names[i]))
        concurrent.futures.wait(futures)

start_time = time.time()

images_dir = 'images'
os.makedirs(images_dir, exist_ok=True)

scrape_categories(images_dir)

print(products_df)
products_df.to_csv('product_data_scraped.csv', sep=';', index=True, index_label='ID')

end_time = time.time()
print("Execution time: ", end_time - start_time)








