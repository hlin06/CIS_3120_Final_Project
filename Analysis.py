from weather import Weather

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

        cloth_suggestion = self.cloth_suggestion(self.temperature)
        print(cloth_suggestion)

        condition_message = self.condition(self.data["days"][0]["conditions"])
        print(condition_message)

        kelvin_temp = self.kelvin(self.temperature)
        print(f"{kelvin_temp}°K")

        fahrenheit_temp = self.fahrenheit(self.temperature)
        print(f"{fahrenheit_temp}°F")

    def cloth_suggestion(self, temperature):
        if temperature > 30:
            return "It must be summer now! So hot!"
        elif temperature < 10:
            return "It's quite cold outside. Make sure to bundle up!"
        else:
            return "The temperature is moderate. Wear something comfortable."

    def condition(self, condition):
        return f"This is the description for today: {self.data["description"]}"

    def kelvin(self, temperature):
        k_temperature = temperature + 273.15
        return f"The temperature is displayed in Kelvin: {k_temperature}°K."

    def fahrenheit(self, temperature):
        f_temperature = temperature * (9/5) + 32
        return f"The temperature is displayed in Fahrenheit: {f_temperature}°F."
