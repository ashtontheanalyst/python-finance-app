# My own Module for doing data things
# Data processing/fixing
import pandas as pd
import os

# Graphs and charts
import base64
from io import BytesIO
from matplotlib.figure import Figure

# Important items
DATA_PATH = './data'



# PROCESSING THE DATA AND FIXING IT


# Counts the amount of files in 'data' directory
def countFilesinData():

    # Checking to make sure we can access the Data folder, if not raise an error
    if os.path.exists(DATA_PATH):
        print("SUCCESS: Correct path to local 'data' directory.")
    else:
        print("ERROR: 'data' folder not able to be reached, check to make sure you have"
        "created the folder. See README.md for more.")

    # List of all files in the 'data' directory
    dataFiles = os.listdir(DATA_PATH)

    # Return the number of files as an int
    return(len(dataFiles))


# Strips the intro data off the top of the CSV from BoA, gets to the main data
def stripCSV(filepath):

    # Open the file and put each individual line into a list called lines
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Find the line is list called lines that starts with "Date", strip that line out
    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Date"):
            header_index = i
            break

    # If 'Date' is not found, marking the start, raise an Error
    if header_index is None:
        raise ValueError(f"ERROR: In {filepath}, value 'Date' not found.")

    # Return that list of lines as a pd data frame
    df = pd.read_csv(filepath, skiprows=header_index)

    # Clean the df for import, correct data types
    cleanFrame(df)

    # Import the cleaned df into the db
    frameToBase(df)

    return df


# Correcting the data types since they come in as all strings
def cleanFrame(df):

    # Change "Running Bal." to "Balance", need this for SQLite later
    df.rename(columns={"Running Bal.":"Balance"}, inplace=True)

    df["Date"]              = pd.to_datetime(df["Date"])
    df["Description"]       = df["Description"].astype('string')
    # Makes sure the amount is a string, deletes the comma if it's a thousands
    # value and then converts that to a two decimal digit float
    df["Amount"]            = df["Amount"].astype("string").str.replace(",", "").astype('float64')
    df["Balance"]      = df["Balance"].astype("string").str.replace(",", "").astype('float64')

    # This drops the first value in the frame, this is the beginning balance line:
    # XX/XX/XXXX,Beginning balance as of XX/XX/XXXX,,"XXX.XX"
    if df["Description"].str.contains("Beginning balance as of", na=False).any():
        df.drop([0], inplace=True)

    return df

# Takes the inbound, stripped data frame, and puts it into the SQLlite3 db
def frameToBase(df):
    pass


'''
# MAKING GRAPHS AND CHARTS


# Function to make a Figure using matplotlib
def genFigure():
    # Flask does NOT like pyplot so we use figures instead
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])

    # Save to a temp memory buffer, then to a png
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Now get it ready for html
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


# Function to make a bar chart with the passed in data frame
def genBarChart(df):
    fig = Figure()
    ax = fig.subplots()

    ax.bar(df['Label'], df['Amount'], color='navy')
    ax.set_title("Top 5 Debits")
    ax.set_xlabel("Transaction")
    ax.set_ylabel("Amount")

    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Now get it ready for html
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
'''