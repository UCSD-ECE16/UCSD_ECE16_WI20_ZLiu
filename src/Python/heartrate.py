#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:04:50 2020

@author: iris
"""
import numpy as np 
from scipy.signal import argrelextrema
def calc_heart_rate_time(signal,fs):
    signal = signal - np.mean(signal)#filter the signal to remove baseline drifting
    signal = moving_average(signal,4)   #filter the signal to remove high frequency noise
    signal = normalize_signal(signal)  #Normalize the signal between 0 and 1
    processed_signal = signal_diff(signal) #Explore using the signal directly or potentially using the diff of the signal. 
    maximums = argrelextrema(processed_signal, np.greater)
    maximums = np.take(processed_signal, maximums)
    threshold = 2.2 * np.mean(maximums) #Count the number of times the signal crosses a threshold.
    print(threshold)
    count = (processed_signal > threshold).sum(axis=0)
    # print(count)
    size = processed_signal.size #Calculate the beats per minute. 
    T = 1/fs 
    time = T * size # the time of for whole signal. in s. 
    # print(time)
    n = (count/time) * 60
    return n 
    
def calc_sampling_rate(data_array):
    time = data_array[:,0]
    #print(time)
    interval = np.diff(time)
    interval = interval[1:]
    # print(interval)
    average_interval = np.mean(interval)
    return average_interval


def signal_diff(s):
    s_diff = np.diff(s)#calculate the gradient using np.diff
    s_diff =np.append(s_diff, 0) 
    return s_diff


def moving_average(s,n_avg):
    ma = s
    for i in np.arange(0,len(s)-n_avg):
      ma_period = s[i : i + n_avg]
      ma[i] = np.mean(ma_period)#mean of s from index i to i+n_avg
    return ma

def normalize_signal(signal):
    signal_min = np.min(signal) #find min of signal
    signal = signal - signal_min #subtract the minimum so the minimum of the signal is zero
    signal_max = np.max(signal) #find the new maximum of the signal
    norm_signal = signal/signal_max #divide the signal by the new maximum so the maximum becomes 1
    return norm_signal

def plotting():
    calculation = np.array([96.7, 103.16, 104.61, 93.50, 102, 103, 88, 96, 95, 93])
    true = np.array([97, 96, 98, 95, 96, 98, 91, 94, 93, 96])
    plt.scatter(true, calculation)
    plt.show()
    RMSE = 0
    for i in range (0, 10):
        RMSE = RMSE + rmse(calculation[i], true[i])
    print(RMSE)
    
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def main():
    data_array_from_file = np.genfromtxt('/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data_07_.csv', delimiter=',')
    time = data_array_from_file[:,0]
    signal = (-1)*data_array_from_file[:,3]
    # print(signal)
    n = calc_heart_rate_time(signal,1000/19.97)
    print(n)
    plotting();
    
if __name__=='__main__':
    main()