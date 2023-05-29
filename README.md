# draftmodel
C-Support vector classification model for professional League of Legends drafts

## Description
This Python tool utilizes Support Vector Classification (SVC) algorithm to predict the outcome of professional League of Legends drafts.

## Requirements
- Python 3.7 or higher
- Scikit-learn library
- Pandas library

## Installation
1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your dataset: Create a CSV file containing the historical data of League of Legends games. Each row represents a game, and each column represents a feature or statistic. Make sure to include the outcome (win/loss) of each game as the target variable.
2. Open the `predictor.py` file in a text editor or IDE.
3. Modify the `dataset_path` variable in the `predict_outcome` function to point to the location of your dataset file.
4. Run the `predictor.py` file. The tool will load the dataset, train the SVC model, and predict the outcome of new games.
5. The predicted outcomes will be displayed on the console.

## Input Format
Champion names should be inputted as

## Limitations and Issues
