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

class ML:
    def graphs(gnd, est):
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
        
    def moving_average(s,n_avg):
        ma = np.zeros_like(s)
        for i in np.arange(0,len(s)):
          ma_period = s[i : i + n_avg]
          # print(ma_period.shape)
          # print(ma_period)
          ma[i] = np.mean(ma_period,axis=0) # mean of s from index i to i+n_avg
          # print(ma[i])
        return s - ma
    
    def detrend(s,n_avg): #remove the moving average from the signal
        ma = moving_average(s,n_avg)
        return ma #s minus the moving_average

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
    def file_names():
    #%% Manipulating filenames
        directory = "/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/"
        # all_files = glob.glob('/Users/iris/UCSD_ECE16_WI20_ZLiu/src/Python/Lab4/Data/training/*.csv')
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
            # print(sub_files)
            #using glob get the files of all files with this subject id
            for each_file in sub_files: #each file in the list of files for this subject
                # print(each_file)
                data = np.genfromtxt(each_file, delimiter=',')#read the csv
                hr_data = data[0:500,4]  #get the ppg signal from data using slicing
                # removing baseline,
                
                ma = np.zeros(500)
                n_avg = 6
                for i in np.arange(0,len(hr_data)):
                    ma_period = hr_data[i : i + n_avg]
                    # print(ma_period)
                    ma[i] = np.mean(ma_period,axis=0) # mean of s from index i to i+n_avg
                    # print(ma[i])
                hr_data_detrend = np.subtract(hr_data, ma)
                print(np.shape(hr_data_detrend))
                # smooth your signal using a low pass filter
                hr_data_new = LowPassFilter(hr_data_detrend)
                print(np.shape(hr_data_new))
                # normalize.
                hr_data_nor = normalize_signal(hr_data_new)
                print(np.shape(hr_data_nor))
                #append the preprocessed data to list_data
                # print('1')
                # print(np.shape(hr_data))
                list_data = np.append(list_data, hr_data_nor, axis = 0)
                #append the subject id to list_sub
                list_sub = np.append(list_sub, sub_id)
                #retrieve the reference heart rate from the filename.
                ref = each_file.split('/')[9].split('_')[2].split('.')[0]
                # print(ref)
                #append the reference heart rate to list_ref
                list_ref = np.append(list_ref, ref)
            # print('i')
            # print(i)
        # print(i)
        # print(list_ref)
        # print(np.size(list_ref))
        # print(list_sub)
        # print(np.size(list_sub))
        # print(np.shape(list_data))
#%%
    def machine_learning():
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
        # Train a GMM model using all the training data 
        # minus the data from one of the subjects each time 
        # and then test the performance on this held out subject
        # doing a hold-out using the first subject of your training set
        
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
            gmm = GMM(n_components = 2).fit(train_data.reshape(-1, 1))
            for i in range(0, 10):
                test_pred = gmm.predict(hold_out_data.reshape(-1, 1)[i*500:(i+1)*500])
                # plt.figure(figsize=(10,10))
                # plt.plot(hold_out_data.reshape(-1, 1)[i*500:(i+1)*500])
                # plt.show()
                # print(list_ref[i])
        #%% # Convert to the heart rate 
        predicted_peaks, _ = scipy.signal.find_peaks(test_pred)
        print('predicted heart rate')
        print((len(predicted_peaks) / (500 / 50)) * 60)
        #%% Compare the reference heart rate for each data file 
        labels = np.zeros((1, 120))
        for i in range(0, 120):
            q = 0
            predicted = gmm.predict(list_data[i*500 : (i+1)*500].reshape(-1, 1))
            print(predicted)
            plt.plot(predicted)
            plt.plot(list_data[i*500 : (i+1)*500].reshape(-1, 1))
            plt.show()
            
            for j in range(0, len(predicted) - 1):
                if predicted[j] == 0 and predicted[j+1] == 1:
                    q += 1
            # ih, _ = scipy.signal.find_peaks(predicted_peak)
            labels[0][i] = (q / (500 / 50)) * 60  # (len(ih)*6)
            # print(len(ih))

        gnd = list_ref.reshape(-1, 1)
        gnd_new = np.zeros(120)
        est_new = np.zeros(120)
        for i in range(len(gnd)):
            gnd_new[i] = int(gnd[i])
        est = labels.reshape(-1, 1)
        for i in range(len(est)):
            est_new[i] = int(est[i])
        est = est_new 
        gnd = gnd_new
        # print(est)
        # print(np.shape(gnd))
        # print(np.shape(est))
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

        
def main():
    ML.file_names()
    ML.machine_learning()
        
        
if __name__== "__main__":
    main()
        
        # should have the GMM model doing automatic threshold tuned using data 