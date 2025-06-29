import requests
from twilio.rest import Client
import os

# Your location
MY_LAT = 24.8968309
MY_LONG = 67.0705956

# API keys from GitHub Secrets
API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Check 4 future 3-hour blocks = next 12 hours
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check if rain is expected
umbrella_needed = any(
    forecast["weather"][0]["id"] < 700 for forecast in weather_data["list"]
)

if umbrella_needed:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="🌧️ Heads up! Rain is expected today during your commute. Take an umbrella! ☔",
        from_="+12679362692",  # Your Twilio number
        to="+923272457411"     # Your phone number
    )
    print(message.status)
else:
    print("No rain expected in the next 12 hours.")
