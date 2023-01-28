#include <Arduino.h>

#define BUTTONPIN 2 // check pin
#define LEDPIN 3 // check pin

int button_state = 0;
uint32_t mode = 0;

void setup() {
    pinMode(BUTTONPIN, INPUT);
}

void loop() {
    buttonstate = digitalRead(BUTTONPIN);

    if (button_state == HIGH) {
        digitalWrite(ledPin, HIGH);
    } else {
        digitalWrite(ledPin, LOW);
    }
}
