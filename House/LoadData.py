import numpy as np
import csv
import sys
import Config as C
sys.path.insert(1, '../Model')
import Core.Poll as Poll
import House.Geographies.CongressionalDistrict as CongressionalDistrict

# Load in Congressional District Data
congressionalDistricts = []
with open('../Data/DistrictFundamentals.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',')
    rowCount = 0
    for row in data:
        if rowCount > 0:
            est = float(row[1])

            district = CongressionalDistrict.CongressionalDistrict(str(row[0]), est, float(row[2]), demName = str(row[3]), gopName = str(row[4]))
            congressionalDistricts.append(district)

        rowCount = rowCount + 1

# Load in polls
polls = []
with open('../Data/Polls.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',')
    rowCount = 0
    for row in data:
        if rowCount > 0:
            geography = str(row[0])
            date = str(row[1])
            result = [float(row[2][:-1]), float(row[3][:-1])]
            pollster = str(row[4])
            sampleSize = int(row[5])
            poll = Poll.Poll(geography, date, result, pollster, sampleSize)
            polls.append(poll)
        rowCount = rowCount + 1


# Load in correlation matrix
cor = np.zeros([435, 435])
with open('../Data/DistrictCorrelation.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',')
    rowCount = 0
    for row in data:
        if rowCount > 0:
            cor[rowCount - 1, :] = row[1:]
        rowCount = rowCount + 1
