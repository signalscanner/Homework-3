import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from numpy import convolve

# Moving average metodu kullan
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

with open('HW03_USD_TRY_Trading.txt','r') as infile:
    RawData = [x.strip().split('\t') for x in infile if len(x.strip()) != 0 ]

RawData = np.delete(RawData, (0), axis=0)

# Butun close degerleri (5 close sutunu, 0 dan basliyor sutunlar)
CloseValues = [row[5] for row in RawData]
xAxisValue = [i for i in range(len(CloseValues))]
