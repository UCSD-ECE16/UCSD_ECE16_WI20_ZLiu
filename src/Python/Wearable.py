#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:25:46 2020

@author: iris
"""

# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'Libraries')



from Connection import Connection
from Visualize import Visualize
from Data import Data
num_samples = 50

class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        self.connection.close_connection()
        #first make sure data sending is stopped by ending streaming
        setup_connection()
        #start sending data
        while self.connection.data.get_num_samples() < num_samples: #collect x samples
            try:
                self.connection.receive_data()#receive data
            except(KeyboardInterrupt):
                self.connection.close_connection()#deal with exception
                break#end streaming
    
    def main(self):
        self.collect_data(num_samples)#number of samples to collect)
        sampling_rate = self.connection.data.calc_sampling_rate(data_array) #calculate sampling rate

if __name__=='__main__':
    main()