import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chifuyu*28',  # Replace with your actual password
    database='feedback_project'
)

query = "SELECT * FROM sentiment_feedback"
df = pd.read_sql(query, connection)

df.to_csv("sentiment_feedback_export.csv", index=False)

print("Sentiment feedback successfully exported to 'sentiment_feedback_export.csv'.")

connection.close()
