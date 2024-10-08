# SpcPatternRecognition-Exercise
# Msc_In_Robotics_NTUA_Exercise

**Exercise on Identification of patterns of statistical control charts with use of artificial
neural networks.**


In the present exercise we were asked to approach the SPC (Statistical Process Control) pattern approach and the
automatic recognition by TND. Our initial approach was to understand the simple and the
complex patterns, as well as our familiarity with Western Electric rules (These rules
detect out-of-control or non-random patterns in control charts). The languages
programming we chose to use is Python for production and
data presentation, R programming language for use and familiarity with standards
Western Electric and finally the MatLab program for the creation and training of the Artificial
Neural Network.


## Creating Patterns
The logic we followed was to create 20 point patterns between the ± 3 values. Specifically
the simple patterns Uptrend, Stratification, Point Outside of Control Limits and Instability were created.
In addition, the complex Cycle and Instability and Instability and Grouping patterns were created. The way
their creation was as follows:
1. Create a 20-dot pattern for each type of pattern we will use
(Uptrend, Stratification, ...., Instability and Grouping) with values ​​that we type manually.
2. Automatic production of 1000 patterns for each of them added to them so White
Noise as well as random noise from Gaussian distribution (Figures 1 to 6 graphic
representation of the manual pattern in relation to what is produced that has been added
randomness). The final Dataset created is 6000 sample patterns.
3. In each of them, an average of 20 points is calculated for four parameters
of each pattern (Mean), minimum and maximum value (min, max) and curvature (Kurtosis)
as defined by Fisher. It is worth noting that others can be added
calculations in future implementation if the Python Pandas library offers us
a variety of options. Therefore the current state of our dataset is an array
dimensions 6000x24.
4. For the 6 patterns we have, a dataset with the targets should be created which
will be binary. This will be in the format 6000x6. Structure:

Stratification Pattern = 1 0 0 0 0 0

Uptrend = 0 1 0 0 0 0

Instability = 0 0 1 0 0 0

Point Outside of Control Limits = 0 0 0 1 0 0

Cycle and Instability = 0 0 0 0 0 1 1 0

Instability and Grouping = 0 0 0 0 0 1


## Data Creation Examples:

