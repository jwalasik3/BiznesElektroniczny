#from deep_translator import GoogleTranslator
import random
from xml.sax import saxutils

import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import os
import base64
import csv

API_URL = "http://localhost:8080/api/pl/"
API_URL_NO_PL = "http://localhost:8080/api/"
API_URL_STOCK = 'http://localhost:8080/api/stock_availables'
API_URL_IMAGES = "http://localhost:8080/api/images/products/"
WEBSERVICE_TOKEN ='KZSAFGYV2D78Z5UQSQSW6PEA2ZU9HLWM'

class Product:
    def __init__(self, id, name, category, price, long_desc, short_desc, image_urls, 
                 polish_name, polish_category, polish_long_desc, polish_short_desc):
        self.id = id
        self.name = name
        self.category = category  
        self.price = price
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.image_urls = image_urls
        self.polish_name = polish_name
        self.polish_category = polish_category
        self.polish_long_desc = polish_long_desc
        self.polish_short_desc = polish_short_desc


    def __repr__(self):
        return (f"Produkt(ID={self.id}, Name={self.name}, Categories={self.category}, "
                f"Long Description={self.long_desc}, Short Description={self.short_desc}, "
                f"Image URL={self.image_urls})")

def convert_price(price):
    try:
        return float(price) if price else 0  # Konwertuj na float, jeśli cena istnieje
    except ValueError:
         return 0

def get_category_name(category_id, lang_id=2):
    try:
        url = f"{API_URL_NO_PL}/categories/{category_id}"
        response = requests.get(url, auth=HTTPBasicAuth(WEBSERVICE_TOKEN, ""), verify=False)
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            for language in root.findall(".//category/name/language"):
                if int(language.get("id")) == lang_id:
                    print("weszlo")
                    text = language.text
                    if text == "Prezenty":
                        text = 'Gifts'
                    elif text == 'Gadżety':
                        text = 'Merch'
                    elif text == "Materiały":
                        text = "Materials"
                    elif text == 'Zestawy':
                        text = 'Crochet Kits'
                    elif text == "Zbiory Wzorów":
                        text = "Pattern Bundles"
                    elif text == 'Wzory':
                        text = 'Crochet Patterns'
                    elif text == "Zestawy Sezonowe":
                        text = "Seasonal Kits"
                    elif text == 'Zestawy Zwykłe':
                        text = 'Regular Kits'
                    elif text == "Karty Podarunkowe":
                        text = "Gift Cards"
                    elif text == 'Inne Prezenty':
                        text = 'Other Gifts'
                    elif text == "Szydełka":
                        text = "Needles"
                    elif text == 'Włóczka':
                        text = 'Yarn'
                    elif text == "Duże zbiory":
                        text = "Big Bundles"
                    elif text == "Zwykłe zbiory":
                        text = "Regular Bundles"
                    elif text == 'Przypinki':
                        text = 'Pins'
                    elif text == "Koszulki":
                        text = "T-Shirts"
                    elif text == 'Wzory Sezonowe':
                        text = 'Seasonal Patterns'
                    elif text == "Zwykłe Wzory":
                        text = "Regular Patterns"
                    return text
        else:
            print(response.status_code)
    except Exception as e:
        print(e)
        return None

def get_categories_tuples(API_TOKEN):
    response = requests.get(API_URL_NO_PL + "categories", auth=HTTPBasicAuth(API_TOKEN, ''), verify=False)
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        ids = [category.get('id') for category in root.findall('.//category')]
        categories = {get_category_name(id): id for id in ids }
        return categories
    else:
        print(f"Failed to retrieve categories: {response.status_code}")    

def find_images(name):
    images_directory = "all_images"
    image_name = name.replace(" ", "")
    image_name = image_name.replace("-", "")
    image_name = image_name.replace(":", "")
    image_name = image_name.replace("–", "")
    images = []
    if not os.path.exists(images_directory):
        print("No such path")
        return []
    for file in os.listdir(images_directory):
        if image_name in file:
            images.append(file)
    return images

