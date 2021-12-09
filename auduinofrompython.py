import serial

opencr = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout = 1) 

while True:
    number = input('Enter a Number :')
    opencr.write(bytes(number, 'utf-8'))
    value = opencr.readline()
    print ("Result :", value)