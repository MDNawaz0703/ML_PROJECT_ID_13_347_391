# Bitcoin Tweet Sentiment Analyzer & Model Comparison

This project analyzes Bitcoin-related tweets for market sentiment and visualizes the accuracy of various machine learning models. The Streamlit app provides a user-friendly interface for sentiment analysis and model performance comparison.

## Features
- Custom sentiment analysis for Bitcoin tweets using crypto-specific keywords
- Confidence score for sentiment detection
- Visualization of model accuracies (Random Forest, XGBoost, Logistic Regression, SVM, Naive Bayes)
- Keyword guide for positive and negative sentiment
- Interactive UI built with Streamlit

## Project Structure
```
ML-PROJECT/ml/
├── streamlit_app/
│   ├── app.py                # Streamlit UI
│   ├── tweet_analyzer.py     # Sentiment analysis logic
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # (this file)
├── ml-project-id-13.ipynb    # Jupyter notebook with model training & visualization
├── BTC_Tweets_Updated.csv    # Tweet dataset
├── btcusd_1-min_data (1).csv # Bitcoin price dataset
```

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/MDNawaz0703/ML_PROJECT_ID_13_347_391.git
cd ML_PROJECT_ID_13_347_391/ml
```

### 2. Install Python & Dependencies
- Make sure you have Python 3.8+ installed.
- Install required packages:
```
pip install -r streamlit_app/requirements.txt
```

### 3. Prepare Data Files
- Place `BTC_Tweets_Updated.csv` and `btcusd_1-min_data (1).csv` in the project root (`ml/`).
- (Optional) If you want to retrain models, use the notebook `ml-project-id-13.ipynb`.

### 4. Run the Streamlit App
```
streamlit run streamlit_app/app.py
```
- The app will open in your browser.
- Enter a Bitcoin-related tweet to analyze sentiment.
- View confidence scores and model accuracy charts.

### 5. Explore the Notebook
- Open `ml-project-id-13.ipynb` in Jupyter or VS Code to see model training, evaluation, and visualizations.

## How Sentiment Analysis Works
- The app uses crypto-specific keywords to detect positive or negative sentiment in tweets.
- Confidence scores are based on the number of sentiment keywords detected.
- Model accuracy is visualized for Random Forest (best performer: 71% overall, 73% positive, 69% negative) and other models.

## Troubleshooting
- If you see missing file errors, ensure all required CSVs are present in the `ml/` folder.
- For package issues, re-run `pip install -r streamlit_app/requirements.txt`.
- For git issues, make sure you have access to the repository and are on the correct branch.

## License
MIT

## Author
Mohammed Nawaz
