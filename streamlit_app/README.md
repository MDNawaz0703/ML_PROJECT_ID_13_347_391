# Bitcoin Price Movement Predictor

A lightweight Streamlit app that predicts Bitcoin price movement using XGBoost and sentiment analysis.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy model files to app directory:
```bash
copy ..\xgb_model.pkl .
copy ..\scaler.pkl .
```

3. Run the app:
```bash
streamlit run app.py
```

## Features

- Predicts Bitcoin price movement (up/down)
- Uses current price, volume and sentiment
- Shows prediction confidence
- Optional feature importance display

## Model Details

The model uses XGBoost with the following features:
- Close price
- Trading volume 
- Twitter sentiment score
- Technical indicators (simplified in live prediction)

## Requirements

See requirements.txt for detailed dependencies.