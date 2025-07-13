import os
from flask import Flask, render_template, request, redirect, url_for
import pData        # My own module for data and visuals

DATA_PATH = './data'

# Initialize the App
app = Flask(__name__)


# Home (Landing)
@app.route("/")
def home():
    NUM_FILES = pData.countFilesinData()

    if NUM_FILES == 0:
        return render_template('noData.html')
    
    # else return the real home page with aggregated data
    else:
        # The RAW sample data, all values, records, and columns
        samp = pData.stripCSV('./data/SAMPweek.csv')

        # Top 5 Debits Decending
        sampT5DD = samp.loc[samp['Amount'] < 0, ['Date', 'Description', 'Amount']].sort_values('Amount').head(5)

        # Top 5 Credits Decending
        sampT5CD = samp.loc[samp['Amount'] > 0, ['Date', 'Description', 'Amount']].sort_values('Amount', ascending=False).head(5)

        return render_template(
            'home.html',
            sampT5DD=sampT5DD.to_html(index=False, justify='left', classes='styled-table'),
            sampT5CD=sampT5CD.to_html(index=False, justify='left', classes='styled-table'),
            )


# Historial page, shows the raw data week to week that's saved
@app.route("/historical-data")
def historical():
    NUM_FILES = pData.countFilesinData()

    if NUM_FILES == 0:
        return render_template('noData.html')
    
    else:
        # The RAW sample data, all values, records, and columns
        samp = pData.stripCSV('./data/SAMPweek.csv')

        return render_template(
            'historical.html',
            samp=samp.to_html(index=False, justify='left', classes='styled-table'),
            )


# This displays the upload page but takes in nothing
@app.route("/upload", methods=["GET"])
def upload():
    return render_template('upload.html')


# This is for posting data to the upload page
@app.route("/upload", methods=["POST"])
def uploadInput():
    files = request.files.getlist("statements")

    # Takes in a max of 4 files, gets the raw filename, saves it to the 
    # data folder
    for f in files[:4]:
        filename = f.filename
        savePath = os.path.join(DATA_PATH, filename)
        f.save(savePath)

    return redirect(url_for("home"))


# Deletes all csv files in the 'data' folder
@app.route("/delete", methods=["POST"])
def delete():
    # Go through each file in the folder and delete it's path and file
    for file in os.listdir(DATA_PATH):
        if file.lower().endswith(".csv"):
            full_path = os.path.join(DATA_PATH, file)
            os.remove(full_path)

    # Since this is just a function, return nothing to the screen
    return ("", 204)


# Runs the app
# Debug mode shows us a bunch of terminal messages, debugging, etc. (not for prod.)
if __name__ == '__main__':
    app.run(debug=True)