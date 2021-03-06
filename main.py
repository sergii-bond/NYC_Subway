import numpy as np
import pandas as pd
import pandasql
import csv
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


import linear_regression_predictions as lrp
#import sgd_regressor as sgd
import compute_r_squared as r2
import plot_residuals as pr

dataframe = pd.read_csv("turnstile_data_master_with_weather.csv")
dataframe = dataframe[0:10000]
#df = dataframe
#df.columns.values
#df['ENTRIESn_hourly'].corr(df['meantempi'])
y = dataframe['ENTRIESn_hourly']
g = lrp.predictions(dataframe)
#g = sgd.predictions(dataframe)

print r2.compute_r_squared(y, g) 
hist = pr.plot_residuals(dataframe, g)
hist.show()

x = y - g
plt.figure()
scipy.stats.probplot((x - np.mean(x))/np.std(x), dist = 'norm', plot = plt)
plt.show()

plt.figure()
plt.title("Residuals per data point")
plt.xlabel("Data point ID")
plt.ylabel("Residuals")
plt.plot(x)
plt.show()
