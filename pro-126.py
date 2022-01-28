from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time,os,ssl
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

browser=webdriver.Chrome("chromedriver")

browser.get(START_URL)
time.sleep(10)

def scrap():
    headers = ["V-Mag","Proper name","Bayer-designation","distance","Spectral Class","Mass","Radius","luminosity"]
    planet_data=[]
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(planet_data)
    
scrap()
