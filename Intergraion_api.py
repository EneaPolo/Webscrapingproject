import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    # Kontrollo statusin e përgjigjes
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return "Error fetching data"
    
    data = response.json()
    
    # Printimi i të dhënave për të parë strukturën
    print(data)  # Kjo do të tregojë të dhënat e marra

    if "main" in data:
        temperature = data['main']['temp']
        return temperature
    else:
        print("Main key not found in response")
        return "Temperature data not available"

# Përdorimi
city = "London"
api_key = "your_api_key_here"  # Vendosni çelësin tuaj të API
temperature = get_weather(city, api_key)
print(f"Temperature in {city}: {temperature}")
