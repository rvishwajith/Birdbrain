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

# DATA PARSING & PREPROCESSING
# Read in the data sets, and Remove unnecessary information:
#   1. ID is not needed, so drop that column.
#   2. Remove Any null valyes.
#   3. In the model, category doesn't exist, rename it so it matches.

# trainingPath: Path to file containing tweets which are used to train the
#   PyTorch analysis model.
# testingPath: Path to file containing tweets that will be analyzed.
trainingPath, testingPath = "data/training-tweets.csv", "data/testing-tweets.csv"

# trainingData: Memory-mapped version of the training tweet data, which is
#   preprocessed before being used to train the model.
# testingData: The Tweet dataset which will be analyzed using the model after
#   it has been trained.
trainingData = (
    pandas.read_csv(trainingPath)
    .drop(columns="Id")
    .rename(columns={"Category": "Tweet"})
)
testingData = (
    pandas.read_csv(testingPath)
    .drop(columns="Id")
    .rename(columns={"Category": "Tweet"})
    .dropna()
)

# TODO: Add a preprocessing function for better reusability.

trainingData, testingData = (
    trainingData[trainingData["Tweet"] != "Not Available"],
    testingData[testingData["Tweet"] != "Not Available"],
)
# ISSUE: Why doesn't this work if appended after .rename(...)?
trainingData, testingData = trainingData.dropna(), testingData.dropna()
print("Printing testing data:", testingData)

# print("Printing training data:", trainingData)
# device: Hardware used to train the model. NVIDIA / CUDA GPU training is
#         faster (testing hardware being is an ARM Mac, so CPU is used).
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
