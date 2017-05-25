"""
Maps visitation between MIT dorms, based on a poll done a while ago.
Raw Data: https://docs.google.com/spreadsheets/d/1UtLEgDPxSmMa7ygvBNk4Gxo5qsSJVVZAbVPIRsoRGO8/edit#gid=2068450999
Results: http://imgur.com/a/ev2tH
"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import csv


rawdata = []
processedData = []
ratioData = []

for i in range(12):
    processedData.append([0]*12)
    ratioData.append([0]*12)


dormDict = {
    'EC': 0,
    'Senior': 1,
    'Random': 2,
    'Bexley': 3,
    'Maseeh': 4,
    'McCormick': 5,
    'Baker': 6,
    'BC': 7,
    'MacGregor': 8,
    'New': 9,
    'Next': 10,
    'Simmons': 11
    }

residents = [0]*12

with open('data.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in datareader:
        rawdata.append(row)

#Tally
for person in rawdata:
    for resDorm in dormDict:
        if resDorm in person[2]:
            residents[dormDict[resDorm]] += 1
            for visDorm in dormDict:
                if visDorm in person[1]:
                    processedData[dormDict[resDorm]][dormDict[visDorm]] += 1

for i in processedData:
    print i

print ""
print residents


#Normalize by residents that responded
normData = []

for resI, residence in enumerate(processedData):
    if residents[resI] != 0:
        normData.append([x/residents[resI] for x in residence])
    else:
        #ahhhhh
        residence = [1.1 for x in residence]

for i in normData:
    print i

print ""
print residents

for resIndex in range(12):
    for visIndex in range(12):
        dir1 = normData[resIndex][visIndex]
        dir2 = normData[visIndex][resIndex]
        if dir1 == 0 or dir2 == 0:
            continue

        big = max(dir1,dir2)
        small = min(dir1,dir2)
        ratio = big/small

        ratioData[resIndex][visIndex] = ratio


        
d = np.array(normData)
e = np.array(ratioData)

plt.figure(1)
plt.subplot(211)
plt.imshow(d, interpolation='nearest')
plt.colorbar()

plt.subplot(212)
plt.imshow(e, interpolation='nearest')
plt.colorbar()

