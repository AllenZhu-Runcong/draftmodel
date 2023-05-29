# Import dependencies
import csv
import joblib
import pandas as pd
from sklearn.svm import SVC

# Function to predict the outcome of a League of Legends draft
def predict(blueChampions, redChampions, patch, disregardSide=False):
    #blueChampion, redChampions, takes list of strings champion + role (e.g. ['GragasTop', 'WukongJungle', 'AnnieMid', 'JinxBot', 'BraumSupport'])
    
    # Load the trained required model
    if disregardSide == False:
        model = joblib.load('svm_draftmodel.pkl')
    else:
        model = joblib.load('svm_draftmodelnormed.pkl')
    
    # Read the base data from a CSV file
    base = pd.read_csv('base.csv')
    
    # Activating corresponding columns for blue champions and red champions 
    base.loc[0, blueChampions] = 1
    base.loc[0, redChampions] = -1
    
    # Set the patch column for the specified patch to 1
    base.loc[0, 'Patch_'+patch] = 1
    
    # Make predictions using the model
    model.predict(base)
    confidence = model.decision_function(base)
    prediction = model.predict(base)
    
    # Return the prediction and confidence as a string
    return confidence