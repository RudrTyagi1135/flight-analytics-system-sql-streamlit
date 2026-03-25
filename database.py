import pymysql
import os
from dotenv import load_dotenv

class DB:

    def __init__(self):
        load_dotenv()

        try:
            self.conn = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                port=int(os.getenv("DB_PORT")),
                cursorclass=pymysql.cursors.Cursor
            )

            self.cursor = self.conn.cursor()
            print("✅ Connection established")

        except Exception as e:
            print("❌ Connection error:", e)

    # ================================
    # Fetch all unique cities
    # ================================
    def fetch_city_names(self):

        query = """
        SELECT DISTINCT Destination FROM flights
        UNION
        SELECT DISTINCT Source FROM flights
        """

        self.cursor.execute(query)
        data = self.cursor.fetchall()

        return [item[0] for item in data]

    # ================================
    # Fetch flights between cities
    # ================================
    def fetch_all_flights(self, source, destination):

        query = """
        SELECT Airline, Route, Dep_Time, Duration, Price
        FROM flights
        WHERE Source = %s AND Destination = %s
        """

        self.cursor.execute(query, (source, destination))
        return self.cursor.fetchall()

    # ================================
    # Airline frequency
    # ================================
    def fetch_airline_frequency(self):

        query = """
        SELECT Airline, COUNT(*)
        FROM flights
        GROUP BY Airline
        """

        self.cursor.execute(query)
        data = self.cursor.fetchall()

        airline = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return airline, frequency

    # ================================
    # Busy airports
    # ================================
    def busy_airport(self):

        query = """
        SELECT Source, COUNT(*) FROM (
            SELECT Source FROM flights
            UNION ALL
            SELECT Destination FROM flights
        ) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """

        self.cursor.execute(query)
        data = self.cursor.fetchall()

        city = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return city, frequency

    # ================================
    # Daily frequency
    # ================================
    def daily_frequency(self):

        query = """
        SELECT Date_of_Journey, COUNT(*)
        FROM flights
        GROUP BY Date_of_Journey
        """

        self.cursor.execute(query)
        data = self.cursor.fetchall()

        date = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return date, frequency

    # ================================
    # Close connection
    # ================================
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("🔒 Connection closed")