# Pro Draft Model for League of Legends
Support vector classification model for professional League of Legends drafts

## Description
This Python tool uses a Support Vector Classification (SVC) algorithm to predict the outcome of professional League of Legends drafts using 17800 professional games played from 2022-2023. This model has a ~55% accuracy against the training set.

## Requirements
- Python 3.7 or higher

## Installation
1. Clone or download the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. 


## Limitations and Issues
1. The model evaluates drafts that are likely to win - this may not be directly causitive (i.e. a draft is likely to win not because the team composition is stronger, but rather a stronger team is likely to draft in such a fashion.) It is impossible the evaluate and effictively parameterise the strengths of teams' play to include in the training data. Thus, the model cannnot account for this.
2. Predictions will often remain in the same direction even when the champions on the teams are switched. This is inconsistent with the general understanding of draft dynamics.
   This can be somewhat remedied (but not entirely as the the kernel is RBF not linear) by duplicating the training data, flipping the outcome and champion label. 
   
## Data Smoothing
