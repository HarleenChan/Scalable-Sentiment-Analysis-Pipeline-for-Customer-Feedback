import mysql.connector

def clean_feedback():
    print("Starting data cleaning...")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",
        database="feedback_project"
    )
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS clean_feedback")

    cursor.execute("""
        CREATE TABLE clean_feedback AS
        SELECT 
            feedback_id,
            customer_name,
            STR_TO_DATE(date, '%Y-%m-%d') AS date,
            LOWER(TRIM(feedback)) AS feedback
        FROM raw_feedback;
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Cleaned data stored in clean_feedback")

if __name__ == "__main__":
    clean_feedback()
