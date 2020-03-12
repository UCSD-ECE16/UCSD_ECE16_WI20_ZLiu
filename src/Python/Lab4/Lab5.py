#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:37:53 2020

@author: iris
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import signal
from matplotlib.gridspec import GridSpec
from scipy.stats import pearsonr
    
def graphs():
    gnd = [85, 86, 86, 85, 81, 91, 91, 85, 83, 90]
    # est = [70, 70, 70, 70, 70, 70, 70, 70, 70, 70]
    # est = []
    """est = [82.15568862275448, 93.89221556886227, 88.02395209580837, 82.15568862275448, 
           88.02395209580837, 82.15568862275448, 82.15568862275448, 82.15568862275448,
           82.15568862275448, 82.15568862275448]"""
    est = [84, 84, 90, 78, 84.0, 90, 90, 72, 78.0, 78.0]

    # I'll just input this manually. 
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

def challenge1():
    # The filter cutoff needs to be normalized between 0 and 1, 
    # where 1 is the Nyquist frequency
    filter_order = 3 
    filter_cutoff = 5 
    b,a = signal.butter(filter_order, filter_cutoff, btype='low')
    s_filt = signal.lfilter(b,a,s)
    w, h = signal.freqz(b,a)
    plt.plot(w, 20 * np.log10(abs(h)))
    subplot(nrows, ncols, index, **kwargs)
    plt.subplot(3, 2)
    plt.subplot(11)

def plot(t, s, fs):
    plt.subplot(211)
    plt.plot(t, s)
    plt.title('With Detrend')
    plt.subplot(212)
    ################The Key Here#########################
    # calculates the `power distribution over the frequency domain, the higher the more 
    Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs) #plot the power spectral density
    plt.show()
    ###calculate the maximum frequency component 
    Pxx_new = Pxx[1:]
    # print(Pxx)
    max_Pxx_index = np.argmax(Pxx_new)
    print('the maximum frequency component is')
    print(Freqs[max_Pxx_index+1])
    # return Pxx, Freqs

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


def LowPassFilter(s):
    # The filter cutoff needs to be normalized between 0 and 1, 
    # where 1 is the Nyquist frequency
    filter_order = 3 
    Nyquist_Freqs = 50
    filter_cutoff = 5 / Nyquist_Freqs
    b,a = signal.butter(filter_order, filter_cutoff, btype='low')
    s_filt = signal.lfilter(b,a,s)
    w, h = signal.freqz(b,a)
    """
    # subplot(nrows, ncols, index, **kwargs)
    gs = GridSpec(3, 2)
    fig = plt.figure(constrained_layout=True)
    ax1 = fig.add_subplot(gs[0, :])
    plt.plot(w, 20 * np.log10(abs(h)))
    ax2 = fig.add_subplot(gs[1, -1])
    plt.plot(t, s)
    ax3 = fig.add_subplot(gs[1, -2])
    plt.psd(s, NFFT=len(t), Fs=fs)
    ax4 = fig.add_subplot(gs[2, -1])
    plt.plot(t, s_filt)
    ax5 = fig.add_subplot(gs[2, -2])
    plt.psd(s_filt, NFFT=len(t), Fs=fs)
    plt.show()
    """
    return s_filt
    
