# Locally Run Finance App

**MISSION:** Develop a locally running application that takes in banking
information and spits out different data metrics and visuals.

## Minimum Viable Product (MVP):
- Hosted in a flask local application
- Can read in a single csv file that is clean with data like the bank
- Screen that shows the data pop up in a table
- A graph or two for PoC

## Goals:
- Dashboard on the front page with a bunch of cool metrics
    - Circle/Pie chart showing the amount of spending in diff. categories
    - Top 5 most expensive purchases
    - Tracks the history of total weekly amount spent, week by week
- Page for sending information
    - Some nice box that you double click, it pops up your files,
    then you double click the one you want. Similar to most web pages

## Progress:
- MVP is done, working towards some formatting and metrics I want
<br><br>


# Instructions for Running and Doing Things
## Running App Locally:
- Activate virtual env. in correct directory/terminal
- Make sure all code is up to date and saved locally
- Run:
```sh
python3 app.py
```
- See it here: [WEBSITE](http://127.0.0.1:5000)


## Running App on PythonAnywhere:
- First: Make sure all local code is pushed to the github repo
- Login to PythonAnywhere with professional email
- Open a bash terminal and pull down the most recent code


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