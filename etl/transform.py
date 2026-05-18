import pandas as pd

def transform_data(orders_df, customers_df, products_df):
    
    # Merge dataframes
    merge_df = pd.merge(
        orders_df, 
        customers_df, 
        on="customer_id", 
        how="inner"
    )

    # Removing _id:
    merge_df = merge_df.drop(columns=["_id"])

    # Ensuring uniform city name
    merge_df["city"] = merge_df["city"].str.lower()

    # Add derived column: customer category based on amt
    merge_df["customer_type"] = merge_df["amount"].apply(
        lambda x: "High Value" if x>=10000 else "Regular")

    # Add derived column: extend timestamp to year and month
    merge_df["year"] = merge_df["created_at"].dt.year
    merge_df["month"] = merge_df["created_at"].dt.month

    final_df = pd.merge(
        merge_df, products_df, 
        on="product_id", how="inner")

    return final_df