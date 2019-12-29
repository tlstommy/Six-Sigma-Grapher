import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import Slider
import numpy as np
from datetime import datetime
from matplotlib.widgets import Button
import matplotlib.patches as patches
class SinkBarGraph(object):


    def __init__(self,floatPercents,sinkPercents,dates):
        

        self.floatPercents = floatPercents
        self.sinkPercents = sinkPercents
        self.dates = dates

        self.barGraph()
    
    def labelBars(self,barGraphRectangle,isBottom):
        #Attach a text label above each bar 
        
        if isBottom:
            for bar in barGraphRectangle:
                yCoord = (bar.get_height() / 2)  
                plt.annotate('{}'.format(round(yCoord*2,2))+"%",xy=(bar.get_x() + bar.get_width() / 2, yCoord),xytext=(0, 3),textcoords="offset points",ha='center',va="bottom",size="small")
        else:
            for bar in barGraphRectangle:
                yCoord = (bar.get_height())
                plt.annotate('{}'.format(round(yCoord,2))+"%",xy=(bar.get_x() + bar.get_width() / 2, 102),xytext=(0, 3),textcoords="offset points",ha='center',va="top",size="small")
        

    def barGraph(self):
        print("self sink percents: ",self.sinkPercents)
        print("self sink percents len : ",len(self.sinkPercents))
        sinkPercentArray = np.array(self.sinkPercents,float)
        self.dates.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
        indentation = np.arange(len(self.dates))

        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)#create as subplot for better integration of sldier
        
        plt.xlabel("Date")
        plt.ylabel("Sinking v Floating %")
        
        x = np.array(self.dates)
        width = .8
        #plt.set_yticks()
        plt.yscale("linear")
        
        p1 = plt.bar(indentation,self.floatPercents,width)
        p2 = plt.bar(indentation,self.sinkPercents,width,bottom=self.floatPercents)
        
        self.labelBars(p1,True)
        self.labelBars(p2,False)
        

        plt.gcf().autofmt_xdate()
        plt.xticks(indentation,self.dates)
        
        plt.xlim(-1,7)
        plt.ylim(0,105)
        
        
        floatPercentPatch = patches.Patch(color="blue",label="Floating (%)")
        sinkPercentPatch = patches.Patch(color="orange",label="Sinking (%)")

        plt.title("Sinking Sample Distribution")
        plt.legend(bbox_to_anchor=(0.018, 1.09, 1.0, .102),loc="upper right",handles=[floatPercentPatch,sinkPercentPatch])
        

        #under is for slider subplot
        #create slider widget
        axpos = plt.axes([0.2, 0.01, 0.65, 0.03])
        positionSlider = Slider(axpos, 'Position: ', -1, len(self.dates),valfmt="%1.0f",dragging=True,valstep=None)

        def updatePosition(val):#update slider position and change axis veiw
            pos = positionSlider.val
            ax.axis([pos,pos+10,0,105])
            fig.canvas.draw_idle()
        

        

        positionSlider.on_changed(updatePosition)#call on changed


        plt.show()
        
        
    #def next(self,event):

  
    #subPlots()
