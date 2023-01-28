import serial
import time

arduinoData = serial.Serial('COMS', 9600)

while True:
    line = arduinoData.readline().decode("utf-8")
    print(line)
    time.sleep(1)