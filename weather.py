from key import API_KEY     #Import my API_KEY from another file
import requests
import pandas as pd

class weather:
    def __init__(self, location, date=None):     #Location is mandatory, but date is not. 
        self.location = location
        self.temperature = None    #Since I didn't ask this part at the beginning. So, I just leave a None here.
        self.date = date
        self.url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}?unitGroup=metric&key={api}&contentType=json"

    
    def current_location(self):
        return f"This is the weather result for {self.location}."
    def current_temperature(self):
        return f"The current temperature is {self.temperature}"
    def current_date(self):
        return f"This is the latest data. It was the data of {self.date}"

    
    def __str__(self):
        return f"Location:{self.location}\nDate:{self.date}\nToday's Average Temperature:{self.temperature}"

    
#To get the basic data from the API link. 
    def weather_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()

#It has multiple days under the "days" object, so I only call the 1st one which represents the current time. 
            self.temperature = data["days"][0]["temp"]
            self.date = data["days"][0]["datetime"]
            return data
        else:
            return "Oops! It looks like something went wrong! Please try again later!"
        

