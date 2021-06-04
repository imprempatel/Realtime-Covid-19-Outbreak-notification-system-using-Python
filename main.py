from plyer import notification
import requests
from bs4 import BeautifulSoup,NavigableString
import time

def notifyMe(title, message):   
    notification.notify(        # syntax for notification function provided by plyer module
        title = title,
        message = message,
        app_icon = r'C:\Users\PREM PATEL\Desktop\MiniProject\corona_virus.ico', #give your own path 
        timeout = 5
    )


def getData(url):
    r = requests.get(url)   #request.get method is a function provided by request module
    return r.text

if __name__ == "__main__":
    while True:
        myHtmlData = getData('https://www.mygov.in/covid-19/')
        soup1 = BeautifulSoup(myHtmlData, 'html.parser')
        div_bs4 = soup1.find_all('div', id = "stateCount")
        data=""
        for div in div_bs4:
            data+=div.get_text()
        # print(data)
        itemList = data.split("\n\n\n\n")
        # print(itemList[1:])
        state=['Maharashtra'] #name of state you want to display
        for item in itemList[1:]:
            finaldata=item.split('\n\n')
            finaldata = [x.replace("\n"," ") for x in finaldata]
            if str(state[0]) in str(finaldata[0]):
                title = 'Cases of Covid-19'
                message=f"State - {state[0]}\nCovid-Cases  : {finaldata[1]}"
                notifyMe(title,message)
                time.sleep(2)
        time.sleep(3600)  #notification repetition time (here 3600s=1hour i.e after every 1 hour the notification will popped up)
        
        
