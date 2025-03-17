import requests

def get_weather(city_name):
    api_url = f"https://wttr.in/{city_name}?format=%C+%t+%T"
    weather_response = requests.get(api_url)

    if weather_response.status_code == 200:
        weather_data = weather_response.text.split()
        sky_condition, celsius_temp, fahrenheit_temp = weather_data[0], weather_data[1], weather_data[2]
        
        # Weather emojis dictionary
        weather_emojis = {
            "Clear": "☀️", "Sunny": "🌞", "Cloudy": "☁️", "Overcast": "☁️",
            "Partly": "⛅", "Rain": "🌧️", "Drizzle": "🌦️", "Thunderstorm": "⛈️",
            "Snow": "❄️", "Mist": "🌫️", "Fog": "🌫️"
        }
        
        # Get the emoji for the weather condition, default to Earth emoji if not found
        weather_emoji = next((emoji for key, emoji in weather_emojis.items() if key in sky_condition), "🌍")
        
        print(f"Weather in {city_name}: {sky_condition} {weather_emoji}")
        print(f"Temperature: {celsius_temp}°C ({fahrenheit_temp}°F)")
    else:
        print("Error fetching weather data. Try again.")

# Get user input for location
city_name = input("Enter a location: ")
get_weather(city_name)
