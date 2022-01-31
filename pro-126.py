
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
)
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
headers=['name', 'distance', 'mass', 'radius']
star_data=[]
star_data.append(temp_list)
print(star_data)
with open("scrapper-stars.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(temp_list)