def determine_subcategory(produkt):
    subcategory_name = '0'
    rand_category = random.randint(0,1)
    if (produkt.category == 'Crochet Patterns'):
        if rand_category == 0:
            subcategory_name = "Seasonal Patterns"
        else:
            subcategory_name = "Regular Patterns"
    elif (produkt.category == 'Crochet Kits'):
        if "Seasonal" in produkt.name:
            subcategory_name = "Seasonal Kits"
        else: 
            subcategory_name = "Regular Kits"
    elif (produkt.category == 'Pattern Bundles'):
        if len(produkt.name) > 37:
            subcategory_name = "Big Bundle"
        else: 
            subcategory_name = "Regular Bundle"
    elif (produkt.category == 'Merch'):
        if "Pin" in produkt.name:
            subcategory_name = "Pins"
        else:
            subcategory_name = "T-Shirts"
    elif (produkt.category == 'Gifts'):
        subcategory_name = "Gift Cards"
    elif (produkt.category == 'Materials'):
        if "Yarn" in produkt.name:
            subcategory_name = "Yarn"
        else:
            subcategory_name = "Needle"
    return subcategory_name

def determine_weight(produkt):
    weight = '0'
    if produkt.category == 'Crochet Kits':
        weight = '20'
    elif produkt.category == 'Crochet Patterns':
        weight = '1'
    elif produkt.category == 'Pattern Bundles':
        weight = '5'
    elif produkt.category == 'Gifts':
        weight = '1'
    elif produkt.category == 'Materials':
        weight = '3'
    elif produkt.category == 'Merch':
        weight = '5'
    return weight

def remove_special_symbols(text):
    text = text.replace("—", "-")
    text = text.replace("–", '-')
    text = text.replace("’", '\'')
    text = text.replace("•", '-')
    text = text.replace("″", '\"')
    text = text.replace("”", '\"')
    text = text.replace("‘", '\'')
    text = text.replace("²", '^2')
    text = text.replace("“", '\"')
    text = text.replace("|", '|')
    text = text.replace("…", "...")
    text = text.replace("é", "e")
    return text

def replace_polish_symbols_with_unicode(text):
    text = text.replace("ą", "&#x0105;")
    text = text.replace("ę", "&#x0119;")
    text = text.replace("ł", "&#x0142;")
    text = text.replace("ń", "&#x0144;")
    text = text.replace("ś", "&#x015b;")
    text = text.replace("ż", "&#x017c;")
    text = text.replace("ź", "&#x017a;")
    text = text.replace("ć", "&#x0107;")
    text = text.replace("ó", "&#x00f3;")
    text = text.replace("Ą", "&#260;")
    text = text.replace("Ę", "&#280;")
    text = text.replace("Ł", "&#321;")
    text = text.replace("Ń", "&#323;")
    text = text.replace("Ś", "&#346;")
    text = text.replace("Ż", "&#379;")
    text = text.replace("Ź", "&#377;")
    text = text.replace("Ć", "&#262;")
    text = text.replace("Ó", "&#211;")
    return text

