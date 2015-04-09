#Syslog-ng - GSoC 2015 task()

#Syslog_ng Configuration Editor's layout.

# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(100, 20, 531, 421))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 250, 97, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 251, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 50, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 90, 531, 41))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tWShapes = QtGui.QTreeWidget(self.centralwidget)
        self.tWShapes.setGeometry(QtCore.QRect(100, 110, 351, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tWShapes.setFont(font)
        self.tWShapes.setObjectName(_fromUtf8("tWShapes"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tWShapes.headerItem().setFont(0, font)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 111, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(450, 126, 181, 31))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.tWProperties = QtGui.QTableWidget(self.centralwidget)
        self.tWProperties.setGeometry(QtCore.QRect(450, 140, 181, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tWProperties.setFont(font)
        self.tWProperties.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tWProperties.setObjectName(_fromUtf8("tWProperties"))
        self.tWProperties.setColumnCount(2)
        self.tWProperties.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tWProperties.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tWProperties.setHorizontalHeaderItem(1, item)
        self.tWProperties.horizontalHeader().setStretchLastSection(True)
        self.tWProperties.verticalHeader().setVisible(False)
        self.verticalScrollBar = QtGui.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(610, 170, 21, 271))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(540, 170, 20, 271))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 80, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(100, 70, 531, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 400, 97, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Layout design", None))
        self.pushButton.setText(_translate("MainWindow", "File", None))
        self.label.setText(_translate("MainWindow", "      Syslog-ng configuration Editor", None))
        self.label_2.setText(_translate("MainWindow", "File", None))
        self.tWShapes.headerItem().setText(0, _translate("MainWindow", "Graph view pane", None))
        self.label_3.setText(_translate("MainWindow", "Properties", None))
        item = self.tWProperties.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property", None))
        item = self.tWProperties.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        self.label_4.setText(_translate("MainWindow", "File Location", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save", None))

import sys
from PyQt4 import QtGui, QtCore
from syslog_layout import Ui_MainWindow

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())

