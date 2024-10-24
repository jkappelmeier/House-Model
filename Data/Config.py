import datetime
import numpy as np
# This provides all constants/config values used by model
# Note that data comes from elections from 1996 - 2020


### Race Specific Strings

incParty = 'D' # Incumbent Party

currentDate = datetime.date.today() # Current Date
electionDate = datetime.date(2024,11,5) # Election Date
startDate =  datetime.date(2024,1,1) # Campaign Start Date


### National-Level Fundamental Consants

incAvg = 0.4843 # Average incumbent 2-party vote share
incSigma = 0.0253 # Standard deviation in incumbent 2-party vote share


### National-Level Polling Constants

pollingSigmaSF = 0.0566 # Average polling error at N = 1000
pollingProcessNoiseNat = 8.6e-6 # Polling process noise per day for national polls
#pollingBiasSigmaNat = 0.03796 # National Polling Bias Noise
pollingBiasSigmaNat = 0.025 # National Polling Bias Noise

### District-Level Polling Constants

pollingProcessNoiseDistrict = 1.32E-05
pollingBiasSigmaDistrict = 0.0316