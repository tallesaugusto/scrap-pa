import requests
from database_writer.database_writer import insert_to_tb_product
headers = {
    'Content-Type': 'application/json'
}

def fech_data_oxxo():
    base_url = 'https://www.oxxo.com.br/'
    response = requests.get(base_url + '/ccstore/v1/products', headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        items = response_data.get('items', [])
        insert_to_tb_product(items, 'OXXO')


