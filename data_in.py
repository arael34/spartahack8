import serial
import time

arduinoData = serial.Serial('COM7', 9600)

while True:
    if arduinoData.inWaiting() > 0:
        line = arduinoData.readline().decode("utf-8")
        print(line)
        # check if temp is too high 
    