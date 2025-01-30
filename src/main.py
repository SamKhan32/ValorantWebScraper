from bs4 import BeautifulSoup
import html
import requests
# Get web page link
html_content = requests.get("https://requests.readthedocs.io/en/latest/")
# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")
