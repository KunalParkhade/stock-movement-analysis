from dotenv import load_dotenv
import os

def load_env():
    """
    Load environment variables from .env file.
    """
    load_dotenv()   

class BaseScraper:
    """
    A base class for all scrapers to ensure a consistent structure.
    """
    def authenticate(self):
        """
        Authentication method for platform APIs (to be overridden by subclasses).
        """
        raise NotImplementedError("Authenticate method not implemented.")
    
    def scrape_data(self, **kwargs):
        """
        Scrape data from the platform (to be overridden by subclasses).
        """
        raise NotImplementedError("Scrape data method not implemented.")
    
    def save_data(self, data, file_path):
        """
        Save scraped data to a file.
        """
        import json
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {file_path}")