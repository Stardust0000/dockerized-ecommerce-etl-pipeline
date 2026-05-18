# E-Commerce Data Pipeline

A multi-source ETL pipeline built using:

- Django
- PostgreSQL
- MongoDB
- Pandas
- SQLAlchemy

## Features

- Extracts order data from PostgreSQL
- Extracts customer data from MongoDB
- Extracts product data from CSV
- Performs data transformation using pandas
- Loads analytics-ready data into PostgreSQL

## Architecture

PostgreSQL + MongoDB + CSV → ETL Pipeline → analytics_db