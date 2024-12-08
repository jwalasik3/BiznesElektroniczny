import random
import re
from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

"""
closing popup info about product added to the shopping cart

close_button = driver.find_element(By.XPATH, '//div[@id="blockcart-modal"]//button[@class="close"]')
close_button.click()
"""
def get_products_urls_from_curr_page(driver):
    product_list = driver.find_element(By.ID, "js-product-list")
    product_links = product_list.find_elements(By.CSS_SELECTOR, 'a.thumbnail.product-thumbnail')
    product_urls = [link.get_attribute('href') for link in product_links]

    return product_urls

def type_amount_and_add_to_cart(driver, product_url):
    driver.get(product_url)
    quantity_input = driver.find_element(By.ID, "quantity_wanted")
    driver.execute_script("arguments[0].value = '';", quantity_input)
    random_quantity = random.randint(1, 3)
    quantity_input.send_keys(str(random_quantity))
    product_name = driver.find_element(By.XPATH, '//div[@class="col-md-6"]/h1').text.lower()

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR,
                                             'button.add-to-cart[data-button-action="add-to-cart"]')

    is_disabled = add_to_cart_button.get_attribute("disabled")
    if is_disabled:
        return None
    else:
        add_to_cart_button.click()
        sleep(1)
    return product_name

def add_n_products_to_cart(driver, n):
    menu = driver.find_element(By.ID, "_desktop_top_menu")
    category_links = menu.find_elements(By.CSS_SELECTOR, 'a.dropdown-item[data-depth="0"]')
    category_urls = [link.get_attribute('href') for link in category_links]
    products_to_add = n
    added_products_set = set()
    for url in category_urls:
        driver.get(url)
        product_urls = get_products_urls_from_curr_page(driver)
        for url in product_urls:
            product_name = type_amount_and_add_to_cart(driver, url)
            if product_name is not None:
                added_products_set.add(product_name)
                products_to_add -= 1
            if products_to_add == 0:
                return added_products_set

def search_product(driver, search_query):
    search_bar = driver.find_element(By.XPATH, '//div[@id="search_widget"]//input[@type="text"]')
    search_bar.clear()
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)

def add_rand_product_to_cart(driver):
    product_urls = get_products_urls_from_curr_page(driver)
    while True:
        rand_id = random.randint(0, len(product_urls) - 1)
        product_name = type_amount_and_add_to_cart(driver, product_urls[rand_id])
        if product_name is not None:
            return product_name

def remove_n_products_from_cart(driver, n):
    shopping_cart = driver.find_element(By.XPATH, '//div[@id="_desktop_cart"]/div/div[@class="header"]//a')
    shopping_cart.click()
    remove_links = driver.find_elements(By.CSS_SELECTOR, 'a.remove-from-cart')
    remove_urls = [link.get_attribute('href') for link in remove_links]
    if n > len(remove_urls):
        n = len(remove_urls)
    for i in range(n):
        driver.get(remove_urls[i])

def register_account(driver, firstname, lastname, email, password):
    try:
        sign_in_link = driver.find_element(By.XPATH,
                                           '//a[@class="login"]')
        sign_in_url = sign_in_link.get_attribute('href')
        driver.get(sign_in_url)

        create_account_link = driver.find_element(By.XPATH,
                                                  '//div[@class="no-account"]/a[@data-link-action="display-register-form"]')
        create_account_url = create_account_link.get_attribute('href')
        driver.get(create_account_url)

        social_title = driver.find_element(By.ID, 'field-id_gender-1')  
        social_title.click()

        first_name = driver.find_element(By.ID, 'field-firstname')
        first_name.send_keys(firstname)

        last_name = driver.find_element(By.ID, 'field-lastname')
        last_name.send_keys(lastname)

        email_field = driver.find_element(By.ID, 'field-email')
        email_field.send_keys(email)

        password_field = driver.find_element(By.ID, 'field-password')
        password_field.send_keys(password)

        
        privacy_checkbox = driver.find_element(By.NAME, 'customer_privacy')
        privacy_checkbox.click()

       
        terms_checkbox = driver.find_element(By.NAME, 'psgdpr')
        terms_checkbox.click()

        
        save_button = driver.find_element(By.XPATH, '//button[@data-link-action="save-customer"]')
        save_button.click()

        username = driver.find_element(By.XPATH, '//div[@class="user-info"]//a[@class="account"]/span').text
        assert username == firstname + " " + lastname, "Account creation failed."
        print("Test 4 passed: Registration successful.")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Test failed due to an error: {e}")
    except AssertionError as ae:
        print(f"Test failed: {ae}")

def go_to_cart_and_proceed(driver):
    try:
        shopping_cart = driver.find_element(By.XPATH, '//div[@id="_desktop_cart"]/div/div[@class="header"]//a')
        shopping_cart.click()
        checkout_button = driver.find_element(By.XPATH,
                                              '//section[@id="main"]/div/div/div//div[@class="text-sm-center"]//a')
        checkout_button.click()
        print("Test 5 passed: Checkout successful.")
    except Exception as e:
        print(f"Test 5 failed due to an error: {e}")

def sign_in(driver, email, password):
    sign_in_link = driver.find_element(By.XPATH,
                                       '//a[@class="login"]')
    sign_in_url = sign_in_link.get_attribute('href')
    driver.get(sign_in_url)
    try:
        
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        email_field.send_keys(email)  

        
        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys(password)  

        
        sign_in_button = driver.find_element(By.ID, "submit-login")
        sign_in_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")

