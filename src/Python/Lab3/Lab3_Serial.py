#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:16:26 2020

@author: iris
"""

import serial

#Make the variables below global
string_buffer = []
data_array = np.array([])



def setup_serial():
    serial_name = '/dev/cu.usbserial-14340'  # replacing using the actual port 
    ser = serial.Serial(serial_name,115200)    # open serial port 
    print(ser.name)
    return ser 

def send_serial(ser):
    S = 'Hello World\n'
    ser.write(S.encode('utf-8'))   # write a string     
    
    
def read_serial(ser):
    s = ser.read(10).decode('utf-8')   #read 30 bytes and decode it 
    print(s)


def read_serial2(ser):
    n=0
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        print(s)
        n=n+1

def read_serial3(ser):
    n=0
    full_string = []
    while (n<30):
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        if (s != '\n' and s != '\r'):
            full_string.append(s)
            n=n+1
    print(full_string)

def readSerial4(ser):
    while True:
        try:
            s = ser.read(1)         # read 1 byte and decode to utf-8
            print(s)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break


    
    
def main():
    ser = setup_serial()
    readSerial4(ser)
    ser.close()


if __name__=='__main__':
    main()