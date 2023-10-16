#!/usr/bin/env python

# GrovePi LED blink Example for the Grove LED Socket (http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
"""
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import time
from grovepi import *
from grove_rgb_lcd import *


dht_sensor = 7
setRGB(0, 255, 0)

pinMode(ledGreen, "OUTPUT")
pinMode(ledRed, "OUTPUT")
time.sleep(1)

print(
    "This example will blink a Grove LED connected to the GrovePi+ on the port D{}.\nIf you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.\nYou may also try reversing the direction of the LED on the sensor.".format(
        dht_sensor
    )
)
print(" ")
print("Connect the LED to the D{} port !".format(dht_sensor))

while True:
    try:
        # Read temperature and humidity from the DHT sensor
        [temperature, humidity] = dht(dht_sensor, 0)

        # Check if the data is valid
        if isnan(temperature) is False and isnan(humidity) is False:
            # Print temperature and humidity to the terminal
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

            # Display the information on the RGB LED display
            setText_norefresh(f"Temp: {temperature}°C\nHumidity: {humidity}%")

        else:
            print("Failed to read data from DHT sensor")

        time.sleep(2)  # Adjust the delay as needed for your desired update rate

    except KeyboardInterrupt:  # Turn LED off before stopping
        digitalWrite(ledGreen, 0)
        digitalWrite(ledRed, 0)
        break
    except IOError:  # Print "Error" if communication error encountered
        print("Error")
