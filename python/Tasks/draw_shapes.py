#Syslog-ng- GSoC 2015 task()

'''
Copyright (C) 2015 by Manikandan Selvaganesh <11bc049@skcet.ac.in>
This file is part of syslog-ng task() for GSoC 2015.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the COPYING file for more details.
'''

#Parsing the yaml file (draw_shapes.yaml) and drawing respective shapes.

#!/usr/bin/python
import sys
import yaml
from PyQt4 import QtGui, QtCore

class Task(QtGui.QWidget):

    def __init__(self):
        super(Task, self).__init__()

        self.initUI()

#Setting the window size

    def initUI(self):

        self.setGeometry(500, 500, 650, 650)
        self.setWindowTitle('Syslog_ng_Task()')
        self.show()

#Loading the yaml file

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        yaml_file = open("draw_shapes.yaml")
        dataMap = yaml.safe_load(yaml_file)
        yaml_file.close()
        self.drawRectangles(qp, dataMap['rectangle'])
	self.drawEllipse(qp, dataMap['circle'])
        qp.end()

#Parsing the yaml file
#Method to draw the rectangle

    def drawRectangles(self, qp, tData):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        tColor = tData['color']
        qp.setBrush(QtGui.QColor(tColor['red'], tColor['green'], tColor['blue']))
        qp.drawRect(tData['x-value'], tData['y-value'], tData['width'], tData['height'])

#Method to draw the Ellipse

    def drawEllipse(self, qp, cData):
        cColor = cData['color']
	qp.setBrush(QtGui.QColor(cColor['red'], cColor['green'], cColor['blue'], cColor['a']))
        qp.drawEllipse(cData['x-value'], cData['y-value'], cData['width'], cData['height'])

#Main method

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Task()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
