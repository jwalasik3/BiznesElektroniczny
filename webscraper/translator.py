import pandas as pd
from deep_translator import GoogleTranslator

def translate_to_polish(text):
    try:
        return GoogleTranslator(source='en', target='pl').translate(text)
    except Exception as e:
        return f"Error: {e}"

data = pd.read_csv('product_data_scraped.csv', delimiter=';')

df = data.head(10).copy()

df['polish_Name'] = df['Name'].apply(translate_to_polish)
df['polish_Categories'] = df['Categories'].apply(translate_to_polish)
df['polish_Long desc'] = df['Long desc'].apply(translate_to_polish)
df['polish_Short desc'] = df['Short desc'].apply(translate_to_polish)
df.to_csv('product_data_scraped_translated.csv', index=False)

