import pandas as pd
import re
import string

def clean_text(text):
    """
    Clean the text by removing special characters, links, and extra spaces.
    Args:
        text (str): The raw text to clean.
    Returns:
        str: The cleaned text.
    """
    if not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove mentions (Twitter handle)
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags (optional, or you can process them separately)
    text = re.sub(r'#\w+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra spaces
    text = ' '.join(text.split())

def preprocess_data(data, text_column='text'):
    """
    Preprocess the data by cleaning the text and handling missing values.
    Args:
        data (pd.DataFrame): The raw data to preprocess.
        text_column (str): The column name containing the text.
    Returns:
        pd.DataFrame: The processed DataFrame with a 'cleaned_text' column.
    """
    if text_column not in data.columns:
        raise KeyError(f"Column '{text_column}' not found in the dataset. Available columns: {data.columns.tolist()}")

    # Clean the text and drop empty rows
    data['cleaned_text'] = data[text_column].apply(clean_text)
    data = data[data['cleaned_text'].str.strip() != ""]
    return data
