#!/bin/python3

import sys
import pandas as pd
from sklearn import linear_model

if __name__ == '__main__':
    timeCharged = float(input().strip())

    d = pd.read_csv('trainingdata.txt', header=None)

    # After plotting, we must remove items with a duration of time greater than eight.
    d = d[d.iloc[:,1] < 8]

    # Adding bias
    d.insert(0, len(d.columns), 0)

    # Seperate dependent and independent variables
    X = d.iloc[:,0:2]
    Y = d.iloc[:,2]

    # Create the classifier model
    model = linear_model.LinearRegression()
    model.fit(X, Y)

    # Set new value to predict
    result = model.predict([[0, timeCharged]])
    if result[0] > 8:
        print (8.0)
    else:
        print (round(result[0],2))
