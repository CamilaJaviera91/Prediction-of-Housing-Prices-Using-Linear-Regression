#Import necessary libraries

import pandas as pd #For creating and manipulating DataFrames and Series
import curses as cr #Create text-based user interfaces (TUIs) in the terminal
from kaggle_connect import kaggle_connect as kc #Custom function to fetch the dataset using Kaggle API
from sklearn.preprocessing import StandardScaler as ss #used for standardizing features in a dataset.

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

    # Wait for user input to exit
    stdscr.addstr("\n\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()

# Run the curses wrapper
if __name__ == "__main__":
    cr.wrapper(menu)