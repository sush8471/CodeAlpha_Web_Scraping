# Web Scraping Project – CodeAlpha Internship Task 1


import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"




# Step 1: Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



# Step 2: Locate and read the top-grossing films table
table = soup.find("table", class_="wikitable")
df = pd.read_html(StringIO(str(table)))[0]




# Step 3: Clean and rename columns
df = df[['Title', 'Worldwide gross', 'Year']]
df.columns = ['Title', 'Gross', 'Year']




# Step 4: Save to CSV
df.to_csv("highest_grossing_movies.csv", index=False)
print("✅ Data scraped and saved to highest_grossing_movies.csv")
