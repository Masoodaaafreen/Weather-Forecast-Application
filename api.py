import requests
API_KEY = "Put your API KEY here"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print("City not found or API error.")
