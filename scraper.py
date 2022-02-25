import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver")
browser.get(start_url)


time.sleep(10)

headers = ["Proper name", "Distance", "Mass", "Radius"]
planet_data = []

def Scrape():

    for i in range(0, 100):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for tr_tag in soup.find_all("tr"):
            td = tr_tag.find_all("td")
            temp_list = []

            for index, td_tags in enumerate(td):
                
                if index == 1 :
                    temp_list.append(td_tags.find_all("a")[0].contents[0])
                    
                else:

                    try:
                        temp_list.append(td_tags.contents[0])

                    except:
                        temp_list.append("")
                        planet_data.append(temp_list)
        
        browser.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/table").click()

Scrape()


with open("Scraper.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)




