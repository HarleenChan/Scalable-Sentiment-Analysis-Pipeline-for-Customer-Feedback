# 💬 Scalable Sentiment Analysis Pipeline

An end-to-end pipeline to process customer feedback, perform sentiment analysis, and visualize results through an interactive dashboard using Python and Streamlit.

---

## 🚀 Overview

This project was built to extract insights from customer feedback by combining the power of data pipelines, sentiment analysis, and real-time dashboards.

It reads raw feedback data, cleans and transforms it, performs sentiment scoring using VADER, and presents results in a clean Streamlit UI.

---

## 🧰 Technologies Used

- **Python**
- **VADER (NLTK)**
- **pandas, re**
- **Streamlit**
- **MySQL (if applicable) or CSV**
- **pathlib, subprocess**

---

## 📂 Project Structure

scalable-sentiment-analysis-pipeline/
│
├── run_pipeline.py # Entry point to run full pipeline
├── src/
│ ├── clean.py # Cleans raw customer feedback text
│ ├── transform.py # Transforms and prepares data
│ ├── ingest.py # Ingests cleaned data into storage
│ ├── sentiment.py # Applies VADER sentiment scoring
│ ├── visualize.py # Plots sentiment results (optional)
│ └── dashboard.py # Streamlit dashboard
│
├── outputs/
│ └── sentiment-feedback-export.csv # Final output with sentiment labels
├── requirements.txt
└── README.md


---

## 🧪 Pipeline Steps

1. **Data Ingestion** (`ingest.py`)  
   Loads raw feedback from CSV or source into memory or database.

2. **Cleaning & Transformation** (`clean.py`, `transform.py`)  
   Applies text preprocessing: removing special chars, lowering case, etc.

3. **Sentiment Analysis** (`sentiment.py`)  
   Uses **VADER** from `nltk.sentiment` to score feedback as Positive, Negative, or Neutral.

4. **Export & Output**  
   Saves final sentiment-labeled data as `sentiment-feedback-export.csv` in `outputs/`.

5. **Dashboard** (`dashboard.py`)  
   Launches a Streamlit dashboard to visualize sentiment distribution, filter reviews, and explore insights interactively.

---

## 📊 Sample Insights

- Bar charts showing count of each sentiment
- Optionally: word clouds or top keywords per sentiment
- Filtered views for exploring actual reviews

_(You can insert a screenshot here if you have one!)_

---

## ▶️ How to Run

```bash
1. Install dependencies:
   pip install -r requirements.txt

2. Run full pipeline:
   python run_pipeline.py

3. Launch dashboard:
   streamlit run src/dashboard.py


