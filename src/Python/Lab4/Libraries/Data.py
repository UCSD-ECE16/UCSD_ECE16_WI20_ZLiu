#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:26:35 2020

@author: edwardwang
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import signal
from matplotlib.gridspec import GridSpec

class Data:
    
    def __init__(self):
        self.data_array = np.array([])
    
    def add_data(self, new_data):
        if(self.get_num_samples() == 0): 
            self.data_array = new_data
        else:
            self.data_array = np.vstack((self.data_array, new_data))
    
    def clear_data(self):
        self.data_array = np.array([])
        
    def get_num_samples(self):
        return self.data_array.shape[0]
        
    def calc_sampling_rate(self):
        mean_diff = np.mean(np.diff(self.data_array[:,0],1,0))
        self.sampling_rate = 1000000/mean_diff
        print(self.sampling_rate)
        
        
    #%% Data processing for machine learning 
    def moving_average(self, s,n_avg):
        ma = np.zeros_like(s)
        for i in np.arange(0,len(s)):
          ma_period = s[i : i + n_avg]
          # print(ma_period.shape)
          # print(ma_period)
          ma[i] = np.mean(ma_period,axis=0) # mean of s from index i to i+n_avg
          # print(ma[i])
        return s - ma
    
    def detrend(self, s,n_avg): #remove the moving average from the signal
        ma = moving_average(s,n_avg)
        return ma #s minus the moving_average


        
    def normalize_signal(self, s):
            norm_signal = (s - np.min(s))/(np.max(s)-np.min(s))
            return norm_signal
    
    def LowPassFilter(self, s):
        # The filter cutoff needs to be normalized between 0 and 1, 
        # where 1 is the Nyquist frequency
        filter_order = 3 
        Nyquist_Freqs = 50
        filter_cutoff = 5 / Nyquist_Freqs
        b,a = signal.butter(filter_order, filter_cutoff, btype='low')
        s_filt = signal.lfilter(b,a,s)
        return s_filt



        
    


