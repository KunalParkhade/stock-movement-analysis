import pandas as pd
from preprocess import preprocess_data

def load_data(file_path, platform):
    """
    Load the raw data from file and map it to a common structure for preprocessing.
    Args:
        file_path (str): Path to the raw data file.
        platform (str): The platform ('twitter', 'reddit', 'telegram').
    Returns:
        pd.DataFrame: Loaded DataFrame with a unified 'text' column.
    """
    data = pd.read_json(file_path)

    if platform == "twitter":
        data['text'] = data['text']  # Text is already in 'text' key
        data = data[['text', 'created_at', 'author_id']]
    elif platform == "reddit":
        data['text'] = data['title']  # Map 'title' to 'text'
        data = data[['text', 'created_at', 'score', 'num_comments']]
    elif platform == "telegram":
        data['text'] = data['text']  # Text is already in 'text' key
        data = data[['text', 'date', 'sender_id']]
    else:
        raise ValueError("Platform must be one of: 'twitter', 'reddit', 'telegram'.")

    # Debug: Print the loaded data
    print(f"Loaded data for {platform}:\n", data.head())
    return data

if __name__ == "__main__":
    try:
        # Preprocess and save for Telegram
        telegram_data = load_data("data/raw/telegram_data.json", platform="telegram")
        processed_telegram_data = preprocess_data(telegram_data, text_column='text')
        processed_telegram_data.to_csv("data/processed/telegram_processed.csv", index=False)
        print("Processed Telegram data saved.")

        # Preprocess and save for Reddit
        reddit_data = load_data("data/raw/reddit_data.json", platform="reddit")
        processed_reddit_data = preprocess_data(reddit_data, text_column='text')
        processed_reddit_data.to_csv("data/processed/reddit_processed.csv", index=False)
        print("Processed Reddit data saved.")

        # Preprocess and save for Twitter
        twitter_data = load_data("data/raw/twitter_data.json", platform="twitter")
        processed_twitter_data = preprocess_data(twitter_data, text_column='text')
        processed_twitter_data.to_csv("data/processed/twitter_processed.csv", index=False)
        print("Processed Twitter data saved.")

    except Exception as e:
        print(f"Error: {e}")