import pandas as pd
import mysql.connector
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment():
    print("Starting sentiment analysis...")

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",  # <-- update your password here
        database="feedback_project"
    )
    cursor = conn.cursor()

    # Read clean feedback
    df = pd.read_sql("SELECT * FROM clean_feedback", conn)

    sid = SentimentIntensityAnalyzer()

    # Analyze sentiment
    def get_sentiment_label(score):
        if score >= 0.05:
            return 'Positive'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    df['sentiment_score'] = df['cleaned_feedback'].apply(lambda x: sid.polarity_scores(x)['compound'])
    df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

    # Create sentiment_feedback table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_feedback (
            feedback_id INT PRIMARY KEY,
            sentiment_score FLOAT,
            sentiment_label VARCHAR(10)
        )
    """)

    # Clear previous data
    cursor.execute("DELETE FROM sentiment_feedback")

    # Insert sentiment results
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO sentiment_feedback (feedback_id, sentiment_score, sentiment_label)
            VALUES (%s, %s, %s)
        """, (row['feedback_id'], row['sentiment_score'], row['sentiment_label']))

    conn.commit()
    conn.close()
    print("✅ Sentiment analysis complete. Results saved in sentiment_feedback.")

if __name__ == "__main__":
    analyze_sentiment()
