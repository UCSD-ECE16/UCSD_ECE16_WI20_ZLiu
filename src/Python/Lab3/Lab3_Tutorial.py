#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:24:03 2020

@author: iris
"""
import numpy as np

# %% Numpy Arrays 
test_array_list = [0, 10, 4, 12]
test_array = np.array(test_array_list)
print(test_array.shape)  # to print shape 
substracted_test_array = np.subtract(test_array, 20)   # to substract 20 
print(substracted_test_array)    # the result could show that the substact is elementwise 


test_2D_array = [[0,10,4,12],[1,20,3,41]]
test_2D_numpy = np.array(test_2D_array)
print("the test_2D_numpy array is", test_2D_numpy,
      "the test_2D_numpy array shape is", test_2D_numpy.shape,
      "the data type is", test_2D_numpy.dtype)

zeros = np.zeros([10, 20])
print(zeros)

test_array_h = np.hstack((test_array, test_array))
test_array_v = np.vstack((test_array_h, test_array_h, test_array_h, test_array_h))
print(test_array_v)


arange_array1 = np.arange(-3, 21, 6)
arange_array2 = np.arange(-7, -21, -2)
print('arange_array1 is', arange_array1, 'arange_array2 is', arange_array2)

linespace = np.linspace(0, 100, 49)
print(linespace)


e = np.array([[12, 3, 1, 2], [0, 0, 1, 2], [4, 2, 3, 1]])
print(e)
print(e[0])     
print(e[1,0])  
print(e[:,1])   
print(e[2, :2])
print(e[2, 2:])
print(e[:,2])  
print(e[1,3])

# %% setting values of array
test_array = np.array([1,2,3,4])
test_array[1] = 10
test_array[1:3] = [2,5]



# %% Setting values from array from comma seperated values 
data_string = '1,2,3,4'
data_array = np.fromstring(data_string,dtype=int,sep=',')
stacked_array = data_array
for i in range(0, 99):
    stacked_array = np.vstack((data_array, stacked_array))
print(stacked_array.shape)
print(stacked_array)


# %% Array Assignment 
e = np.zeros((3, 4))

e[0] = [12, 3, 1, 2]
e[1,0] = 0
e[:,1] = [3, 0, 2]
e[2, :2] = [4, 2]
e[2, 2:] = [3, 1] 
e[:,2] = [1, 1, 3]
e[1,3] = 2
print(e)











































