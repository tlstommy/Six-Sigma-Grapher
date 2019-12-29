import pandas,numpy,sys,os
from statistics import stdev
import barGraphSink
#bar graph float data calc
#################################################################################
#init
#################################################################################
dates = []
floatingWeights = []
sinkingWeights = []
totalWeights = []
floatPercents = []
sinkPercents = []
dataSet = []



def getDataFrame(fileName):
    global dataSet
    del dataSet[:]
    cwd = os.getcwd()
    df = pandas.read_csv(os.path.join(cwd,"Sink Data\\",fileName))
    print(df)
    dataset = df.values.tolist()
    for item in dataset:
        dataSet.append(item)
    print(dataset)
    
    return dataset

def getDates():
    global dates
    print("dates: ",dates)
    
    del dates[:]
    print("dataset: ",dataSet)
    print("dates after del: ",dates)
    for items in dataSet:
        #print(items[0])
        
        
        dates.append(items[0])
    print("dates: ", dates)

def getFloatWeight():
    del floatingWeights[:]
    for items in dataSet:
        #print(items[1])
        floatingWeights.append(items[2])

def getSinkWeight():
    del sinkingWeights[:]
    for items in dataSet:
        #print(items[2])
        sinkingWeights.append(items[1])

def totalWeight(sinkL,floatL): #get total weight of sink weight and float weight and add to list
    del totalWeights[:]
    for i in range(len(sinkL)):
        totalWeightItem = sinkL[i] + floatL[i]
        totalWeights.append(totalWeightItem) 
def floatPercent(totalL,floatL):
    
    del floatPercents[:]
    for i in range(len(floatL)):
        floatPercent = round((floatL[i] / totalL[i]) * 100,1)
        floatPercents.append(floatPercent)
        
def sinkPercent(totalL,sinkL):
    del sinkPercents[:]
    for i in range(len(sinkL)):
        sinkPercent = round((sinkL[i] / totalL[i]) * 100,1)
        sinkPercents.append(sinkPercent)


###########################################################################

def callLineGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
    graphFloat.plotGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates)




#average = findAverage(floatPercents)
#standardDeviation(floatPercents)


#ssigmas,ucl,lcl = updateControls(100,True)
#floatGraphs = lineGraphFloat.FloatGraphs(3,ucl,lcl,average,floatPercents,sinkPercents,dates)

def call():
    dataSet = getDataFrame("sinking_data.csv")
    getDates()
    getSinkWeight()
    getFloatWeight()
    totalWeight(sinkingWeights,floatingWeights)
    floatPercent(totalWeights,floatingWeights)
    sinkPercent(totalWeights,sinkingWeights)
    
    barGraph = barGraphSink.SinkBarGraph(floatPercents,sinkPercents,dates)
