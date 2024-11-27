from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment(data):
    """
    Analyze the sentiment of the cleaned text using VADER.
    """
    analyzer = SentimentIntensityAnalyzer()
    
    # Apply sentiment analysis to each cleaned text
    sentiment_scores = data['cleaned_text'].apply(lambda text: analyzer.polarity_scores(text)['compound'])
    
    # Add the sentiment score to the data
    data['sentiment_score'] = sentiment_scores
    
    # Categorize sentiment into 'Positive', 'Negative', or 'Neutral'
    data['sentiment'] = data['sentiment_score'].apply(lambda score: 'Positive' if score > 0 else ('Negative' if score < 0 else 'Neutral'))
    
    return data
