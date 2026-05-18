from extract import (extract_orders, extract_customers, extract_products)
from transform import transform_data
from load import load_data

orders_df = extract_orders()

customers_df = extract_customers()

products_df = extract_products() 

final_df = transform_data (
    orders_df,
    customers_df,
    products_df
)

print(final_df)

load_data(final_df)