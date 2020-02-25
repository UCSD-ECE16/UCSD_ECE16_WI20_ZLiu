

# Lab4 

## Tutorials 

### MAX30105 Pulse Sensor

**Using the SparkFun MAX30105 Arduino Library**

![T11](fig/Lab4/T11.png)

> Q. Note that you can connect both the heart rate sensor and your OLED at the same time, both of which use the I2C SDA and SCL lines. Why does this work?

> A.
>
> Because that the OLED and the heart rate sensor would use the same pins(battery, ground, IO21, IO22), I need to connect to the those pins on my ESP32 twice. I can do this by 
>
> (1) Conntecting OLED to the female fire jumper on ESP32 and heart rate sensor to the breadboard or the opposite. Shown in the following picture. 
>
> ![T16](fig/Lab4/T16.jpg)
>
> (2) Connect the heart rate sensor to the pins of OLED, as shown in the graph below 
>
> ![T17](fig/Lab4/T17.png)

>  Q. Notice the while(1) statement. What happens if the device is not connected? What happens if the error is printed and then you connect the device? Will the code proceed? Try it and describe the behavior.

> A. 
>
> the while(1) statement
>
> creates an endless loop. The only way to stop it is to press the reset button.
>
> **If the device is not connected**
>
> As shown in the graph below 
>
> Wouldn't be lighted up if connected again. 

> Q. what would the settings look like if you were to: set the led brightness to 25mA, use only the Red + IR LED, Sample at 200Hz, and use an ADC range of 8192?

> A. 
>
> **set the led brightness to 25mA**:Here we are using the 16 positional notation, and if we want it to be 25 mA, we should set the ledBrightness to be 127. (50mA represented by 255.) So the corresponding positional notation is 0*7F. 
>
> **use only the Red + IR LEDled**: Mode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
>
> byte ledBrightness = 0x7F;
>
> byte sampleAverage = 8; //Options: 1, 2, 4, 8, 16, 32
>
> byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
>
> int sampleRate = 200; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
>
> int pulseWidth = 411; //Options: 69, 118, 215, 411
>
> int adcRange = 8192; //Options: 2048, 4096, 8192, 16384

>  Q. What are the units of the pulse width? Would the bigger the pulseWidth result in a more intense or less intense measurement? Why?

> A.
>
> According to the datasheet, the units of the pulse width is ns. (As shown in the following picture.)
>
> ![T12](fig/Lab4/T12.png)

> Q. How many bits are needed for an ADC range of 16384?

> A. 
>
> 15 bits are needed.

> Q. What is **the peak wavelength of the R, IR, and G LEDs? **

> A. 
>
> ![T13](fig/Lab4/T13.png)
>
> ![T14](fig/Lab4/T14.png)
>
> ![T15](fig/Lab4/T15.png)
>
> According to the datasheet (as shown in the pictures above), the peak wavelength of the R, IR, and G LEDs are respectively 670 nm, 900 nm and 545 nm. 

> Q. If you want to read the Green value, what Mode do you need the setting to be in and what function will you need to use to get the green signal?

> To get the green signal, the Mode: getGreen; the Function: particleSensor.getGreen(); 

### Matplotlib

Use Python to plot the signal. To achieve this, we use a library called Matplotlib.

> Q. What was plotted? What does this tell you about how plt.plot interprets the input? 

> A. 
>
> ![T21](fig/Lab4/T21.png)

> The way it interprets the input is like, if we plot two vectors directly, it would take the first row as the x and the second row as the y. If we plot a matrix variable with two rows, it would take the columns as y and the index as x. 

The first plot: 

![T22](fig/Lab4/T22.png)

The first subplots: 

![T23](fig/Lab4/T23.png)

### Saving and Reading Data with File I/O

Save the data and read it again later. 

Do do that, we need to use python to write the data into a file and then also use python to read the file. 

The path of the saved file is shown in the following picture. 

![T24](fig/Lab4/T24.png)

Plotting each of the three axis of data on a different subplot. 



Q. What is approximately the frequency of oscillation of the x axis signal in the plot above? 

> With about 0.034 us, x oscilated 8 times, so the frequency is 1/T(oscilate) = 8/0.034 = 235.29 * 10^6. 

Q. Try your best to replicate the above plot by shaking your accelerometer. The above was sampled at 50Hz for 10 seconds. Make a gif of you running your program, shaking your accelerometer, and a plot showing up similar to the one above.

> ![1](fig/Lab4/1.gif)

### **Removing Mean Offset** 

Remove the **MEAN** of the signal. 

The codes: 

> (In the picture)

The mean-removed signal: 

The signal used to test the 

![accelerometer](fig/Lab4/accelerometer.png)

