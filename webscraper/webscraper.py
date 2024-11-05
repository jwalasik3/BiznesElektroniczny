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

products_df = pd.DataFrame(columns=['name', 'price', 'description1', 'description2'])

def make_valid_directory_name(input_string):
    valid_name = input_string.replace(' ', '_')
    valid_name = re.sub(r'[<>:"/\\|?*]', '', valid_name)
    valid_name = valid_name.strip()

    return valid_name

# Function to download a single image with retries and timeout settings
def download_single_image(img_url, img_path, retries=10, timeout=15):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for attempt in range(retries):
        try:
            response = requests.get(img_url, headers=headers, stream=True, timeout=timeout)
            if response.status_code == 200:
                with open(img_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                return
            else:
                print(f"Failed to download {img_url}, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {img_url}: {e}")
            time.sleep(2)
    print(f"Failed to download {img_url} after {retries} attempts")

# Function to download multiple images concurrently
def download_images(images, imgs_dir):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i, img in enumerate(images):
            img_url = img.get_attribute('src')
            img_name = f'image_{i + 1}.jpg'
            img_path = os.path.join(imgs_dir, img_name)
            futures.append(executor.submit(download_single_image, img_url, img_path))
        concurrent.futures.wait(futures)

def scrape_images(images_dir, driver):
    big_imgs_dir = os.path.join(images_dir, 'full_size')
    os.makedirs(big_imgs_dir, exist_ok=True)

    try:
        images = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'figure'))
        ).find_elements(By.TAG_NAME, 'img')

        if not images:
            print(f"No images found for {images_dir}")
            raise RuntimeError(f"Failed to find images for {images_dir}")
        else:
            download_images(images, big_imgs_dir)

    except Exception:
        print(f"No images found for {images_dir}")
        raise RuntimeError(f"Failed to find images for {images_dir}")

    try:
        WebDriverWait(driver, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//ol[@class="flex-control-nav flex-control-thumbs"]//img'))
        )

        min_imgs_dir = os.path.join(images_dir, 'miniatures')
        os.makedirs(min_imgs_dir, exist_ok=True)

        miniatures = driver.find_elements(By.XPATH, '//ol[@class="flex-control-nav flex-control-thumbs"]//img')
        if miniatures:
            download_images(miniatures, min_imgs_dir)
    except TimeoutException:
        pass

    if not os.listdir(big_imgs_dir):
        print(f"Warning: {images_dir} is empty after scraping.")
        raise RuntimeError(f"No images downloaded for {images_dir}")

def scrape_data(product_name, driver):
    try:
        price = driver.find_element(By.XPATH, '//div[@class="product-title-container"]/p/span/bdi').text
    except NoSuchElementException:
        try:
            price = driver.find_element(By.XPATH, '//div[@id="open-atc-options"]/span[last()]').text.strip()
        except NoSuchElementException:
            price = None

    try:
        description1 = driver.find_element(By.XPATH, '//div[@class="woocommerce-product-details__short-description"]').text
    except NoSuchElementException:
        try:
            description1 = driver.find_element(By.XPATH, '//div[@class="product-long-desc"]').text
        except NoSuchElementException:
            description1 = None
    try:
        description2 = driver.find_element(By.ID, "tab-description").text
    except NoSuchElementException:
        description2 = None

    products_df.loc[len(products_df)] = {'name': product_name,
                                         'price': price,
                                         'description1': description1,
                                         'description2': description2 }


def scrape_product_page(url, product_dir, driver, product_name):
    try:
        driver.get(url)
        os.makedirs(product_dir, exist_ok=True)
        scrape_images(product_dir, driver)
        scrape_data(product_name, driver)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def scrape_products_from_current_page(driver, images_dir):
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
        scrape_product_page(url, product_dir, driver, product_names[i])

def scrape_single_page(page_url, images_dir):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(page_url)
        scrape_products_from_current_page(driver, images_dir)
    except Exception as e:
        print(f"Error scraping {page_url}: {e}")
    finally:
        driver.quit()

def scrape_all_pages_concurrently(page_urls, images_dir):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor: # set 3 with poor internet
        futures = []
        for page_url in page_urls:
            futures.append(executor.submit(scrape_single_page, page_url, images_dir))
        concurrent.futures.wait(futures)

def scrape_one_category(category_url, category_dir_name):
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
                scrape_products_from_current_page(driver, category_dir_name)
            break  # No more pages, stop gathering URLs

    driver.quit()

    if len(page_urls) > 1:
        scrape_all_pages_concurrently(page_urls, category_dir_name)

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

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: # set 1 with poor internet
        futures = []
        for i, url in enumerate(category_urls):
            category_dir_name = os.path.join(images_dir,make_valid_directory_name(category_names[i]))
            os.makedirs(category_dir_name, exist_ok=True)
            futures.append(executor.submit(scrape_one_category, category_urls[i], category_dir_name))
        concurrent.futures.wait(futures)

start_time = time.time()

images_dir = 'images'
os.makedirs(images_dir, exist_ok=True)

scrape_categories(images_dir)
print(products_df)
products_df.to_csv('product_data_scraped.csv')

end_time = time.time()
print("Execution time: ", end_time - start_time)








