class Analysis(Weather):
    def __init__(self, location, date):
        super().__init__(location, date)  
        self.data = None

    def analyze(self):
        self.data = self.weather_data()
        print(self)
        print(self.current_location())
        print(self.current_temperature())
        print(self.current_date())

        average_temp = self.average_temp()
        print(f"Average Temperature: {average_temp}")

        cloth_suggestion = self.cloth_suggestion(self.temperature)
        print(cloth_suggestion)

        condition_message = self.condition(self.data["days"][0]["conditions"])
        print(condition_message)

        kelvin_temp = self.kelvin(self.temperature)
        print(f"{kelvin_temp}")

        fahrenheit_temp = self.fahrenheit(self.temperature)
        print(fahrenheit_temp)

    def average_temp(self):
        df = pd.DataFrame(self.data["days"])
        average = df["temp"].mean()
        return average
        
    def cloth_suggestion(self, temperature):
        if temperature > 30:
            return "It must be summer now! So hot!"
        elif temperature < 10:
            return "It's quite cold outside. Make sure to bundle up!"
        else:
            return "The temperature is moderate. Wear something comfortable."

    def condition(self, condition):
        if condition == "Rainy":
            return "It's rainy outside! Remember to take an umbrella!"
        elif condition == "Sunny":
            return "Wow! What a sunny day! It's a great opportunity to go out and enjoy nature."
        elif condition == "Cloudy":
            return "It's cloudy now."
        else:
            return "The weather is a bit unusual now. Please take care! Try again later it may change."

    def kelvin(self, temperature):
        k_temperature = temperature + 273.15
        return f"The temperature is displayed in Kelvin: {k_temperature}."

    def fahrenheit(self, temperature):
        f_temperature = temperature * (9/5) + 32
        return f"The temperature is displayed in Fahrenheit: {f_temperature}."