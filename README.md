# Dockerized E-Commerce Data Pipeline
This project demonstrates a multi-source ETL pipeline integrating PostgreSQL, MongoDB, and CSV data sources using Python and Pandas. The workflow is orchestrated using Apache Airflow and containerized using Docker.

A multi-source ETL pipeline built using:

- Django
- PostgreSQL
- MongoDB
- Pandas
- SQLAlchemy

## Tech Stack

- Python
- Django
- PostgreSQL
- MongoDB
- Pandas
- Apache Airflow
- Docker

## Features

- Multi-source ETL pipeline
- PostgreSQL + MongoDB integration
- Data transformation using Pandas
- Automated orchestration using Airflow
- Dockerized workflow execution

## Architecture

PostgreSQL + MongoDB + CSV → ETL Pipeline → analytics_db

PostgreSQL ─┐
MongoDB ────┼──> ETL Pipeline ───> analytics_db
CSV ────────┘
                     │
                     ▼
                 Airflow


## Setup Instructions

### Clone Repository

```bash
git clone <repo-url>
cd ecommerce-etl-pipeline
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Airflow

```bash
docker compose up
```