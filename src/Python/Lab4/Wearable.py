#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:25:46 2020

@author: iris
"""
# import numpy as np 
# some_file.py
import sys
import serial
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'Libraries')

from Connection import Connection
from Visualize import Visualize
from Data import Data
from HR import HR 

serial_name = '/dev/cu.usbserial-14330'
baud_rate = 115200
ser = serial.Serial(serial_name, 115200)
num_samples = 14000


class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        self.connection.close_connection()
        self.connection.end_streaming()
        #first make sure data sending is stopped by ending streaming
        self.connection.setup_connection()
        self.connection.start_streaming()
        #start sending data
        while self.connection.data.get_num_samples() < num_samples: #collect x samples
            try:
                data_array = self.connection.receive_data()#receive data
            except(KeyboardInterrupt):
                self.connection.close_connection()#deal with exception
                break#end streaming
    
    def main(self):
        self.collect_data(num_samples) #number of samples to collect)
        sampling_rate = self.connection.data.calc_sampling_rate(data_array) #calculate sampling rate

        time = data_array[:,0]
        signal = (-1)*data_array[:,3]
        # print(signal)
        n = calc_heart_rate_time(signal,1000/19.97)
        print(n)
        plotting();


wearable = Wearable(serial_name, baud_rate)
if __name__=='__main__':
    wearable.main()