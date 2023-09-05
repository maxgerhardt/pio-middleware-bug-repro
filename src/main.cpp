#include <Arduino.h>
#include "MyTestLib.h"

void setup() {
    Serial.begin(9600);
}

void loop() {
    int ret = MyTestLib_Function();
    Serial.println(ret);
    delay(1000);
}