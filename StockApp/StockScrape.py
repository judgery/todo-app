import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from openpyxl import Workbook

headers = {'user-agent': 'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64; rv:136.0) \
            Gecko/20100101 Firefox/136.0'}

urls = [
    'https://groww.in/us-stocks/nke',
    'https://groww.in/us-stocks/tlph',
    'https://groww.in/us-stocks/flws',
    'https://groww.in/us-stocks/etnb',
    'https://groww.in/us-stocks/acmr',
    'https://groww.in/us-stocks/afcg',
    'https://groww.in/us-stocks/amc',
    'https://groww.in/us-stocks/acrs',
    'https://groww.in/us-stocks/ades',
    'https://groww.in/us-stocks/amtx',
    'https://groww.in/us-stocks/afmd',
    'https://groww.in/us-stocks/agl',
    'https://groww.in/us-stocks/allk',
    'https://groww.in/us-stocks/amrn',
    'https://groww.in/us-stocks/poww',
    'https://groww.in/us-stocks/aqb',
    'https://groww.in/us-stocks/apwc',
    'https://groww.in/us-stocks/astr',
    'https://groww.in/us-stocks/alot'
]

all = []
for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        company = soup.find('h1', {'class': 'usph14Head displaySmall'}).text
        price = soup.find('span', {'class': 'uht141Pri contentPrimary displayBase'}).text
        try:
            change = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentNegative'}).text.split('(')[0]
        except Exception:
            change = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentPositive'}).text.split('(')[0]
        try:
            perchange = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentNegative'}).text.split('(')[1]
        except Exception:
            perchange = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentPositive'}).text.split('(')[1]
        #change = soup.find_all('div', {'class': ['uht141Day bodyBaseHeavy contentNegative', 'uht141Day bodyBaseHeavy contentPositive']}).text
        #volume = soup.find('td', {'class': 'col l3 bodyLargeHeavy'}).find_all('td').text
        start = '('
        end = ')'
        percentageChange = perchange[perchange.find(start)+len(start):perchange.rfind(end)]
        x = [company, price, change, percentageChange]#, volume]
        all.append(x)

    except AttributeError:
        print("Change the Element id")
    # Wait for a short time to avoid rate limiting
    time.sleep(1)

# print(change)

column_names = ["Company", "Price", "Changes", "Percentage Change"]
df = pd.DataFrame(columns=column_names)
for i in all:
    index = 0
    df.loc[index] = i
    df.index = df.index + 1
df = df.reset_index(drop=True)
df.to_excel('stocks.xlsx')
