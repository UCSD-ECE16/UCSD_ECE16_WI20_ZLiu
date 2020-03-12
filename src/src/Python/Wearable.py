#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:14:57 2020

@author: edwardwang
"""

from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
from Libraries.HR import HR
import matplotlib.pyplot as plt
import numpy as np

class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        self.connection.end_streaming()
        self.connection.start_streaming()
        while self.connection.data.get_num_samples() < num_samples:
            try:
                self.connection.receive_data()
            except(KeyboardInterrupt):
                self.connection.end_streaming()
                self.connection.close_connection()
                print("Exiting program due to KeyboardInterrupt")
                break
        self.connection.end_streaming()
    
    def main(self):
        self.collect_data(500)
        print(self.connection.data.data_array)
        self.connection.close_connection()
        collected_data = self.connection.data
        self.connection.data.calc_sampling_rate()
        test = self.connection.data.sampling_rate

        fs = int(test) #round to nearest int
        np.savetxt("data_file.csv", collected_data.data_array, delimiter=",")
        data_array = np.genfromtxt('data_file.csv', delimiter=',')
        [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
        time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
        plt.clf()
        plt.plot(time, HR.normalize_signal(HR.detrend(-data_array[:,4],fs)))
        plt.plot(time, s_thresh_up)
        print("BPM = "+str(BPM_Estimate))      


def main():
    wearable = Wearable('/dev/cu.usbserial-14330',115200)
    wearable.main()

if __name__== "__main__":
    main()