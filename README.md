# ✈️ Flight Analytics System (SQL + Streamlit)

A **full-stack data analytics application** that enables users to explore flight data using **SQL-powered queries** and visualize insights through an **interactive Streamlit dashboard**.

🔗 **Live App:** https://prcqczhhrpgbczsmwr73ld.streamlit.app/

---

## 🚀 Project Overview

This project is a **flight analytics platform** built on top of a relational database, combining:

- **MySQL database** for structured data storage  
- **PyMySQL-based backend layer** for query abstraction  
- **Streamlit UI** for user interaction  
- **Plotly visualizations** for insights  

It allows users to:

- Search flights between cities  
- Analyze airline distribution  
- Identify high-traffic airports  
- Track daily flight trends  

---

## ⚙️ System Architecture

```
Streamlit UI (app.py)
        ↓
Database Layer (database.py)
        ↓
MySQL Database (flights)
```

### Layer Breakdown

- **UI Layer (`app.py`)**  
  Handles user input, layout, and visualizations using Streamlit  

- **Database Layer (`database.py`)**  
  Encapsulates SQL queries and connection logic using a reusable class  

- **Data Layer (MySQL)**  
  Stores flight dataset and supports analytical queries  

---

## 📂 Project Structure

```
flight-analytics-system/
│
├── app.py                # Streamlit dashboard (UI layer)
├── database.py           # DB abstraction layer (PyMySQL)
├── crud_demo.py          # DB setup + CRUD demo
├── data_loader.py        # CSV → MySQL loader (local / AWS)
├── flights.csv           # Dataset
│
├── requirements.txt
├── .env                  # Environment variables (ignored)
├── .gitignore
└── README.md
```

---

## 🔍 Core Features

### 🔎 1. Flight Search

- Select **source and destination**
- Fetch results using parameterized SQL queries  
- Display structured results in table format  

```sql
SELECT Airline, Route, Dep_Time, Duration, Price
FROM flights
WHERE Source = %s AND Destination = %s;
```

---

### 📊 2. Airline Distribution

- Pie chart showing number of flights per airline  
- Uses Plotly for interactive visualization  

---

### 🏙️ 3. Busy Airports Analysis

- Combines **source + destination traffic**

```sql
SELECT Source, COUNT(*) FROM (
    SELECT Source FROM flights
    UNION ALL
    SELECT Destination FROM flights
) t
GROUP BY t.Source
ORDER BY COUNT(*) DESC;
```

---

### 📅 4. Daily Flight Trends

- Time-series analysis of flights per day  

```sql
SELECT Date_of_Journey, COUNT(*)
FROM flights
GROUP BY Date_of_Journey;
```

---

## 🗄️ Database Layer Design

All database operations are handled via a reusable class:

📄 See implementation: :contentReference[oaicite:0]{index=0}

### Key Methods

- `fetch_city_names()` → Unique cities  
- `fetch_all_flights()` → Flight search  
- `fetch_airline_frequency()` → Airline distribution  
- `busy_airport()` → Airport traffic  
- `daily_frequency()` → Time-series data  

### Key Design Decisions

- Environment-based credentials (`.env`)
- Parameterized queries (SQL injection safe)
- Modular and reusable DB layer

---

## 🧪 Database Setup (CRUD Demo)

The project includes a demo script:

📄 See: :contentReference[oaicite:1]{index=1}

This demonstrates:

- Database creation  
- Table creation  
- Insert, update, delete operations  
- Basic SQL workflow  

---

## 📦 Data Ingestion

Dataset loading is handled via:

📄 See: :contentReference[oaicite:2]{index=2}

Supports:

- Local MySQL ingestion  
- AWS RDS connection (via SQLAlchemy)

---

## 🖥️ Application Logic

Main application flow:

📄 See: :contentReference[oaicite:3]{index=3}

### UI Sections

- **Check Flights**
  - Input: Source, Destination  
  - Output: Flight table  

- **Analytics Dashboard**
  - Airline distribution (Pie chart)
  - Busy airports (Bar chart)
  - Daily trends (Line chart)

---

## 🛠️ How to Run (Local)

### 1. Clone Repository

```bash
git clone https://github.com/your-username/flight-analytics-system.git
cd flight-analytics-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure `.env`

```env
DB_HOST=127.0.0.1
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=flights
DB_PORT=3306
```

---

### 5. Load Dataset

```bash
python data_loader.py
```

---

### 6. Run Application

```bash
streamlit run app.py
```

---

## 🌐 Deployment Notes

- Deployed using **Streamlit Cloud**
- Requires external database (local DB will not work)
- Use Streamlit secrets for DB credentials

---

## 🧰 Tech Stack

| Layer         | Technology |
|--------------|-----------|
| UI            | Streamlit |
| Visualization | Plotly |
| Backend       | Python |
| Database      | MySQL |
| Connector     | PyMySQL |
| Data Handling | Pandas |

---

## 🔐 Security Practices

- Credentials stored in `.env`
- Parameterized SQL queries
- No hardcoded secrets
- Recommended: avoid root user

---

## ⚠️ Limitations

- No caching (performance can degrade)
- No pagination for large datasets
- No authentication system
- Tight coupling between UI and DB layer

---

## 📈 Future Improvements

- Add filters (price, airline, duration)
- Implement caching (`st.cache_data`)
- Introduce API layer (FastAPI)
- Move DB to AWS RDS
- Add authentication
- Modularize backend (service layer)

---

## 🎯 What This Project Demonstrates

- SQL query design & optimization  
- Backend abstraction using Python  
- Data pipeline (CSV → DB → UI)  
- Interactive dashboard development  
- Real-world analytics system design  

---

## 📌 Strategic Value

This is a **strong system-oriented project** because it shows:

- End-to-end data flow  
- Real database usage  
- UI + backend integration  

To make it top-tier:

➡️ Add **API layer + AWS deployment + caching**

---

## 👤 Author

**Rudra Tyagi**

ML Systems | MLOps | AI Infrastructure  
B.Tech Final Year Student