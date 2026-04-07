import serial

gps = serial.Serial('COM3', 9600, timeout=1)

while True:
    data = gps.readline().decode().strip()
    print(data)