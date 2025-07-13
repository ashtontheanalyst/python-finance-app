# Locally Run Finance App

**GOAL:** Develop a locally running application that takes in banking
information and spits out different data metrics and visuals.

## Minimum Viable Product (MVP):
- Locally hosted flask web application
- Ingests a single, clean, TEST data set with bank style information
- Multiple tables with specific filters and/or sorting
- A graph of some sort from plotly or matplotlib

## Ideas:
- Show some graphs of week to week spending
- A separate tab to look at data week to week, unfiltered, RAW and split up nicely
- Persistent storage

## Achieved:
- (06/20) MVP is done, working towards some formatting and metrics I want
- (07/10) Working on some new goals, shifting what I want out of the product
- (07/10) There's now a Main (home) page showing key metrics, and then the
Historial page shows the whole RAW dataset
- (07/11) Created a page called 'Upload' where the user can click a button and
upload a csv file statement. Right now it has to be the hard named sample one
right now, anything else and it bugs out: SampGTP20June16-22.csv
- (07/11) Created a button on the 'Upload' page that will delete all csv files
in the 'data' folder. Basically, it clears all uploaded data to fresh
- (07/12) Created the noData.html page which is returned upon clicking the 'Main'
or 'Historical' tab if there are no .csv files in the local 'data' folder yet.
Makes the page not crash if there's no data, makes the user upload.
- (07/12) Made a pData.py file to house all of my data processing, cleaning, and 
analysis functions as well as the graphs. It's referenced my the main file, app.py,
to then conduct those operations. Cleans up the readbility of the app.
- (07/13) Works on both sample statement .csv files as well as REAL statements now.
Only hiccup is that the filename has to be hardcoded in instead of detected.
- (07/13) Data is properly cleaned up when it comes in. Correct types and everything.

## Working on:
- (07/12) Tutorial specifically on SQLite3, it's in my github repo under 'Python'
<br><br>


# Instructions for Running and Doing Things

## Initial Set-Up:
- Pull this repo down from github
- In the main repo folder that you now have locally, create a folder named 'data' 
exactly. This will hold your statements.

## Running App Locally:
- Activate virtual env. in correct directory/terminal
- Make sure all code is up to date and saved locally
- Run:
```sh
python3 app.py
```
- See it here: [WEBSITE](http://127.0.0.1:5000)

## Virtual Environment (myenv)
NOTE: This is all done within VS Code, in the ./code/website folder.

### Creating:
```sh
python -m venv myenv
```

### Starting:
- Windows:
    ```sh
    myenv\Scripts\activate
    ```
- Linux:
    ```sh
    source myenv/bin/activate
    ```

### Stopping:
- Windows:
    ```sh
    myenv\Scripts\deactivate.bat
    ```
- Linux:
    ```sh
    deactivate
    ```

## Downloading Requirements.txt
NOTE: Make sure the virtual environment is active before doing this or it
will install eveything locally instead.
```sh
pip install -r requirements.txt
```