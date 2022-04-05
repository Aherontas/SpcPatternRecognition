# SpcPatternRecognition
# NTUA

Exercise on Identification of patterns of statistical control charts with artificial
neural networks


In the present exercise we were asked to approach the SPC (Statistical Process Control) pattern approach and the
automatic recognition by TND. Our initial approach was to understand the simple and the
complex patterns, as well as our familiarity with Western Electric rules (These rules
detect out-of-control or non-random patterns in control charts). The languages
programming we chose to use is Python for production and
data presentation, R programming language for use and familiarity with standards
Western Electric and finally the MatLab program for the creation and training of the Artificial
Neural Network.


Creating Patterns
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
