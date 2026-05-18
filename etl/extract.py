import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

# from sqlalchemy import create_engine => connects Python to PostgreSQL
# from pymongo import MongoClient => connects Python to MongoDB

## Extract
def extract_orders():
    # Connect to postgresql:
    postgre_engine = create_engine("postgresql://postgres:ABC%40123@localhost:5432/orders_db")

    # create_engine = creates a communication bridge b/w python and postgreSQL

    # Fetch orders data
    orders_df = pd.read_sql("SELECT * FROM orders_order",
                            postgre_engine)
    # orders_order => bcz Django names tables as appnam_modelname so: ordeers + Order -> orders_order
    # orders_df is stored inside Python memory i.e., RAM
    return orders_df

def extract_customers():
    # Connect to MongoDB:
    mongo_client = MongoClient("mongodb://localhost:27017/")

    # Access Database
    mongo_db = mongo_client["ecommerce_db"]

    # Access Collection
    customers_collection = mongo_db["customers"] #rep ecommerce_db.customers

    #Fetch docs:
    customers_data = list(customers_collection.find()) #find() = select * from customers
    # MongoDB returns cursor object like lazy iterator so list() converts it into actual Py list

    # Convert to DataFrame
    customers_df = pd.DataFrame(customers_data)

    return customers_df

def extract_products():
    # Read CSV file:
    products_df = pd.read_csv("../data/products.csv")
    return products_df