import json,csv,pandas,os
dataSet = []


#Things i need to calculate:
# percent floating
# percent sinking
# average of float% or sink % data
# standard deviation
# UCL & LCL
# 
def getDataSet(mode,fileName):
    dataSetJsonFormat = {}
    data = []
    date = ""
    sink = ""
    floatV = ""
    cwd = os.getcwd()
    if mode == "0":    
        with open(os.path.join(cwd,"Float Data\\",fileName),"r") as dataSetFile:
            for entry in dataSetFile.readlines():
                entry = entry.replace("\n","")
                dataSetJsonFormat = json.loads(entry)
                
                date = dataSetJsonFormat["date"]
                sink = dataSetJsonFormat["sink"]
                floatV = dataSetJsonFormat["float"]
                
                listItem = [date,sink,floatV]
                data.append(listItem)


                print(data)
        dataSetFile.close()
    
    
    
    elif mode == "1":    
        with open(os.path.join(cwd,"Sink Data\\",fileName),"r") as dataSetFile:
            for entry in dataSetFile.readlines():
                entry = entry.replace("\n","")
                dataSetJsonFormat = json.loads(entry)
                
                date = dataSetJsonFormat["date"]
                sink = dataSetJsonFormat["sink"]
                floatV = dataSetJsonFormat["float"]
                
                listItem = [date,sink,floatV]
                data.append(listItem)


                print(data)
        dataSetFile.close()
    print("\n")
    for item in data:
        print(item[0])

    print("dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: ",data)
    return data


def createCSVFile(mode,dataList):
    print(mode)
    cwd = os.getcwd()
    #0 = create float
    if mode == "0":
        dates = []
        sinkingValues = []
        floatingValues = []
        for chunk in dataList:
            dates.append(chunk[0])
            sinkingValues.append(chunk[1])
            floatingValues.append(chunk[2])
        print("-----------------------------------------\n")

        print("DATES: ",dates)
        print("Sinking vals: ",sinkingValues)
        print("FLoating vals: ",floatingValues)

        print(len(dates))
        print(len(sinkingValues))
        print(len(floatingValues))


        print("\n-----------------------------------------")
        with open(os.path.join(cwd,"Float Data\\","floating_data.csv"),"w+", newline='') as csvFile:
            csvWriter = csv.writer(csvFile,delimiter=",")
            #swriter.writeheader()
            csvWriter.writerow(["Date","Float Weight","Sink Weight"])
            for item in dataList:
                csvWriter.writerow((item[0],item[1],item[2]))
        csvFile.close()
    elif mode == "1":
        dates = []
        sinkingValues = []
        floatingValues = []
        for chunk in dataList:
            dates.append(chunk[0])
            sinkingValues.append(chunk[1])
            floatingValues.append(chunk[2])
        print("-----------------------------------------\n")

        print("DATES: ",dates)
        print("Sinking vals: ",sinkingValues)
        print("FLoating vals: ",floatingValues)

        print(len(dates))
        print(len(sinkingValues))
        print(len(floatingValues))

        cwd = os.getcwd()

        print("\n-----------------------------------------")
        with open(os.path.join(cwd,"Sink Data\\","sinking_data.csv"),"w+",newline="")as csvFile:
            csvWriter = csv.writer(csvFile,delimiter=",")
            #swriter.writeheader()
            csvWriter.writerow(["Date","Float Weight","Sink Weight"])
            for item in dataList:
                csvWriter.writerow((item[0],item[1],item[2]))
        csvFile.close()








def create(mode,fileName):
    dataSet = getDataSet(mode,fileName)
    createCSVFile(mode,dataSet)
    
    #readCsv(fileName)

#def calculateAverage():
