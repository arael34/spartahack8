# Spartahack 8 project
by JJA

## Inspiration
Honestly, we just grabbed an Arduino Uno from the hardware room, read the docs, and went from there. Our original idea was to try to predict the weather from temperature and humidity readings and we went in that direction for half of the first day. Then, Amrit came up with the idea of a safety system and that's where we're at now. 
## What it does
We programmed the OLED display to display simple statistics, like temperature, humidity, and noise level. The display can be cycled through by pressing a button on the board. Furthermore, it prints temperature and noise level to a serial port. If the temperature is abnormally high or low, it will send the user a text message notifying them, through Twilio. The user can also text simple commands like "sound" to receive current measurements. 
## How we built it
We started with the Arduino docs on the board, so the first feature implemented was the OLED display. This can be done relatively easily with the built-in libraries:
```c++
#include "DHT.h"

#define DHTPIN 3
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE); // setup
float temp = dht.readTemperature();
Serial.println(temp);
```
The code snippet above uses the DHT reader to measure the current temperature, in Celsius, as a float. It then prints to the serial port.

We then listen on that port in a python script:
```python
arduinoData = serial.Serial('COM7', 9600)
while True:
  if arduinoData.inWaiting() > 0:
    block = arduinoData.readline().decode("utf-8")
```
This data can then be processed. Finally, we used the Twilio API and Ngrok to send and receive messages. 
## Challenges we ran into
The biggest challenge was that we only had one Arduino board so only one person could effectively test their code at a time. This was pretty inconvenient and we had to frequently swap laptops, which had different port numbers. Testing text messages was difficult as well. T-mobile starts blocking messages if it detects spam and Twilio is sometimes detected as such. Overall, workflow was our greatest challenge. 
## Accomplishments that we're proud of
This was the first hackathon for all of us, so we're proud to have created a somewhat coherent project without any ideas going in. For the most part, it works as intended. 
## What we learned
We learned a lot about reading, processing and sending data to a server. This is important because we want users to be able to communicate with the device from their phones. We also learned how to use many python libraries. 
## What's next for our project
A feature that we wanted to add but didn't have the time for was a much better user experience. Right now, most of our intended functionality was implemented, but it's difficult to use without reading documentation. A userauth system and better ux are next.
