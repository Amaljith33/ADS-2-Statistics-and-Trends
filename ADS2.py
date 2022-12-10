import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Bar graph 1
Renewable_Electricity_Output= pd.read_excel("Renewable Electricity Output.xlsx")
Renewable_Electricity_Output= Renewable_Electricity_Output.drop(['Series Name','Series Code','Country Code'], axis=1).dropna()
Renewable_Electricity_Output_Transpose= Renewable_Electricity_Output.transpose()
print(Renewable_Electricity_Output.set_index)
width = .2
plt.figure(figsize=(15,16))
Years= ["1990 [YR1990]", "1995 [YR1995]", "2000 [YR2000]", "2005 [YR2005]", "2010 [YR2010]", "2015 [YR2015]"]
X_axis = np.arange(len(Years))
Renewable_Electricity_Output.plot(x = "Country Name" , y = Years, kind='bar')
plt.title('Renewable electricity output (% of total electricity output)', fontsize=12)
plt.xlabel('Countries', fontsize=7)
plt.xticks(fontsize=7, rotation = 90)
plt.ylabel('% of total electricity output', fontsize=7)
plt.yticks(fontsize=7)
plt.legend(frameon=False, fontsize=6)
plt.savefig('REO Bargraph.png')
plt.show()

#Bar graph 2
Renewable_Energy_Consumption= pd.read_excel("Renewable Energy Consumption.xlsx")
Renewable_Energy_Consumption= Renewable_Energy_Consumption.drop(['Series Name','Series Code','Country Code'], axis=1).dropna()
Renewable_Energy_Consumption_Transpose= Renewable_Energy_Consumption.transpose()
print(Renewable_Energy_Consumption.set_index)
width = .2
plt.figure(figsize=(15,16))
Years= ["1990 [YR1990]", "1995 [YR1995]", "2000 [YR2000]", "2005 [YR2005]", "2010 [YR2010]", "2015 [YR2015]"]
X_axis = np.arange(len(Years))
Renewable_Energy_Consumption.plot(x = "Country Name" , y = Years, kind='bar')
plt.title('Renewable energy consumption (% of total final energy consumption)', fontsize=12)
plt.xlabel('Countries', fontsize=7)
plt.xticks(fontsize=7, rotation = 90)
plt.ylabel('% of total final energy consumption', fontsize=7)
plt.yticks(fontsize=7)
plt.legend(frameon=False, fontsize=6)
plt.savefig('REC Bargraph.png')
plt.show() 

#Line Graph 1
Agricultural_Nitrous_Oxide_Emissions= pd.read_excel("Agricultural Nitrous Oxide Emissions.xlsx")
Agricultural_Nitrous_Oxide_Emissions= Agricultural_Nitrous_Oxide_Emissions.drop(['Series Name','Series Code','Country Code'], axis=1).dropna()
Agricultural_Nitrous_Oxide_Emissions= Agricultural_Nitrous_Oxide_Emissions.set_index("Country Name")
Agricultural_Nitrous_Oxide_Emissions_Transpose= Agricultural_Nitrous_Oxide_Emissions.transpose()
print(Agricultural_Nitrous_Oxide_Emissions.set_index)

#Line Graph 2
Cereal_Yield= pd.read_excel("Cereal Yield.xlsx")
Cereal_Yield= Cereal_Yield.drop(['Series Name','Series Code','Country Code'], axis=1).dropna()
Cereal_Yield= Cereal_Yield.set_index("Country Name")
Cereal_Yield_Transpose= Cereal_Yield.transpose()
print(Cereal_Yield.set_index)