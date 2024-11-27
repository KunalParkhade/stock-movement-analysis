from twitter_scraper import TwitterScraperV2
from reddit_scraper import RedditScraper
from telegram_scraper import TelegramScraper
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    twitter_scraper = TwitterScraperV2()
    twitter_scraper.authenticate()
    tweets = twitter_scraper.scrape_data(query="stocks", count=10)
    twitter_scraper.save_data(tweets, "data/raw/twitter_data.json")

    reddit_scraper = RedditScraper()
    reddit_scraper.authenticate()
    posts = reddit_scraper.scrape_data(subreddit="stocks", limit=50)
    reddit_scraper.save_data(posts, "data/raw/reddit_data.json")

    telegram_scraper = TelegramScraper()
    telegram_scraper.authenticate()
    messages = telegram_scraper.scrape_data(channel="https://t.me/s/moneycontrolcom", limit=50)
    telegram_scraper.save_data(messages, "data/raw/telegram_data.json")