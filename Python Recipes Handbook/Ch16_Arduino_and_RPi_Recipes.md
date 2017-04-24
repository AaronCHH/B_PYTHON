
# Chapter 16: Arduino and RPi Recipes
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 16: Arduino and RPi Recipes](#chapter-16-arduino-and-rpi-recipes)
  * [16-1. Sending Data to an Arduino](#16-1-sending-data-to-an-arduino)
  * [16-2. Reading Data from an Arduino](#16-2-reading-data-from-an-arduino)
  * [16-3. Writing to the Raspberry Pi’s GPIO Bus](#16-3-writing-to-the-raspberry-pis-gpio-bus)
  * [16-4. Reading from the Raspberry Pi’s GPIO Bus](#16-4-reading-from-the-raspberry-pis-gpio-bus)

<!-- tocstop -->


## 16-1. Sending Data to an Arduino
* Problem
* Solution
* How It Works


```python
pip install --user pyserial
```


```python
import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)
ser.write(b'5')
```

## 16-2. Reading Data from an Arduino
* Problem
* Solution
* How It Works


```python
import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)
data = ser.readline()
```

## 16-3. Writing to the Raspberry Pi’s GPIO Bus
* Problem
* Solution
* How It Works


```python
sudo apt-get install python-dev python-rpi.gpio
```


```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(1, GPIO.HIGH)
```

## 16-4. Reading from the Raspberry Pi’s GPIO Bus
* Problem
* Solution
* How It Works


```python
import RPi.GPIO asGPIO
GPIO.setup(1, GPIO.IN)
if GPIO.input(1):
    print('Input was HIGH')
else:
    print('Input was LOW')
```
