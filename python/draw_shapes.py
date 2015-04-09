#Syslog-ng- GSoC 2015 task()

#Parsing the yaml file and drawing respective shapes

#!/usr/bin/python
import sys
import yaml
from PyQt4 import QtGui, QtCore

class Task(QtGui.QWidget):

    def __init__(self):
        super(Task, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 650, 650)
        self.setWindowTitle('Task()')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        yaml_file = open("test.yaml")
        dataMap = yaml.safe_load(yaml_file)
        yaml_file.close()
        self.drawRectangles(qp, dataMap['rectangle'])
	self.drawEllipse(qp, dataMap['circle'])
        qp.end()

    def drawRectangles(self, qp, tData):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        tColor = tData['color']
        qp.setBrush(QtGui.QColor(tColor['red'], tColor['green'], tColor['blue']))
        qp.drawRect(tData['x-value'], tData['y-value'], tData['width'], tData['height'])

    def drawEllipse(self, qp, cData):
        cColor = cData['color']
	qp.setBrush(QtGui.QColor(cColor['red'], cColor['green'], cColor['blue'], cColor['a']))
        qp.drawEllipse(cData['x-value'], cData['y-value'], cData['width'], cData['height'])



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Task()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
