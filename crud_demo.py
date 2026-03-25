#demo file
import pymysql
import os
from dotenv import load_dotenv

print("STEP 0: Script started")

load_dotenv()

try:
    print("STEP 1: Connecting to MySQL server")

    # 🔹 connect WITHOUT database
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT"))
    )

    cursor = conn.cursor()

    print("✅ Connected to MySQL server")

except Exception as e:
    print("❌ Connection error:", e)
    exit()

# ================================
# CREATE DATABASE (SAFE)
# ================================
cursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
print("✅ Database ensured")

# ================================
# RECONNECT TO DATABASE
# ================================
conn.select_db("indigo")

# ================================
# CREATE TABLE
# ================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS airport(
    airport_id INTEGER PRIMARY KEY,
    code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL
)
""")
conn.commit()

# ================================
# INSERT DATA
# ================================
cursor.execute("""
INSERT INTO airport (airport_id, code, city, name)
VALUES (1,'DEL','New Delhi','IGIA'),
       (2,'CCU','Kolkata','NSCA'),
       (3,'BOM','Mumbai','CSMA')
ON DUPLICATE KEY UPDATE name=VALUES(name)
""")
conn.commit()

# ================================
# SELECT
# ================================
cursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = cursor.fetchall()

print("\n📌 Filtered Data:")
for row in data:
    print(row)

# ================================
# UPDATE
# ================================
cursor.execute("""
UPDATE airport
SET name = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

# ================================
# VERIFY UPDATE
# ================================
cursor.execute("SELECT * FROM airport")
print("\n📌 After Update:")
print(cursor.fetchall())

# ================================
# DELETE
# ================================
cursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

# ================================
# VERIFY DELETE
# ================================
cursor.execute("SELECT * FROM airport")
print("\n📌 After Delete:")
print(cursor.fetchall())

# ================================
# CLEANUP
# ================================
cursor.close()
conn.close()

print("\n✅ DB operations completed")