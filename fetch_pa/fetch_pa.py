import requests
from database_writer.database_writer import insert_to_tb_product

# Define the headers and the payload
headers = {
    'Content-Type': 'application/json'
}


def fech_data_pa(page, url, param, field_param):

    data = {
        "partner": "linx",
        "page": page,
        "resultsPerPage": 200,
        field_param: param,
        "sortBy": "relevance",
        "department": "ecom",
        "storeId": 461,
        "customerPlus": True,
        "filters": []
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        products = response_data.get('products', [])
        all_products = []

        for product in products:
            # Prepare the product row for the DataFrame
            row = {
                'id': product.get('id', ''),
                'name': product.get('name', ''),
                'price': product.get('price', ''),
                'brand': product.get('brand', ''),
                'sku': product.get('sku', ''),
                'urlDetails': product.get('urlDetails', ''),
                'sellerName': product.get('sellerName', ''),
            }

            # Add product images by concatenating base URL with image paths
            base_url = "https://static.paodeacucar.com"
            product_images = product.get('productImages', [])
            for idx, img_path in enumerate(product_images):
                row[f'fullUri_{idx + 1}'] = base_url + img_path

            # Append the row to the list of products
            all_products.append(row)

        insert_to_tb_product(all_products, 'PA')
        fech_data_pa(page + 1, url, param, field_param)

    if response.status_code == 404:
        raise Exception(f" [PA] - END url:{url} page:{page} param:{param} field_param:{field_param} \n")
