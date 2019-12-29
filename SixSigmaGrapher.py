from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
import sys,datetime,json,pickle,os,time,platform
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import sixSigmaCalcFloatLine as SSCFL
import sixSigmaCalcFloatBar as SSCFB
import sixSigmaCalcFloatPercentChangeChart as SSCFPCC
import sixSigmaCalcSinkBar as SSCSB
import sixSigmaCalcSinkLine as SSCSL
import sixSigmaCalcSinkPercentChangeChart as SSCSPCC

import csvMaker as csvMaker
import sinkingFileClass as SFC
from tkinter import *
from tkinter.filedialog import askopenfilename

import numpy.core._methods #For cxfreeze
import numpy.lib.format #For cxfreeze
import matplotlib.backends.backend_tkagg #For cxfreeze


class LaunchWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 252)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 20, 301, 91))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setGeometry(QtCore.QRect(50, 80, 241, 41))
        self.launchButton.setObjectName("launchButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(50, 130, 241, 41))
        self.quitButton.setObjectName("quitButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.firstTimeSetupCheck()

        self.launchButton.clicked.connect(self.floatPressed)

        self.quitButton.clicked.connect(self.quitProgram)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Six Sigma Grapher"))
        self.label.setText(_translate("MainWindow", "Six Sigma Grapher"))
        self.launchButton.setText(_translate("MainWindow", "Launch"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.label_2.setText(_translate("MainWindow", "Created by Thomas Smith"))

    def firstTimeSetupCheck(self):
        dirList = ["Float Data","Backups","Sink Data","Exported Data"]
        for dirr in dirList:
            print(dirr)
            try:
                if (os.path.isfile(dirr) == False):
                    os.mkdir(dirr)
                    print("made, ",dirr," in ",os.getcwd())
            except FileExistsError:
                pass



    @staticmethod
    def floatPressed(self):
        
        
        runClass("floatOrSinkMenu")

    @staticmethod
    def quitProgram(self):
        time.sleep(.5)
        sys.exit()




class floatOrSinkMenu(object):
    
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.floatingButton = QtWidgets.QPushButton(self.centralwidget)
        self.floatingButton.setGeometry(QtCore.QRect(10, 80, 331, 31))
        self.floatingButton.setObjectName("floatingButton")
        self.sinkingButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinkingButton.setGeometry(QtCore.QRect(10, 120, 331, 31))
        self.sinkingButton.setObjectName("sinkingButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        #floating pressed
        self.floatingButton.clicked.connect(self.floatPressed)
        

        #sinking pressed
        self.sinkingButton.clicked.connect(self.sinkingPressed)
        
    
    @staticmethod#static binds the function just to object, in this case window, instead of float pressed
    def floatPressed(self):
        #call run class and run flmm section
        runClass("floatMainMenu")

    @staticmethod
    def sinkingPressed(self):       
        runClass("SinkMainMenu")
        #pass
    
        #kreygasm

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float | Sink   Menu"))
        
        self.floatingButton.setText(_translate("MainWindow", "Floating"))
        self.sinkingButton.setText(_translate("MainWindow", "Sinking"))
        self.label.setText(_translate("MainWindow", "Would you like to run the program for floating or shrinking?"))


#choose what graph to run
class floatChooseGraphType(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 412)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.veiwLineGraphFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLineGraphFloatButton.setGeometry(QtCore.QRect(10, 80, 411, 31))
        self.veiwLineGraphFloatButton.setObjectName("veiwLineGraphFloatButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.veiwBarGraphFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwBarGraphFloatButton.setGeometry(QtCore.QRect(10, 150, 411, 31))
        self.veiwBarGraphFloatButton.setObjectName("veiwBarGraphFloatButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.veiwLPercentageChangeFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLPercentageChangeFloatButton.setGeometry(QtCore.QRect(10, 230, 411, 31))
        self.veiwLPercentageChangeFloatButton.setObjectName("veiwLPercentageChangeFloatButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.returnToFloatMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToFloatMenuButton.setGeometry(QtCore.QRect(10, 310, 411, 31))
        self.returnToFloatMenuButton.setObjectName("returnToFloatMenuButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.returnToFloatMenuButton.clicked.connect(self.backButtonPressed)
        
        self.veiwLineGraphFloatButton.clicked.connect(lambda: self.veiwLineGraphPressed())
        self.veiwBarGraphFloatButton.clicked.connect(lambda: self.veiwBarGraphPressed())
        self.veiwLPercentageChangeFloatButton.clicked.connect(lambda: self.veiwSTDGraphPressed())
        
    


    #go back to add data point menu
    @staticmethod
    def backButtonPressed(self):
        runClass("floatMainMenu")
    
    
        
    
    #veiw Linegraph
    def veiwLineGraphPressed(self):
        csvMaker.create("0","floatData.txt")
        try:
            
            csvMaker.create("0","floatData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        SSCFL.call()#six sigma calc float line graph    

    #veiw BarGraph
    
    def veiwBarGraphPressed(self):
        
        
        try:
            
            csvMaker.create("0","floatData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        SSCFB.call()#six sigma calc float bar graph    

    #veiw std graph
    
    def veiwSTDGraphPressed(self):
        
        try:
            
            csvMaker.create("0","floatData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        print("STD GRAPH PRESSED")
        SSCFPCC.call()#six sigma calc float bar graph    


    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Choose Graph"))
        self.veiwLineGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Data Line Graph"))
        self.label.setText(_translate("MainWindow", "Default graph. Contains UCL and LCL data for floating data percentages in a detailed line graph"))
        self.veiwBarGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Distribution Bar Graph"))
        self.label_2.setText(_translate("MainWindow", "Bar graph that shows the distribution of the percent of floating plastic versus the sinking plastic percentage."))
        self.veiwLPercentageChangeFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Deviation Graph"))
        self.label_3.setText(_translate("MainWindow", "Graph that shows distrubitons from the mean of the dataset. Can be used as another way to analyze data from the line graph."))
        self.returnToFloatMenuButton.setText(_translate("MainWindow", "Return to Float menu"))
        self.label_4.setText(_translate("MainWindow", "Return to previous menu."))
        self.label_5.setText(_translate("MainWindow", "How would you like to veiw your data?"))


#main menu for float data
class floatMainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setGeometry(QtCore.QRect(20, 110, 260, 31))
        self.viewGraphButton.setObjectName("viewGraphButton")
        
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(20, 190, 260, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(150, 230, 131, 31))
        self.quitToSelectButton.setObjectName("quitToSelectButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(20, 150, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(20, 70, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 260, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.helpMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpMenuButton.setGeometry(QtCore.QRect(20, 230, 128, 31))
        self.helpMenuButton.setObjectName("helpMenuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Back to float main menu
        self.quitToSelectButton.clicked.connect(self.backButtonPressed)

        self.addNewDPandGraphButton.clicked.connect(self.addPointsPressed)
        
        
        self.viewGraphButton.clicked.connect(self.graphSelection)
        
        
        self.editDataPointButton.clicked.connect(self.veiwAndEditDatapoints)

        self.settingsButton.clicked.connect(self.floatSettingsPressed)

        self.helpMenuButton.clicked.connect(self.floatHelpPressed)




    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("floatChooseGraphType")

    @staticmethod
    def backButtonPressed(self):
        runClass("floatOrSinkMenu")

    @staticmethod
    def addPointsPressed(self):
        runClass("fmmAddDP")

    @staticmethod
    def veiwAndEditDatapoints(self):
        runClass("editFloatDataPoint")

    #run settings
    @staticmethod
    def floatSettingsPressed(self):
        runClass("floatSettings")

    #run help
    @staticmethod
    def floatHelpPressed(self):
        runClass("floatHelpMenu")
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Main Menu"))
        self.viewGraphButton.setText(_translate("MainWindow", "view Graphs"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "view And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.label.setText(_translate("MainWindow", "Floating Data"))
        self.helpMenuButton.setText(_translate("MainWindow", "Help Menu"))


class fmmAddDP(object):
    def setupUi(self, MainWindow):
        self.currentDateCBChecked = True
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 377)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sinkingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.sinkingWeightTextBox.setEnabled(True)
        self.sinkingWeightTextBox.setGeometry(QtCore.QRect(220, 70, 111, 21))
        self.sinkingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sinkingWeightTextBox.setObjectName("sinkingWeightTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 151, 41))
        self.label_2.setObjectName("label_2")
        self.floatingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.floatingWeightTextBox.setEnabled(True)
        self.floatingWeightTextBox.setGeometry(QtCore.QRect(220, 100, 111, 21))
        self.floatingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.floatingWeightTextBox.setObjectName("floatingWeightTextBox")
        self.useCurrentDatecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.useCurrentDatecheckBox.setGeometry(QtCore.QRect(30, 160, 171, 20))
        self.useCurrentDatecheckBox.setObjectName("useCurrentDatecheckBox")
        self.useCurrentDatecheckBox.toggle()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 181, 41))
        self.label_3.setObjectName("label_3")
        self.dateTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.dateTextBox.setEnabled(True)
        self.dateTextBox.setGeometry(QtCore.QRect(220, 130, 111, 21))
        self.dateTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateTextBox.setObjectName("dateTextBox")
        #get date and disable date box
        self.dateTextBox.setDisabled(True)
        self.currentDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentDateLabel.setGeometry(QtCore.QRect(190, 160, 121, 20))
        self.currentDateLabel.setObjectName("currentDateLabel")
        self.currentDateLabel.setText(_translate("MainWindow", self.currentDateFormatted()))        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 271, 31))
        self.pushButton.setObjectName("pushButton")#veiw graphs
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 240, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 271, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.quitToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToMenuButton.setGeometry(QtCore.QRect(30, 280, 271, 31))
        self.quitToMenuButton.setObjectName("quitToMenuButton")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(60, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.useCurrentDatecheckBox.stateChanged.connect(lambda:self.dateCBEval(self.useCurrentDatecheckBox))#lambda fycbiton call checkbox eval

        self.pushButton.clicked.connect(self.addPoint)

        self.quitToMenuButton.clicked.connect(self.backButtonPressed)
        self.pushButton_2.clicked.connect(self.graphSelection)

    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("floatChooseGraphType")
    #go back to flaot main menu
    @staticmethod
    def backButtonPressed(self):
        runClass("floatMainMenu")
    
    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()

    def dateCBEval(self,checkbox):#toggle text box
        if checkbox.isChecked() == True:
            self.dateTextBox.setDisabled(True)
        else:
            self.dateTextBox.setDisabled(False)
    
    

    def addPoint(self):
        sinkWeightFloat = ""
        floatWeightFloat = ""
        if self.useCurrentDatecheckBox.isChecked():
            dateString = str(self.currentDateFormatted())
        else:
            dateString = self.dateTextBox.toPlainText()
        sinkWeightString = self.sinkingWeightTextBox.toPlainText()
        floatWeightString = self.floatingWeightTextBox.toPlainText()

        sinkErrorIn = False
        floatErrorIn = False
        try:
            sinkWeightFloat = float(sinkWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Sink Weight is Invalid!")
            self.updateStatusLabel("red",False,str("ERROR: Sink weight Error!"))
            sinkErrorIn = True
        try:
            floatWeightFloat = float(floatWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Float Weight is Invalid!")
            floatErrorIn = True
            self.updateStatusLabel("red",False,str("ERROR: Float weight Error!"))
        if dateString == "" or re.search('[a-zA-Z]', dateString):
            self.createErrorMessage("Error!","Input for Date is Invalid!")
            self.updateStatusLabel("red",False,str("ERROR: Date Error!"))
            sinkErrorIn = True
        if floatErrorIn != False or sinkErrorIn != False:
            print(floatErrorIn)
            print(sinkErrorIn)
            return None

        print(dateString)
        print(sinkWeightFloat)
        print(floatWeightFloat)
        
        
        data = self.makeJsonData(dateString,sinkWeightFloat,floatWeightFloat)
        

        self.saveToJson(data)
        self.updateStatusLabel("green",False,str("Point: "+str(dateString)+" added!"))
    
    def updateStatusLabel(self,color,clear,text):
        self.statusLabel.setText("<font color='"+color+"'>"+text+"</font>")




    #format data to json dict
    def makeJsonData(self,date,sinkWeight,floatWeight):
        
        data = {"date":date,"sink":sinkWeight,"float":floatWeight}
            
        print(data)
        return data


    

 
    #save data
    def saveToJson(self,data):

        cwd  = os.getcwd()
        with open(os.path.join(cwd,"Float Data\\floatData.txt"), 'a') as file:
            json.dump(data, file)
            file.write("\n")

         

        





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Add Datapoint"))
        self.label.setText(_translate("MainWindow", "Sinking weight (g) :"))
        self.label_2.setText(_translate("MainWindow", "Floating weight (g) :"))
        self.useCurrentDatecheckBox.setText(_translate("MainWindow", "use Current Date : "))
        self.label_3.setText(_translate("MainWindow", "Date ( MM/DD/YYYY) :"))
        
        self.pushButton.setText(_translate("MainWindow", "Add data point"))
        self.pushButton_2.setText(_translate("MainWindow", "Veiw Graphs"))
        self.label_4.setText(_translate("MainWindow", "Add Float Data point"))
        self.quitToMenuButton.setText(_translate("MainWindow", "Return to menu"))
    
    def currentDateFormatted(self):
        currentDate = datetime.date.today()
        day = currentDate.day
        month = currentDate.month
        year = currentDate.year

        formattedDate = "%s/%s/%s" % (month,day,year)

        return formattedDate

#edit fmm data points
class editFloatDataPoint(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 51, 301, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSpacing(5)
        
        self.removeEntryButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeEntryButton.setGeometry(QtCore.QRect(15, 360, 301, 31))
        self.removeEntryButton.setObjectName("removeEntryButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(15, 400, 301, 31))
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 40, 301, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 10, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.entries = self.fillList("floatData.txt")
        
       

        print(self.entries)

        self.fillTable(self.entries)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #get current item
        self.currentItem = ""
        self.listWidget.itemSelectionChanged.connect(self.returnSelectedItem)

    




        #return to menu
        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)
        
        #remove entry pressed
        
        #lamba im using kinda like static
        #maybe better than static for non class things?
        self.removeEntryButton.clicked.connect(lambda: self.removeEntryPressed(self.currentItem))
    


    #return active item
    def returnSelectedItem(self):
        selectedItem = self.listWidget.currentItem().text()
        print(selectedItem)
        self.currentItem = selectedItem
        print("current item")
        print(self.currentItem)


    def removeEntryPressed(self,currentItem):
        entryStr = currentItem
        self.confirmDeleteMessage(entryStr)

    

    def removeItemFromList(self,item,file):
        #HOW WORKS
        #FIND DATA IN FILE AND THEN WRITE BACK TO FILE EXCLUDING ORIGNINAL DATA POINT
        dataLines = []
        
        itemData = item.strip("\n")
        itemData = itemData.replace("Entry Date: ","")
        itemData = itemData.replace("Sinking Plastic Weight: ",":")
        itemData = itemData.replace("Floating Plastic Weight: ",":")
        itemData = itemData.replace("\n","")
        
        itemDataList = itemData.split(":")

        date = itemDataList[0]
        sinking = itemDataList[1]
        floating = itemDataList[2]
        
        
        print("====================================")
        print("itemData: ",itemDataList)
        print("====================================")

        cwd = os.getcwd()
        
       
        

        with open(os.path.join(cwd,"Float Data\\"+str(file)),"r") as entryFile:
            for entry in entryFile.readlines():
                dataLines.append(entry)
        entryFile.close

        for line in dataLines:
            lineJson = json.loads(line)
            
            

            if str(lineJson["date"]) == str(date) and str(lineJson["sink"]) == str(sinking) and str(lineJson["float"]) == str(floating):
                print("MATCH FOUND")
                print(lineJson)
                print(itemDataList)
                lineToExclude = line#exclude this line during writeback thus deleting it

                print("Lines: ",dataLines)

                
                cwd = os.getcwd()
                with open(os.path.join(cwd,"Float Data\\"+ str(file)),"r") as entryFile:
                    lines = entryFile.readlines()
                with open(os.path.join(cwd,"Float Data\\"+ str(file)),"w") as entryFile:
                    for line in lines:
                        
                        if line != lineToExclude:
                            entryFile.write(line)
                        else:
                            print("LINE REMOVED")
                self.createAlertPopup("Removed!","Entry was removed succesfully!","Entry Removed!")
                
                runClass("editFloatDataPoint") #it updates

    def createAlertPopup(self,title,message,winTitle):
        alertMsg = QMessageBox()
        alertMsg.setIcon(QMessageBox.Information)
        alertMsg.setText(title)
        alertMsg.setInformativeText(message)
        alertMsg.setWindowTitle(winTitle)
        alertMsg.exec()

    @staticmethod
    def returnToMenuPressed(self):
        runClass("floatMainMenu")

    def confirmDeleteMessage(self,item):
        item = item.replace("----------------------------------------------------","")

        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete the following entry? This action cannot be undone.")
        
        
        confirmDeleteMessagebox.setInformativeText(item)
        confirmDeleteMessagebox.setWindowTitle("Confirm Deletion?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()
        
        print(buttonResult)

        if buttonResult == "yes":#yes button is pressed
            print("yes")
            self.removeItemFromList(item,"floatData.txt")
        
        if buttonResult == "no":#no button is pressed
            print("nomegalul")
            pass
        
        

       

    def fillList(self,list):
        entries = []
        cwd = os.getcwd()
        with open(os.path.join(cwd,"Float Data\\"+ str(list)),"r") as entryFile:
            for entry in entryFile.readlines():
                entries.append(entry)
                print(entry,"\n")
                
        #print(entries)
        entryFile.close()
        return entries



    def formatEntry(self,item):
        
        item = json.loads(item)
        date = item["date"]
        sinkingWeight = item["sink"]
        floatingWeight = item["float"]

        #==================================
        #----------------------------------------------------
        formattedString = "----------------------------------------------------\nEntry Date: " + str(date) + "\nSinking Plastic Weight: " + str(sinkingWeight) + "\nFloating Plastic Weight: " + str(floatingWeight) +"\n----------------------------------------------------" 

        print(formattedString)


        return(formattedString)


    def fillTable(self,entryList):
        for item in entryList:
            item = self.formatEntry(item)
            
            self.listWidget.addItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Edit Floating Data"))
        self.removeEntryButton.setText(_translate("MainWindow", "Remove Selected Entry"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.label.setText(_translate("MainWindow", "Edit Floating Data"))





class floatSettings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.uclTargetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.uclTargetInput.setGeometry(QtCore.QRect(220, 80, 41, 21))
        self.uclTargetInput.setAcceptDrops(True)
        self.uclTargetInput.setAutoFillBackground(False)
        self.uclTargetInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uclTargetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.uclTargetInput.setObjectName("uclTargetInput")
        self.setUclTargetButton = QtWidgets.QPushButton(self.centralwidget)
        self.setUclTargetButton.setGeometry(QtCore.QRect(270, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setUclTargetButton.setFont(font)
        self.setUclTargetButton.setObjectName("setUclTargetButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.uclTargetLabel = QtWidgets.QLabel(self.centralwidget)
        self.uclTargetLabel.setGeometry(QtCore.QRect(170, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uclTargetLabel.setFont(font)
        self.uclTargetLabel.setObjectName("uclTargetLabel")
        self.exportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataButton.setGeometry(QtCore.QRect(20, 180, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exportDataButton.setFont(font)
        self.exportDataButton.setObjectName("exportDataButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.importDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.importDataButton.setGeometry(QtCore.QRect(20, 250, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importDataButton.setFont(font)
        self.importDataButton.setObjectName("importDataButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.resetDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetDataButton.setGeometry(QtCore.QRect(20, 390, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetDataButton.setFont(font)
        self.resetDataButton.setObjectName("resetDataButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(20, 460, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returnToMenuButton.setFont(font)
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 201, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.createBackupButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBackupButton.setGeometry(QtCore.QRect(20, 320, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createBackupButton.setFont(font)
        self.createBackupButton.setObjectName("createBackupButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.updateUclLabel()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)

        self.setUclTargetButton.clicked.connect(lambda: self.settingsSetUcl())

        self.exportDataButton.clicked.connect(lambda: self.exportFloatData("floatDataExported.ssg"))

        self.importDataButton.clicked.connect(lambda: self.importFloatData())

        self.createBackupButton.clicked.connect(lambda: self.createFloatBackup())

        self.resetDataButton.clicked.connect(lambda: self.clearAllData())
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Settings"))
        self.label.setText(_translate("MainWindow", "Float Settings"))
        self.label_2.setText(_translate("MainWindow", "Upper Control Limit Target: "))
        self.setUclTargetButton.setText(_translate("MainWindow", "Set"))
        self.label_3.setText(_translate("MainWindow", "Current UCL Target:"))
        self.label_4.setText(_translate("MainWindow", "Sets the upper control limit target. Default = 100"))
        self.uclTargetLabel.setText(_translate("MainWindow", "100"))
        self.exportDataButton.setText(_translate("MainWindow", "Export Data"))
        self.label_5.setText(_translate("MainWindow", "Export floating data in .SSG format so that it can be reimported to the program elsewhere "))
        self.label_6.setText(_translate("MainWindow", "Import floating data in .SSG format so that it can be used."))
        self.importDataButton.setText(_translate("MainWindow", "Import Data"))
        self.label_7.setText(_translate("MainWindow", "Resets all floating data"))
        self.resetDataButton.setText(_translate("MainWindow", "Reset all Floating Data"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.createBackupButton.setText(_translate("MainWindow", "Create a Data Backup"))
        self.label_8.setText(_translate("MainWindow", "Backup floating data to .SSG format so that it can be reimported as needed."))

        self.updateUclLabel()
    
    

    


    @staticmethod
    def returnToMenuPressed(self):
        runClass("floatMainMenu")
    
    def settingsSetUcl(self):
        
        
        uclString = self.uclTargetInput.toPlainText()
        
        
        try:
            uclInt = round(int(uclString),0)
        except ValueError:
            self.createErrorMessage("Value Error","Error! Value must be a whole number (ex. '100') not a decimal or non numeric value.)")
            return

        print("ucl int: ",uclInt)

        
        cwd = os.getcwd()
        with open(os.path.join(cwd,"Float Data\\floatSettings.txt"),"w") as settingsFile:
            
            
            settingsFile.write(str(uclInt))
        settingsFile.close()
        self.updateUclLabel()

    def updateUclLabel(self):
        cwd = os.getcwd()
        try:
            with open(os.path.join(cwd,"Float Data\\floatSettings.txt"),"r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        except FileNotFoundError:
            with open(os.path.join(cwd,"Float Data\\floatSettings.txt"),"w") as settingsFile:
                
                
                settingsFile.write("100")
            settingsFile.close()
            with open(os.path.join(cwd,"Float Data\\floatSettings.txt"),"r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        
        ucl = lines[0]
        self.uclTargetLabel.setText(str(ucl))
    

    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()
    
    def createInfoMessage(self,title,message):
        infoMsg = QMessageBox()
        infoMsg.setIcon(QMessageBox.Information)
        infoMsg.setText(title)
        infoMsg.setInformativeText(message)
        infoMsg.setWindowTitle(title)
        infoMsg.exec()

    def backupFloatData(self,fileExportName):
        lines =[]
        
        cwd = os.getcwd()
        print("cwd: ",cwd)
        with open(os.path.join(cwd,"Float Data\\floatData.txt"),"r") as floatData:
            lines = floatData.readlines() 
        floatData.close()

        

        with open(os.path.join(cwd,"Backups\\",fileExportName),"wb") as outfile:
            pickle.dump(lines,outfile)
        outfile.close()
        self.createInfoMessage("Data Backup Succesful!","A backup had been created and saved with the Filename: '"+ str(fileExportName) +"' in directory: " +str(cwd) +"\\Backups")


    def exportFloatData(self,fileExportName):
        lines =[]
        cwd = os.getcwd()
        print("cwd: ",cwd)
        with open(os.path.join(cwd,"Float Data\\floatData.txt"),"r") as floatData:
            lines = floatData.readlines() 
        floatData.close()

        #"floatDataExported.ssg"

        with open(os.path.join(cwd,"Exported Data\\",fileExportName),"wb") as outfile:
            pickle.dump(lines,outfile)
        outfile.close()
        self.createInfoMessage("Data Exported Succesfully!","File: '"+ str(fileExportName) +"' has been exported to directory: " +str(cwd) +"\\Exported Data")

    def importFloatData(self):
        root = Tk()
        
        root.withdraw() #don't want a full GUi keep the root window from appearing
        ftypes = [
        ('Six Sigma Grapher files', '*.ssg'),  
        ('All files', '*'), 
        ]
        
        filePath = askopenfilename(filetypes=ftypes) # show "Open" dialog box and return path
        
        if ".ssg" in filePath:
            print("acceptable file")

            
        

            confirmImportMessagebox= QMessageBox()
            confirmImportMessagebox.setIcon(QMessageBox.Warning)
            confirmImportMessagebox.setText("Are you sure you would like to import this data? This action cannot be undone and all current data will be overwritten.")
        

            
            confirmImportMessagebox.setWindowTitle("Import and Overwrite?")
            confirmImportMessagebox.addButton(QMessageBox.Yes)
            confirmImportMessagebox.addButton(QMessageBox.No)
            confirmImportMessagebox.exec()
            buttonResult = confirmImportMessagebox.clickedButton().text() #could cause probs
            buttonResult= buttonResult.replace("&","").lower()

            

            if buttonResult == "yes":#yes button is pressed
                print("yes")
                importedFile = open(filePath,"rb")
                importedFileData = pickle.load(importedFile)
                importedFile.close()
                print(importedFileData)
                print(type(importedFileData))
                cwd = os.getcwd()
                with open(os.path.join(cwd,"Float Data\\floatData.txt"),"w") as floatData:
                    for line in importedFileData:
                        floatData.write(line)
                floatData.close()
                self.createInfoMessage("File imported succesfully!","File: 'floatData.txt' has been imported succesfully!")

                
        
            if buttonResult == "no":#no button is pressed
                print("nomegalul")
                pass


        else:
            self.createErrorMessage("Invalid Filetype!","This is an invalid filetype! Only '.ssg' files are accepeted!")
            return

    
    

    def clearAllData(self):
        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete all data? This action is irreversible and all current data will be lost!")
    

        
        confirmDeleteMessagebox.setWindowTitle("Delete data?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()

        if buttonResult == "yes":#yes button is pressed
            
            time.sleep(1)
            
            proceedMessagebox= QMessageBox()
            proceedMessagebox.setIcon(QMessageBox.Warning)
            proceedMessagebox.setText("Are you sure you would like proceed?")
        

            
            proceedMessagebox.setWindowTitle("Proceed?")
            proceedMessagebox.addButton(QMessageBox.Yes)
            proceedMessagebox.addButton(QMessageBox.No)
            proceedMessagebox.exec()
            proceedButtonResult =proceedMessagebox.clickedButton().text() #could cause probs
            proceedButtonResult= proceedButtonResult.replace("&","").lower()

            if proceedButtonResult == "yes":#yes button is pressed
                print("proceeding to delete.")
                time.sleep(.3)
                print("proceeding to delete..")
                time.sleep(.3)
                print("proceeding to delete...")
                time.sleep(.3)
                print("Deleted!")

                currentDate = datetime.date.today()
                day = currentDate.day
                month = currentDate.month
                year = currentDate.year

                formattedDate = "%s-%s-%s" % (month,day,year)
        

                backupFileName = str("floatDataExported-Backup-"+formattedDate+".ssg")


                self.exportFloatData(str(backupFileName))
                
                cwd = os.getcwd()
                
                with open(os.path.join(cwd,"Float Data\\floatData.txt"),"w") as floatData:
                    floatData.write("")
                floatData.close()

                self.createInfoMessage("Data Deleted and Backup Created!","All exsiting data has been deleted. A backup of the data was saved to folder ExportedData called '"+str(backupFileName)+"' before it was deleted.")
    
    
    def createFloatBackup(self):
        confirmBackupMessagebox= QMessageBox()
        confirmBackupMessagebox.setIcon(QMessageBox.Warning)
        confirmBackupMessagebox.setText("Are you sure you would like to create a backup?")
        confirmBackupMessagebox.setWindowTitle("Create float data backup?")
        confirmBackupMessagebox.addButton(QMessageBox.Yes)
        confirmBackupMessagebox.addButton(QMessageBox.No)
        confirmBackupMessagebox.exec()
        buttonResult = confirmBackupMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()

        if buttonResult == "yes":#yes button is pressed

            currentDate = datetime.date.today()
            day = currentDate.day
            month = currentDate.month
            year = currentDate.year

            formattedDate = "%s-%s-%s" % (month,day,year)
        

            backupFileName = str("floatData-Backup-"+formattedDate+".ssg")


            self.backupFloatData(str(backupFileName))
class floatHelpMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(207, 50, 391, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(47, 20, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 81, 771, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(280, 600, 241, 31))
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Help Menu"))
        self.label.setText(_translate("MainWindow", "Help Menu -  Float Menu"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Entering a new datapoint</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To enter a new datapoint, navigate to the add a datapoint menu by clicking the button labeled &quot;Add New Datapoint&quot;. A new window will load where you will be able to enter the data.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Sinking Weight input box - Input the weight of the sinking plastic (in grams) in this box.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Floating Weight input box - Input the weight of the floating plastic (in grams) in this box.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Date input box- Input the date of when the data is to be recorded. Date must be in month/day/year format (MM/DD/YYYY) This input is automatically disabled when the window is launched. To enable the input, uncheck the &quot;use current date&quot; checkbox below.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Use Current Date checkbox - When this box is checked, the Date Input Box will be disabled and the date for data entered will be the current date.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Add Datapoint button -  Pressing this button processes the data from the input fields and registers it as a new data point</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• View Graph button - Closes the current window and opens the view graphs menu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return to menu Button - Returns to the float main menu </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Troubleshooting errors</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">If data is entered in an invalid format, the program will automatically throw an error and prevent the data from being entered.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for Sink Weight is Invalid&quot; error -  This error is thrown if data entered in the Sinking Weight feild is invalid. Please ensure that data being entered is a integer or decimal value and does not include letters or other special characters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for Float Weight is Invalid&quot; error -  This error is thrown if data entered in the Floating Weight feild is invalid. Please ensure that data being entered is a integer or decimal value and does not include letters or other special characters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for date is Invalid&quot; error -  This error is thrown if data entered in the Date feild is invalid. Please ensure that data being entered is in the proper month/day/year format and has no letters. acceptable characters are numbers and &quot;/&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">A status label will appear at the top of the screen showing if data entry was succesful or if there was a problem.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Viewing Graphs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To view graphs, navigate to the graph menu by clicking the button labeled &quot;Veiw Graphs&quot;. A new window will load where you will be able to select the type of graph to view the data. The graphs have a scroll bar underneath them which allows the graph to be &quot;scrolled&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">There are three diffrent types of graphs, a Floating Percentage Line graph, a Distribution bar graph, and a Deviation plot.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Viewing and Removing Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To view a list of datapoints, or to remove a specific point, click the button labeled: &quot;View and Edit Datapoints&quot; from the main menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Remove Selected Entry button - Begins the removal process.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return To Menu button - Returns user to the float menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Removing Specific Datapoints</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To remove a specific datapoint, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Select the datapoint from the list by clicking on it so that it is highlighted.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Click the button labeled &quot;Remove Selected Entry&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Confirm by clicking the &quot;Yes&quot; button</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The entry should now be removed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Float Settings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To access the settings menu for floating data, click the button labeled &quot;Settings&quot; from the float menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Upper Control Limit Target input box - Input a value for the upper control limit, confirm it by pressing &quot;set&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Export Data button - Exports data to a .SSG file.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Import Data button - Allows data from an .SSG file to be imported.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Create Data backup button - Creates a backup of all data in .SSG format.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Reset all Floating Data button - Resets all floating data and creates a backup just in case.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return to menu button - Returns user to the float menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Exporting Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To export data in .SSG format, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Export Data&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. A file will be created in directory shown.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Importing Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To import data from a  .SSG file, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Import Data&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. A file browser will be opened, navigate to your .SSG file and click it to select it.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Click the &quot;Open&quot; Button.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Confirm your decision.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. Your data should now be imported.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Creating a Data Backup</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To create a data backup, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Create a Data Backup&quot;. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Confirm that you would like to create a backup.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. A backup should be created.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Reset all Floating Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To reset all floating data, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Reset All Floating Data&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Confirm that you would like to proceed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Confrim your confirmation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. A safety backup will be created and all existing data will be destroyed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Help Menu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To enter the help menu (this menu), click the button labeled &quot;Help Menu&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To exit the help menu, click the button labeled, &quot;Return to menu&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        

    @staticmethod
    def returnToMenuPressed(self):
        runClass("floatMainMenu")            


#=================================================================================================================================================================================================
#=================================================================================================================================================================================================
#easyiest way to integrate the too but certainly not the best. using it for now
#=================================================================================================================================================================================================
#=================================================================================================================================================================================================


#choose what graph to run
class sinkChooseGraphType(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.veiwLineGraphSinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLineGraphSinkButton.setGeometry(QtCore.QRect(10, 80, 411, 31))
        self.veiwLineGraphSinkButton.setObjectName("veiwLineGraphSinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.veiwBarGraphSinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwBarGraphSinkButton.setGeometry(QtCore.QRect(10, 150, 411, 31))
        self.veiwBarGraphSinkButton.setObjectName("veiwBarGraphSinkButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.veiwLPercentageChangeSinkButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLPercentageChangeSinkButton.setGeometry(QtCore.QRect(10, 230, 411, 31))
        self.veiwLPercentageChangeSinkButton.setObjectName("veiwLPercentageChangeSinkButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.returnToSinkMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToSinkMenuButton.setGeometry(QtCore.QRect(10, 310, 411, 31))
        self.returnToSinkMenuButton.setObjectName("returnToSinkMenuButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.returnToSinkMenuButton.clicked.connect(self.backButtonPressed)
        
        self.veiwLineGraphSinkButton.clicked.connect(lambda: self.veiwLineGraphPressed())
        self.veiwBarGraphSinkButton.clicked.connect(lambda: self.veiwBarGraphPressed())
        self.veiwLPercentageChangeSinkButton.clicked.connect(lambda: self.veiwSTDGraphPressed())

    #go back to add data point menu
    @staticmethod
    def backButtonPressed(self):
        runClass("SinkMainMenu")
    
    #veiw Linegraph
    
    def veiwLineGraphPressed(self):
        csvMaker.create("1","sinkData.txt")
        try:
            csvMaker.create("1","sinkData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        SSCSL.call()#six sigma calc sink line graph    

    #veiw BarGraph
    def veiwBarGraphPressed(self):
        try:
            csvMaker.create("1","sinkData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        SSCSB.call()#six sigma calc sink bar graph    

    #veiw std graph

    def veiwSTDGraphPressed(self):
        try:
            csvMaker.create("1","sinkData.txt")
        except:
            self.createErrorMessage("Error!","Error occured while trying to load graph. Please ensure that you have a suffcient amount of data available to graph.")
            return None
        SSCSPCC.call()#six sigma calc float bar graph    



    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Choose Graph"))
        self.veiwLineGraphSinkButton.setText(_translate("MainWindow", "Veiw Sinking Percentage Data Line Graph"))
        self.label.setText(_translate("MainWindow", "Default graph. Contains UCL and LCL data for sinking data percentages in a detailed line graph"))
        self.veiwBarGraphSinkButton.setText(_translate("MainWindow", "Veiw Sinking Distribution Bar Graph"))
        self.label_2.setText(_translate("MainWindow", "Bar graph that shows the distribution of the percent of sinking plastic versus the floating plastic percentage."))
        self.veiwLPercentageChangeSinkButton.setText(_translate("MainWindow", "Veiw Sinking Percentage Deviation Graph"))
        self.label_3.setText(_translate("MainWindow", "Graph that shows distrubitons from the mean of the dataset. Can be used as another way to analyze data from the line graph."))
        self.returnToSinkMenuButton.setText(_translate("MainWindow", "Return to Sink menu"))
        self.label_4.setText(_translate("MainWindow", "Return to previous menu."))
        self.label_5.setText(_translate("MainWindow", "How would you like to veiw your data?"))


#main menu for Sink data
class SinkMainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setGeometry(QtCore.QRect(20, 110, 260, 31))
        self.viewGraphButton.setObjectName("viewGraphButton")
        
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(20, 190, 260, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(150, 230, 131, 31))
        self.quitToSelectButton.setObjectName("quitToSelectButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(20, 150, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(20, 70, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 260, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.helpMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpMenuButton.setGeometry(QtCore.QRect(20, 230, 128, 31))
        self.helpMenuButton.setObjectName("helpMenuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Back to sink main menu
        self.quitToSelectButton.clicked.connect(self.backButtonPressed)

        self.addNewDPandGraphButton.clicked.connect(self.addPointsPressed)
        
        
        self.viewGraphButton.clicked.connect(self.graphSelection)
        
        
        self.editDataPointButton.clicked.connect(self.veiwAndEditDatapoints)

        self.settingsButton.clicked.connect(self.sinkSettingsPressed)

        self.helpMenuButton.clicked.connect(self.sinkHelpPressed)


    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("sinkChooseGraphType")

    @staticmethod
    def backButtonPressed(self):
        runClass("floatOrSinkMenu")

    @staticmethod
    def addPointsPressed(self):
        runClass("smmAddDP")

    @staticmethod
    def veiwAndEditDatapoints(self):
        runClass("editSinkDataPoint")

    #run settings
    @staticmethod
    def sinkSettingsPressed(self):
        runClass("sinkSettings")

    @staticmethod
    def sinkHelpPressed(self):
        runClass("sinkHelpMenu")
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Main Menu"))
        self.viewGraphButton.setText(_translate("MainWindow", "view Graphs"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "view And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.label.setText(_translate("MainWindow", "Sinking Data"))
        self.helpMenuButton.setText(_translate("MainWindow", "Help Menu"))


class smmAddDP(object):
    def setupUi(self, MainWindow):
        self.currentDateCBChecked = True
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 377)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sinkingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.sinkingWeightTextBox.setEnabled(True)
        self.sinkingWeightTextBox.setGeometry(QtCore.QRect(220, 70, 111, 21))
        self.sinkingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sinkingWeightTextBox.setObjectName("sinkingWeightTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 151, 41))
        self.label_2.setObjectName("label_2")
        self.floatingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.floatingWeightTextBox.setEnabled(True)
        self.floatingWeightTextBox.setGeometry(QtCore.QRect(220, 100, 111, 21))
        self.floatingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.floatingWeightTextBox.setObjectName("floatingWeightTextBox")
        self.useCurrentDatecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.useCurrentDatecheckBox.setGeometry(QtCore.QRect(30, 160, 171, 20))
        self.useCurrentDatecheckBox.setObjectName("useCurrentDatecheckBox")
        self.useCurrentDatecheckBox.toggle()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 181, 41))
        self.label_3.setObjectName("label_3")
        self.dateTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.dateTextBox.setEnabled(True)
        self.dateTextBox.setGeometry(QtCore.QRect(220, 130, 111, 21))
        self.dateTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateTextBox.setObjectName("dateTextBox")
        #get date and disable date box
        self.dateTextBox.setDisabled(True)
        self.currentDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentDateLabel.setGeometry(QtCore.QRect(190, 160, 121, 20))
        self.currentDateLabel.setObjectName("currentDateLabel")
        self.currentDateLabel.setText(_translate("MainWindow", self.currentDateFormatted()))
        
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 271, 31))
        self.pushButton.setObjectName("pushButton")#veiw graphs
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 240, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 271, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.quitToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToMenuButton.setGeometry(QtCore.QRect(30, 280, 271, 31))
        self.quitToMenuButton.setObjectName("quitToMenuButton")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(60, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.useCurrentDatecheckBox.stateChanged.connect(lambda:self.dateCBEval(self.useCurrentDatecheckBox))#lambda fycbiton call checkbox eval

        self.pushButton.clicked.connect(self.addPoint)

        self.quitToMenuButton.clicked.connect(self.backButtonPressed)
        self.pushButton_2.clicked.connect(self.graphSelection)

    



    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("sinkChooseGraphType")
    #go back to flaot main menu
    @staticmethod
    def backButtonPressed(self):
        runClass("SinkMainMenu")
    
    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()

    def dateCBEval(self,checkbox):#toggle text box
        if checkbox.isChecked() == True:
            self.dateTextBox.setDisabled(True)
        else:
            self.dateTextBox.setDisabled(False)
        

    def addPoint(self):
        sinkWeightFloat = ""
        floatWeightFloat = ""
        
        if self.useCurrentDatecheckBox.isChecked():
            dateString = str(self.currentDateFormatted())
        else:
            dateString = self.dateTextBox.toPlainText()
        sinkWeightString = self.sinkingWeightTextBox.toPlainText()
        floatWeightString = self.floatingWeightTextBox.toPlainText()

        sinkErrorIn = False
        floatErrorIn = False
        try:
            sinkWeightFloat = float(sinkWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Sink Weight is Invalid!")
            self.updateStatusLabel("red",False,str("ERROR: Sink weight Error!"))
            sinkErrorIn = True
        try:
            floatWeightFloat = float(floatWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Float Weight is Invalid!")
            self.updateStatusLabel("red",False,str("ERROR: Float weight Error!"))
            floatErrorIn = True
        if dateString == "" or re.search('[a-zA-Z]', dateString):
            self.createErrorMessage("Error!","Input for Date is Invalid!")
            self.updateStatusLabel("red",False,str("ERROR: Date Error!"))
            sinkErrorIn = True
        

        if floatErrorIn != False or sinkErrorIn != False:
            print(floatErrorIn)
            print(sinkErrorIn)
            return None

        

        print(dateString)
        print(sinkWeightFloat)
        print(floatWeightFloat)
        
        
        data = self.makeJsonData(dateString,sinkWeightFloat,floatWeightFloat)
        self.saveToJson(data)
        self.updateStatusLabel("green",False,str("Point: "+str(dateString)+" added!"))
    
    def updateStatusLabel(self,color,clear,text):
        self.statusLabel.setText("<font color='"+color+"'>"+text+"</font>")

    #format data to json dict
    def makeJsonData(self,date,sinkWeight,floatWeight):
        
        data = {"date":date,"sink":sinkWeight,"float":floatWeight}
            
        print(data)
        return data
    #save data
    def saveToJson(self,data):
        cwd = os.getcwd()
        with open(os.path.join(cwd,"Sink Data\\sinkData.txt"),"a") as file:
            json.dump(data, file)
            file.write("\n")

         

        





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Add Point"))
        self.label.setText(_translate("MainWindow", "Sinking weight (g) :"))
        self.label_2.setText(_translate("MainWindow", "Floating weight (g) :"))
        self.useCurrentDatecheckBox.setText(_translate("MainWindow", "use Current Date : "))
        self.label_3.setText(_translate("MainWindow", "Date ( MM/DD/YYYY) :"))
        
        self.pushButton.setText(_translate("MainWindow", "Add data point"))
        self.pushButton_2.setText(_translate("MainWindow", "Veiw Graphs"))
        self.label_4.setText(_translate("MainWindow", "Add Sink Data point"))
        self.quitToMenuButton.setText(_translate("MainWindow", "Return to menu"))
    
    def currentDateFormatted(self):
        currentDate = datetime.date.today()
        day = currentDate.day
        month = currentDate.month
        year = currentDate.year

        formattedDate = "%s/%s/%s" % (month,day,year)

        return formattedDate

#edit smm data points
class editSinkDataPoint(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 51, 301, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSpacing(5)
        
        self.removeEntryButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeEntryButton.setGeometry(QtCore.QRect(15, 360, 301, 31))
        self.removeEntryButton.setObjectName("removeEntryButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(15, 400, 301, 31))
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 40, 301, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 10, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.entries = self.fillList("sinkData.txt")
        
       

        print(self.entries)

        self.fillTable(self.entries)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #get current item
        self.currentItem = ""
        self.listWidget.itemSelectionChanged.connect(self.returnSelectedItem)

    




        #return to menu
        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)
        
        #remove entry pressed
        
        #lamba im using kinda like static
        #maybe better than static for non class things?
        self.removeEntryButton.clicked.connect(lambda: self.removeEntryPressed(self.currentItem))
    
    


    #return active item
    def returnSelectedItem(self):
        selectedItem = self.listWidget.currentItem().text()
        print(selectedItem)
        self.currentItem = selectedItem
        print("current item")
        print(self.currentItem)


    def removeEntryPressed(self,currentItem):
        entryStr = currentItem
        self.confirmDeleteMessage(entryStr)


    def removeItemFromList(self,item,file):
        #HOW WORKS
        #FIND DATA IN FILE AND THEN WRITE BACK TO FILE EXCLUDING ORIGNINAL DATA POINT
        dataLines = []
        
        itemData = item.strip("\n")
        itemData = itemData.replace("Entry Date: ","")
        itemData = itemData.replace("Sinking Plastic Weight: ",":")
        itemData = itemData.replace("Floating Plastic Weight: ",":")
        itemData = itemData.replace("\n","")
        
        itemDataList = itemData.split(":")

        date = itemDataList[0]
        sinking = itemDataList[1]
        floating = itemDataList[2]
        
        
        print("====================================")
        print("itemData: ",itemDataList)
        print("====================================")

        
        cwd = os.getcwd()
        
        with open(os.path.join(cwd,"Sink Data\\",str(file)),"r") as entryFile:
            for entry in entryFile.readlines():
                dataLines.append(entry)
        entryFile.close

        for line in dataLines:
            lineJson = json.loads(line)
            
            

            if str(lineJson["date"]) == str(date) and str(lineJson["sink"]) == str(sinking) and str(lineJson["float"]) == str(floating):
                print("MATCH FOUND")
                print(lineJson)
                print(itemDataList)
                lineToExclude = line#exclude this line during writeback thus deleting it

                print("Lines: ",dataLines)

                with open(os.path.join(cwd,"Sink Data\\",str(file)),"r") as entryFile:
                    lines = entryFile.readlines()
                with open(os.path.join(cwd,"Sink Data\\",str(file)),"w") as entryFile:
                    for line in lines:
                        
                        if line != lineToExclude:
                            entryFile.write(line)
                        else:
                            print("LINE REMOVED")
                self.createAlertPopup("Removed!","Entry was removed succesfully!","Entry Removed!")
                
                runClass("editSinkDataPoint") #it updates

    def createAlertPopup(self,title,message,winTitle):
        alertMsg = QMessageBox()
        alertMsg.setIcon(QMessageBox.Information)
        alertMsg.setText(title)
        alertMsg.setInformativeText(message)
        alertMsg.setWindowTitle(winTitle)
        alertMsg.exec()

    @staticmethod
    def returnToMenuPressed(self):
        runClass("SinkMainMenu")

    def confirmDeleteMessage(self,item):
        item = item.replace("----------------------------------------------------","")

        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete the following entry? This action cannot be undone.")
        
        
        confirmDeleteMessagebox.setInformativeText(item)
        confirmDeleteMessagebox.setWindowTitle("Confirm Deletion?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()
        
        print(buttonResult)

        if buttonResult == "yes":#yes button is pressed
            print("yes")
            self.removeItemFromList(item,"sinkData.txt")
        
        if buttonResult == "no":#no button is pressed
            print("nomegalul")
            pass
        
        

       

    def fillList(self,list):
        entries = []
        cwd = os.getcwd()
        with open(os.path.join(cwd,"Sink Data\\",str(list)),"r") as entryFile:
            for entry in entryFile.readlines():
                entries.append(entry)
                print(entry,"\n")
                
        #print(entries)
        entryFile.close()
        return entries



    def formatEntry(self,item):
        
        item = json.loads(item)
        date = item["date"]
        sinkingWeight = item["sink"]
        floatingWeight = item["float"]

        #==================================
        #----------------------------------------------------
        formattedString = "----------------------------------------------------\nEntry Date: " + str(date) + "\nSinking Plastic Weight: " + str(sinkingWeight) + "\nFloating Plastic Weight: " + str(floatingWeight) +"\n----------------------------------------------------" 

        print(formattedString)


        return(formattedString)


    def fillTable(self,entryList):
        for item in entryList:
            item = self.formatEntry(item)
            
            self.listWidget.addItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Edit Data"))
        self.removeEntryButton.setText(_translate("MainWindow", "Remove Selected Entry"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.label.setText(_translate("MainWindow", "Edit Sinking Data"))





class sinkSettings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.uclTargetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.uclTargetInput.setGeometry(QtCore.QRect(220, 80, 41, 21))
        self.uclTargetInput.setAcceptDrops(True)
        self.uclTargetInput.setAutoFillBackground(False)
        self.uclTargetInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uclTargetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.uclTargetInput.setObjectName("uclTargetInput")
        self.setUclTargetButton = QtWidgets.QPushButton(self.centralwidget)
        self.setUclTargetButton.setGeometry(QtCore.QRect(270, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setUclTargetButton.setFont(font)
        self.setUclTargetButton.setObjectName("setUclTargetButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.uclTargetLabel = QtWidgets.QLabel(self.centralwidget)
        self.uclTargetLabel.setGeometry(QtCore.QRect(170, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uclTargetLabel.setFont(font)
        self.uclTargetLabel.setObjectName("uclTargetLabel")
        self.exportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataButton.setGeometry(QtCore.QRect(20, 180, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exportDataButton.setFont(font)
        self.exportDataButton.setObjectName("exportDataButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.importDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.importDataButton.setGeometry(QtCore.QRect(20, 250, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importDataButton.setFont(font)
        self.importDataButton.setObjectName("importDataButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.resetDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetDataButton.setGeometry(QtCore.QRect(20, 390, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetDataButton.setFont(font)
        self.resetDataButton.setObjectName("resetDataButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(20, 460, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returnToMenuButton.setFont(font)
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 201, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.createBackupButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBackupButton.setGeometry(QtCore.QRect(20, 320, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createBackupButton.setFont(font)
        self.createBackupButton.setObjectName("createBackupButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.updateUclLabel()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)

        self.setUclTargetButton.clicked.connect(lambda: self.settingsSetUcl())

        self.exportDataButton.clicked.connect(lambda: self.exportSinkData("sinkDataExported.ssg"))

        self.importDataButton.clicked.connect(lambda: self.importSinkData())

        self.resetDataButton.clicked.connect(lambda: self.clearAllData())

        self.createBackupButton.clicked.connect(lambda: self.createSinkBackup())
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Settings"))
        self.label.setText(_translate("MainWindow", "Sink Settings"))
        self.label_2.setText(_translate("MainWindow", "Upper Control Limit Target: "))
        self.setUclTargetButton.setText(_translate("MainWindow", "Set"))
        self.label_3.setText(_translate("MainWindow", "Current UCL Target:"))
        self.label_4.setText(_translate("MainWindow", "Sets the upper control limit target. Default = 100"))
        self.uclTargetLabel.setText(_translate("MainWindow", "100"))
        self.exportDataButton.setText(_translate("MainWindow", "Export Data"))
        self.label_5.setText(_translate("MainWindow", "Export sinking data in .SSG format so that it can be reimported to the program elsewhere "))
        self.label_6.setText(_translate("MainWindow", "Import sinking data in .SSG format so that it can be used."))
        self.importDataButton.setText(_translate("MainWindow", "Import Data"))
        self.label_7.setText(_translate("MainWindow", "Resets all sinking data"))
        self.resetDataButton.setText(_translate("MainWindow", "Reset all sinking Data"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.createBackupButton.setText(_translate("MainWindow", "Create a Data Backup"))
        self.label_8.setText(_translate("MainWindow", "Import sinking data in .SSG format so that it can be used."))

        self.updateUclLabel()
        
    



    @staticmethod
    def returnToMenuPressed(self):
        runClass("SinkMainMenu")
    
    def settingsSetUcl(self):
        
        
        uclString = self.uclTargetInput.toPlainText()
        
        
        try:
            uclInt = round(int(uclString),0)
        except ValueError:
            self.createErrorMessage("Value Error","Error! Value must be a whole number (ex. '100') not a decimal or non numeric value.)")
            return

        print("ucl int: ",uclInt)

        
        cwd = os.getcwd()
        with open(os.path.join(cwd,"Sink Data\\sinkSettings.txt"),"w") as settingsFile:
            
            
            settingsFile.write(str(uclInt))
        settingsFile.close()
        self.updateUclLabel()

    def updateUclLabel(self):
        cwd = os.getcwd()
        try:
            with open(os.path.join(cwd,"Sink Data\\sinkSettings.txt"),"r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        except FileNotFoundError:
            with open(os.path.join(cwd,"Sink Data\\sinkSettings.txt"),"w") as settingsFile:
                
                
                settingsFile.write("100")
            settingsFile.close()
            with open(os.path.join(cwd,"Sink Data\\sinkSettings.txt"),"r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        
        ucl = lines[0]
        self.uclTargetLabel.setText(str(ucl))
    

    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()
    
    def createInfoMessage(self,title,message):
        infoMsg = QMessageBox()
        infoMsg.setIcon(QMessageBox.Information)
        infoMsg.setText(title)
        infoMsg.setInformativeText(message)
        infoMsg.setWindowTitle(title)
        infoMsg.exec()

    def backupSinkData(self,fileExportName):
        lines =[]
        cwd = os.getcwd()
        print("cwd: ",cwd)
        with open(os.path.join(cwd,"Sink Data\\sinkData.txt"),"r") as sinkData:
            lines = sinkData.readlines() 
        sinkData.close()

        

        with open(os.path.join(cwd,"Backups\\",fileExportName),"wb") as outfile:
            pickle.dump(lines,outfile)
        outfile.close()
        self.createInfoMessage("Data Backup Succesful!","A backup had been created and saved with the Filename: '"+ str(fileExportName) +"' in directory: " +str(cwd) +"\\Backups\\"+"")


    def exportSinkData(self,fileExportName):
        lines =[]
        cwd = os.getcwd()
        print("cwd: ",cwd)
        with open(os.path.join(cwd,"Sink Data\\sinkData.txt"),"r") as sinkData:
            lines = sinkData.readlines() 
        sinkData.close()

        #"sinkDataExported.ssg"

        with open(os.path.join(cwd,"Exported Data\\",fileExportName),"wb") as outfile:
            pickle.dump(lines,outfile)
        outfile.close()
        self.createInfoMessage("Data Exported Succesfully!","File: '"+ str(fileExportName) +"' has been exported to directory: " + str(cwd) + "\\Exported Data\\"+"")

    def importSinkData(self):
        root = Tk()
        
        root.withdraw() #don't want a full GUi keep the root window from appearing
        ftypes = [
        ('Six Sigma Grapher files', '*.ssg'),  
        ('All files', '*'), 
        ]
        
        filePath = askopenfilename(filetypes=ftypes) # show "Open" dialog box and return path
        
        if ".ssg" in filePath:
            print("acceptable file")

            
        

            confirmImportMessagebox= QMessageBox()
            confirmImportMessagebox.setIcon(QMessageBox.Warning)
            confirmImportMessagebox.setText("Are you sure you would like to import this data? This action cannot be undone and all current data will be overwritten.")
        

            
            confirmImportMessagebox.setWindowTitle("Import and Overwrite?")
            confirmImportMessagebox.addButton(QMessageBox.Yes)
            confirmImportMessagebox.addButton(QMessageBox.No)
            confirmImportMessagebox.exec()
            buttonResult = confirmImportMessagebox.clickedButton().text() #could cause probs
            buttonResult= buttonResult.replace("&","").lower()

            

            if buttonResult == "yes":#yes button is pressed
                print("yes")
                importedFile = open(filePath,"rb")
                importedFileData = pickle.load(importedFile)
                importedFile.close()
                print(importedFileData)
                print(type(importedFileData))
                cwd = os.getcwd()
                with open(os.path.join(cwd,"Sink Data\\sinkData.txt"),"w") as sinkData:
                    for line in importedFileData:
                        sinkData.write(line)
                sinkData.close()
                self.createInfoMessage("File imported succesfully!","File: 'sinkData.txt' has been imported succesfully!")

                
        
            if buttonResult == "no":#no button is pressed
                print("nomegalul")
                pass


        else:
            self.createErrorMessage("Invalid Filetype!","This is an invalid filetype! Only '.ssg' files are accepeted!")
            return
        

    def clearAllData(self):
        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete all data? This action is irreversible and all current data will be lost!")
    

        
        confirmDeleteMessagebox.setWindowTitle("Delete data?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()

        if buttonResult == "yes":#yes button is pressed
            
            time.sleep(1)
            
            proceedMessagebox= QMessageBox()
            proceedMessagebox.setIcon(QMessageBox.Warning)
            proceedMessagebox.setText("Are you sure you would like proceed?")
        

            
            proceedMessagebox.setWindowTitle("Proceed?")
            proceedMessagebox.addButton(QMessageBox.Yes)
            proceedMessagebox.addButton(QMessageBox.No)
            proceedMessagebox.exec()
            proceedButtonResult =proceedMessagebox.clickedButton().text() #could cause probs
            proceedButtonResult= proceedButtonResult.replace("&","").lower()

            if proceedButtonResult == "yes":#yes button is pressed
                print("proceeding to delete.")
                time.sleep(.3)
                print("proceeding to delete..")
                time.sleep(.3)
                print("proceeding to delete...")
                time.sleep(.3)
                print("Deleted!")

                currentDate = datetime.date.today()
                day = currentDate.day
                month = currentDate.month
                year = currentDate.year

                formattedDate = "%s-%s-%s" % (month,day,year)
        

                backupFileName = str("sinkDataExported-Backup-"+formattedDate+".ssg")


                self.exportSinkData(str(backupFileName))
                
                cwd = os.getcwd()
                
                with open(os.path.join(cwd,"Sink Data\\sinkData.txt"),"w") as sinkData:
                    sinkData.write("")
                sinkData.close()
                
                
                self.createInfoMessage("Data Deleted and Backup Created!","All exsiting data has been deleted. A backup of the data was saved to file '"+str(backupFileName)+"' before it was deleted.")
    def createSinkBackup(self):
        confirmBackupMessagebox= QMessageBox()
        confirmBackupMessagebox.setIcon(QMessageBox.Warning)
        confirmBackupMessagebox.setText("Are you sure you would like to create a backup?")
        confirmBackupMessagebox.setWindowTitle("Create sinking data backup?")
        confirmBackupMessagebox.addButton(QMessageBox.Yes)
        confirmBackupMessagebox.addButton(QMessageBox.No)
        confirmBackupMessagebox.exec()
        buttonResult = confirmBackupMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()

        if buttonResult == "yes":#yes button is pressed

            currentDate = datetime.date.today()
            day = currentDate.day
            month = currentDate.month
            year = currentDate.year

            formattedDate = "%s-%s-%s" % (month,day,year)
        

            backupFileName = str("sinkData-Backup-"+formattedDate+".ssg")


            self.backupSinkData(str(backupFileName))

class sinkHelpMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(207, 50, 391, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(47, 20, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 81, 771, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(280, 600, 241, 31))
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sink Data - Help Menu"))
        self.label.setText(_translate("MainWindow", "Help Menu -  Sink Menu"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Entering a new datapoint</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To enter a new datapoint, navigate to the add a datapoint menu by clicking the button labeled &quot;Add New Datapoint&quot;. A new window will load where you will be able to enter the data.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Sinking Weight input box - Input the weight of the sinking plastic (in grams) in this box.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Floating Weight input box - Input the weight of the floating plastic (in grams) in this box.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Date input box- Input the date of when the data is to be recorded. Date must be in month/day/year format (MM/DD/YYYY) This input is automatically disabled when the window is launched. To enable the input, uncheck the &quot;use current date&quot; checkbox below.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Use Current Date checkbox - When this box is checked, the Date Input Box will be disabled and the date for data entered will be the current date.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Add Datapoint button -  Pressing this button processes the data from the input fields and registers it as a new data point</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• View Graph button - Closes the current window and opens the view graphs menu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return to menu Button - Returns to the sink main menu </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Troubleshooting errors</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">If data is entered in an invalid format, the program will automatically throw an error and prevent the data from being entered.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for Sink Weight is Invalid&quot; error -  This error is thrown if data entered in the Sinking Weight feild is invalid. Please ensure that data being entered is a integer or decimal value and does not include letters or other special characters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for Float Weight is Invalid&quot; error -  This error is thrown if data entered in the Floating Weight feild is invalid. Please ensure that data being entered is a integer or decimal value and does not include letters or other special characters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• &quot;Input for date is Invalid&quot; error -  This error is thrown if data entered in the Date feild is invalid. Please ensure that data being entered is in the proper month/day/year format and has no letters. acceptable characters are numbers and &quot;/&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">A status label will appear at the top of the screen showing if data entry was succesful or if there was a problem.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Viewing Graphs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To view graphs, navigate to the graph menu by clicking the button labeled &quot;Veiw Graphs&quot;. A new window will load where you will be able to select the type of graph to view the data. The graphs have a scroll bar underneath them which allows the graph to be &quot;scrolled&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">There are three diffrent types of graphs, a Sinking Percentage Line graph, a Distribution bar graph, and a Deviation plot.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Viewing and Removing Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To view a list of datapoints, or to remove a specific point, click the button labeled: &quot;View and Edit Datapoints&quot; from the main menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Remove Selected Entry button - Begins the removal process.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return To Menu button - Returns user to the sink menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Removing Specific Datapoints</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To remove a specific datapoint, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Select the datapoint from the list by clicking on it so that it is highlighted.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Click the button labeled &quot;Remove Selected Entry&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Confirm by clicking the &quot;Yes&quot; button</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The entry should now be removed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Sink Settings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To access the settings menu for Sinking data, click the button labeled &quot;Settings&quot; from the sink menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Window actions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Upper Control Limit Target input box - Input a value for the upper control limit, confirm it by pressing &quot;set&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Export Data button - Exports data to a .SSG file.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Import Data button - Allows data from an .SSG file to be imported.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Create Data backup button - Creates a backup of all data in .SSG format.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Reset all Sinking Data button - Resets all Sinking data and creates a backup just in case.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• Return to menu button - Returns user to the sink menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Exporting Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To export data in .SSG format, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Export Data&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. A file will be created in directory shown.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Importing Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To import data from a  .SSG file, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Import Data&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. A file browser will be opened, navigate to your .SSG file and click it to select it.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Click the &quot;Open&quot; Button.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Confirm your decision.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. Your data should now be imported.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Creating a Data Backup</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To create a data backup, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Create a Data Backup&quot;. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Confirm that you would like to create a backup.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. A backup should be created.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Reset all Sinking Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To reset all sinking data, follow these instructions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Click the button labeled &quot;Reset All sinkinging Data&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Confirm that you would like to proceed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Confrim your confirmation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. A safety backup will be created and all existing data will be destroyed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Help Menu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To enter the help menu (this menu), click the button labeled &quot;Help Menu&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To exit the help menu, click the button labeled, &quot;Return to menu&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        

    @staticmethod
    def returnToMenuPressed(self):
        runClass("SinkMainMenu")            



#callable class called to call another class. hows that for an alitteration?
def runClass(name):
    #must calll as a static method
    MainWindow.close
    className = eval(name)()
    className.setupUi(MainWindow)
    MainWindow.show





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
lm = LaunchWindow()
lm.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
