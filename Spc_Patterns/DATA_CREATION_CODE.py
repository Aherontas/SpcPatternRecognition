import numpy as np
import csv
import matplotlib.pyplot as plt
import statistics as statistics
from matplotlib.ticker import PercentFormatter
import pandas as pd

plt.style.use('seaborn-colorblind')

# Data gia grafima timon apo -2 eos 2 me 20 Sample points

#SIMPLE PATTERNS

#Kanoume uncomment gia paragogi pattern STRATIFICATION kai csv export line

#STRATIFICATION PATTERN
# data_standard = np.array([0.782255,0.662182,0.150645,-0.896467,-0.876443,-0.808987,-1.699870,0.712200,0.171865,-0.762727,0.468775,0.051673,-1.015500
#                        ,0.720511,0.654035,0.050556,-0.477682,1.407893,-0.019590,-0.817530])

#Kanoume uncomment gia paragogi pattern UPTREND kai csv export line

#UPTREND PATTERN
# data_standard = np.array([-1.782255,-1.662182,-1.550645,-1.496467,-1.276443,-1.008987,-1.199870,-0.712200,-0.571865
#                           ,-0.262727,-0.168775,0.651673,0.315500 ,0.820511,0.954035,1.050556,1.277682,1.307893,1.619590,1.917530])

#Kanoume uncomment gia paragogi pattern INSTABILITY  kai csv export line

#INSTABILITY PATTERN
# data_standard = np.array([1.782255,-1.662182,1.150645,-1.896467,1.876443,-1.808987,2.399870,-1.712200,1.171865,-1.762727,1.468775,-2.051673,1.015500
#                          ,-1.720511,1.654035,-1.050556,1.477682,-1.407893,1.019590,-1.817530])

#Kanoume uncomment gia paragogi pattern POINT OUTSIDE OF CONTROL kai csv export line

#POINT OUTSIDE OF CONTROL PATTERN
# data_standard = np.array([0.782255,0.662182,0.150645,-0.896467,-0.876443,-0.808987,-1.699870,0.712200,0.171865,-0.762727,3.268775,0.051673,-1.015500
#                          ,0.720511,0.654035,0.050556,-0.477682,1.407893,-0.019590,-0.817530])

#COMPLEX PATTERNS

#Kanoume uncomment gia paragogi pattern POINT OUTSIDE OF CONTROL kai csv export line

#CYCLE AND INSTABILITY PATTERN
# data_standard = np.array([0.6662255, 1.22161, 2.861231, 0.35153, -2.846512, -0.98643, 1.35411, 2.32315, 2.23567, -1.88734, -2.79877, -0.78535, 1.794234
#                           ,2.78903, 0.234553, -2.015465, -0.51234, 1.78243, 2.612341, 0.21236])

#Kanoume uncomment gia paragogi pattern INSTABILITY AND GROUPING kai csv export line

#INSTABILITY_AND_GROUPING
# data_standard = np.array([0.12765, 2.13453, 0.25437, 1.96353, 0.21468, 2.93457, 0.55328, 2.89354, 0.35388, 2.79534, 0.62347, 2.59123, 0.58009, 2.26755
#                           ,0.11355, 2.98790, 1.9535, 2.83245, 1.89009, 2.85123])

class MR_ControlChart:

       def fit(self, data):
              self.X = data
              self.number_of_sample = len(self.X)
              self.mR = np.zeros(((self.number_of_sample - 1), 1))

              for i in range(len(self.mR)):
                     self.mR[i] = abs(self.X[i + 1] - self.X[i])

       def ControlChart(self, d2, D4, D3):

              #Ypologismos UCL, CL kai LCL
              ucl_X = self.X.mean() + (3 / d2 * np.sqrt(self.number_of_sample)) * self.mR.mean()
              cl_X = self.X.mean()
              lcl_X = self.X.mean() - (3 / d2 * np.sqrt(self.number_of_sample)) * self.mR.mean()

              #Ypologismos meson oron gia UCL, CL kai LCL
              ucl_mR = D4 * self.mR.mean()
              cl_mR = self.mR.mean()
              lcl_mR = D3 * self.mR.mean()

              #Kodikas gia plot dedomenon stin katallili morfi
              plt.figure(figsize=(15, 5))
              plt.plot(self.X, marker="o", color="k", label="X")
              plt.plot([ucl_X] * len(self.X), color="r", label="UCL={}".format(ucl_X.round(2)))
              plt.plot([cl_X] * len(self.X), color="b", label="CL={}".format(cl_X.round(2)))
              plt.plot([lcl_X] * len(self.X), color="r", label="LCL={}".format(lcl_X.round(2)))
              plt.title("X Chart")
              plt.xticks(np.arange(len(self.X)))
              plt.legend()
              plt.show()

              plt.figure(figsize=(15, 5))
              plt.plot(self.mR, marker="o", color="k", label="mR ")
              plt.plot([ucl_mR] * len(self.X), color="r", label="UCL={}".format(ucl_mR.round(2)))
              plt.plot([cl_mR] * len(self.X), color="b", label="CL={}".format(cl_mR.round(2)))
              plt.plot([lcl_mR] * len(self.X), color="r", label="LCL={}".format(lcl_mR.round(2)))
              plt.title("mR  Chart")
              plt.xticks(np.arange(len(self.X)))
              plt.legend()
              plt.show()



