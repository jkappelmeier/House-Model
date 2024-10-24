import Core.Model as Model
import Config as C
import numpy as np

# Implements the Model superclass for the house election
class HouseModel(Model.Model):

    # Constructor for this class
    #
    # Inputs:
    #   name - name of this object
    #   geography - Head of geography class tree
    #   cor - correlation matrix to be used (must match lengths of all children of geography)
    #   currentDate - current date to run Model
    # Output:
    #   Instance of this class
    def __init__(self, name, geography, cor, currentDate = C.currentDate):

        # Call superclass
        Model.Model.__init__(self, name, geography, cor, currentDate)


    # Simulate the eleciton nSamples times
    #
    # Input:
    #   nRuns - Number of times to simulate election
    # Output:
    #   incAvg - Average house seats of incumbent president party
    #   chalAvg - Average house seats of challenger president party
    #   winRate - Percent of times incumbent party wins
    #   lossRate - Percent of times incumbent party loses
    #   simDistrictVoteList - List of all the district results generated
    def runSimulation(self, nRuns):
        self.estimateVote()

        # Collect data
        stateEst = np.array(np.transpose(self.finalEst))[0]

        nWins = 0
        nLoses = 0
        nDistrictsInc = []
        nDistrictsChal = []
        simDistrictVoteList = []
        tippingPoint = np.zeros(len(stateEst))
        for i in range(nRuns):
            simVote = np.random.multivariate_normal(stateEst, self.finalCov)
            # Get rid of votes outside of 0 - 1 range
            simVote[simVote > 1] = 1
            simVote[simVote < 0] = 0
            districtsWon = [1 if a_ > 0.5 else 0 for a_ in simVote]
            districtsWon = sum(districtsWon)
            districtsLost = 435 - districtsWon
            nDistrictsInc.append(districtsWon)
            nDistrictsChal.append(districtsLost)

            if districtsWon > districtsLost:
                nWins = nWins + 1
            elif districtsLost > districtsWon:
                nLoses = nLoses + 1
            simDistrictVoteList.append(simVote)

            # Find Tipping Point State
            sortedIndices = np.argsort(simVote)
            districts = 0
            count = 0
            while districts < 218:
                districts = districts + 1
                count = count + 1
            tippingPoint[sortedIndices[count-1]] = tippingPoint[sortedIndices[count-1]] + 1

            if i % 100 == 0:
                print(str(i) + ' / ' + str(nRuns) + ' Runs completed')

        winRate = nWins /  nRuns
        lossRate = nLoses / nRuns
        incAvg = sum(nDistrictsInc) / nRuns
        chalAvg = sum(nDistrictsChal) / nRuns
        tippingPoint = tippingPoint / np.sum(tippingPoint)

        return [incAvg, chalAvg, winRate, lossRate, tippingPoint, simDistrictVoteList]
