import calc
import sklearn
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy


def predMultipie():
    #特徴データと正解データを引っ張ってくる
    trainFeature,trainTarget = calc.generateMultipleDataSet(multiple=3,start=1,end=100)

    #テストする情報
    testFeature,testTarget = calc.generateMultipleDataSet(multiple=3,start=101,end=200)


    #モデルを学習させる
    dtClassFier = tree.DecisionTreeClassifier()
    dtClassFier.fit(trainFeature,trainTarget)

    predLabel = dtClassFier.predict(testFeature)

    score = accuracy_score(testTarget, predLabel)
    print(score)

def predThreshold():
    #特徴データと正解データを引っ張ってくる
    trainFeature,trainTarget = calc.generateThresholdDataSet(max=1000)

    #テストする情報
    testFeature,testTarget = calc.generateThresholdDataSet(max=1000)

    #モデルを学習させる
    dtClassFier = tree.DecisionTreeClassifier()
    dtClassFier.fit(trainFeature,trainTarget)

    predLabel = dtClassFier.predict(testFeature)

    score = accuracy_score(testTarget, predLabel)
    print(score)




predThreshold()


exit()