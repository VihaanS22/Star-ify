#importing all necessary algorithms
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd
import gtts
from playsound import playsound


#initializing a url of the star data to be scraped
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


#using chromedriver to get the url var and put it in a browser var. To open up the table when the code is run
browser = webdriver.Chrome("chromedriver")
browser.get(start_url)

#sleeping the code for some time to get the program ready for extraction
time.sleep(10)


#making arrays for all the data to be extracted
Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

#making a function scrape to scrape the data using all the inputs mentioned above
def Scrape():

    #using beautiful soup to get to the page source and use the inspect option to extract in form of html
    soup = BeautifulSoup(browser.page_source, "html.parser")

    #making a temporary list and extracting data from all the tr and then td tags
    
    temp_list = []
    for tr_tag in soup.find_all("tr"):
        td = tr_tag.find_all("td")
        row = []
        
        for i in td:
            row.append(i.text.rstrip())
        temp_list.append(row)   
                
    #Appending the data in the arrays made before for the data points
    for i in range(1,len(temp_list)):
        Star_names.append(temp_list[i][1])
        Distance.append(temp_list[i][3])
        Mass.append(temp_list[i][5])
        Radius.append(temp_list[i][6])
        Lum.append(temp_list[i][7])

#mentioning the function to use and start it
Scrape()

#making a df to group all the appended arrays together and naming columns. Then changing the df to a csv file.
df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)
df.to_csv('Scraper.csv')


stars = gtts.gTTS("Hello there rocketeer. An important mission has brought us scientists and engineers together.All along we knew that the sun would sustain a billion years till it explodes. Due to certain disasters and star movements, we have found out that the sun is closer to dying now. We have built a technology to shift earth from its orbit to another solar system. But which star exactly? You have been assigned the task to research about stars and tell us which star is the best for Earth! Good luck on Project Light Brigade!! ")
stars.save("starify.mp3")
playsound("starify.mp3")

code = gtts.gTTS("The given code is a program made to execute some info of your research which we have filtered. You will receive further updates on further parts of Project Light Brigade to further pre-process and clean the data. You shall then try to find a suitable star for us!")
code.save("intro.mp3")
playsound("intro.mp3")