#By:Ajinkya
#Final Project SIE507
#Analysis of petroleum production, Import, Export and Consumption in USA

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from matplotlib import style
style.use('ggplot')

def raw_data_petroleum():#function created to display raw data

    df = pd.read_csv('Final.csv', index_col=0)#read the data from the downloaded CSV file
    print(df.head())#print all Raw data
    df["Price"].plot(kind='area')#plot graph with respect to price
    plt.title("Change of Price ")#Title for this graph is Change in Price
    plt.ylabel("Doller$")#Lables
    plt.legend()

    plt.show()#Show the plotted graph

def price_yearly_summaries_plot():#new function with change in date format
    df = pd.read_csv('Final.csv')

    df['datetime'] = pd.to_datetime(df['Date'])#convert DATE values into a datatime format (needed for groupby)

    df.groupby(df.datetime.dt.year)['Price'].sum().plot.bar()#Group by price to plot Graph

    plt.title("Price of Gas/Year in USA")
    plt.ylabel("Doller$")
    plt.legend()
    plt.show()


def PIE_yearly_summaries_plot_():
    df = pd.read_csv('Final.csv')

    df['datetime'] = pd.to_datetime(df['Date'])#convert DATE values into a datatime format (needed for groupby)

    df.groupby(df.datetime.dt.year)['export'].sum().plot()#Group by Export to plot Graph
    df.groupby(df.datetime.dt.year)['import'].sum().plot()#Group by Import to plot Graph
    df.groupby(df.datetime.dt.year)['production'].sum().plot()#Group by production to plot Graph
    plt.title("Production,Import,Export/Year in USA")
    plt.ylabel("Thousand Barrels")
    plt.legend()
    plt.show()


print("\nThis program Do exploratory data analysis of Petroleum Production,Import,Export,Price with Respect to Time \n")

print("Option 1: Read the raw data from file and plot it")
print("Option 2: calculate yearly change in Price summaries and plot them")
print("Option 3: calculate yearly Production,Import,Export for Petroleum  summaries and plot them")
print("Option 4:  plot All Option them one by one")

choice = int(input("\nwhich option do you choose:"))

if choice == 1:
    raw_data_petroleum()

if choice == 2:
    price_yearly_summaries_plot()

if choice == 3:
    PIE_yearly_summaries_plot_()

if choice == 4:
    raw_data_petroleum()
    price_yearly_summaries_plot()
    PIE_yearly_summaries_plot_()
else:
    print("not a valid option")