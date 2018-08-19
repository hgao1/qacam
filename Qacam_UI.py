# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qacam_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qacam(object):
    def setupUi(self, Qacam):
        Qacam.setObjectName("Qacam")
        Qacam.resize(868, 531)
        self.centralwidget = QtWidgets.QWidget(Qacam)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabScan = QtWidgets.QWidget()
        self.tabScan.setObjectName("tabScan")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabScan)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scanner = QtWidgets.QWidget(self.tabScan)
        self.scanner.setMaximumSize(QtCore.QSize(16777215, 40))
        self.scanner.setObjectName("scanner")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scanner)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.n1 = QtWidgets.QLCDNumber(self.scanner)
        self.n1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.n1.setObjectName("n1")
        self.horizontalLayout.addWidget(self.n1)
        spacerItem = QtWidgets.QSpacerItem(197, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.scan = QtWidgets.QPushButton(self.scanner)
        self.scan.setObjectName("scan")
        self.horizontalLayout.addWidget(self.scan)
        spacerItem1 = QtWidgets.QSpacerItem(196, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.n2 = QtWidgets.QLCDNumber(self.scanner)
        self.n2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.n2.setObjectName("n2")
        self.horizontalLayout.addWidget(self.n2)
        self.verticalLayout.addWidget(self.scanner)
        self.plot = PlotWidget(self.tabScan)
        self.plot.setObjectName("plot")
        self.verticalLayout.addWidget(self.plot)
        self.tabWidget.addTab(self.tabScan, "")
        self.tabAmplitude = QtWidgets.QWidget()
        self.tabAmplitude.setObjectName("tabAmplitude")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabAmplitude)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plotAmplitude = PlotWidget(self.tabAmplitude)
        self.plotAmplitude.setObjectName("plotAmplitude")
        self.verticalLayout_2.addWidget(self.plotAmplitude)
        self.tabWidget.addTab(self.tabAmplitude, "")
        self.tabPhase = QtWidgets.QWidget()
        self.tabPhase.setObjectName("tabPhase")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabPhase)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plotPhase = PlotWidget(self.tabPhase)
        self.plotPhase.setObjectName("plotPhase")
        self.verticalLayout_3.addWidget(self.plotPhase)
        self.tabWidget.addTab(self.tabPhase, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.controlWidget = QtWidgets.QWidget(self.centralwidget)
        self.controlWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.controlWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.controlWidget.setObjectName("controlWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.controlWidget)
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelPolargraph = QtWidgets.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPolargraph.setFont(font)
        self.labelPolargraph.setObjectName("labelPolargraph")
        self.verticalLayout_5.addWidget(self.labelPolargraph)
        self.polargraph = QPolargraphSettings(self.controlWidget)
        self.polargraph.setObjectName("polargraph")
        self.verticalLayout_5.addWidget(self.polargraph)
        self.labelFunctionGenerator = QtWidgets.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFunctionGenerator.setFont(font)
        self.labelFunctionGenerator.setObjectName("labelFunctionGenerator")
        self.verticalLayout_5.addWidget(self.labelFunctionGenerator)
        self.frameFunctionGenerator = QtWidgets.QFrame(self.controlWidget)
        self.frameFunctionGenerator.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameFunctionGenerator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFunctionGenerator.setLineWidth(2)
        self.frameFunctionGenerator.setObjectName("frameFunctionGenerator")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameFunctionGenerator)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.functionGenerator = QDS345Settings(self.frameFunctionGenerator)
        self.functionGenerator.setObjectName("functionGenerator")
        self.verticalLayout_4.addWidget(self.functionGenerator)
        self.verticalLayout_5.addWidget(self.frameFunctionGenerator)
        self.labelLockin = QtWidgets.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLockin.setFont(font)
        self.labelLockin.setObjectName("labelLockin")
        self.verticalLayout_5.addWidget(self.labelLockin)
        self.lockin = QSR830Settings(self.controlWidget)
        self.lockin.setMinimumSize(QtCore.QSize(100, 0))
        self.lockin.setObjectName("lockin")
        self.verticalLayout_5.addWidget(self.lockin)
        self.horizontalLayout_2.addWidget(self.controlWidget)
        Qacam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Qacam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Qacam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Qacam)
        self.statusbar.setObjectName("statusbar")
        Qacam.setStatusBar(self.statusbar)
        self.actionSave_Settings = QtWidgets.QAction(Qacam)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionSave_Hologram = QtWidgets.QAction(Qacam)
        self.actionSave_Hologram.setAutoRepeat(False)
        self.actionSave_Hologram.setObjectName("actionSave_Hologram")
        self.action_Quit = QtWidgets.QAction(Qacam)
        self.action_Quit.setObjectName("action_Quit")
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionSave_Hologram)
        self.menuFile.addAction(self.action_Quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Qacam)
        self.tabWidget.setCurrentIndex(0)
        self.action_Quit.triggered.connect(Qacam.close)
        QtCore.QMetaObject.connectSlotsByName(Qacam)

    def retranslateUi(self, Qacam):
        _translate = QtCore.QCoreApplication.translate
        Qacam.setWindowTitle(_translate("Qacam", "Scanning Acoustic Camera"))
        self.scan.setText(_translate("Qacam", "Scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScan), _translate("Qacam", "Scanner"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAmplitude), _translate("Qacam", "Amplitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPhase), _translate("Qacam", "Phase"))
        self.labelPolargraph.setText(_translate("Qacam", "Polargraph"))
        self.labelFunctionGenerator.setText(_translate("Qacam", "Function Generator"))
        self.labelLockin.setText(_translate("Qacam", "Lockin Amplifier"))
        self.menuFile.setTitle(_translate("Qacam", "File"))
        self.actionSave_Settings.setText(_translate("Qacam", "Save Settings"))
        self.actionSave_Settings.setStatusTip(_translate("Qacam", "Save Instrument Settings"))
        self.actionSave_Settings.setShortcut(_translate("Qacam", "Meta+T"))
        self.actionSave_Hologram.setText(_translate("Qacam", "Save Hologram ..."))
        self.actionSave_Hologram.setStatusTip(_translate("Qacam", "Save Hologram"))
        self.actionSave_Hologram.setShortcut(_translate("Qacam", "Meta+S"))
        self.action_Quit.setText(_translate("Qacam", "&Quit"))

from QDS345 import QDS345Settings
from QPolargraph import QPolargraphSettings
from QSR830 import QSR830Settings
from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qacam = QtWidgets.QMainWindow()
    ui = Ui_Qacam()
    ui.setupUi(Qacam)
    Qacam.show()
    sys.exit(app.exec_())

