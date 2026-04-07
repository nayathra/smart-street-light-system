def decide_brightness(vehicle_count, pedestrian, weather):

    weather = weather.lower()

    brightness = 30

    if pedestrian:
        brightness = 60

    if vehicle_count >= 1:
        brightness = 80

    if "rain" in weather or "fog" in weather or "mist" in weather:
        brightness = 90

    if vehicle_count >= 2:
        brightness = 100

    return brightness


def predictive_lighting(vehicle_count):

    if vehicle_count == 0:
        pole1 = 30
        pole2 = 30
        pole3 = 30

    elif vehicle_count == 1:
        pole1 = 100
        pole2 = 80
        pole3 = 60

    else:
        pole1 = 100
        pole2 = 100
        pole3 = 80

    return pole1, pole2, pole3