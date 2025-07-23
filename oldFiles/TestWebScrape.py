import options
from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import concurrent.futures

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) firefox/91.0.4472.124 Safari/537.36')

#service = Service("C:\\Users\\judge\\AppData\\Local\\Programs\\Python\\Python313\\pythonProject1\\.venv\\Lib\\site-packages\\selenium\\webdriver\\firefox\\")
driver = webdriver.firefox(service=service, options=options)


# URL of the sitemap
sitemap_url = "https://www.oddschecker.com/sport/football/sitemap.xml"

try:
    # Load the sitemap page
    driver.get(sitemap_url)

    time.sleep(5)

    xml_content = driver.page_source
    soup = BeautifulSoup(xml_content, 'xml')

    url_tags = soup.find_all('loc')
    urls = [url_tag.text for url_tag in url_tags]

    print(f"Found {len(urls)} URLs.")
    print(urls)

finally:
    # Close the browser
    driver.quit()
