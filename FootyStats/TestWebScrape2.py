import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.sofascore.com/tournament/football/england/premier-league/17#id:61627" # Example URL
response = requests.get(url)
response.raise_for_status() # Raise an exception for bad status codes
soup = BeautifulSoup(response.content, "html.parser")

# # Example: Find the table containing match results
# table = soup.find("div", {"class": "Box klGMtt"})
#
# # Example: Extract data from the table
# rows = table.find_all("tr")
# data = []
# for row in rows[1:]:  # Skip the header row
#     cells = row.find_all("td")
#     # Extract relevant data from each cell
#     match_date = cells[0].text
#     home_team = cells[1].text
#     away_team = cells[3].text
#     home_score = cells[2].text
#     away_score = cells[4].text
#     data.append([match_date, home_team, away_team, home_score, away_score])

print(response.content)