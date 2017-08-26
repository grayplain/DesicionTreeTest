import random

'''
1〜max
 multiple: 倍数
 max:
'''
def generateMultipleDataSet(multiple,start = 1, end = 50):
    #array = []
    featureArray = []
    targetArray = []

    isMultipileValue = 0
    for i in range(start, end):
        if i % multiple == 0:
            isMultipileValue = 1
        else:
            isMultipileValue = 0

        featureArray.append(list(format(i,'010b')))
        targetArray.append(isMultipileValue)
        #array.append((format(i, '10b'), isMultipileValue))
        #array.append((list(format(i,'10b')), isMultipileValue))
    return featureArray, targetArray



def generateThresholdDataSet(threshold=0.5, max = 1000):
    featureArray = []
    targetArray = []

    isThreshold = 0
    for i in range(1, max):
        randomValue = random.uniform(0.0, threshold * 2)
        valueClass = ""
        likeHood = ""
        if randomValue >= threshold:
            isThreshold = 1
        else:
            isThreshold = 0

        if randomValue >=0.0 and randomValue < 0.2:
            valueClass = 1
            likeHood = 0
        elif randomValue >=0.2 and randomValue < 0.4:
            valueClass = 2
            likeHood = 0
        elif randomValue >=0.4 and randomValue < 0.6:
            valueClass = 3

            likeHood = 1
            '''
            if randomValue >= 0.4 and randomValue < 0.45:
                likeHood = 1
            elif randomValue >= 0.45 and randomValue < 0.5:
                likeHood = 2
            elif randomValue >= 0.5 and randomValue < 0.55:
                likeHood = 3
            elif randomValue >= 0.55 and randomValue < 0.6:
                likeHood = 4
            '''
        elif randomValue >=0.6 and randomValue < 0.8:
            valueClass = 4
            likeHood = 0
        elif randomValue >=0.8 and randomValue <= 1.0:
            valueClass = 5
            likeHood = 0

        featureArray.append([valueClass,likeHood])
        targetArray.append(isThreshold)

    return featureArray, targetArray

