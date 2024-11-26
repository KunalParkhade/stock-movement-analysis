import praw
from base_scraper import BaseScraper
import os
from dotenv import load_dotenv

load_dotenv()

class RedditScraper(BaseScraper):
    """
    Scraper for fetching data from Reddit using the PRAW library.
    """

    def __init__(self):
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")
        self.reddit = None

    def authenticate(self):
        """
        Authenticate using PRAW.
        """
        self.reddit = praw.Reddit(
            client_id = self.client_id,
            client_secret = self.client_secret,
            user_agent = self.user_agent
        )
        print("Reddit authentication successful.")

    def scrape_data(self, subreddit, limit=100):
        """
        Scrape posts from a subreddit.
        """
        if self.reddit is None:
            raise ValueError("Reddit is not authenticated. Call authenticate() first.")
        
        posts = []
        for submission in self.reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({
                "title": submission.title,
                "created_at": submission.created_utc,
                "score": submission.score,
                "num_comments": submission.num_comments
            })
        print(f"Scraped {len(posts)} posts from r/{subreddit}.")
        return posts