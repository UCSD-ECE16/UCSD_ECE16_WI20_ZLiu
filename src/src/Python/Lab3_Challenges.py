#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:38:46 2019

@author: edwardwang
"""

import serial
import time
import numpy as np
import matplotlib.pyplot as plt

string_buffer = []
data_array = np.array([])

def setupSerial():
    serial_name = '/dev/cu.Edward_Firebeetle-ESP32'
    serial_name = '/dev/cu.usbserial-14220'
    ser = serial.Serial(serial_name, 115200)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def sendSerial(ser, message):
    ser.write(message.encode('utf-8'))         # write a string

def readSerial(ser):
    while True:
        try:
            s = ser.read(1).decode('utf-8')        # read 1 byte
            print(s)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break

def readSerial_1(ser):
    n = 0
    while(n<30):
        s = ser.read(1).decode('utf-8')         # read 1 byte
        print(s)
        n=n+1

def receiveData(ser):
    global string_buffer
    global data_array
    sample_number = 0
    sendSerial(ser,'Start Data\n')
    while sample_number < 600:
        try:
            c = ser.read(1).decode('utf-8')         # read 1 byte
            if( c == '\n'):
                data_string = ''.join(string_buffer)
                print(data_string)
                temp_data_array = np.fromstring(data_string,dtype=int,sep=',')
                if(data_array.size == 0): 
                    data_array = temp_data_array
                else:
                    data_array = np.vstack((data_array,temp_data_array))
                sample_number = sample_number + 1
                string_buffer = []
            else:
               string_buffer.append(c)
        except(KeyboardInterrupt):
            sendSerial(ser,'Stop Data\n')
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    sendSerial(ser,'Stop Data\n')
    return data_array

def calcSamplingRate(data_array):
    mean_diff = np.mean(np.diff(data_array[:,0],1,0))
    print(1000000/mean_diff)

def plotData(data_array):
    plt.clf()
    plt.subplot(411)
    
    plt.title("Example Data Plot")
    
    plt.plot(data_array[:,0],data_array[:,1])
    
    plt.ylabel("X Amplitude")
    
    plt.subplot(412)
    plt.plot(data_array[:,0],data_array[:,2])
    plt.ylabel("Y Amplitude")
    
    plt.subplot(413)
    plt.plot(data_array[:,0],data_array[:,3])
    plt.ylabel("Z Amplitude")
    
    plt.subplot(414)
    plt.plot(data_array[:,0],-data_array[:,4])
    
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("R Amplitude")
    
    plt.show()
    
def plotAccel(data_array):
    plt.clf()
    plt.subplot(311)
    
    plt.title("Example Data Plot")
    
    plt.plot(data_array[:,0],data_array[:,1])
    
    plt.ylabel("X Amplitude")
    
    plt.subplot(312)
    plt.plot(data_array[:,0],data_array[:,2])
    plt.ylabel("Y Amplitude")
    
    plt.subplot(313)
    plt.plot(data_array[:,0],data_array[:,3])
    plt.ylabel("Z Amplitude")

    
    plt.xlabel(u'Time(${\mu}s$)')
    
    plt.show()

def main():
    ser = setupSerial()
    data_array = receiveData(ser)
    calcSamplingRate(data_array)
    np.savetxt("data_file_tap_1.csv", data_array, delimiter=",")
    data_array1 = np.genfromtxt('data_file_tap_1.csv', delimiter=',')
    plotData(data_array1)
    ser.close()

if __name__== "__main__":
    main()