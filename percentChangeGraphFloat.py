import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
from matplotlib.widgets import Button,Slider
import matplotlib.patches as patches

class PercentFloatGraph(object):
    def __init__(self,sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates,std):
        self.sigmas = sigmas
        self.ucl = ucl
        self.std = std  
        self.lcl = lcl
        self.lineRunning = True
        self.barRunning = False
        avg = average
        self.average = avg
        self.floatPercents = floatPercents
        self.sinkPercents = sinkPercents
        self.dates = dates
        self.floatPercentsMin = self.listMin(floatPercents)
        self.floatPercentsMax = self.listMax(floatPercents)
        self.percentDevGraph()
    def listMin(self,list):
        print(min(list))
        return min(list)
    def listMax(self,list):
        print(max(list))
        return max(list)
    
    def returnYLims(self,ucl,lcl,floatPercentsMin,floatPercentsMax):
        lowerYLim = 0
        upperYLim = 0
        if lcl < floatPercentsMin:
            lowerYLim = lcl
        else:
            lowerYLim = floatPercentsMin    
        if ucl > floatPercentsMax:
            upperYLim = ucl
        else:
            upperYLim = floatPercentsMax

        return lowerYLim,upperYLim
    
    def makeDateList(self):
        dateList=[]
        for i in range(len(self.dates)):
            dateList.append(i)
        return dateList
    def percentDevGraph(self):
        
        y = np.array(self.floatPercents,float)
        x = np.array(len(self.dates))
        
        fig, ax = plt.subplots(figsize=(8,6.6))
        plt.subplots_adjust(bottom=0.25)#create as subplot for better integration of sldier
        
        plt.xlabel("Date")
        plt.ylabel("Deviations from mean")


        plt.title("Floating Percent Deviations From Mean")

        #setup graph limits
        yLimLow,yLimHigh = self.returnYLims(self.ucl,self.lcl,self.floatPercentsMin,self.floatPercentsMax)
        plt.ylim(yLimLow - 1,yLimHigh + 1)

        meanPatch = patches.Patch(color = "red",label="Mean = "+str(round(self.average,1)))
        perPatch = patches.Patch(color="blue",label="Float Percentage")
        uclPatch = patches.Patch(color = "green",label="UCL = "+str(round(self.ucl,1)))
        lclPatch = patches.Patch(color = "orange",label="LCL = "+str(round(self.lcl,1)))

        plt.legend(loc='upper right',ncol=2,handles=[meanPatch,perPatch,uclPatch,lclPatch],framealpha=1, borderaxespad=0.5)
        
        plt.axhline(self.lcl, color='orange', linestyle='--')#plot lcl line
        
        plt.axhline(self.ucl, color='green', linestyle='--')#plot ucl line
        



        oneSig = self.average + self.std
        twoSig = self.average + self.std + self.std
        oneSigUnd = self.average - self.std
        twoSigUnd = self.average - self.std - self.std

        print(self.lcl,twoSigUnd,oneSigUnd,self.average,oneSig,twoSig, self.ucl)


        plt.yticks([self.lcl,twoSigUnd,oneSigUnd,self.average,oneSig,twoSig, self.ucl],["-3 σ","-2 σ","-1 σ","Mean","+1 σ","+2 σ","+3 σ"])
        
        dateList = self.makeDateList()
        

        plt.xticks(dateList,self.dates)
        
        # rotate and align the tick labels so they look better
        plt.gcf().autofmt_xdate()

        xList = []
        for i in range(len(dateList)):
            xList.append(i)
        print(xList)
        
        li = plt.stem(xList,y,markerfmt='h', bottom=self.average,linefmt="grey")
        
        plt.ylim(self.lcl - 1,self.ucl+1)
 

        

        xVals = li[0].get_xdata()
        yVals = li[0].get_ydata()
    




        for i in range(len(xVals)):
            if yVals[i] < self.average:
                plt.annotate(str(yVals[i]),(xVals[i],yVals[i]),textcoords="offset points",xytext=(-10,-12))
            else:
                plt.annotate(str(yVals[i]),(xVals[i],yVals[i]),textcoords="offset points",xytext=(-10,10))

        plt.axhline(self.average, color='r', linestyle='-')#plot avg line
        
        # Don't mess with the limits!
        plt.autoscale(enable=False)
        
        plt.grid(axis="y")
        
        
        
        #under is for slider subplot
        #create slider widget
        axpos = plt.axes([0.2, 0.01, 0.65, 0.03])
        positionSlider = Slider(axpos, 'Position: ', -1 , len(self.dates),valfmt="%1.0f",dragging=True,valstep=None)

        def updatePosition(val):#update slider position and change axis veiw
            pos = positionSlider.val
            ax.axis([pos,pos+10,yLimLow - 1,yLimHigh + 1])
            fig.canvas.draw_idle()
        

        

        positionSlider.on_changed(updatePosition)#call on changed

        
        
        
        
        
        
        
        
        
        
        
        
        
        plt.show()