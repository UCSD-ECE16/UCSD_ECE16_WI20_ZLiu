#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:15:17 2020

@author: iris
"""
import matplotlib.pyplot as plt
import numpy as np
import serial
#Make the variables below global
string_buffer = []
data_array = np.array([])
S_list = ["", "", ""]

def setup_serial():
    serial_name = '/dev/cu.usbserial-14330'  # replacing using the actual port 
    ser = serial.Serial(serial_name, 115200)    # open serial port 
    print(ser.name)
    return ser 

def receive_sample(ser):
    global string_buffer
    global data_array
    s = ser.read(1).decode('utf-8')      # read 1 byte and decode it
    # read a byte from serial (remember to decode)
    if(s == '\n'):   # received \n):
       data_string = ''.join(string_buffer)#JOIN buffer 
       #print(data_string)
       temp_data_array = np.fromstring(data_string, dtype=int, sep=',')#string to np array
       #print(temp_data_array)
       #print(data_array.size)
       
       if(data_array.size == 0): 
           data_array = temp_data_array
       
       else:
           data_array = np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
       string_buffer = []
    else:
        string_buffer.append(s)
    
    return data_array
        
def receive_data(ser):
    
    # Send start data
    sample_number = 0
    ser.write('start data\n'.encode('utf-8'))
    while sample_number < 3000:
        try:
            sample_number = sample_number + 1
            data_array = receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.write('stop data'.encode('utf-8'))
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    ser.write('stop data'.encode('utf-8'))
    np.savetxt("accelerometer.csv", data_array, delimiter=",")
    # print(data_array)
    return data_array
# Send stop data




    
def calc_sampling_rate(data_array):
    time = data_array[:,0]
    #print(time)
    interval = np.diff(time)
    interval = interval[1:]
    # print(interval)
    average_interval = np.mean(interval)
    print(average_interval)
    
    #code to calculate sampling rate from data_array

def plotting():
    plt.clf()
    data_array = np.genfromtxt('accelerometer.csv', delimiter=',')
    time = data_array[:, 0]
    x = data_array[:, 1]
    y = data_array[:, 2]
    z = data_array[:, 3]
    plt.subplot(311)
    plt.title("Example Data Plot")
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("X Amplitude")
    plt.plot(time,x)
    plt.subplot(312)
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("Y Amplitude")
    plt.plot(time,y)
    plt.subplot(313)
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("Y Amplitude")
    plt.plot(time,z)
    plt.show()

def main():
    ser = setup_serial()
    data_array = receive_data(ser)
    print(data_array)
    calc_sampling_rate(data_array)
    ser.close()
    plotting()


if __name__=='__main__':
    main()