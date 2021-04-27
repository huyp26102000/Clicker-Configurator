# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
def write_read(datain):
    arduino.write(bytes(datain, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return str(data.decode("utf-8"))
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value)