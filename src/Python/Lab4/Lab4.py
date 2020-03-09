#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:37:35 2020

@author: iris
"""

# we are not able to look at what the signal looks like, just the raw numbers. 
# Much like in Arduino IDE, we can use Python to plot the signal. 
import matplotlib.pyplot as plt
import numpy as np
""""

#%% Tutorial 2 
plt.clf() #clear any existing plot
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

a = np.array([[1,2,3,4],[1,4,9,16]])
plt.clf()
plt.plot(a)
plt.show()

a = np.array([[1,2,3,4],[1,4,9,16]])
x = a[0]#index from a to get [1,2,3,4]
y = a[1]#index from a to get [1,4,9,16]
plt.clf()
plt.title("First plot!")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()


#  Try removing the plt.clf() function 
# and change the array slightly and plot again.

a = np.array([[1,2,3,4],[1,4,9,16]])
b = np.array([[1,2,3,4],[4,2,1,6]])

plt.clf()
plt.subplot(211)
plt.plot(x,y) #fill in ax and ay
plt.subplot(212)
plt.plot(y,x) #fill in bx and by
plt.show()
"""
#%% Starting from the test data 
"""
data_array = np.array([[10252533,     1806,     1823,     2255],
       [10262471,     1808,     1822,     2246],
       [10272472,     1804,     1823,     2241],
       [10282472,     1805,     1830,     2239],
       [10292477,     1806,     1821,     2235],
       [10302475,     1808,     1823,     2247],
       [10312480,     1808,     1829,     2239],
       [10322483,     1807,     1828,     2242],
       [10332484,     1809,     1825,     2246],
       [10342488,     1799,     1823,     2243],
       [10352490,     1802,     1817,     2243],
       [10362492,     1803,     1822,     2235],
       [10372495,     1808,     1827,     2243],
       [10382499,     1802,     1822,     2251],
       [10392500,     1800,     1830,     2241],
       [10402502,     1793,     1825,     2245],
       [10412504,     1808,     1826,     2246],
       [10422506,     1803,     1829,     2247],
       [10432509,     1799,     1823,     2253],
       [10442511,     1795,     1823,     2239],
       [10452514,     1808,     1830,     2246],
       [10462514,     1797,     1820,     2237],
       [10472519,     1801,     1823,     2246],
       [10482524,     1802,     1827,     2249],
       [10492526,     1799,     1827,     2251],
       [10502526,     1808,     1819,     2229],
       [10512527,     1796,     1824,     2256],
       [10522533,     1795,     1823,     2241],
       [10532535,     1810,     1825,     2250],
       [10542538,     1811,     1822,     2243],
       [10552539,     1803,     1828,     2231],
       [10562543,     1807,     1819,     2240],
       [10572544,     1807,     1833,     2239],
       [10582549,     1806,     1819,     2237],
       [10592549,     1809,     1834,     2243],
       [10602553,     1808,     1826,     2242],
       [10612554,     1803,     1830,     2240],
       [10622557,     1802,     1827,     2253],
       [10632559,     1807,     1815,     2235],
       [10642561,     1809,     1823,     2254],
       [10652564,     1808,     1826,     2253],
       [10662565,     1808,     1823,     2251],
       [10672568,     1808,     1821,     2247],
       [10682572,     1803,     1822,     2249],
       [10692574,     1795,     1826,     2239],
       [10702577,     1796,     1823,     2231],
       [10712579,     1803,     1822,     2247],
       [10722581,     1805,     1828,     2239],
       [10732582,     1802,     1830,     2245],
       [10742586,     1799,     1823,     2243],
       [10752590,     1808,     1823,     2247],
       [10762591,     1799,     1827,     2234],
       [10772593,     1812,     1819,     2237],
       [10782595,     1801,     1827,     2241],
       [10792598,     1805,     1825,     2247],
       [10802600,     1802,     1828,     2240],
       [10812603,     1801,     1820,     2243],
       [10822606,     1798,     1826,     2238],
       [10832609,     1803,     1823,     2243],
       [10842612,     1806,     1828,     2239],
       [10852613,     1804,     1825,     2239],
       [10862616,     1808,     1823,     2239],
       [10872617,     1805,     1823,     2239],
       [10882620,     1793,     1829,     2247],
       [10892623,     1790,     1818,     2238],
       [10902624,     1801,     1818,     2255],
       [10912627,     1808,     1829,     2239],
       [10922627,     1798,     1822,     2249],
       [10932630,     1808,     1825,     2243],
       [10942633,     1807,     1830,     2253],
       [10952634,     1801,     1831,     2238],
       [11035974,     1817,     1803,     2212],
       [11045974,     1793,     1822,     2239],
       [11055980,     1808,     1818,     2231],
       [11065981,     1809,     1824,     2239],
       [11075982,     1807,     1828,     2241],
       [11085985,     1805,     1821,     2239],
       [11095987,     1799,     1824,     2245],
       [11105990,     1807,     1822,     2239],
       [11115992,     1808,     1822,     2249],
       [11125997,     1808,     1824,     2231],
       [11135999,     1809,     1792,     2242],
       [11146000,     1808,     1825,     2251],
       [11156003,     1811,     1823,     2246],
       [11166004,     1809,     1829,     2251],
       [11176006,     1805,     1822,     2242],
       [11186007,     1808,     1814,     2228],
       [11196010,     1818,     1826,     2239],
       [11206012,     1808,     1829,     2231],
       [11216015,     1803,     1829,     2242],
       [11226016,     1814,     1823,     2238],
       [11236019,     1808,     1824,     2239],
       [11246021,     1807,     1829,     2243],
       [11256024,     1793,     1823,     2251],
       [11266024,     1803,     1825,     2239],
       [11276027,     1808,     1821,     2238],
       [11286029,     1801,     1827,     2245],
       [11296032,     1806,     1823,     2247],
       [11306035,     1797,     1808,     2237],
       [11316037,     1768,     1837,     2238]])
