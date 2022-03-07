#importing all necessary algorithms
import csv
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import pandas as pd
import gtts
from playsound import playsound

print("")

sound = input("Do you want an audio intro or a textual one? Enter 'audio' or 'text' :-").lower()

print("")

if(sound == "audio"):

    stars = gtts.gTTS("Hello there rocketeer. An important mission has brought us scientists and engineers together.All along we knew that the sun would sustain a billion years till it explodes. Due to certain disasters and star movements, we have found out that the sun is closer to dying now. We have built a technology to shift earth from its orbit to another solar system. But which star exactly? You have been assigned the task to research about stars and tell us which star is the best for Earth! Good luck on Project Light Brigade!! ")
    stars.save("starify.mp3")
    playsound("starify.mp3")

    code = gtts.gTTS("You have to choose between the stars data to scrape. Enter your scraping choice in the input below.")
    code.save("intro.mp3")
    playsound("intro.mp3")

if(sound == "text"):

    print("")

    print("Hello there rocketeer. An important mission has brought us scientists and engineers together.All along we knew that the sun would sustain a billion years till it explodes. Due to certain disasters and star movements, we have found out that the sun is closer to dying now. We have built a technology to shift earth from its orbit to another solar system. But which star exactly? You have been assigned the task to research about stars and tell us which star is the best for Earth! Good luck on Project Light Brigade!! ")
    print("You have to choose wether to scrape or merge the already scraped data. Enter your choice in the input below.")

print("")
print("Scrape")
print("Merge")

dataset = input("Please enter you choice:-").lower()

if(dataset == "scrape"):

    print("Bright Stars")
    print("Dwarf Stars")

    starify = input("Please enter you choice:-").lower()

    if(starify == "bright stars"):

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
            soup = bs(browser.page_source, "html.parser")

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
        df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
        print(df)
        df.to_csv('bright_stars.csv')

        


    if(starify == "dwarf stars"):

        url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

        page = requests.get(url)

        soup = bs(page.text,'html.parser')

        star_table = soup.find_all('table')
        print(len(star_table))

        temp_list= []

        table_rows = star_table[5].find_all('tr')

        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        print(temp_list)

        Star_names = []
        Distance =[]
        Mass = []
        Radius =[]

        for i in range(1,len(temp_list)):
            
            Star_names.append(temp_list[i][0])
            Distance.append(temp_list[i][5])
            Mass.append(temp_list[i][7])
            Radius.append(temp_list[i][8])

        df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
        df2.to_csv('dwarf_stars.csv')


if(dataset == "merge"):

    brights = 'bright_stars.csv'
    dwarfs = 'dwarf_stars.csv'

    df1 = []
    df2 = []

    with open(brights) as f:
        csv_reader =csv.reader(f)
        
        for i in csv_reader:
            df1.append(i)
            
    with open(dwarfs) as f:
        csv_reader = csv.reader(f)
        
        for i in csv_reader:
            df2.append(i)

    brights_headers = df1[0]
    brights_data = df1[1:]

    dwarfs_headers = df2[0]
    dwarfs_data = df2[1:]

    final_headers = brights_headers

    final_data = brights_data + dwarfs_data

    with open("final_stars.csv",'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(final_headers)   
        csvwriter.writerows(final_data)

