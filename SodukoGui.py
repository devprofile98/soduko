# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sudoku2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def __init__(self):
        self.Btn=[]
    def setupUi(self, mainWindow):
        self.Btn=[]
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 510)
        mainWindow.setMinimumSize(QtCore.QSize(500, 510))
        mainWindow.setMaximumSize(QtCore.QSize(500, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/1200x630wa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 10, 41, 41))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 10, 41, 41))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 10, 41, 41))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 10, 41, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 10, 41, 41))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 10, 41, 41))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 10, 41, 41))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 60, 41, 41))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 60, 41, 41))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(270, 60, 41, 41))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 60, 41, 41))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(170, 60, 41, 41))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(380, 60, 41, 41))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(430, 60, 41, 41))
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(330, 110, 41, 41))
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(270, 110, 41, 41))
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 110, 41, 41))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(220, 110, 41, 41))
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(110, 110, 41, 41))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(430, 110, 41, 41))
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(60, 110, 41, 41))
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(170, 110, 41, 41))
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(380, 110, 41, 41))
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(270, 270, 41, 41))
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(220, 270, 41, 41))
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(220, 170, 41, 41))
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(270, 170, 41, 41))
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 170, 41, 41))
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(60, 170, 41, 41))
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(430, 220, 41, 41))
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(110, 170, 41, 41))
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(170, 270, 41, 41))
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(380, 220, 41, 41))
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(330, 220, 41, 41))
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(380, 270, 41, 41))
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(330, 170, 41, 41))
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(430, 270, 41, 41))
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(170, 220, 41, 41))
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(110, 270, 41, 41))
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(270, 220, 41, 41))
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(380, 170, 41, 41))
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(10, 220, 41, 41))
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(330, 270, 41, 41))
        self.pushButton_47.setText("")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setGeometry(QtCore.QRect(170, 170, 41, 41))
        self.pushButton_48.setText("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_49.setGeometry(QtCore.QRect(60, 270, 41, 41))
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(220, 220, 41, 41))
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(110, 220, 41, 41))
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(430, 170, 41, 41))
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(60, 220, 41, 41))
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_54.setGeometry(QtCore.QRect(10, 270, 41, 41))
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(10, 370, 41, 41))
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_56.setGeometry(QtCore.QRect(60, 420, 41, 41))
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_57.setGeometry(QtCore.QRect(330, 420, 41, 41))
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setGeometry(QtCore.QRect(220, 370, 41, 41))
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setGeometry(QtCore.QRect(430, 370, 41, 41))
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_60.setGeometry(QtCore.QRect(10, 420, 41, 41))
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_61.setGeometry(QtCore.QRect(270, 320, 41, 41))
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_62.setGeometry(QtCore.QRect(10, 320, 41, 41))
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_63.setGeometry(QtCore.QRect(270, 420, 41, 41))
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_64.setGeometry(QtCore.QRect(380, 370, 41, 41))
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_65.setGeometry(QtCore.QRect(60, 370, 41, 41))
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_66.setGeometry(QtCore.QRect(60, 320, 41, 41))
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_67.setGeometry(QtCore.QRect(330, 370, 41, 41))
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_68.setGeometry(QtCore.QRect(380, 320, 41, 41))
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_69.setGeometry(QtCore.QRect(220, 420, 41, 41))
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_70.setGeometry(QtCore.QRect(170, 420, 41, 41))
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_71.setGeometry(QtCore.QRect(270, 370, 41, 41))
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_72.setGeometry(QtCore.QRect(170, 370, 41, 41))
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_73.setGeometry(QtCore.QRect(110, 370, 41, 41))
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(430, 320, 41, 41))
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_75.setGeometry(QtCore.QRect(430, 420, 41, 41))
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_76.setGeometry(QtCore.QRect(220, 320, 41, 41))
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_77.setGeometry(QtCore.QRect(330, 320, 41, 41))
        self.pushButton_77.setText("")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_78.setGeometry(QtCore.QRect(110, 420, 41, 41))
        self.pushButton_78.setText("")
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_79.setGeometry(QtCore.QRect(110, 320, 41, 41))
        self.pushButton_79.setText("")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_80.setGeometry(QtCore.QRect(170, 320, 41, 41))
        self.pushButton_80.setText("")
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_81.setGeometry(QtCore.QRect(380, 420, 41, 41))
        self.pushButton_81.setText("")
        self.pushButton_81.setObjectName("pushButton_81")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menustart = QtWidgets.QMenu(self.menubar)
        self.menustart.setObjectName("menustart")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionstart = QtWidgets.QAction(mainWindow)
        self.actionstart.setObjectName("actionstart")
        self.actionrestart = QtWidgets.QAction(mainWindow)
        self.actionrestart.setObjectName("actionrestart")
        self.menustart.addAction(self.actionstart)
        self.menustart.addAction(self.actionrestart)
        self.menubar.addAction(self.menustart.menuAction())
        self.pushButton_12.setText("1")
        self.Btn+=[
        [self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5,self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9],
        [self.pushButton_17,self.pushButton_12,self.pushButton_14,self.pushButton_15,self.pushButton_10,self.pushButton_13,self.pushButton_11,self.pushButton_16,self.pushButton_18],
        [self.pushButton_21,self.pushButton_25,self.pushButton_23,self.pushButton_26,self.pushButton_22,self.pushButton_20,self.pushButton_19,self.pushButton_27,self.pushButton_24],
        [self.pushButton_32,self.pushButton_33,self.pushButton_35,self.pushButton_48,self.pushButton_30,self.pushButton_31,self.pushButton_40,self.pushButton_45,self.pushButton_52],
        [self.pushButton_46,self.pushButton_53,self.pushButton_51,self.pushButton_42,self.pushButton_50,self.pushButton_44,self.pushButton_38,self.pushButton_37,self.pushButton_34],
        [self.pushButton_54,self.pushButton_49,self.pushButton_43,self.pushButton_36,self.pushButton_29,self.pushButton_28,self.pushButton_47,self.pushButton_39,self.pushButton_41],
        [self.pushButton_62,self.pushButton_66,self.pushButton_79,self.pushButton_80,self.pushButton_76,self.pushButton_61,self.pushButton_77,self.pushButton_68,self.pushButton_74],
        [self.pushButton_55,self.pushButton_65,self.pushButton_73,self.pushButton_72,self.pushButton_58,self.pushButton_71,self.pushButton_67,self.pushButton_64,self.pushButton_59],
        [self.pushButton_60,self.pushButton_56,self.pushButton_78,self.pushButton_70,self.pushButton_69,self.pushButton_63,self.pushButton_57,self.pushButton_81,self.pushButton_75],

    ]
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        for i in range(9):
            for j in range(9):
                self.Btn[i][j].setText(str(board[i][j]))
    def setV(self):
        pass
                
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Soduko"))
        self.menustart.setTitle(_translate("mainWindow", "me&nu"))
        self.actionstart.setText(_translate("mainWindow", "start"))
        self.actionrestart.setText(_translate("mainWindow", "restart"))

def backtrack(board):
    Position = FindEmpty(board)
    if Position == None:
        return True
    else:
        x , y = Position
    for i in range(1,10):
        board[x][y] = i
        if promising(board,x,y):  
            if backtrack(board):
                return True
        board[x][y]=0
def promising(board,i,j):
 
    switch = True
    for x in range(0,j+1):
        for y in range(0,j+1):
            if x!=y and board[i][x] == board[i][y] and board[i][x]!=0:
                switch = False
    for x in range(0,i+1):
        for y in range(0,i+1):
            if x!=y and board[x][j]==board[y][j] and board[x][j]!=0:
                switch = False
           
    include =[0,1,2,3,4,5,6,7,8,9]
    for x in range(i-(i%3),(i-(i%3))+3):
        for y in range(j-(j%3),(j-(j%3))+3): 
            if include[int(board[x][y])] == None:
                switch = False
                break
            if int(board[x][y])!=0:
                include[int(board[x][y])] = None
    return switch

def FindEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None




if __name__ == "__main__":
    board=[[2,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,9,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]
        ]
    backtrack(board)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.setV()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
