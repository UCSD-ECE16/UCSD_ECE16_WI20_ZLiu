#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:15:17 2020

@author: iris
"""
import numpy as np
import serial
#Make the variables below global
string_buffer = []
data_array = np.array([])
S_list = ["", "", ""]

""""
for incoming_byte in incoming_stream:
    c = incoming_byte.decode('utf-8')
    #this takes the place of reading the byte from serial
    if(c == '\n'):
        data_string = ''.join(string_buffer)#JOIN buffer 
        print(data_string)
        temp_data_array = np.fromstring(data_string, dtype=int, sep='')
        #csv string to 1x4 np array
        if(data_array.size == 0):#data_array is empty): 
            data_array = temp_data_array
        else:
            data_array = np.vstack((data_array,temp_data_array))
            #vstack temp_data_array to end of data_array
        string_buffer = []# reset buffer to []
    else:
        string_buffer.append(c)
        # append the new char to string_buffer
        
"""
def setup_serial():
    serial_name = '/dev/cu.IrissFirebeetle-ESP32SPP'  # replacing using the actual port 
    ser = serial.Serial(serial_name, 115200)    # open serial port 
    print(ser.name)
    return ser 

def receive_sample(ser):
    global string_buffer
    global data_array
    s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
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
    while sample_number < 5000:
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
    # print(data_array)
    return data_array
# Send stop data




    
def calc_sampling_rate(data_array):
    time = data_array[:,0]
    #print(time)
    interval = np.diff(time)
    interval = interval[1:]
    print(interval)
    average_interval = np.mean(interval)
    print(average_interval)
    
    #code to calculate sampling rate from data_array

def main():
    ser = setup_serial()
    data_array = receive_data(ser)
    # print(data_array)
    calc_sampling_rate(data_array)
    ser.close()


if __name__=='__main__':
    main()