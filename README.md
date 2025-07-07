# Weather-Forecast-Application

This repository contains a basic Python script that fetches and displays current weather data for a specified city. It uses the OpenWeatherMap API to get the weather information.

Project Structure
weather_app_simple.py: The main Python script that handles fetching and displaying weather data.

weather_app_simple.py - Code Overview
This Python script is a simple command-line tool for getting quick weather forecasts.

Key Components:
Import Libraries:

requests: Used to make HTTP requests to the OpenWeatherMap API.

Configuration:

API_KEY: A placeholder for your OpenWeatherMap API key. You must replace 'your_api_key_here' with your actual API key.

city: Prompts the user to enter the name of the city they want to get the weather for.

Construct API URL:

url: Builds the complete API endpoint URL using the provided city name, your API key, and specifies units=metric for Celsius temperatures.

Fetch Weather Data:

response = requests.get(url): Sends an HTTP GET request to the constructed URL.

data = response.json(): Parses the JSON response received from the API into a Python dictionary.

Display Weather Information:

The script checks response.status_code.

If 200 (OK), it extracts and prints the city name, weather description, temperature in Celsius, and humidity.

If the status code is not 200, it prints an error message indicating that the city was not found or there was an API error.

Dependencies
The weather_app_simple.py script relies on the following external Python library:

requests: For making HTTP requests.

You can install it using pip:

pip install requests

How to Run
Obtain an API Key: Get a free API key from OpenWeatherMap.

Configure API Key:

Open weather_app_simple.py.

Replace 'your_api_key_here' in the API_KEY variable with your actual OpenWeatherMap API key.

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key

Save the script: Save the provided code as weather_app_simple.py (or any other .py file name you prefer).

Install Dependencies: Ensure you have the requests library installed (as shown in the Dependencies section above).

Execute: Run the script from your terminal:

python weather_app_simple.py

The script will prompt you to "Enter city name:". Type the city name (e.g., London, Tokyo) and press Enter to see the weather forecast.

**Output**
![WhatsApp Image 2025-07-05 at 20 11 36_18a5b86b](https://github.com/user-attachments/assets/44902446-b036-4cf2-a8da-8fbdc43346a7)
