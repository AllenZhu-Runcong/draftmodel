# draftmodel
Support vector classification model for professional League of Legends drafts

## Description
This Python tool utilizes Support Vector Classification (SVC) algorithm to predict the outcome of professional League of Legends drafts using 17800 professional games played from 2022-2023. This model has a ~55% accuracy against the training set.

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
1. The model evaluates drafts that are likely to win - this may not be directly causitive (i.e. a draft is likely to win not because the team composition is stronger, but rather a stronger team is likely to draft in such a fashion) .It is impossible the evaluate and effictively parameterise the strengths of teams' play to include in the training data. Thus, the model cannnot account for this.
2. Predictions will often remain in the same direction even when the champions on the teams are switched. This is inconsistent with the general understanding of draft dynamics.

## Data Smoothing