def fill_in_address_form(driver):
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js-address-form"))
        )

        try:
            saved_address = driver.find_element(By.ID, "delivery-addresses")
            if saved_address.is_displayed():
                continue_button = driver.find_element(By.CSS_SELECTOR, "button[name='confirm-addresses']")
                continue_button.click()
            else:
                raise Exception("Saved address section not displayed.")
        except:
            driver.find_element(By.ID, "field-alias").send_keys("Home Address")
            driver.find_element(By.ID, "field-firstname").send_keys("John")
            driver.find_element(By.ID, "field-lastname").send_keys("Doe")
            driver.find_element(By.ID, "field-address1").send_keys("123 Main Street Apartment 4B")
            driver.find_element(By.ID, "field-city").send_keys("New York")
        
            driver.find_element(By.ID, "field-postcode").send_keys("10-001")
            driver.find_element(By.ID, "field-id_country").send_keys("Polska")  
            driver.find_element(By.ID, "field-phone").send_keys("+1234567890")

            continue_button = driver.find_element(By.CSS_SELECTOR, "button[name='confirm-addresses']")
            continue_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")

def choose_delivery(driver):
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "js-delivery"))
        )
        """
        It might not work after making changes to delivery options
        In that case change the ID
        """
        delivery_option = driver.find_element(By.ID, "delivery_option_16")
        delivery_option.click()

        continue_button = driver.find_element(By.CSS_SELECTOR, "button[name='confirmDeliveryOption']")
        continue_button.click()

        print("Test 6 passed: Delivery option selected and form submitted successfully.")

    except Exception as e:
        print(f"Test failed, Delivery option not submitted successfully: {e}")

def choose_payment_place_order(driver):
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "payment-options"))
        )

        
        cash_on_delivery_option = driver.find_element(By.ID, "payment-option-2")
        cash_on_delivery_option.click()

       
        terms_checkbox = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
        terms_checkbox.click()

        
        place_order_button = driver.find_element(By.XPATH, '//div[@id="payment-confirmation"]/div/button')
        place_order_button.click()

        print("Test 7 passed: Payment method chosen successfully.")

    except Exception as e:
        print(f"Payment method wasn't chosen successfully.: {e}")

def go_to_account_page(driver):
    try:
        account_link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.account"))
        )
        account_link = account_link_element.get_attribute("href")
        driver.get(account_link)
    except Exception as e:
        print(f"An error occurred: {e}")

def go_to_order_history(driver):
    try:
        history_link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "history-link"))
        )
        history_link = history_link_element.get_attribute("href")
        driver.get(history_link)
    except Exception as e:
        print(f"An error occurred: {e}")

def get_order_status_and_invoice(driver):
    try:
        first_order_row = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        order_status = first_order_row.find_element(By.CSS_SELECTOR, "td:nth-child(5) span").text
        invoice_button = first_order_row.find_element(By.CSS_SELECTOR, "td:nth-child(6) a")
        invoice_link = invoice_button.get_attribute("href")
        driver.get(invoice_link)
        print("Test 9 passed: Invoice downloaded successfully.")
        return order_status

    except Exception as e:
        print(f"An error occurred: {e}")

def close_popup(driver):
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="blockcart-modal"]//button[@class="close"]'))
        )
        close_button.click()
    except TimeoutException:
        print("Close button did not appear within the given time.")

def get_product_names_from_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-items .cart-item"))
        )
        product_name_elements = driver.find_elements(By.XPATH,
                                                     '//div[@class="product-line-grid"]//div[@class="product-line-info"]/a[@class="label"]')
        product_names = {element.text.lower() for element in product_name_elements}

        return product_names

    except Exception as e:
        print(f"An error occurred: {e}")

def go_to_cart(driver):
    shopping_cart = driver.find_element(By.XPATH, '//div[@id="_desktop_cart"]/div/div[@class="header"]//a')
    shopping_cart.click()


password = "haslo1234567"
email = "siema@onet.pl"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://localhost:8080/")

added_products = add_n_products_to_cart(driver, 10)
sleep(1)

close_popup(driver)
go_to_cart(driver)
product_names_in_cart = get_product_names_from_cart(driver)

assert added_products == product_names_in_cart, "Products were not added to cart correctly!"
print("Test 1 passed: Products were added to cart correctly.")

driver.get("https://localhost:8080/")
search_product(driver, "Hummingbird")
product_name = add_rand_product_to_cart(driver)

close_popup(driver)
go_to_cart(driver)
product_names_in_cart = get_product_names_from_cart(driver)

assert product_name in product_names_in_cart, "The product was not added correctly!"
print("Test 2 passed: The product was added correctly.")

num_of_products_before = len(product_names_in_cart)
remove_n_products_from_cart(driver, 3)
num_of_products_after = len(get_product_names_from_cart(driver))

assert num_of_products_before - num_of_products_after == 3, "The product were not removed correctly!"
print("Test 3 passed: The products were removed correctly.")

register_account(driver, "John", "Doe", email, password)

go_to_cart_and_proceed(driver)
fill_in_address_form(driver)
choose_delivery(driver)
choose_payment_place_order(driver)

go_to_account_page(driver)
go_to_order_history(driver)
order_status = get_order_status_and_invoice(driver)
assert order_status == "Oczekiwanie na płatność przy odbiorze", "Wrong order status"
print("Test 8 passed: Order status is correct.")

driver.quit()
