import tweepy
from base_scraper import BaseScraper
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

class TwitterScraperV2(BaseScraper):
    """
    Scraper for fetching data from Twitter using the Tweepy library.
    """

    def __init__(self):
        # self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        # self.consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        # self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        # self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.bearer_token = os.getenv("BEARER_TOKEN")
        self.base_url = "https://api.x.com/2/tweets/search/recent"
        self.api = None

    def authenticate(self):
        """
        Authenticate using Tweepy's OAuthHandler.
        """
        # auth = tweepy.OAuth1UserHandler(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        # self.api = tweepy.API(auth)
        # print("Twitter authentication successful.")
        if not self.bearer_token:
            raise ValueError("Bearer token is required.")
        print("Twitter v2 authentication successful.")

    def scrape_data(self, query, count):
        """
        Scrape tweets based on a search query.
        """
        # if self.api is None:
        #     raise ValueError("API is not authenticated. Call authenticate() first.")
        
        # tweets = []
        # for tweet in tweepy.Cursor(self.api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
        #     tweets.append({
        #         "text": tweet.full_text,
        #         "created_at": str(tweet.created_at),
        #         "user": tweet.user.scree_name
        #     })
        # print(f"Scraped  {len(tweets)} tweets.")
        # return tweets
        headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }
        params = {
            "query": query,
            "max_results": min(count, 100), # Twitter API allows max 100 per request
            "tweet.fields": "created_at,text,author_id"
        }

        all_tweets = []
        for _ in range(count // 100 + 1):  # Handle multiple requests if needed
            response = requests.get(self.base_url, headers=headers, params=params)
            if response.status_code == 429:
                print("Rate limit exceeded. Waiting for 15 minutes...")
                time.sleep(900)  # Wait 15 minutes (900 seconds) before retrying
                continue
            elif response.status_code != 200:
                raise Exception(f"Error {response.status_code}: {response.text}")
            
            data = response.json()
            tweets = [{
                "text": tweet["text"],
                "created_at": tweet["created_at"],
                "author_id": tweet["author_id"]
            } for tweet in data.get("data", [])]
            all_tweets.extend(tweets)

            if len(tweets) < 100:  # No more tweets available
                break

        print(f"Scraped {len(all_tweets)} tweets.")
        return all_tweets