#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:06:24 2020
@author: iris
"""


import glob 
import numpy as np 
import re
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import signal
from matplotlib.gridspec import GridSpec
from scipy.stats import pearsonr

#%% Data processing 
    
def normalize_signal(s):
        norm_signal = (s - np.min(s))/(np.max(s)-np.min(s))
        return norm_signal

def LowPassFilter(s):
    # The filter cutoff needs to be normalized between 0 and 1, 
    # where 1 is the Nyquist frequency
    filter_order = 3 
    Nyquist_Freqs = 50
    filter_cutoff = 5 / Nyquist_Freqs
    b,a = signal.butter(filter_order, filter_cutoff, btype='low')
    s_filt = signal.lfilter(b,a,s)
    return s_filt

# #%% Manipulating filenames

directory = "/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/"
# all_files = glob.glob('/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/*.csv')
all_files = glob.glob("/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/*.csv")
unique_ids = [item.split('/')[9].split('_')[0] for item in all_files]

# Challenge 4 
# actually read the training files  
list_data = []
list_sub = []
list_ref = []

for sub_id in unique_ids: #sub_id in the list of unique_ids
    sub_files = glob.glob('/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/' + sub_id + '*.csv')
    #using glob get the files of all files with this subject id
    for each_file in sub_files: #each file in the list of files for this subject
        # print(each_file)
        data = np.genfromtxt(each_file, delimiter=',')#read the csv
        hr_data = data[0: 500][4]  #get the ppg signal from data using slicing
        # removing baseline, 
        hr_data = hr_data - np.mean(hr_data)
        # smooth your signal using a low pass filter
        hr_data = LowPassFilter(hr_data)
        # normalize. 
        hr_data = normalize_signal(hr_data)
        #append the preprocessed data to list_data
        list_data = np.append(list_data, hr_data, axis = 0)
        #append the subject id to list_sub
        list_sub = np.append(list_sub, sub_id)
        #retrieve the reference heart rate from the filename.
        ref = each_file.split('/')[9].split('_')[2].split('.')[0]
        #append the reference heart rate to list_ref
        list_ref = np.append(list_ref, ref)
"""
print(list_ref)
print(np.size(list_ref))
print(list_sub)
print(np.size(list_sub))
print(np.shape(list_data))
"""
#%% Challenge 5 
# take one PPG as an example
import numpy as np
import matplotlib.pyplot as plt
trace = 9 
data_array = list_data[(trace-1) * 500: trace * 500]
# print(data_array)
# print(np.shape(data_array))
plt.hist(data_array)
plt.show()

from sklearn.mixture import GaussianMixture as GMM
# Train a GMM model using all the training data 
# minus the data from one of the subjects each time 
# and then test the performance on this held out subject
# doing a hold-out using the first subject of your training set

train_data = np.empty((0))
hold_out_data = np.empty((0))
train_ids = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
hold_out_subject = train_ids[3] # for now we'll hold out the first training subject 

for ind, sub_id in enumerate(list_sub): #enumerate the list_sub starting at 0.
    print(ind)
    if([sub_id] != [hold_out_subject]):
        train_data = np.concatenate((train_data, list_data[ind * 500: (ind + 1) * 500]))
    else: 
        hold_out_data = np.concatenate((hold_out_data, list_data[ind * 500: (ind + 1) * 500]))
        print(hold_out_data)

gmm = GMM(n_components = 2).fit(train_data.reshape(-1, 1))
test_pred = gmm.predict(hold_out_data.reshape(-1, 1))
print(hold_out_data)
plt.plot(hold_out_data)
plt.show()


# should have the GMM model doing automatic threshold tuned using data 