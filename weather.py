import requests

# Function to fetch weather data from OpenWeatherMap API
# Function to fetch weather data from OpenWeatherMap API
def get_weather(location, api_key):
    # Construct API URL based on the user input
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Make a request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "Location": data['name'],
            "Temperature": data['main']['temp'],
            "Humidity": data['main']['humidity'],
            "Conditions": data['weather'][0]['description'].capitalize()
        }
        return weather_info
    else:
        # Print the entire error response for more details
        print(f"Error fetching weather data: {response.json()}")
        return None


# Main function to run the weather app
def main():
    # Ask user for a location (city name or ZIP code)
    location = input("Enter a city name or ZIP code to get the current weather: ")
    
    # OpenWeatherMap API key (insert your actual API key here)
    api_key = "2a4e26b2ced8ce5407ffde8217d7d073"  # Your OpenWeatherMap API key
    
    # Fetch and display the weather data
    weather = get_weather(location, api_key)
    if weather:
        print(f"\nWeather in {weather['Location']}:")
        print(f"Temperature: {weather['Temperature']}°C")
        print(f"Humidity: {weather['Humidity']}%")
        print(f"Conditions: {weather['Conditions']}")
if __name__ == "__main__":
    main()