def upload_product(produkt, categories_tuple, lang="1"):
    
    prestashop = ET.Element("prestashop", {"xmlns:xlink": "http://www.w3.org/1999/xlink"})
    new_product = ET.SubElement(prestashop, "product")
    name_elem = ET.SubElement(new_product, "name")
    
    # corrected_name = remove_special_symbols(produkt.polish_name)
    corrected_name = saxutils.escape(produkt.polish_name)
    #translated_name = GoogleTranslator(source='auto', target='pl').translate(corrected_name)
    # corrected_name = replace_polish_symbols_with_unicode(corrected_name)

    name_elem.text =  f"<![CDATA[{corrected_name }]]>"
    #name_lang = ET.SubElement(name_elem, "language", {"id": "2"})
    #name_lang.text =  f"<![CDATA[{corrected_name }]]>"
    ET.SubElement(new_product, "price").text = str(produkt.price)

    weight = determine_weight(produkt)
    
    ET.SubElement(new_product, "weight").text = weight

    description_elem = ET.SubElement(new_product, "description")
    corrected_description = saxutils.escape(produkt.polish_long_desc + produkt.polish_short_desc)
    # corrected_description = replace_polish_symbols_with_unicode(corrected_description)
    description_elem.text = "<![CDATA[" + (corrected_description) + "]]>"

    associations = ET.SubElement(new_product, "associations")
    categories = ET.SubElement(associations, "categories")
    category = ET.SubElement(categories, "category")
    ET.SubElement(category, "id").text = str(categories_tuple.get(produkt.category))

    home_category = ET.SubElement(categories, "category")
    ET.SubElement(home_category, "id").text = str("2")

    subcategory = determine_subcategory(produkt)
    if subcategory != 0:
        subcategory_elem = ET.SubElement(categories, "category")
        ET.SubElement(subcategory_elem, "id").text = str(categories_tuple.get(subcategory))

    ET.SubElement(new_product, "active").text = "1"
    ET.SubElement(new_product, "visibility").text = "both"
    ET.SubElement(new_product, "state").text = "1"
    ET.SubElement(new_product, "available_for_order").text = "1"
    ET.SubElement(new_product, "minimal_quantity").text = "1"

    reference = produkt.name.replace(" ", "")
    reference = reference.replace("—", "-")
    reference = reference.replace("-", "")
    reference = reference.replace(":", "")
    reference = reference.replace("–", "")
    reference = reference.replace("’", '')
    ET.SubElement(new_product, "reference").text =  (f"<![CDATA[{reference}]]>")

    ET.SubElement(new_product, "id_tax_rules_group").text = "53"
    ET.SubElement(new_product, "indexed").text = "1"
    ET.SubElement(new_product, "product_type").text = "standard"
    ET.SubElement(new_product, "type").text = "1"
    ET.SubElement(new_product, "show_price").text = "1"

    #prestashop = replace_polish_symbols_with_unicode(prestashop)
    finished_product = ET.tostring(prestashop, encoding="utf-8", method="xml").decode("utf-8")
    finished_product = finished_product.replace("&lt;![CDATA[", "<![CDATA[").replace("]]&gt;", "]]>")
    #finished_product = finished_product.replace("amp;", "")
    finished_product = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + finished_product
    # print(finished_product)

    encoded_key = base64.b64encode(f"{WEBSERVICE_TOKEN}:".encode()).decode()

    headers = {
        'Authorization': f'Basic {encoded_key}',
        'Content-Type': 'application/xml; charset=utf-8'
    }
    response = requests.post(API_URL + "/?url=products", headers=headers, data=finished_product, verify=False)

    if response.status_code == 201:
        root = ET.fromstring(response.text)
        product_id = root.find('.//id').text
        print("Produkt added.")
        change_product_stock(WEBSERVICE_TOKEN, product_id)
        images_list = find_images(produkt.name)
        upload_images_from_list(product_id, images_list, images_directory = "all_images")
        
    else:
       print(f"{response.status_code} - {response.text}")
       print("Header Request:", response.request.headers)
       print("Produkt sent:", finished_product)


def upload_images_from_list(product_id, images_list, images_directory):
    endpoint = f"{API_URL_IMAGES}{product_id}"
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{WEBSERVICE_TOKEN}:".encode()).decode()}'
    }

    for idx, image in enumerate(images_list):
        path_to_image = os.path.join(images_directory, image)
        try:
            print(f"Uploading image: {path_to_image}")  # Debugging info
            with open(path_to_image, 'rb') as image_file:
                # Set cover for the first image
                is_cover = "?cover=1" if idx == 0 else ""
                full_endpoint = endpoint + is_cover

                files = {
                    'image': (image, image_file, 'image/jpeg')
                }
                response = requests.post(full_endpoint, headers=headers, files=files, verify=False)

            if response.status_code < 300:
                print(f"Uploaded Image: {image}")
            else:
                print(f"Upload Failure: {response.status_code} - {response.text}")

        except FileNotFoundError:
            print(f"File not found: {path_to_image}")
        except Exception as e:
            print(f"Error uploading image: {e}")


