from sqlalchemy import create_engine

def load_data(final_df):
    ## Load 
    # Store this final dataset somewhere usable
    analytics_engine = create_engine("postgresql://postgres:ABC%40123@localhost:5432/analytics_db")

    final_df.to_sql(
        "customer_order_summary", 
        analytics_engine, 
        if_exists="replace", 
        index=False)

    print("Data loaded successfully!")