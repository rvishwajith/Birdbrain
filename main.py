# Rohith Vishwajith
# October 4, 2024

import torch
import torch.nn as neuralNetworks
import numpy
import pandas

"""
print("Testing if PyTorch is running.")
print(torch.rand(3, 3))
print("PyTorch is confirmed to be running.")
"""

# trainingPath: Path to file containing tweets which are used to train the PyTorch analysis model.
trainingPath = "Data/training-tweets.csv"
# testingPath: Path to file containing tweets that analysis will be performed on.
testingPath = "Data/testing-tweets.csv"
# device: Hardware used to train the model. NVIDIA / CUDA GPU training is faster, but the testing
# hardware being used is an ARM Mac, so a CPU will be used.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Read in the data sets, and Remove unnecessary information:
# 1. ID is not needed, so drop that column.
# 2. Remove Any null valyes.
# 3. In the model, category doesn't exist, rename it so it matches.
trainingData = (
    pandas.read_csv(trainingPath)
    .drop(columns="Id")
    .rename(columns={"Category": "Tweet"})
)
trainingData = trainingData[trainingData["Tweet"] != "Not Available"]
# Why doesn't this work if appended after .rename(...)?
trainingData = trainingData.dropna()
# print("Printing training data:", trainingData)
testingData = (
    pandas.read_csv(testingPath)
    .drop(columns="Id")
    .rename(columns={"Category": "Tweet"})
    .dropna()
)
testingData = testingData[testingData["Tweet"] != "Not Available"]
testingData = testingData.dropna()
print("Printing testing data:", testingData)
