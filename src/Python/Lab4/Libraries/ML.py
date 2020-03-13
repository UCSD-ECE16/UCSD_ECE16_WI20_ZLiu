#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:06:24 2020
@author: iris
"""
import glob 
import numpy as np 
import re
import matplotlib.pyplot as plt
import scipy 
from scipy import signal
from matplotlib.gridspec import GridSpec
from sklearn.mixture import GaussianMixture as GMM
from scipy.stats import pearsonr 
from Libraries.Data import Data

# calc_hr(self,s,fs)test_hr_model(self,directory)


class ML:
    def __init__(self):
        self.data = Data()
        self.fs = 50 
        
#%%
    def calc_hr(self,s,fs):
        predicted_peaks, _ = scipy.signal.find_peaks(s)
        predicted_heart_rate = (len(predicted_peaks) / (500 / fs)) * 60
        return predicted_heart_rate
#%%         
    def train_hr_model(self, directory):
        # directory = "/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/"
        all_files = glob.glob("/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/*.csv")
        unique_ids = [item.split('/')[9].split('_')[0] for item in all_files]
        # Challenge 4 
        # actually read the training files  
        list_data = []
        list_sub = []
        list_ref = []
        i = 0 
        
        train_ids = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        for sub_id in train_ids: #sub_id in the list of unique_ids
            sub_files = glob.glob('/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/' + sub_id + '*.csv')
            for each_file in sub_files: #each file in the list of files for this subject
                import numpy as np 
                data = np.genfromtxt(each_file, delimiter=',')#read the csv
                hr_data = data[0:500,4]  #get the ppg signal from data using slicing
                # removing baseline,
                ma = np.zeros(500)
                n_avg = 6
                for i in np.arange(0,len(hr_data)):
                    ma_period = hr_data[i : i + n_avg]
                    ma[i] = np.mean(ma_period,axis=0) # mean of s from index i to i+n_avg
                hr_data_detrend = np.subtract(hr_data, ma)
                # smooth your signal using a low pass filter
                hr_data_new = self.data.LowPassFilter(hr_data_detrend)
                # normalize.
                hr_data_nor = self.data.normalize_signal(hr_data_new)
                #append the preprocessed data to list_data
                list_data = np.append(list_data, hr_data_nor, axis = 0)
                #append the subject id to list_sub
                list_sub = np.append(list_sub, sub_id)
                #retrieve the reference heart rate from the filename.
                ref = each_file.split('/')[9].split('_')[2].split('.')[0]
                #append the reference heart rate to list_ref
                list_ref = np.append(list_ref, ref)
        self.list_data = list_data
        self.list_sub = list_sub
        self.list_ref = list_ref
        
        #%% Challenge 5 
        # take one PPG as an example
        import numpy as np
        import matplotlib.pyplot as plt
        trace = 9 
        data_array = list_data[(trace-1) * 500 : trace * 500]
        # print(data_array)
        # print(np.shape(data_array))
        plt.hist(data_array)
        plt.show()
        
        from sklearn.mixture import GaussianMixture as GMM
        
        train_data = np.empty((0))
        hold_out_data = np.empty((0))
        train_ids = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
        for k in range(0 ,10):
            hold_out_subject = train_ids[k] # for now we'll hold out the first training subject 

            for ind, sub_id in enumerate(list_sub): #enumerate the list_sub starting at 0.
                if(sub_id != hold_out_subject):
                    train_data = np.concatenate((train_data, list_data[ind * 500: (ind + 1) * 500]))
                    # print(list_data[ind * 500: (ind + 1) * 500])
                else:
                    hold_out_data = np.concatenate((hold_out_data, list_data[ind * 500: (ind + 1) * 500]))
            self.gmm = GMM(n_components = 2).fit(train_data.reshape(-1, 1))
            for i in range(0, 10):
                test_pred = self.gmm.predict(hold_out_data.reshape(-1, 1)[i*500:(i+1)*500])
                # print('test_heart_rate')
                test_heart_rate = self.calc_hr(test_pred,self.fs)
                # print(test_heart_rate)


#%% 
    def test_hr_model(self,directory):
        gnd = self.list_ref.reshape(-1, 1)
        gnd_new = np.zeros(120)
        est_new = np.zeros(120)
        for i in range(0, 120):
            q = 0
            predicted = self.gmm.predict(self.list_data[i*500 : (i+1)*500].reshape(-1, 1))
            plt.plot(predicted)
            plt.plot(self.list_data[i*500 : (i+1)*500].reshape(-1, 1))
            plt.show()
            for j in range(0, len(predicted) - 1):
                est_new[i] = int(self.calc_hr(predicted,self.fs))


        for i in range(len(gnd)):
            gnd_new[i] = int(gnd[i])
        est = est_new 
        gnd = gnd_new
        [R,p] = pearsonr(gnd,est)
        plt.figure(1)
        plt.clf()
        plt.subplot(121)
        plt.plot(gnd,gnd)
        plt.scatter(gnd,est)
        plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2)))
        plt.ylabel("estimate HR (BPM)")
        plt.xlabel("reference HR (BPM)")
        
        avg = np.true_divide((np.add(gnd, est)), 2)
        """avg = ( gnd + est ) ./ 2 """
        """dif = abs((gnd - est)) #take the difference of gnd and est """
        dif = abs (np.subtract(gnd, est))
        std = np.std(dif) #get the standard deviation of the difference (using np.std)
        bias = np.mean(dif) #the mean value of the difference
        upper_std = np.add(bias, 1.96 * std) #the bias plus 1.96 times the std
        lower_std = np.subtract(bias, 1.96 * std) #the bias minus 1.96 times the std
        
        
        plt.subplot(122)
        plt.scatter(avg, dif)
        plt.plot([np.min(avg),np.max(avg)],[bias,bias])
        plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
        plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
        plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(np.subtract(gnd, est)),2)))
        plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
        plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
        plt.ylabel("Difference of Est and Gnd (BPM)")
        plt.xlabel("Average of Est and Gnd (BPM)")
        plt.show()
        return np.stack((gnd, est))