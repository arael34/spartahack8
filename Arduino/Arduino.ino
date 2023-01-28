#include <Arduino.h>
#include <Wire.h>
#include <U8x8lib.h> // OLED
#include "DHT.h" // temp/humidity
#include "Seeed_BMP280.h" // air pressure

/*
Mode 1: temperature/humidity
Mode 2: air pressure
Mode 3: light/sound level
Mode 4: acceleration MAYBE
*/
#define MODECOUNT 3

// check pins every time
#define BUTTONPIN 6
#define DHTPIN 3
#define SOUNDPIN 162
#define LIGHTPIN 166
#define DHTTYPE DHT11
// #define ROTARYPIN 160
// #define LEDPIN 3

// OLED display
U8X8_SSD1306_128X64_ALT0_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

DHT dht(DHTPIN, DHTTYPE);
BMP280 bmp280;

uint32_t mode = 1;
int previous_button_state = 0;

void setup() {
  // pin modes
  pinMode(BUTTONPIN, INPUT);
  pinMode(DHTPIN, INPUT); // maybe INPUT_PULLOUT?
  pinMode(SOUNDPIN, INPUT);
  pinMode(LIGHTPIN, INPUT);

  // initializations
  Serial.begin(9600);
  dht.begin();
  u8x8.begin();
  u8x8.setPowerSave(0);
  u8x8.setFlipMode(1);
  if (!bmp280.init()) {
    Serial.println("air pressure device not connected or broken");
  }
}

void loop() {
  int button_state = digitalRead(BUTTONPIN);
  // int rotary_value = analogRead(ROTARYPIN) % 4;
  if (button_state != previous_button_state && button_state == HIGH) {
    mode = mode < MODECOUNT ? mode + 1 : 1;
    u8x8.clear();
  }

  u8x8.setFont(u8x8_font_chroma48medium8_r);
  u8x8.setCursor(0, 0);
  float temp = dht.readTemperature();
  Serial.println(temp);
  switch(mode) {
    case 1: {
      u8x8.print("Temp: ");
      u8x8.print(temp);
      u8x8.print("C");
      u8x8.setCursor(0, 25);
      float humid = dht.readTemperature();
      u8x8.print("Humidity: ");
      u8x8.print(humid);
      u8x8.print("%");
      break;
    }
    case 2: {
      float pressure = bmp280.getPressure();
      u8x8.print("Pressure: ");
      u8x8.setCursor(0, 25);
      u8x8.print(pressure);
      u8x8.print("Pa");
      break;
    }
    case 3: {
      int sound_state = analogRead(SOUNDPIN);
      int light_state = analogRead(LIGHTPIN);
      u8x8.print("Noise level: ");
      u8x8.print(sound_state);
      u8x8.setCursor(0, 25);
      u8x8.print("Light level: ");
      u8x8.print(light_state);
      break;
    }
    default:
      u8x8.print("Error: reached default case");
  }
  u8x8.refreshDisplay();
  delay(50);
  previous_button_state = button_state;
}