![UptrendExample1](https://user-images.githubusercontent.com/25718684/161730949-dfc7328e-6160-4cf3-97dd-0d62dc8cb33f.png)
![UptrendExample2](https://user-images.githubusercontent.com/25718684/161730951-0a4f95ad-ba3a-484d-8018-0b51f7a7f042.png)
![UptrendExample3](https://user-images.githubusercontent.com/25718684/161730954-b83c3270-70c0-49ae-bbcd-a1b2f6967948.png)


(Figure 1 Examples of data generation for pattern: Uptrend)


![StratificationExample2](https://user-images.githubusercontent.com/25718684/161731270-16509919-0965-4182-99d2-8b6fdf3fbf0d.png)
)![StratificationExample3](https://user-images.githubusercontent.com/25718684/161731264-406ef024-8a66-4227-b6aa-4ab2b36dea6d.png)
![StratificationExample1](https://user-images.githubusercontent.com/25718684/161731267-22fc2c41-1c13-4913-8850-718f70ba3fcc.png)

(Figure 2 Examples of pattern data creation: Stratification)

![OutsideOfControlExample2](https://user-images.githubusercontent.com/25718684/161731704-c14f4824-cf4a-413c-bd3d-312f3b86f39d.png)
![OutsideOfControlExample3](https://user-images.githubusercontent.com/25718684/161731708-b5240915-4fe4-42e2-8302-a96582faf615.png)
![OutsideOfControlExample1](https://user-images.githubusercontent.com/25718684/161731709-56622a9c-5377-42cb-8db7-f5706bedd031.png)

(Figure 3 Examples of pattern data generation: Point Outside Of Control)

![InstabilityExample1](https://user-images.githubusercontent.com/25718684/161731780-8e169ecc-e2b5-45cd-95df-1ccaf3a8d7d8.png)
![InstabilityExample2](https://user-images.githubusercontent.com/25718684/161731784-df9a159d-ac64-46b7-b791-700317733b7c.png)
![InstabilityExample3](https://user-images.githubusercontent.com/25718684/161731785-090ab9ec-d5e8-4c3d-b039-6c4ce7eabca4.png)

(Figure 4 Examples of data creation for pattern: Instability)

![CycleAndInstabilitylExample1](https://user-images.githubusercontent.com/25718684/161731932-1c0f2513-2a79-45a9-b8ba-ac0fc0e5399d.png)
![CycleAndInstabilitylExample2](https://user-images.githubusercontent.com/25718684/161731935-63dd0852-cfb2-44cb-a730-8ef9ceb47952.png)
![CycleAndInstabilitylExample3](https://user-images.githubusercontent.com/25718684/161731936-156b97b8-788a-4268-a86d-1d46094b94fa.png)

(Figure 5 Examples of data generation for pattern: Cycle and Instability)

![Instability_And_GroupingExample3](https://user-images.githubusercontent.com/25718684/161732031-1f5ceac6-8885-4707-adc1-59ba6098bb4c.png)
![Instability_And_GroupingExample1](https://user-images.githubusercontent.com/25718684/161732035-6ae7773b-dffe-42ef-856d-16eda3931bb2.png)
![Instability_And_GroupingExample2](https://user-images.githubusercontent.com/25718684/161732039-bf554acc-3708-4149-b822-dc4780113429.png)

(Figure 6 Examples of data creation for pattern: Instability and Grouping)


## Creation of the Artificial Neural Network
The TND was created using MatLab's Neural Pattern Recognition library.
We have selected this tool for the ease of use it offers as well as the plethora of options.
Below we see the steps we followed to create 2 TND. The only difference
two TNDs is that one consists of one Hidden Layer and the other of two (Figure 7). Education
of TND was done with a percentage of 80-5-15, ie 4800 training data, 300 validation data and 900 testing
data (Figure 8).


![Network_Architecture_2Hidden_Layers](https://user-images.githubusercontent.com/25718684/161732869-2f924abe-81a8-41bf-ae3f-969f156bb844.PNG)
![Network_Architecture_1Hidden_Layer](https://user-images.githubusercontent.com/25718684/161732871-5459d03a-e3d0-43fe-8186-204d0021a5c2.PNG)

(Figure 7 Architecture of the two ANNs)

![Validation_and_Test_Data_Parameters](https://user-images.githubusercontent.com/25718684/161733191-16f0be11-8fcc-462b-b46d-2b8f125c9b81.PNG)

(Figure 8 training data structure)


## Training Results
After training both ANNs we came to the following range of results (Figures 9-13 contain a simulation for each ANN):

![image](https://user-images.githubusercontent.com/25718684/161733477-c09a3872-8765-4569-ae68-1948a9143b2c.png)

### More Information from Plot Confusion Graphs:

![1_LAYER_PLOT_CONFUSION](https://user-images.githubusercontent.com/25718684/161733715-e8f7c738-d813-4dd2-992a-71adbba861c6.png)

(Figure 9 Plot Confusion for NN with one Hidden Layer)

![2_LAYER_PLOT_CONFUSION](https://user-images.githubusercontent.com/25718684/161733795-d9037f71-d3f4-460e-98df-4adb576d8109.png)

(Figure 10 Plot Confusion for NN with two Hidden Layers)

### More Information from ROC Graphs:

![1_PLOT_ROC](https://user-images.githubusercontent.com/25718684/161734075-4f9bcba9-e6cb-42c1-8775-9290745b3b55.png)

(Figure 11 Plot ROC for NN with a Hidden Layer)

![2_PLOT_ROC](https://user-images.githubusercontent.com/25718684/161734238-c83edc80-3a51-463a-8e82-2efabb4e5a53.png)

(Figure 12 Plot ROC for NN with two Hidden Layers)

![Training_State_1Layer](https://user-images.githubusercontent.com/25718684/161734509-b0f66201-2340-48cc-ace5-f48b70b41b6d.png)
![Training_State_2Layers](https://user-images.githubusercontent.com/25718684/161734511-c39a48a6-c0b9-4a39-b919-0b4787f6433f.png)

(Figure 13 Training state of Neural Nets Gradients in correlation with epochs for 1 Layer and 2 Layers)


# Conclusions
The two ANNs gave us quite reliable results and we did not detect any signs of overfitting, however providing more patterns both simple and complex would definitely make ANN more demanding. Additionally we notice that the ANN with a Hidden Layer, has mainly the difficulty in separating Class 3-4-6 (Instability, Point Outside of Control Limits and Instability and Grouping) patterns which have the most similarities between them. One of future upgrades that could make our system more reliable would be extraction of primary patterns from real processing machines. Finally it is quite easy with the structure of our program in Python to add a variety of other methods data for patterns such as UCL, LCL and feature addition (median, percentage change between the current and a prior element etc.)