#Plot tis class MR_ControlChart
# chart = MR_ControlChart()
# chart.fit(data_standard)
# chart.ControlChart(d2 = 1.128,D3 = 0 ,D4 = 3.267)


#Dimiourgia noise gia tin sinartisi, .05 pano kato apo tis proigoymenes times
plt.xlabel("Timestamp")
plt.ylabel("Measurement")

input_mean_list = []
#Plot ton dio grafimaton me kai xoris noise
holder_list = []
for i in range(1000):
       print("Loading : ",i ," /1000")
       #Noise added to standard data
       noise_backup = (np.random.normal(0, 0.5) + data_standard)
       #HardCoded Data ONLY
       chart1 = plt.plot(data_standard, 'k-', label="HardCoded Data ONLY")
       #HardCoded + RAW-Noise
       chart2 = plt.plot(noise_backup, 'r-', label="HardCoded + RAW-Noise")
       #Mean calculation
       Mean = (noise_backup/20)
       input_mean_list = statistics.mean(noise_backup)

       chart3 = plt.plot(Mean , 'b-', label="Mean of HardCoded + RAW-Noise")
       ##print(type(noise_backup))

       holder_list.append(noise_backup)

       ##print("This is standard deviation: ", standard_deviation)

       #Ypologismos Variance
       # Variance_holder=0
       # for j in range(19):
       #        difference_from_mean =((noise_backup[j])-Mean)
       #        difference_square_value = ((difference_from_mean)**2)
       #        Variance_holder = difference_square_value + Variance_holder
       #        print(Variance_holder)
       # Variance = Variance_holder/20
       # # print("This is Variance: ", Variance)


       leg = plt.legend(loc='lower right')
       ##print("These are HardCoded + RAW-Noise Data: \n", noise_backup)

       plt.show()

       #Assigning data to datafram csv
       df = pd.DataFrame(holder_list)
       #Calculation of Mean for each Measurement
       df["mean"] = df.mean(axis=1)
       #Calculation of Fisher's Kurtosis for each Measurement
       df["kurtosis"] = df.kurtosis(axis=1)
       #Calculation of Min for each Measurement
       df["min"] = df.min(axis=1)
       #Calculation of Max for each Measurement
       df["max"] = df.max(axis=1)

       df_targets = pd.DataFrame()

       #Generation of Targets for Neural Network
       # #ID Target of DATA_STRATIFICATION
       # df[23] = 1
       # df[24] = 0
       # df[25] = 0
       # df[26] = 0
       # df[27] = 0
       # df[28] = 0

       #ID Target of DATA_FRAME_UPTREND
       # df[23] = 0
       # df[24] = 1
       # df[25] = 0
       # df[26] = 0
       # df[27] = 0
       # df[28] = 0


       # #ID Target of DATA_FRAME_INSTABILITY
       # df[23] = 0
       # df[24] = 0
       # df[25] = 1
       # df[26] = 0
       # df[27] = 0
       # df[28] = 0


       # #ID Target of DATA_POINT_OUTSIDE_OF_CONTROL
       # df[23] = 0
       # df[24] = 0
       # df[25] = 0
       # df[26] = 1
       # df[27] = 0
       # df[28] = 0


       # #ID Target of DATA_CYCLE_AND_INSTABILITY
       # df[23] = 0
       # df[24] = 0
       # df[25] = 0
       # df[26] = 0
       # df[27] = 1
       # df[28] = 0


       # #ID Target of DATA_I
       #INSTABILITY_AND_GROUPING
       # df[23] = 0
       # df[24] = 0
       # df[25] = 0
       # df[26] = 0
       # df[27] = 0
       # df[28] = 1



       #print("This is df: \n", df)

       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_STRATIFICATION.csv', index=False)
       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_FRAME_UPTREND.csv', index=False)
       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_FRAME_INSTABILITY.csv', index=False)
       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_POINT_OUTSIDE_OF_CONTROL.csv', index=False)

       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_CYCLE_AND_INSTABILITY.csv', index=False)
       #df.to_csv(r'F:\Users\FIREWIND\Desktop\Μεταπτυχιακό\DATA_INSTABILITY_AND_GROUPING.csv', index=False)
       #print("Printing Data Frame (pandas):", df)

#Maybe include Grand Mean as an input for each pattern.

