from bs4 import BeautifulSoup
import requests
import cloudscraper
import sys
import io
sys.stdout.reconfigure(encoding='utf-8')
# Get web page link
scraper = cloudscraper.create_scraper(delay = 10)  # returns a CloudScraper instance

response = scraper.get("https://tracker.gg/valorant")

# Print status code and page content
print(f"Status Code: {response.status_code}")
print(response.text) 