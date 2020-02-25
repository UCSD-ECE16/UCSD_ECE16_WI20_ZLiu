#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:27:22 2020

@author: iris
"""

import serial
import numpy as np
import sys
import serial
sys.path.insert(1, 'Libraries')
from Data import Data #need to import the library you need
serial_name = '/dev/cu.usbserial-14330'
baud_rate = 115200
ser = serial.Serial(serial_name, baud_rate)

class Connection:

    def __init__(self, serial_name, baud_rate):
        self.serial_name = serial_name
        self.baud_rate = baud_rate
        self.data = Data()
        self.setup_connection()
        self.string_buffer = []

    def setup_connection(self):
        self.ser = serial.Serial(self.serial_name, self.baud_rate)  # open serial port
        
        
    def close_connection(self):
        
        ser.close()
        #close the serial connection
        
    def send_serial(self, message):
        self.start_streaming(self)
        #write message to serial

    def read_serial(self):
        #read a byte at a time and print to console
        global string_buffer
        global data_array
        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
        return s 
        
    def start_streaming(self):
        ser.write('start data\n'.encode('utf-8'))
        # send 'Start Data\n' through serial
    
    def receive_data(self):
        c = self.ser.read(1).decode('utf-8')         # read 1 byte
        if( c == '\n'):
            data_string = ''.join(self.string_buffer)
            print(data_string)
            temp_data_array = np.fromstring(data_string,dtype=int,sep=',')
            self.data.add_data(temp_data_array) #using the Data module
            self.string_buffer = []
        else:
           self.string_buffer.append(c)
    
    def end_streaming(self):
        ser.write('stop data'.encode('utf-8'))# send 'Stop Data\n' through serial
