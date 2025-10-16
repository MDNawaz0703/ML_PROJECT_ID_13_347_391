"""Tweet sentiment analyzer for Bitcoin price prediction."""
import re

def clean_tweet(tweet):
    """Clean tweet text by removing links, special characters."""
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#\w+', '', tweet)
    tweet = tweet.lower()
    return tweet.strip()

# Keywords for sentiment analysis
POSITIVE_KEYWORDS = {
    'bullish', 'moon', 'rise', 'rising', 'up', 'upward', 'gain', 'gains', 
    'profit', 'profitable', 'strong', 'strength', 'stronger', 'buy', 'buying',
    'accumulate', 'accumulating', 'bull', 'bulls', 'bullrun', 'ath', 'high',
    'higher', 'pump', 'pumping', 'good', 'great', 'best', 'positive', 'success',
    'successful', 'win', 'winning', 'won', 'green', 'climb', 'climbing',
    'breakout', 'breakthrough', 'confident', 'confidence', 'support', 'backed'
}

NEGATIVE_KEYWORDS = {
    'bearish', 'dump', 'dumping', 'fall', 'falling', 'down', 'downward',
    'loss', 'losses', 'weak', 'weakness', 'weaker', 'sell', 'selling',
    'bear', 'bears', 'crash', 'low', 'lower', 'bottom', 'bad', 'worse',
    'worst', 'negative', 'fail', 'failing', 'failed', 'red', 'drop',
    'dropping', 'dropped', 'decrease', 'decreasing', 'decreased', 'poor',
    'panic', 'fear', 'worried', 'worry', 'concerning', 'concern'
}

def analyze_sentiment(tweet):
    """
    Analyze tweet sentiment based on crypto/trading keywords.
    Returns: 
        sentiment_score: float (-1 to 1)
        sentiment_label: str ('positive', 'negative', or 'neutral')
        confidence: float (0 to 1)
    """
    tweet = clean_tweet(tweet)
    words = set(tweet.split())
    
    # Count positive and negative keywords
    pos_count = len(words.intersection(POSITIVE_KEYWORDS))
    neg_count = len(words.intersection(NEGATIVE_KEYWORDS))
    
    # Calculate sentiment score (-1 to 1)
    total = pos_count + neg_count
    if total == 0:
        return 0.0, "neutral", 0.5  # Neutral with 50% confidence
        
    sentiment_score = (pos_count - neg_count) / (pos_count + neg_count)
    
    # Determine sentiment label and confidence
    if sentiment_score > 0:
        confidence = (pos_count) / (pos_count + neg_count)
        return sentiment_score, "positive", confidence
    elif sentiment_score < 0:
        confidence = (neg_count) / (pos_count + neg_count)
        return sentiment_score, "negative", confidence
    else:
        return 0.0, "neutral", 0.5