#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:27:33 2020

@author: iris
"""
serial_name = '/dev/cu.usbserial-14330'
baud_rate = 115200
import serial
ser = serial.Serial(serial_name, baud_rate)
import numpy as np
class Visualize:
    def plotData(data_array):
        plt.clf()
        time = data_array[:, 0]
        x = data_array[:, 1]
        y = data_array[:, 2]
        z = data_array[:, 3]
        R = (data_array[:, 4])
        r = (-1)*R
        # print(r)
        plt.subplot(411)
        plt.title("Example Data Plot")
        plt.xlabel('ms')
        plt.ylabel("X Amplitude")
        plt.plot(time,x)
        plt.subplot(412)
        plt.xlabel('ms')
        # plt.xlabel(u'Time(${\mu}s$)')
        plt.ylabel("Y Amplitude")
        plt.plot(time,y)
        plt.subplot(413)
        plt.xlabel('ms')
        plt.ylabel("Y Amplitude")
        plt.plot(time,z)
        plt.subplot(414)
        plt.xlabel('ms')
        plt.ylabel("R amplitude")
        plt.plot(time,r)
        plt.show()
        #plot the 3 axis accelerometer data and the heart pulse data into 4 subplots
        
    def plotAccel(data_array):
        plt.clf()
        time = data_array[:, 0]
        x = data_array[:, 1]
        y = data_array[:, 2]
        z = data_array[:, 3]
        # print(r)
        plt.subplot(311)
        plt.title("Example Data Plot")
        plt.xlabel('ms')
        plt.ylabel("X Amplitude")
        plt.plot(time,x)
        plt.subplot(312)
        plt.xlabel('ms')
        # plt.xlabel(u'Time(${\mu}s$)')
        plt.ylabel("Y Amplitude")
        plt.plot(time,y)
        plt.subplot(313)
        plt.xlabel('ms')
        plt.ylabel("Y Amplitude")
        plt.plot(time,z)
        # plot the 3 axis accelerometer data

    def plotHr(data_array):
        plt.clf()
        time = data_array[:, 0]
        R = (data_array[:, 4])
        r = (-1)*R
        plt.xlabel('ms')
        plt.ylabel("R amplitude")
        plt.plot(time,r)
        plt.show()
        
        # plot the heart pulse data
