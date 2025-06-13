import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chifuyu*28',
    database='feedback_project'
)

# Load sentiment data
query = "SELECT * FROM sentiment_feedback"
df = pd.read_sql(query, connection)
connection.close()

# Streamlit UI
st.set_page_config(page_title="Sentiment Dashboard", layout="centered")
st.title("📊 Sentiment Analysis Dashboard")

# Show DataFrame
with st.expander("View Raw Data"):
    st.dataframe(df)

# Pie Chart
st.subheader("Sentiment Distribution")
sentiment_counts = df['sentiment_label'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Histogram
st.subheader("Sentiment Score Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df['sentiment_score'], bins=10, kde=True, ax=ax2)
ax2.set_title("Sentiment Score Histogram")
ax2.set_xlabel("Sentiment Score")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

st.markdown("---")
st.caption("Crafted with love by Haru & Fuyu")
