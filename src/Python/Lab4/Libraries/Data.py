#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 02:23:15 2020

@author: iris
"""
import numpy as np
import sys
import serial
sys.path.insert(1, 'Libraries')
serial_name = '/dev/cu.usbserial-14330'
baud_rate = 115200
ser = serial.Serial(serial_name, baud_rate)
class Data:
    
    def __init__(self):
        self.data_array = np.array([])
    
    def add_data(self,new_data):
        
        sample_number = 0
        while sample_number < 14000:
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
        np.savetxt("xyzr1.csv", data_array, delimiter=",")
        # print(data_array)
        return data_array
        
    

        #check the number of samples using get_num_samples and add the new data into the data_array accordingly. 
    
    def clear_data(self):
        data_array = numpy.empty[data_array.shape]
        # reset data_array to empty np array
        
    def get_num_samples(self):
        
        return data_array.size #the size of data_array
    def calc_sampling_rate(self, data_array):
        time = data_array[:,0]
        #print(time)
        interval = np.diff(time)
        interval = interval[1:]
        # print(interval)
        average_interval = np.mean(interval)
        return average_interval
        #calculate the sampling rate
