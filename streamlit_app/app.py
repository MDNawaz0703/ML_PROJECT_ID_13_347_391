import streamlit as st
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from tweet_analyzer import analyze_sentiment

# Set page config
st.set_page_config(page_title="Bitcoin Price Movement Predictor", layout="wide")

def load_model():
    """Load the saved model and scaler."""
    try:
        model = joblib.load("xgb_model.pkl")
        scaler = joblib.load("scaler.pkl")
        return model, scaler
    except:
        st.error("⚠️ Model files not found. Please ensure xgb_model.pkl and scaler.pkl are in the same directory.")
        return None, None

def create_feature_vector(close, volume, sentiment):
    """Create a complete feature vector matching the training data."""
    features = {
        'Close': close,
        'Volume': volume,
        'Avg_Sentiment': sentiment,
        'Return_1': 0.0,
        'Return_2': 0.0,
        'Return_3': 0.0,
        'Return_4': 0.0,
        'Return_5': 0.0,
        'MA3': close,  # Simplify by using current close
        'MA5': close,
        'Volatility3': 0.0,
        'Volatility5': 0.0,
        'Sentiment_Lag1': sentiment,
        'Sentiment_Lag2': sentiment,
        'Sentiment_Lag3': sentiment,
        'Sentiment_Lag4': sentiment,
        'Sentiment_Lag5': sentiment,
        'Vol_Change': 0.0
    }
    return pd.DataFrame([features])

def main():
    st.title("🔮 Bitcoin Tweet Sentiment Analyzer")
    st.write("Enter a tweet about Bitcoin to analyze market sentiment")
    
    # Show keyword guide
    with st.expander("📖 Keyword Guide - Click to expand"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🟢 Positive Keywords")
            positive_words = [
                "bullish", "moon", "rise", "rising", "up", "upward",
                "gain(s)", "profit", "strong", "strength", "buy",
                "accumulate", "bull(s)", "ATH", "pump", "good",
                "breakout", "confident", "support", "backed"
            ]
            st.write("Use these words for positive sentiment:")
            for word in positive_words:
                st.write(f"• {word}")
                
        with col2:
            st.markdown("### 🔴 Negative Keywords")
            negative_words = [
                "bearish", "dump", "fall", "falling", "down",
                "loss(es)", "weak", "sell", "bear(s)", "crash",
                "bottom", "fail", "drop", "decrease", "panic",
                "fear", "worry", "concern", "red", "poor"
            ]
            st.write("Use these words for negative sentiment:")
            for word in negative_words:
                st.write(f"• {word}")
    
    # Tweet input and analysis
    tweet = st.text_area("Enter your tweet about Bitcoin:", height=100,
                        help="Example: 'Bitcoin looking very bullish today, strong support at current levels!'")
    
    if tweet:
        sentiment_score, sentiment_label, confidence = analyze_sentiment(tweet)
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"Sentiment Analysis: **{sentiment_label.upper()}**")
        with col2:
            st.info(f"Confidence: **{confidence:.1%}**")
        
        # Show detailed analysis
        st.markdown("---")
        st.markdown("### Analysis Results")
        
        # Display sentiment with relevant emoji
        if sentiment_label == "positive":
            st.success("🎯 **POSITIVE SENTIMENT DETECTED**")
            st.info(f"Accuracy for positive sentiment: 73% based on Random Forest model")
        elif sentiment_label == "negative":
            st.error("🎯 **NEGATIVE SENTIMENT DETECTED**")
            st.info(f"Accuracy for negative sentiment: 69% based on Random Forest model")
        else:
            st.warning("🤔 **NEUTRAL SENTIMENT DETECTED**")
            st.info("Neutral sentiments have a balanced influence")
        
        # Show confidence bar
        st.markdown("### Sentiment Confidence")
        st.progress(confidence)
        st.write(f"Confidence Score: {confidence:.1%}")
        
        # Show analysis details
        if st.checkbox("Show Detailed Analysis"):
            st.markdown("### Analysis Details")
            st.write({
                "Cleaned Tweet": tweet,
                "Sentiment Score": f"{sentiment_score:.2f} (-1 to +1)",
                "Sentiment Label": sentiment_label.title(),
                "Model Confidence": f"{confidence:.1%}",
                "Model Used": "Random Forest (71% overall accuracy)"
            })
            
            # Display model performance chart
            st.markdown("### Model Performance Comparison")
            st.write("Accuracy breakdown for different models:")
            
            models = ['Random Forest', 'XGBoost', 'Logistic Regression', 'SVM', 'Naive Bayes']
            pos_accuracy = [73, 56, 52, 50, 49]  # Positive class
            neg_accuracy = [69, 52, 50, 48, 47]  # Negative class
            
            chart_data = pd.DataFrame({
                'Model': models * 2,
                'Accuracy': pos_accuracy + neg_accuracy,
                'Class': ['Positive'] * len(models) + ['Negative'] * len(models)
            })
            
            st.bar_chart(data=chart_data, x='Model', y='Accuracy', color='Class')

if __name__ == "__main__": 
    main()