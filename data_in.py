import serial
import time

arduinoData = serial.Serial('COM7', 9600)

while True:
    if arduinoData.inWaiting() > 0:
        line = arduinoData.readline().decode("utf-8")
        print(line)
        # need to read line by line, careful
        temps = map(float, line.split('\n'))
        for temp in temps:
            if temp > 60: # arbitrary
                break # twilio too hot
            elif temp < 0:
                break # twilio too cold
    