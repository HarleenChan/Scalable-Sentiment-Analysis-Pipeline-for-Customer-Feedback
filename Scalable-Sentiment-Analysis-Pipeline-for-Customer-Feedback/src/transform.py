import pandas as pd
import mysql.connector
import re

def clean_text(text):
    # Remove non-alphabetic characters, lowercase, strip spaces
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = text.lower().strip()
    return text

def transform_feedback():
    print("✨ Starting transformation...")

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",   # <-- update this
        database="feedback_project"
    )
    cursor = conn.cursor()

    # Read raw_feedback
    df = pd.read_sql("SELECT * FROM raw_feedback", conn)

    # Clean feedback column
    df['cleaned_feedback'] = df['feedback'].apply(clean_text)

    # Create table for clean feedback
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clean_feedback (
            feedback_id INT PRIMARY KEY,
            cleaned_feedback TEXT
        )
    """)

    # Optional: clear previous data
    cursor.execute("DELETE FROM clean_feedback")

    # Insert cleaned data
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO clean_feedback (feedback_id, cleaned_feedback)
            VALUES (%s, %s)
        """, (row['feedback_id'], row['cleaned_feedback']))

    conn.commit()
    conn.close()
    print("✅ Transformation complete. Data saved to clean_feedback.")

if __name__ == "__main__":
    transform_feedback()