### **Smoothing with Moving Average** 

Smooth the noise out by using the moving average. 

![accelerometer](fig/Lab4/smooth.png)

### Detrending a Moving Average

![Detrend](fig/Lab4/detrend.png)

## Challenges 

### Challenge 1 

Q. Why do we plot the negative of the signal? This has to do with light absorption. We talked about it in class.

> For the Heart Rate sensor, more blood means more absorption and less light. So, if we want to see the pulse of the blood, we need to take the inverse of the heart rate signal. 

 Q. Try different sample Average parameters and plot them. What is the effect of sample Average on the smoothness of the signal? 

> The bigger the sample Average is, the **less** smoother the signal is. 
>
> Plottings of different Sample Rates:
>
> 1
>
> ![C1_1](fig/Lab4/C1_1.png)
>
> 2 
>
> ![C1_2](fig/Lab4/C1_2.png)
>
> 4 
>
> ![C1_4](fig/Lab4/C1_4.png)
>
> 8 
>
> ![C1_8](fig/Lab4/C1_8.png)
>
> 16 
>
> ![C1_16](fig/Lab4/C1_16.png)
>
> 32 
>
> ![C1_32](fig/Lab4/C1_32.png)

Q. Try different led Brightness. Is brighter always better? Why or why not.

> Brighter is not always better. (sample Average: 8) 
>
> If it is too bright, the heart beat we could observe is a fixed line.  
>
> I guess this is because that when it is too light, 
>
> 0*1F 
>
> ![C1_8](fig/Lab4/C1_8.png)
>
> 0*4F 
>
> ![C1_B4f](fig/Lab4/C1_B4F.png)

**Deliverable**: Tune the settings so that you ultimately get a **sampling rate of 50Hz**. What setting did you land on that gave you a clean signal and at the right sampling rate?

> The settings:
>
> ![C1_S1](fig/Lab4/C1_S1.png)
>
> ![C1_S2](fig/Lab4/C1_S2.png) 

Show a gif of you starting your code, and end with the plot appearing. Also include a still image of the plot. 

> Getting  a **sampling rate of 50Hz** means having the interval of 20 ms between 2 outputs.
>
> The screenshot&gif have output as the first item on each line the time in ms. 

> The gif 
>
> ![C1_S](fig/Lab4/C1_S.gif)

> The still image of the plot: 
>
> ![C1_S](fig/Lab4/C1_S.png)



### Challenge 2 

> Several plottings of the recorded data (I'm only going to use the time&R data)

![C21_1](fig/Lab4/C21_1.png)

![C21_2](fig/Lab4/C21_2.png)

![C21_3](fig/Lab4/C21_3.png)

The calculation result: 

![C2_2](fig/Lab4/C2_2.png)

Q. Note that it is very important to normalize AFTER you’ve done the filtering. Try normalizing before filtering and describe what happens and why it doesn’t work for helping with our threshold. 

> What happens: 
>
> ![C2_3](fig/Lab4/C2_3.png)

> Why it doesn't work for helping with our threshold:
>
> If we do that, the noise is also normalized, making it harder to filter out the noise. 

Q. What threshold did you find to work well and how did you determine it? 

> I determined it by 
>
> 1. Getting the local maxima first 
> 2. Calculate the mean of local maximas
> 3. Scale the mean according to the real heart rate -> the threshold 
>
> I found that the threshold which is 2.2*mean works well. 
>
> I also tried using the minmum among the local maximas, but it turned out to be too small. 

Q. Show a scatter plot of your heart rate calculation (y axis) vs the heart rate of the reference. Calculate the Root Mean Squared Error (RMSE) of your detected heart rate vs the reference heart rate. RMSE is calculated as the square root of the mean of the square of the difference between your estimated heart rate and the reference heart rate. More about RMSE can be found here: https://towardsdatascience.com/what-does-rmse-really-mean-806b65f2e48e. 

> ![truevscal](fig/Lab4/truevscal.png)
>
> RMSE: 36.57 

### Challenge 3 

Q. We made a few mistakes in the above code, identify them and fix them. :)



>  ![C31](fig/Lab4/C31.png)

> There should be a self here. ![C34](fig/Lab4/C34.png)should be (self, new_data)![C33](fig/Lab4/C33.png)
>
> from Data import Data. 



Q. Now add a new module in Libraries called HR.py for the heart rate and signal processing methods we made in this lab. And then in the Wearable.py, add the code to calculate heart rate and print out the heart rate. **Show in a gif capturing the pulse for 10 seconds, plot and print out the calculated heart rate. **

>  ![c3](fig/Lab4/c3.gif)

![C3](fig/Lab4/C3.png)