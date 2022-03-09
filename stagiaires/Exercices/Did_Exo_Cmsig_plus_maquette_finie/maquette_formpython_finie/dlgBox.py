import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,500,430).size()).expandedTo(Dialog.minimumSizeHint()))

        #Exemple de QLabel
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(5,25,80,18))
        self.label.setObjectName("label")
        self.label.setText("<i>QComboBox !</i>")

        #Exemple de QComboBox
        LstOPGEO = ("A l'intérieur","Chevauche","Contient","Croise","Disjoint","Est égal","Intersecte","Touche")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90,25,150,23))
        self.comboBox.setObjectName("comboBox")
        #Exemple d'alimentation de la QComboBox avec LstOPGEO
        for i in range(len(LstOPGEO)):  self.comboBox.addItem(LstOPGEO[i])

        #Exemple de QLabel
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(280,25,90,18))
        self.label2.setObjectName("label2")
        self.label2.setText("<u>QDoubleSpinBox !</u>")

        #Exemple de QDoubleSpinBox
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(380,25,60,25))
        self.doubleSpinBox.setMaximum(15.55)
        self.doubleSpinBox.setMinimum(0.50)
        self.doubleSpinBox.setValue(12.00)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        #Exemple de QLabel
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(10,60,90,18))
        self.label3.setObjectName("label3")
        self.label3.setText("<font color='#0000FF'>QCalendarWidget !</font>")

        #Exemple de QCalendarWidget
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 80, 250, 180))
        self.calendarWidget.setObjectName("calendarWidget")        
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.showToday()


        #Exemple de QLabel
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(10,270,100,18))
        self.label4.setObjectName("label4")
        self.label4.setText("<b>QFontComboBox !</b>")

        #Exemple de QFontComboBox
        self.FontComboBox = QtWidgets.QFontComboBox(Dialog)
        self.FontComboBox.setGeometry(QtCore.QRect(10, 290, 150, 20))
        self.FontComboBox.setObjectName("FontComboBox")         


        #Exemple de QLabel
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(280,80,100,18))
        self.label5.setObjectName("label5")
        self.label5.setText("<b>QLCDNumber !</b>")

        #Exemple de QLCDNumber
        self.LCDNumber = QtWidgets.QLCDNumber(Dialog)
        self.LCDNumber.setGeometry(QtCore.QRect(380, 80, 100, 20))
        self.LCDNumber.setObjectName("LCDNumber")
        self.LCDNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.LCDNumber.setStyleSheet(
            """QLCDNumber {border: 2px solid grey; border-radius: 5px; background-color: #6C96C6;   text-align: center;}"""
        )
        self.LCDNumber.setDigitCount(8)
        today = datetime.datetime.now()
        self.LCDNumber.display(today.strftime("%H%M%S"))

        #Exemple de QLabel
        self.label6 = QtWidgets.QLabel(Dialog)
        self.label6.setGeometry(QtCore.QRect(280,110,100,18))
        self.label6.setObjectName("label6")
        self.label6.setText("<font color='#FF00FF'><u><i>QProgressBar !</i></u></font>")

        #Exemple de QLCDNumber
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimumSize(QtCore.QSize(210, 15))
        self.progressBar.setMaximumSize(QtCore.QSize(210, 15))
        self.progressBar.setGeometry(QtCore.QRect(280,130,210,15))
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(
            """QProgressBar {border: 2px solid grey; border-radius: 5px; text-align: center;}"""
            """QProgressBar::chunk {background-color: #6C96C6; width: 20px;}"""
        )

        #Exemple de QLabel
        self.label7 = QtWidgets.QLabel(Dialog)
        self.label7.setGeometry(QtCore.QRect(280,150,80,18))
        self.label7.setObjectName("label7")
        self.label7.setText("QPushButton !")

        #Exemple de QPushButton
        self.PushButton = QtWidgets.QPushButton(Dialog)
        self.PushButton.setMinimumSize(QtCore.QSize(140, 20))
        self.PushButton.setMaximumSize(QtCore.QSize(140, 20))
        self.PushButton.setGeometry(QtCore.QRect(350, 150, 140,20))
        self.PushButton.setObjectName("PushButton")
        self.PushButton.setText("Tester la progression !")

        #Exemple de QLabel
        self.label8 = QtWidgets.QLabel(Dialog)
        self.label8.setGeometry(QtCore.QRect(280,180,60,18))
        self.label8.setObjectName("label8")
        self.label8.setText("QTabWidget !")

        #Exemple de QTabWidget
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QtCore.QSize(150, 150))
        self.tabWidget.setMaximumSize(QtCore.QSize(150, 150))
        self.tabWidget.setGeometry(QtCore.QRect(340, 180, 150,150))

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")

        self.tabWidget.addTab(self.tab1, "")
        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.addTab(self.tab3, "")
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), "1")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), "2")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), "3")

        #Exemple de QLabel
        self.label9 = QtWidgets.QLabel(Dialog)
        self.label9.setGeometry(QtCore.QRect(240,340, 100,18))
        self.label9.setObjectName("label9")
        self.label9.setText("QSlider & QDial!")

        #Exemple de QSlider
        self.Slider = QtWidgets.QSlider(Dialog)
        self.Slider.setObjectName("Slider")
        self.Slider.setMinimumSize(QtCore.QSize(150, 20))
        self.Slider.setMaximumSize(QtCore.QSize(150, 20))
        self.Slider.setGeometry(QtCore.QRect(340, 340, 150,20))
        self.Slider.setOrientation(Qt.Horizontal)
        self.Slider.setMinimum(0)
        self.Slider.setMaximum(100)
        self.Slider.setValue(50)

        #Exemple de QDial
        self.Dial = QtWidgets.QDial(Dialog)
        self.Dial.setObjectName("Dial")
        self.Dial.setMinimumSize(QtCore.QSize(80, 80))
        self.Dial.setMaximumSize(QtCore.QSize(80, 80))
        self.Dial.setGeometry(QtCore.QRect(370, 350, 80,80))
        self.Dial.setMinimum(0)
        self.Dial.setMaximum(100)
        self.Dial.setValue(50)


        #Exemple de QLabel
        self.label10 = QtWidgets.QLabel(Dialog)
        self.label10.setGeometry(QtCore.QRect(10,340,150,18))
        self.label10.setObjectName("label10")
        self.label10.setText("QPushButton Close !")

        #Exemple de QPushButton
        self.CloseButton = QtWidgets.QPushButton(Dialog)
        self.CloseButton.setMinimumSize(QtCore.QSize(150, 20))
        self.CloseButton.setMaximumSize(QtCore.QSize(150, 20))        
        self.CloseButton.setGeometry(QtCore.QRect(10, 360, 150, 20))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setText("Action Fermer !")
      
        #Pose a minima une valeur de la barre de progression / slide contrôle
        self.progressBar.setValue(self.Slider.value())

        self.PushButton.clicked.connect(self.MakeProgr)
        self.Slider.valueChanged.connect(self.MakeProgrA)
        self.Dial.valueChanged.connect(self.FixeValueSlider)
        self.CloseButton.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def MakeProgr(self):
        self.progressBar.setValue(0)
        zDim = 100000
        for i in range(zDim+1):
            #Progression de la barre  
            zPercent = int(100 * i / zDim)
            self.progressBar.setValue(zPercent)

    def MakeProgrA(self):
        self.progressBar.setValue(self.Slider.value())
        self.Dial.setValue(self.Slider.value())
        
    def FixeValueSlider(self): self.Slider.setValue(self.Dial.value())
        
    def retranslateUi(self, Dialog): Dialog.setWindowTitle("QWidgets ou Contrôles !")


