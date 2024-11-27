from dotenv import load_dotenv
import os
import json

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
        Save scraped data to a file, appending if the file already exists.
        """
        # Check if the file exists
        if os.path.exists(file_path):
            # If the file exists, read the existing data and append new data
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
            # Append the new data to the existing data
            existing_data.extend(data)
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
            print(f"Appended data to {file_path}")
        else:
            # If the file doesn't exist, create it and write the data
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {file_path}")