import random

import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import os
import base64
import csv

API_URL = "http://localhost:8080/api/"
WEBSERVICE_TOKEN ='KZSAFGYV2D78Z5UQSQSW6PEA2ZU9HLWM'

def load_categories_from_csv(nazwa_pliku):
    unique_categories = set()  
    with open(nazwa_pliku, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Ustawienie separatora na średnik 
        for row in reader:
            if 'Categories' in row:  
                kategorie = row['Categories'] 
                unique_categories.add(kategorie)
    return unique_categories

def upload_category(category, parents_id='2'):
    prestashop = ET.Element("prestashop", {"xmlns:xlink": "http://www.w3.org/1999/xlink"})
    new_category = ET.SubElement(prestashop, "category")
    id_parent = ET.SubElement(new_category, "id_parent")
    id_parent.text = parents_id
    ET.SubElement(new_category, "active").text = "1"
    name_elem = ET.SubElement(new_category, "name")
    lang = "2"
    name_lang = ET.SubElement(name_elem, "language", {"id":lang})
    name_lang.text = str(category)
    link_rewrite = str(category.lower())
    link_rewrite = link_rewrite.replace(" ", "-")
    link_rewrite_elem = ET.SubElement(new_category, "link_rewrite")
    link_rewrite_lang = ET.SubElement(link_rewrite_elem, "language", {"id":"1"})
    link_rewrite_lang.text = link_rewrite
    
    finished_category = ET.tostring(prestashop, encoding="utf-8", method="xml").decode("utf-8")
    print(finished_category)

    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.post(API_URL + "/categories", headers=headers, auth=(WEBSERVICE_TOKEN, ''), data=finished_category, verify=False)
    if response.status_code == 201:
        print("Kategoria została utworzona pomyślnie.")
    else:
        print("Błąd przy tworzeniu kategorii:", response.status_code, response.text)

def get_category_name(category_id, lang_id=2):
    try:
        url = f"{API_URL}/?url=categories/{category_id}"
        response = requests.get(url, auth=HTTPBasicAuth(WEBSERVICE_TOKEN, ""), verify=False)
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            for language in root.findall(".//category/name/language"):
                if int(language.get("id")) == lang_id:
                    text = language.text
                    if text == "Prezenty":
                        text = 'Gifts'
                    elif text == 'Towary':
                        text = 'Merch'
                    elif text == "Materiały":
                        text = "Materials"     
                    return text
    except Exception as e:
        print(e)
        return None

def get_categories_tuples(API_TOKEN):
    response = requests.get(API_URL + "/categories", auth=HTTPBasicAuth(API_TOKEN, ''), verify=False)
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        ids = [category.get('id') for category in root.findall('.//category')]
        categories = {get_category_name(id): id for id in ids }
        return categories
    else:
        print(f"Failed to retrieve categories: {response.status_code}")  


file_csv = "product_data_scraped_translated.csv"
categories = load_categories_from_csv(file_csv)
for category in categories:
    #print(category)
    upload_category(category)

category_tuples = get_categories_tuples(WEBSERVICE_TOKEN)
print(category_tuples)
for category_name in category_tuples:
    category_id = category_tuples.get(category_name)
    #print(category_name + " " + category_id)
    if (category_name == 'Crochet Patterns'):
        upload_category("Seasonal Patterns", category_id)
        upload_category("Regular Patterns", category_id)
    elif (category_name == 'Gifts'):
        upload_category("Gift Cards", category_id)
        upload_category("Other Gifts", category_id)
    elif (category_name == 'Crochet Kits'):
        upload_category("Seasonal Kits", category_id)
        upload_category("Regular Kits", category_id)
    elif (category_name == 'Merch'):
        upload_category("Pins", category_id)
        upload_category("T-Shirts", category_id)
    elif (category_name == 'Pattern Bundles'):
        upload_category("Big Bundle", category_id)
        upload_category("Regular Bundle", category_id)
    elif (category_name == 'Materials'):
        upload_category("Needle", category_id)
        upload_category("Yarn", category_id)
