#Import necessary libraries

import pandas as pd #For creating and manipulating DataFrames and Series
import curses as cr #Create text-based user interfaces (TUIs) in the terminal
from sklearn.model_selection import train_test_split as ts #Divides data into training and testing sets in a random and stratified way (if needed).
from sklearn.linear_model import LinearRegression as lr #Fits a linear model to data by finding the line (or hyperplane) that minimizes the sum of squared differences between predicted and actual values.
from sklearn.metrics import mean_squared_error as mse #Measures the average squared difference between predicted and actual values.
from sklearn.metrics import mean_absolute_error as mae #Measures the average absolute difference between predicted and actual values.
import numpy as np #Handles arrays, performs linear algebra, matrix computations, random number generation, and other mathematical operations.
from kaggle_connect import kaggle_connect as kc #Custom function to fetch the dataset using Kaggle API

#Wrapper function to run Kaggle connect using curses.
def run_kaggle():
    return cr.wrapper(kc) #kc is passed as a function, not as a pre-executed call.

def menu(stdscr):
    #Clear the screen
    stdscr.clear()
    stdscr.refresh()

    boston = run_kaggle()
    data = pd.DataFrame(boston)
    data.columns = data.columns.str.lower()

    #Change medv to price and black to b
    if 'medv' in data.columns:
        data.rename(columns={'medv': 'price'}, inplace=True)
    if 'black' in data.columns:
        data.rename(columns={'black': 'b'}, inplace=True)

    #Drop unnecesary columns
    columns_to_drop = ['medv', 'black', 'Unnamed: 0']
    data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

    header = "\n\nBoston Housing Dataset\n\n"
    stats = data.describe().round(1).to_string()
    
    #display
    stdscr.addstr(header)
    stdscr.addstr("Descriptive Statistics:\n")
    stdscr.addstr(stats)
    stdscr.addstr("\n")

    #Split the data into features (X) and target (y)
    X = data.drop(columns=['price'])
    y = data['price']

    #Split the dataset into trainig and test sets
    X_train, X_test,  y_train, y_test = ts(X, y, test_size=0.2, random_state=42)

    #Create and train the linear regression model
    model = lr()
    model.fit(X_train, y_train)

    #Predict on the test set
    y_pred = model.predict(X_test)

    #Evaluate the model
    rmse = np.sqrt(mse(y_test, y_pred))
    mae_ = mae(y_test, y_pred)

    #Show mae and mse
    stdscr.addstr("Mae and Mse\n\n")
    stdscr.addstr(f"RMSE: {rmse:.2f}\n")
    stdscr.addstr(f"MAE: {mae_:.2f}\n")


    # Wait for user input to exit
    stdscr.addstr("\n\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()

# Run the curses wrapper
if __name__ == "__main__":
    cr.wrapper(menu)