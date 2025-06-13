# src/visualize.py

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sentiment_data():
    # Connect to MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Chifuyu*28',
        database='feedback_project'
    )

    # Load data
    query = "SELECT * FROM sentiment_feedback"
    df = pd.read_sql(query, connection)

    # 1. Pie chart of sentiment labels
    sentiment_counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
    plt.title('Sentiment Distribution')
    plt.savefig('outputs/sentiment_pie_chart.png')
    plt.close()

    # 2. Histogram of sentiment scores
    plt.figure(figsize=(8, 5))
    sns.histplot(df['sentiment_score'], bins=10, kde=True, color='skyblue')
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.savefig('outputs/sentiment_score_histogram.png')
    plt.close()

    print("📊 Sentiment visualizations saved to 'outputs/' directory.")

if __name__ == "__main__":
    visualize_sentiment_data()
