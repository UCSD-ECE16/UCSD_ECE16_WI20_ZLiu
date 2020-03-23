#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:14:17 2020

@author: iris
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
import matplotlib.pyplot as plt
import numpy as np
import serial
import scipy
from scipy import signal

#Make the variables below global
string_buffer = []
data_array = np.array([])
S_list = ["", "", ""]


def setup_serial():
    serial_name = '/dev/cu.usbserial-14330'  # replacing using the actual port 
    ser = serial.Serial(serial_name, 115200)    # open serial port 
    # print(ser.name)
    return ser 
def receive_sample(ser):
    global string_buffer
    global data_array
    s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
    # read a byte from serial (remember to decode)
    if(s == '\n'):   # received \n):
       data_string = ''.join(string_buffer)#JOIN buffer 
       temp_data_array = np.fromstring(data_string, dtype=int, sep=',')#string to np array
       #print(temp_data_array)
       #print(data_array.size)
       
       if(data_array.size == 0): 
           data_array = temp_data_array
       
       else:
           data_array = np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
       string_buffer = []
    else:
        string_buffer.append(s)
    
    return data_array
        
def receive_data(ser):
    
    # Send start data
    sample_number = 0
    ser.write('Start Data'.encode('utf-8'))
    while sample_number < 5000:
        try:
            sample_number = sample_number + 1
            print(sample_number)
            data_array = receive_sample(ser)
            print(data_array)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.write('Stop Data'.encode('utf-8'))
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    ser.write('Stop Data'.encode('utf-8'))
    # hb_array = data_array[:,4]
    # np.savetxt("Data_3_csv", data_array, delimiter=",")
    # print(data_array)
    return data_array
# Send stop data

#%% Tapping Detection
def tapping_detection(z):
    index, _ = scipy.signal.find_peaks(z)
    peak_number = 0 
    for i in range(10, len(index)):
        if ((abs(z[index[i]]) - abs(np.max(z[index[i] - 10 : index[i]])) > 13)):
            print(index[i])
            # print('a')
            peak_number = peak_number + 1
    print(peak_number)
    return peak_number

#%%
def plotting(z):
    # t = data_array[:, 0]
    # x = data_array[:, 1]
    # y = data_array[:, 2]
    # z = data_array[:, 3]
    # plt.clf()
    # plt.subplot(311)
    # plt.plot(t, x)
    # plt.subplot(312)
    # plt.plot(t, y)
    # plt.subplot(313)
    plt.plot(z)
    plt.show()
    
    
#%% Main 
    
def main():
    ser = setup_serial()
    data_array = receive_data(ser)
    # np.savetxt("counting_8.csv", data_array, delimiter=",")
    # signal = np.genfromtxt('counting_8.csv', delimiter=',')
    z = data_array[:, 3]
    peaks = tapping_detection(z)
    plotting(z)
    # plotting(data_array)
    ser.close()


if __name__=='__main__':
    main()