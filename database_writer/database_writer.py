import pg8000
from util.util import clean_and_upper_text
conn = pg8000.connect(
    user="root",
    password="root",
    host="localhost",
    port=5432,
    database="mydatabase"
)


def insert_to_tb_product(data, company_id):
    cursor = conn.cursor()
    sql_columns = [
        "description", "description_normalized", "general_price", "company_id", "category_id", "brand", "image_1", "image_2", "image_3",
        "image_4", "image_5",
    ]

    columns = ', '.join(sql_columns)
    placeholders = ', '.join(['%s'] * len(sql_columns))
    already_exists = f""" ON CONFLICT (id, company_id) 
    DO UPDATE SET
        description = EXCLUDED.description,
        description_normalized = EXCLUDED.description_normalized,
        general_price = EXCLUDED.general_price,
        brand = EXCLUDED.brand,
        image_1 = EXCLUDED.image_1,
        image_2 = EXCLUDED.image_2,
        image_3 = EXCLUDED.image_3,
        image_4 = EXCLUDED.image_4,
        image_5 = EXCLUDED.image_5,
        updated_at = NOW(); -- Update the 'updated_at' field when a conflict occurs
    """
    sql = f"INSERT INTO quantoqueta.TB_PRODUCT ({columns}) VALUES ({placeholders}) {already_exists}"

    for d in data:
        row_values = get_rows_based_company_id(company_id, d)
        try:
            cursor.execute(sql, row_values)
        except Exception as e:
            print(sql)
            print(e)
            print(row_values)
            print('\n')
            conn.rollback()  # Rollback transaction on error

    conn.commit()
    cursor.close()


def get_rows_based_company_id(company_id, d):
    row_values = []
    if company_id == 'PA':
        row_values.append(d.get('name'))
        row_values.append(clean_and_upper_text(d.get('name')))
        row_values.append(d.get('price'))
        row_values.append(company_id)
        row_values.append(1) #Alimentos
        row_values.append(d.get('sellername'))
        row_values.append(d.get('fullUri_1'))
        row_values.append(d.get('fullUri_2'))
        row_values.append(d.get('fullUri_3'))
        row_values.append(d.get('fullUri_4'))
        row_values.append(d.get('fullUri_5'))

    if company_id == 'OXXO':
        row_values.append(d.get('displayName'))
        row_values.append(clean_and_upper_text(d.get('displayName')))
        row_values.append(d.get('salePrice'))
        row_values.append(company_id)
        row_values.append(1)  # Alimentos
        row_values.append(d.get('brand'))

        fullImageURLs = d.get('fullImageURLs', [])  # Default to an empty list if the key doesn't exist
        for i in range(5):
            # Use the image from fullImageURLs if it exists; otherwise, append a default value (e.g., None or "")
            row_values.append('https://www.oxxo.com.br' + fullImageURLs[i] if i < len(fullImageURLs) else None)

    return row_values
