from telethon.sync import TelegramClient
from base_scraper import BaseScraper
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramScraper(BaseScraper):
    """
    Scraper for fetching data from Telegram channels using Telethon.
    """

    def __init__(self):
        self.api_id = os.getenv("TELEGRAM_API_ID")
        self.api_hash = os.getenv("TELEGRAM_API_HASH")
        self.client = None

    def authenticate(self):
        """
        Authenticate using Telethon.
        """
        self.client = TelegramClient("session_name", self.api_id, self.api_hash)
        self.client.start()
        print("Telegram authentication successful.")

    def scrape_data(self, channel, limit=100):
        """
        Scrape messages from a Telegram channel.
        """
        if self.client is None:
            raise ValueError("Telegram client is not authenticated. Call authenticate() first.")

        messages = []
        for message in self.client.iter_messages(channel, limit=limit):
            messages.append({
                "text": message.text,
                "date": str(message.date),
                "sender_id": message.sender_id
            })
        print(f"Scraped {len(messages)} messages from {channel}.")
        return messages