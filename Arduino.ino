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

// check pins for all
#define BUTTONPIN D6
#define DHTPIN D3
#define SOUNDPIN A2
#define LIGHTPIN A6
#define DHTTYPE DHT11
// #define LEDPIN 3

// OLED display
U8X8_SSD1306_128X64_ALT0_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

DHT dht(DHTPIN, DHTTYPE);
BMP280 bmp280;

int button_state = 0;
uint32_t mode = 1;

void setup() {
    // pin modes
    pinMode(BUTTONPIN, INPUT);
    pinMode(DHTPIN, INPUT); // maybe INPUT_PULLOUT?

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
    buttonstate = digitalRead(BUTTONPIN);

    if (button_state == HIGH) {
        if (mode < MODECOUNT) {
            ++mode;
        } else {
            mode = 1;
        } // this could be cleaner with ternary
        delay(1000);
    } 

    // int sound_state = analogRead(SOUNDPIN);
    // int light_state = analogRead(LIGHTPIN);

    // float pressure; bmp280.getTemperature();

    u8x8.setFont(u8x8_font_chroma48medium8_r);
    u8x8.setCursor(0, 0);
    switch(mode) {
        case 1:
            u8x8.print("temp/humid");
            break;
        case 2:
            u8x8.print("air pressure");
            break;
        case 3:
            u8x8.print("light/sound");
            break;
        default:
            u8x8.print("Error: reached default case");
    }

    // delay(1000); // one second delay
}