def data():
    d1 = np.genfromtxt('05_01_86.csv', delimiter=',')

    d2 = np.genfromtxt('05_02_86.csv', delimiter=',')

    d3 = np.genfromtxt('05_03_85.csv', delimiter=',')

    d4 = np.genfromtxt('05_04_81.csv', delimiter=',')

    d5 = np.genfromtxt('05_05_91.csv', delimiter=',')

    d6 = np.genfromtxt('05_06_91.csv', delimiter=',')

    d7 = np.genfromtxt('05_07_85.csv', delimiter=',')

    d8 = np.genfromtxt('Data_08_71.csv', delimiter=',')

    d9 = np.genfromtxt('Data_09_58.csv', delimiter=',')

    d10 = np.genfromtxt('Data_10_71.csv', delimiter=',')

    plt.figure(figsize=(10,10))
    ax1=plt.subplot(10, 2, 1)
    s, t1 = plotting_data(d1)
    ax1=plt.subplot(10, 2, 2)
    plotting_data_filter(d1)
    
    ax2=plt.subplot(10, 2, 3)
    s, t2 = plotting_data(d2)
    ax2=plt.subplot(10, 2, 4)
    plotting_data_filter(d2)
    
    ax3=plt.subplot(10, 2, 5)
    s, t3 = plotting_data(d3)
    ax3=plt.subplot(10, 2, 6)
    plotting_data_filter(d3)
    
    ax4=plt.subplot(10, 2, 7)
    s, t4 = plotting_data(d4)
    ax4=plt.subplot(10, 2, 8)
    plotting_data_filter(d4)
    
    ax5=plt.subplot(10, 2, 9)
    s, t5 = plotting_data(d5)
    ax5=plt.subplot(10, 2, 10)
    plotting_data_filter(d5)
    
    ax6=plt.subplot(10, 2, 11)
    s, t6 = plotting_data(d6)
    ax6=plt.subplot(10, 2, 12)
    plotting_data_filter(d6)
    
    ax7=plt.subplot(10, 2, 13)
    s, t7 = plotting_data(d7)
    ax7=plt.subplot(10, 2, 14)
    plotting_data_filter(d7)
    
    ax8=plt.subplot(10, 2, 15)
    s, t8 = plotting_data(d8)
    ax8=plt.subplot(10, 2, 16)
    plotting_data_filter(d8)
    
    ax9=plt.subplot(10, 2, 17)
    s, t9 = plotting_data(d9)
    ax9=plt.subplot(10, 2, 18)
    plotting_data_filter(d9)
    
    ax10=plt.subplot(10, 2, 19)
    s, t1 = plotting_data(d10)
    ax1=plt.subplot(10, 2, 20)
    plotting_data_filter(d10)
    return d1,d2, d3, d4, d5, d6, d7, d8, d9, d10
    
    
def plotting_data(data):
    t = data[:,0]
    t1 = t/1000
    t1 = t1 - min(t1)
    fs = 50
    s = data[:, 4]
    plt.plot(t1, s)
    plt.xlabel('t / s')
    
    return s, t1

def plotting_data_filter(data):
    t = data[:,0]
    fs = 50
    s = data[:, 4]
    s = detrend(s, 6)
    Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs) #plot the power spectral density
    plt.xlabel('Frequency/Hz')
    plt.ylabel(' ')
    max_Pxx_index = np.argmax(Pxx)
    print('the maximum frequency component is')
    print(Freqs[max_Pxx_index])

def calc_heart_rate_freq(signal,fs):
    t = signal[:,0]
    s = signal[:,4]
    s = LowPassFilter(s)
    Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs) #Take the PSD
    index, _ = scipy.signal.find_peaks(Pxx)
    # print(index)
    peaks = Pxx[index]
    # print(peaks)
    index_of = np.argmax(peaks)
    q = Freqs[index[index_of]]
    
    """
    while (q > 2):
        peaks = peaks[0: index_of - 1]
        print(peaks)
        index_of = np.argmax(peaks)
        q = Freqs[index[index_of]]
        print(q)
    """
    
    # print(index_)
    # index_ = 3 
    index__ = index[index_of]
    # print(index__)
    print('the heart rate is')
    print(Freqs[index__] * 60)
    return (Freqs[index__] * 60)
    #Calculate HR based on find peak    
    


def main():
    """
    data_array = np.genfromtxt('appendix_a.csv', delimiter=',')
    d1,d2, d3, d4, d5, d6, d7, d8, d9, d10 = data()
    hr_data = np.zeros((500, 50))
    hr_data[0:len(d1),0:5] = d1
    hr_data[0:len(d2),5:10] = d2
    hr_data[0:len(d3),10:15] = d3 
    hr_data[0:len(d4),15:20] = d4 
    hr_data[0:len(d5),20:25] = d5 
    hr_data[0:len(d6),25:30] = d6 
    hr_data[0:len(d7),30:35] = d7 
    hr_data[0:len(d8),35:40] = d8
    hr_data[0:len(d9),40:45] = d9 
    hr_data[0:len(d10),45:50] = d10 
    # get data from Appendix A and save as .csv.
    """
    fs = 50 #sampling rate in Hz
    """
    t = data_array[:,0]# get the time array
    s = data_array[:,4]# get the x-acceleration array
    y = data_array[:,2]
    z = data_array[:,3]
    s = detrend(s, 6)
    y = detrend(y, 6)
    z = detrend(z, 6)
    # plot(t, y, fs)
    # plot(t, z, fs)
    
    # plot(t, s, fs)

    """
    # graphs()
    signal = np.genfromtxt('05_10_85.csv', delimiter=',')
    calc_heart_rate_freq(signal,fs)
    

if __name__=='__main__':
    main()
    