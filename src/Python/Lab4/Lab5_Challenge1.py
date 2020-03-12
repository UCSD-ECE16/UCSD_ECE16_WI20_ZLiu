#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:48:10 2020

@author: iris
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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

