import requests
from plyer import notification

city_name = input('Enter the city name: ')
API_KEY = 'c14dbafdd2ad4a465963ca14e66ed5e1'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather_desc = data['weather'][0]['description']
    temperature = data['main']['temp']

    # Display Notification
    notification_title = f"Weather Update: {city_name}"
    notification_message = f"Condition: {weather_desc}\nTemperature: {temperature}°C"

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name="Weather Notifier",
        timeout=10  # Notification duration in seconds
    )
else:
    notification.notify(
        title="Error",
        message="City not found or invalid API key.",
        app_name="Weather Notifier",
        timeout=5
    )
p