from flask import Flask, render_template
import pandas as pd

# For matplotlib
import base64
from io import BytesIO
from matplotlib.figure import Figure

# For plotly
import plotly.express as px
import plotly.io as pio

# INIT APP --------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)


# FUNCTIONS -------------------------------------------------------------------------------------------------------------------
# Function to strip the summary data off the bank csv and get to the nitty gritty
def stripCSV(filepath):
    # Open the file and read all lines
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Find the index of the line that starts with 'Date'
    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Date"):
            header_index = i
            break

    # If 'Date' is not found, marking the start, raise an Error
    if header_index is None:
        raise ValueError(f"ERROR: In {filepath}, value 'Date' not found.")

    # Return the real body of the csv into a data frame
    df = pd.read_csv(filepath, skiprows=header_index)
    return df

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


# PAGES -----------------------------------------------------------------------------------------------------------------------
# Home (Landing)
@app.route("/")
def home():
    # The RAW sample data, all values, records, and columns
    samp = stripCSV('./upload/SampGTP20June16-22.csv')

    # Top 5 Debits Decending
    sampT5DD = samp.loc[samp['Amount'] < 0, ['Amount', 'Date', 'Description']].sort_values('Amount').head(5)

    # Top 5 Credits Decending
    sampT5CD = samp.loc[samp['Amount'] > 0, ['Amount', 'Date', 'Description']].sort_values('Amount', ascending=False).head(5)

    # Testing the matplotlib Figure
    sampFigure = genFigure()

    # Top 5 Debits, only the date and amount (x, y) for matplotlib
    sampT5DamountDate = samp.loc[samp['Amount'] < 0, ['Date', 'Amount']].sort_values('Amount').head(5)
    sampT5DamountDate['Label'] = sampT5DamountDate['Date'] + "\n" + sampT5DamountDate['Amount'].astype(str)
    
    # Bar chart for matplot lib
    sampBar = genBarChart(sampT5DamountDate)

    # Pushing the tables to the html page
    return render_template(
        'home.html',
        samp=samp.to_html(index=False, justify='left'),
        sampT5DD=sampT5DD.to_html(index=False, justify='left'),
        sampT5DamountDate=sampT5DamountDate.to_html(index=False, justify='left'),
        sampT5CD=sampT5CD.to_html(index=False, justify='left'),
        sampFigure=sampFigure,
        sampBar=sampBar,)

# Adding some styling
@app.route("/new")
def new():
    return render_template('new.html')


# RUNNING ---------------------------------------------------------------------------------------------------------------------
# Debug mode shows us a bunch of terminal messages, debugging, etc. (not for prod.)
if __name__ == '__main__':
    app.run(debug=True)