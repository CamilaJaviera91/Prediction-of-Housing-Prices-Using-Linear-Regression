#Import necessary libraries

import pandas as pd #For creating and manipulating DataFrames and Series
import curses as cr #Create text-based user interfaces (TUIs) in the terminal
from kaggle_connect import kaggle_connect as kc #Custom function to fetch the dataset using Kaggle API

#Wrapper function to run Kaggle connect using curses.
def run_kaggle():
    return cr.wrapper(kc) #kc is passed as a function, not as a pre-executed call.

boston = run_kaggle()
data = pd.DataFrame(boston)

#Change medv to price and black to b
data['price'] = data['medv']
data['b'] = data['black']
data = data.drop(['medv', 'black'], axis=1)

#Delete unnamed columns
data = data.drop(columns=[col for col in data.columns if col == ''])

#Show basic information
print(data.head())