from bs4 import BeautifulSoup
import html
import requests
# Get web page link
html_content = requests.get("https://tracker.gg/valorant")   
# Create a BeautifulSoup object
soup = BeautifulSoup(html_content.text, "html.parser")
print(soup.prettify)
