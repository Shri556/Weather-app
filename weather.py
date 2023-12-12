import requests

def weather_details(location):
    api_key = open("weather_api.txt").read()
    
    Base_url = "https://api.weatherapi.com/v1/"
    endpont = "current.json"
    url = f"{Base_url}{endpont}?key={api_key}&q={location}"
    response = requests.get(url)
    weather_dictionary = {}
    if response.status_code == 200:
        weather_data = response.json()
        
        weather_dictionary["location"] = f"{weather_data['location']['name']} , {weather_data['location']['country']}"
        weather_dictionary["temp_c"] = f'{weather_data["current"]["temp_c"]}°'
        weather_dictionary["temp_f"] = weather_data["current"]["temp_f"]
        weather_dictionary['condition'] = weather_data["current"]["condition"]["text"]
        weather_dictionary['Icon'] = weather_data['current']['condition']['icon']
        weather_dictionary['humidity'] = f"{weather_data['current']['humidity']} %"
        weather_dictionary['windspeed'] = f"{weather_data['current']['wind_kph']} km/hr"
        weather_dictionary['pressure'] = f"{weather_data['current']['pressure_mb']} millibars"
        weather_dictionary['precipitation'] = f"{weather_data['current']['precip_in']} inches"
        weather_dictionary['Gust'] = f"{weather_data['current']['gust_kph']} km/hr"
        weather_dictionary['uv_index'] = f"{weather_data['current']['uv']}"
        
        weather_dictionary['Icon'] = weather_dictionary['Icon'].split('/')
        weather_dictionary['Icon'][-1] = weather_dictionary['Icon'][-1].replace('png','svg')
        weather_dictionary['Icon'] = weather_dictionary['Icon'][-2] + "/" + weather_dictionary['Icon'][-1]
        
        return weather_dictionary
    else:
        return f"ERROR: {response.status_code} - {response.text}"
    
    
def forecast_details(location):
    api_key = open("weather_api.txt").read()
    
    Base_url = "https://api.weatherapi.com/v1/"
    endpont = "forecast.json"
    url = f"{Base_url}{endpont}?key={api_key}&q={location}"
    response = requests.get(url)
    forecast_dictionary = {}
    
    if response.status_code == 200:
        forecast_data = response.json()
        hourly_data = forecast_data["forecast"]["forecastday"][0]['hour']
        
        for i in hourly_data:
            timestamp = i["time"]
            timestamp = timestamp.split(" ")
            time = timestamp[-1]
            
            icon = i["condition"]["icon"]
            icon_location = icon.split("/")
            icon_location[-1] = icon_location[-1].replace("png","svg")
            icon_location = icon_location[-2] + "/" + icon_location[-1]
            
            temp_c = int(round(float(i["temp_c"])))
            temp_c = str(temp_c) + "°"
            
            forecast_dictionary[time] = {"logo":icon_location,"temp_c":temp_c}
        return forecast_dictionary
    else:
        return f"ERROR: {response.status_code} - {response.text}"