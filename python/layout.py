#Syslog-ng- GSoC 2015 task()

#Initial sample layout

import sys
from PyQt4 import QtGui


class Layout(QtGui.QMainWindow):
    
    def __init__(self):
        super(Layout, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(900, 900, 950, 850)
        self.setWindowTitle('Syslog-ng Configuration Editor layout')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
