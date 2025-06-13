import pandas as pd
import mysql.connector
from pathlib import Path

print("Starting ingestion...")

# Define CSV path
DATA_PATH = Path(__file__).parents[1] / "data" / "raw_feedback.csv"

def ingest_csv_to_mysql():
    # Load data
    # Load CSV
    df = pd.read_csv(DATA_PATH)

    #  Fix date format
    df['date'] = pd.to_datetime(df['date'], dayfirst=True).dt.date


    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",     # <--- replace with your actual password
        database="feedback_project"  # <--- make sure this DB exists
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_feedback (
            feedback_id INT PRIMARY KEY,
            customer_name VARCHAR(100),
            date DATE,
            feedback TEXT
        )
    """)

    # Delete old data (optional)
    cursor.execute("DELETE FROM raw_feedback")

    # Insert each row from DataFrame
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO raw_feedback (feedback_id, customer_name, date, feedback)
            VALUES (%s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    conn.close()

    print("✅ Data ingested successfully into MySQL table.")

if __name__ == "__main__":
    ingest_csv_to_mysql()

