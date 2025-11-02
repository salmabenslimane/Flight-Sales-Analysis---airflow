# ✈️ Flight Sales Data Pipeline 

A **mini data engineering project** simulating how an airline like **Air France** could collect, process, and analyze flight sales data using modern tools — **DuckDB**, **Apache Airflow**, and **Python**. 

## 🧭 Table of Contents 
- [Overview](#overview)
- [⚙️ Tech Stack](#tech-stack)
- [📂 Project Structure](#project-structure)
- [🧩 How It Works](#how-it-works)
- [📊 Example Insights](#example-insights)
- [🚀 Quickstart Guide](#quickstart-guide)
  - [Set up the database](#set-up-the-database)
  - [Fetch mock flight data](#fetch-mock-flight-data)
  - [Orchestrate with Airflow](#orchestrate-with-airflow)
  - [(Optional) Visualize in Streamlit](#optional-visualize-in-streamlit)
- [🧠 What You’ll Learn](#what-youll-learn)
- [📈 Future Improvements](#future-improvements)
- [🏁 Author](#author)

---

## <a id="overview"></a>📘 Overview 
The goal of this project is to **simulate an airline sales data pipeline**. It automatically:
1. Fetches flight booking data from a mock API (Mockaroo).
2. Stores it in a local analytical database (DuckDB).
3. Automates the ETL process with Apache Airflow.
4. (Optionally) Visualizes insights using Streamlit.

This project mirrors what a **real data engineering team at Air France** might do — at a smaller, simpler scale.

---

## <a id="tech-stack"></a>⚙️ Tech Stack 
| Layer               | Tool               | Purpose                                   |
|---------------------|--------------------|-------------------------------------------|
| 🐍 Programming       | **Python**         | Main scripting language                   |
| 🪶 Storage           | **DuckDB**         | Analytical database                       |
| 🌐 Data Source       | **Mockaroo API**   | Generates realistic fake flight sales data|
| 🧩 Orchestration     | **Apache Airflow**  | Automates the ETL workflow                |
| 📊 Visualization      | **Streamlit** *(optional)* | Interactive dashboard for business KPIs |
| 🐳 Containerization   | **Docker**         | Runs Airflow and Postgres services       |

---

## <a id="project-structure"></a>📂 Project Structure 

  - `mini_data_pipeline/`
    - `db/`
      - `raw_data.duckdb`          # DuckDB database file
      - `db_connection.py`          # Connection helper
      - `init_schema.py`            # Defines tables
      - `fetch_and_insert.py`        # Fetches & inserts mock data
    - `airflow/`
      - `dags/`
        - `etl_pipeline.py`        # Airflow DAG
      - `logs/`                    # Airflow logs
      - `plugins/`                 # (optional) custom operators
      - `docker-compose.yaml`       # Airflow + Postgres setup
    - `dashboard/`
      - `app.py`                   # Streamlit dashboard (optional)
    - `config/`
      - `config.json`              # API URLs, keys, etc.
    - `cli_tools/`
      - `init-db.py`               # CLI wrapper for schema creation
      - `fetch-data.py`            # CLI wrapper for data fetching
    - `requirements.txt`           # Python dependencies
    - `.gitignore`                 # Git ignore file
    - `README.md`                  # Project documentation

---

## <a id="how-it-works"></a>🧩 How It Works 
1. **init_schema.py**: Creates a raw schema in DuckDB with a bookings table: 
   - Booking_ID, Booking_Date, Flight_Date, Passenger_ID, Passenger_Name, Email, Gender, Country_Code, Ticket_Class, Quantity, Unit_Price, Revenue
2. **fetch_and_insert.py**: Fetches JSON from Mockaroo API and inserts into raw.bookings.
3. **Airflow DAG (etl_pipeline.py)**: 
   - Orchestrates the ETL process: Extract → Transform → Load
   - Can be scheduled daily/weekly.
   - Logs every run and keeps track of success/failure.
4. **Streamlit Dashboard (optional)**: 
   - Visualizes key metrics:
     - Total revenue
     - Best-selling ticket class
     - Weekly sales trend
     - Top booking countries

---

## <a id="example-insights"></a>📊 Example Insights 
| KPI                     | Example Insight                     |
|-------------------------|-------------------------------------|
| 💰 Total Revenue        | €145,000 in the last 30 days       |
| 🛫 Best Route           | Paris → New York                    |
| 👩‍💼 Top Customer Country| France                              |
| 🏷️ Most Popular Ticket Class | Economy                       |
| 📅 Bookings Trend       | +8% week-over-week                  |

---

## <a id="quickstart-guide"></a>🚀 Quickstart Guide 
### <a id="set-up-the-database"></a>Set up the database