# sample was collected using receiveData(ser)

# save it as a comma separated value file (.csv). 
np.savetxt("foo.csv", data_array, delimiter=",")

data_array_from_file = np.genfromtxt('/Users/iris/UCSD_ECE16_WI20_ZLiu/
src/Python/Lab4/accelerometer.csv', delimiter=',')
"""

# Next, plot each of the three axis of data on a different subplot. 
# Label the figure as “Example Data Plot”, 
# All y axis as “Amplitude” and the bottom x-axis as Time(μs). 
# You can get the special symbol with the following: 
# plt.xlabel(u'Time(${\mu}s$)')
"""
plt.clf()
time = data_array_from_file[:, 0]
x = data_array_from_file[:, 1]
y = data_array_from_file[:, 2]
z = data_array_from_file[:, 3]
//print(time)
//print(x)
//print(y)
//print(z)
plt.subplot(311)
plt.title("Example Data Plot")
plt.xlabel(u'Time(${\mu}s$)')
plt.ylabel("X Amplitude")
plt.plot(time,x)
plt.subplot(312)
plt.xlabel(u'Time(${\mu}s$)')
plt.ylabel("Y Amplitude")
plt.plot(time,y)
plt.subplot(313)
plt.xlabel(u'Time(${\mu}s$)')
plt.ylabel("Y Amplitude")
plt.plot(time,z)
plt.show()
"""
# %% reading the accelerometer
# data_array_from_file = np.genfromtxt('accelerometer.csv', delimiter=',')
# s = data_array_from_file

# %% Remove the mean 
def remove_mean():
    s = data_array_from_file[:,3] #get the z axis
    mean_s = np.mean(s)#take the mean of s with numpy
    s_removed = s - mean_s
    plt.title('the plot of z after removing the mean of z')
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("Z Amplitude after removed mean")
    plt.plot(time,s_removed)
    plt.show()

# %% Smoothing with Moving Average 

def moving_average(s,n_avg):
    ma = s
    for i in np.arange(0,len(s)-n_avg):
      ma_period = s[i : i + n_avg]
      ma[i] = np.mean(ma_period)#mean of s from index i to i+n_avg
    return ma
""""
ma = moving_average(s_removed, 3)
plt.title('the plot of z after removing the mean of z and smoothing')
plt.xlabel(u'Time(${\mu}s$)')
plt.ylabel("Z Amplitude after removed mean")
plt.plot(time, ma)
plt.show()

"""



# %% Looking at the signal in different ways
# calculating the change between subsequent samples by taking the derivative
def signal_diff(s):
    s_diff = np.diff(s)#calculate the gradient using np.diff
    s_diff =np.append(s_diff, 0) 
    return s_diff;
    #np.diff returns one shorter, so need to add a 0

""""
s_difference = signal_diff(s)


plt.title('difference z')
plt.xlabel(u'Time(${\mu}s$)')
plt.ylabel("Z difference")
plt.plot(time, s_difference)
plt.show()
"""
# %% Challenge (1)

def setup_serial():
    serial_name = '/dev/cu.usbserial-14230'  # replacing using the actual port 
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
       #print(data_string)
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
    ser.write('start data\n'.encode('utf-8'))
    while sample_number < 500:
        try:
            sample_number = sample_number + 1
            print(sample_number)
            data_array = receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.write('stop data'.encode('utf-8'))
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    ser.write('stop data'.encode('utf-8'))
    hb_array = data_array[4]
    np.savetxt("5_14000_ReferenceHR.csv", hb_array, delimiter=",")
    # print(data_array)
    return data_array
# Send stop data





import matplotlib.pyplot as plt
import numpy as np
import serial
#Make the variables below global
string_buffer = []
data_array = np.array([])
S_list = ["", "", ""]

    
def calc_sampling_rate(data_array):
    time = data_array[:,0]
    #print(time)
    interval = np.diff(time)
    interval = interval[1:]
    # print(interval)
    average_interval = np.mean(interval)
    # print(average_interval)


def plotting(data_array):
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

def Four_Key_Analysis:
    
    import numpy as np
    from scipy.stats import pearsonr
    import matplotlib.pyplot as plt
    
    gnd = #reference heart rate
    est = #estimate of your algorithm
    
    [R,p] = pearsonr(gnd,est)
    
    plt.figure(1)
    plt.clf()
    plt.subplot(121)
    plt.plot(gnd,gnd)
    plt.scatter(gnd,est)
    plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2)))
    plt.ylabel("estimate HR (BPM)")
    plt.xlabel("reference HR (BPM)")
    
    avg = #take the average of gnd and est
    dif = #take the difference of gnd and est
    std = #get the standard deviation of the difference (using np.std)
    bias = #the mean value of the difference
    upper_std = #the bias plus 1.96 times the std
    lower_std = #the bias minus 1.96 times the std
    
    plt.subplot(122)
    plt.scatter(avg, dif)
    plt.plot([np.min(avg),np.max(avg)],[bias,bias])
    plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
    plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
    plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(gnd-est),2)))
    plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
    plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
    plt.ylabel("Difference of Est and Gnd (BPM)")
    plt.xlabel("Average of Est and Gnd (BPM)")
    plt.show()






def calc_heart_rate_time(signal,fs):
        
    signal = signal - np.mean(signal)#filter the signal to remove baseline drifting
    signal = moving_average(signal,4)   #filter the signal to remove high frequency noise
    signal = normalize_signal(signal)  #Normalize the signal between 0 and 1
    processed_signal = signal_diff(signal) #Explore using the signal directly or potentially using the diff of the signal. 
    maximums = argrelextrema(processed_signal, np.greater)
    maximums = np.take(processed_signal, maximums)
    threshold = 2.2 * np.mean(maximums) #Count the number of times the signal crosses a threshold.
    # print(threshold)
    count = (processed_signal > threshold).sum(axis=0)
    # print(count)
    size = processed_signal.size #Calculate the beats per minute. 
    T = 1/fs 
    time = T * size # the time of for whole signal. in s. 
    # print(time)
    n = (count/time) * 60
    return n 

def main():
    ser = setup_serial()
    data_array = receive_data(ser)
    calc_sampling_rate(data_array)
    # np.savetxt("Data_10_.csv", data_array, delimiter=",")
    # signal = np.genfromtxt('data_file.csv', delimiter=',')
    plotting(data_array)
    ser.close()

if __name__=='__main__':
    main()