def change_product_stock(api_key, product_id):
    encoded_key = base64.b64encode(api_key.encode()).decode()
    headers = {
        'Authorization': f'Basic {encoded_key}',
        'Content-Type': 'application/xml'
    }

    stock_url = API_URL_STOCK
    new_quantity = random.randint(0, 10)
    params = {
        "filter[id_product]": product_id,
        "display": "full"
    }
    response = requests.get(stock_url, params=params, auth=(api_key, ''), verify=False)

    if response.status_code != 200:
        raise Exception(f"{response.status_code}, {response.text}")

    root = ET.fromstring(response.content)
    stock_id = root.find(".//stock_available/id").text
    id_shop = root.find(".//stock_available/id_shop").text
    id_product_attribute = root.find(".//stock_available/id_product_attribute").text
    id_shop_group = root.find(".//stock_available/id_shop_group").text
    depends_on_stock = root.find(".//stock_available/depends_on_stock").text
    location = root.find(".//stock_available/location").text
    if not stock_id:
        raise Exception(f"Nie znaleziono stock_available dla produktu o ID {product_id}")


    update_url = f"{stock_url}/{stock_id}"

    prestashop = ET.Element("prestashop", {"xmlns:xlink": "http://www.w3.org/1999/xlink"})
    stock_available = ET.SubElement(prestashop, "stock_available")
    ET.SubElement(stock_available, "id").text = str(stock_id)
    ET.SubElement(stock_available, "id_product").text = str(product_id)
    ET.SubElement(stock_available, "id_product_attribute").text = str(id_product_attribute)
    ET.SubElement(stock_available, "id_shop").text = str(id_shop)
    ET.SubElement(stock_available, "quantity").text = str(new_quantity)
    ET.SubElement(stock_available, "id_shop_group").text = str(id_shop_group)
    ET.SubElement(stock_available, "depends_on_stock").text = str(depends_on_stock)
    ET.SubElement(stock_available, "out_of_stock").text = "0"
    ET.SubElement(stock_available, "location").text = str(location)

    update_data = ET.tostring(prestashop, encoding="utf-8", method="xml").decode("utf-8")

    update_response = requests.put(update_url, headers=headers, data=update_data, auth=(api_key, ''), verify=False)

    if update_response.status_code not in [200, 204]:
        raise Exception(
            f" {update_response.status_code}, {update_response.text}")

    return {"status": "success", "stock_id": stock_id, "new_quantity": new_quantity}

def load_products_from_csv(nazwa_pliku):
    products = []
    with open(nazwa_pliku, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Ustawienie separatora na średnik
        for row in reader:
            product = Product(
            id=row['ID'],
            name=row['Name'],
            category=row['Categories'],  # Rozdzielanie kategorii
            price=convert_price(row['Price']),  # Cena jako liczba zmiennoprzecinkowa
            long_desc=row['Long desc'],
            short_desc=row['Short desc'],
            image_urls=row['Image URLs'].split('|'),  # Rozdzielenie wielu URL-i obrazów. Nie wykorzystywane
            polish_name=row['polish_Name'],
            polish_category=row['polish_Categories'],
            polish_long_desc=row['polish_Long desc'],
            polish_short_desc=row['polish_Short desc']
            )
            products.append(product)
    return products


categories = get_categories_tuples(WEBSERVICE_TOKEN)
print(categories)
file_csv = "product_data_scraped_translated.csv"

produkty = load_products_from_csv(file_csv)
for produkt in produkty:
    #print(produkt.category)
    #print(categories.get(produkt.category))
    upload_product(produkt, categories)