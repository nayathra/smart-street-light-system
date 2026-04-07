import requests
from datetime import datetime

API_KEY = "ebd2be1b2553911f6625a0527e826546"
CITY = "Chennai"


def street_light_logic(condition):

    condition = condition.lower()

    if "clear" in condition:
        return "White", "100%"

    elif "cloud" in condition:
        return "Warm Yellow", "80%"

    elif "rain" in condition or "drizzle" in condition:
        return "Blue", "90%"

    elif "thunderstorm" in condition:
        return "Purple", "100%"

    elif "mist" in condition or "fog" in condition:
        return "Yellow", "100%"

    elif "snow" in condition:
        return "Cool White", "90%"

    else:
        return "White", "70%"


def time_based_brightness():

    hour = datetime.now().hour

    if 0 <= hour < 4:
        return "100%"

    elif 4 <= hour < 6:
        return "100%"

    elif 6 <= hour < 7:
        return "50%"

    elif 7 <= hour < 17:
        return "0%"

    elif 17 <= hour < 18:
        return "50%"

    else:
        return "100%"


def get_weather_light():

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        weather = data["weather"][0]["description"]

        color, brightness_weather = street_light_logic(weather)
        brightness_time = time_based_brightness()

        return weather, color, brightness_weather, brightness_time

    except Exception as e:

        print("Weather API Error:", e)
        return "unknown", "White", "70%", "70%"


# Test section
if __name__ == "__main__":

    weather, color, brightness_weather, brightness_time = get_weather_light()

    print("\n🌦 Weather Module Test\n")

    print("Weather Condition:", weather)
    print("Street Light Colour:", color)
    print("Brightness (Weather):", brightness_weather)
    print("Brightness (Time):", brightness_time)