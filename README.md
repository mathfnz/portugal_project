# Portugal Project: Urban Infrastructure Analysis

## About This Project

This project was developed as a practical study to build and understand the architecture of a modern, end-to-end data pipeline. The primary focus was on implementing a full **ELT (Extract, Load, Transform)** workflow using professional-grade tools such as Docker, PostgreSQL, and Streamlit.

The goal is to demonstrate foundational skills across the entire data lifecycle, from collecting data via external APIs to making it available in an interactive dashboard.

---

This project involves the collection, storage, and transformation of public data from the city of Braga for urban infrastructure analysis.

## Project Architecture

![Project Data Architecture Diagram](./assets/data_architecure_portugal.png)

## Tech Stack

* **Language:** Python
* **Data Collection:** Requests, Pandas
* **Storage:** PostgreSQL + PostGIS
* **Containerization:** Docker, Docker Compose
* **Visualization:** Streamlit
* **Transformation (in development):** dbt

## How to Run This Project

To run this project locally, ensure you have Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```

2.  **Start the services with Docker Compose:**
    This command will build the application image and start the database and dashboard containers.
    ```bash
    docker-compose up --build -d
    ```

3.  **Load the initial data:**
    Run the extraction and load scripts to populate the database.
    ```bash
    # (Optional, if data is not loaded automatically)
    # python extracao_osm.py
    # python load_to_postgres.py
    ```

4.  **Access the Dashboard:**
    Open your browser and navigate to:
    [**http://localhost:8501**](http://localhost:8501)