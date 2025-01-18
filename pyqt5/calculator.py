# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.resize(484, 602)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "    background-color: rgb(32, 32, 32)\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("#frame { background-color: rgb(32,32,32)}\n"
                                 "QWidget#frame > * { color: rgb(255, 255, 255)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(360, 180, 120, 421))
        self.frame_3.setStyleSheet("#frame_3 > * { background-color: rgb(60,60,60)}\n"
                                   "QWidget#frame_3 > * { color: rgb(255, 255, 255)}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.backspace_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.backspace())
        self.backspace_button.setGeometry(QtCore.QRect(0, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backspace_button.sizePolicy().hasHeightForWidth())
        self.backspace_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.backspace_button.setFont(font)
        self.backspace_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backspace_button.setAutoFillBackground(False)
        self.backspace_button.setObjectName("backspace_button")
        self.divide_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.press_it('/'))
        self.divide_button.setGeometry(QtCore.QRect(0, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.divide_button.setFont(font)
        self.divide_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divide_button.setAutoFillBackground(False)
        self.divide_button.setObjectName("divide_button")
        self.multiply_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.press_it('x'))
        self.multiply_button.setGeometry(QtCore.QRect(0, 140, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiply_button.sizePolicy().hasHeightForWidth())
        self.multiply_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.multiply_button.setFont(font)
        self.multiply_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiply_button.setAutoFillBackground(False)
        self.multiply_button.setObjectName("multiply_button")
        self.minus_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.press_it('-'))
        self.minus_button.setGeometry(QtCore.QRect(0, 210, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus_button.sizePolicy().hasHeightForWidth())
        self.minus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.minus_button.setFont(font)
        self.minus_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus_button.setAutoFillBackground(False)
        self.minus_button.setObjectName("minus_button")
        self.plus_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.press_it('+'))
        self.plus_button.setGeometry(QtCore.QRect(0, 280, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_button.sizePolicy().hasHeightForWidth())
        self.plus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.plus_button.setFont(font)
        self.plus_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_button.setAutoFillBackground(False)
        self.plus_button.setObjectName("plus_button")
        self.equal_button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.equal())
        self.equal_button.setGeometry(QtCore.QRect(0, 350, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.equal_button.setFont(font)
        self.equal_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal_button.setAutoFillBackground(False)
        self.equal_button.setStyleSheet("QPushButtons{\n"
                                        "    background-color: rgb(60, 60, 60)\n"
                                        "}")
        self.equal_button.setObjectName("equal_button")
        self.input_line_edit = QtWidgets.QLineEdit(self.frame)
        self.input_line_edit.setGeometry(QtCore.QRect(0, 40, 471, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_line_edit.sizePolicy().hasHeightForWidth())
        self.input_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.input_line_edit.setFont(font)
        self.input_line_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        regex = r'^[0-9+-/x*%√²%.\s]+$'
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(regex))
        self.input_line_edit.setValidator(validator)
        self.input_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_line_edit.setAutoFillBackground(False)
        self.input_line_edit.setStyleSheet("#input_line_edit{\n"
                                           "    border: none;\n"
                                           "    background-color: rgb(32, 32, 32)\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.input_line_edit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.input_line_edit.setObjectName("input_line_edit")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 180, 361, 141))
        self.frame_2.setStyleSheet("#frame_2 > * {\n"
                                   "    background-color:rgb(60,60,60)\n"
                                   "}\n"
                                   "QWidget#frame_2 > * { color: rgb(255, 255, 255)} ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.clear_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.clear())
        self.clear_button.setGeometry(QtCore.QRect(240, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.clear_button.setFont(font)
        self.clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_button.setAutoFillBackground(False)
        self.clear_button.setObjectName("clear_button")
        self.percent_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.press_it('%'))
        self.percent_button.setGeometry(QtCore.QRect(0, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percent_button.sizePolicy().hasHeightForWidth())
        self.percent_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.percent_button.setFont(font)
        self.percent_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.percent_button.setAutoFillBackground(False)
        self.percent_button.setObjectName("percent_button")
        self.clear_all_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.clear_all())
        self.clear_all_button.setGeometry(QtCore.QRect(120, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_all_button.sizePolicy().hasHeightForWidth())
        self.clear_all_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all_button.setAutoFillBackground(False)
        self.clear_all_button.setObjectName("clear_all_button")
        self.inverse_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.press_it('1/'))
        self.inverse_button.setGeometry(QtCore.QRect(0, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inverse_button.sizePolicy().hasHeightForWidth())
        self.inverse_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.inverse_button.setFont(font)
        self.inverse_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inverse_button.setAutoFillBackground(False)
        self.inverse_button.setObjectName("inverse_button")
        self.sq_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.press_it('²'))
        self.sq_button.setGeometry(QtCore.QRect(120, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sq_button.sizePolicy().hasHeightForWidth())
        self.sq_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sq_button.setFont(font)
        self.sq_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sq_button.setAutoFillBackground(False)
        self.sq_button.setObjectName("sq_button")
        self.sq_root_button = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.press_it('√'))
        self.sq_root_button.setGeometry(QtCore.QRect(240, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sq_root_button.sizePolicy().hasHeightForWidth())
        self.sq_root_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sq_root_button.setFont(font)
        self.sq_root_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sq_root_button.setAutoFillBackground(False)
        self.sq_root_button.setObjectName("sq_root_button")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 320, 361, 281))
        self.frame_4.setToolTipDuration(-6)
        self.frame_4.setStyleSheet("#frame_4 > * { background-color: rgb(50,50,50)}\n"
                                   "QWidget#frame_4 > * { color: rgb(255, 255, 255)}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.four_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('4'))
        self.four_button.setGeometry(QtCore.QRect(0, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.four_button.setFont(font)
        self.four_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four_button.setAutoFillBackground(False)
        self.four_button.setObjectName("four_button")
        self.five_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('5'))
        self.five_button.setGeometry(QtCore.QRect(120, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.five_button.setFont(font)
        self.five_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five_button.setAutoFillBackground(False)
        self.five_button.setObjectName("five_button")
        self.three_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('3'))
        self.three_button.setGeometry(QtCore.QRect(240, 140, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.three_button.setFont(font)
        self.three_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three_button.setAutoFillBackground(False)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('2'))
        self.two_button.setGeometry(QtCore.QRect(120, 140, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.two_button.setFont(font)
        self.two_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two_button.setAutoFillBackground(False)
        self.two_button.setObjectName("two_button")
        self.eight_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('8'))
        self.eight_button.setGeometry(QtCore.QRect(120, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight_button.sizePolicy().hasHeightForWidth())
        self.eight_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.eight_button.setFont(font)
        self.eight_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight_button.setAutoFillBackground(False)
        self.eight_button.setObjectName("eight_button")
        self.nine_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('9'))
        self.nine_button.setGeometry(QtCore.QRect(240, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.nine_button.setFont(font)
        self.nine_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine_button.setAutoFillBackground(False)
        self.nine_button.setObjectName("nine_button")
        self.dot_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('.'))
        self.dot_button.setGeometry(QtCore.QRect(240, 210, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dot_button.sizePolicy().hasHeightForWidth())
        self.dot_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.dot_button.setFont(font)
        self.dot_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dot_button.setAutoFillBackground(False)
        self.dot_button.setObjectName("dot_button")
        self.six_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('6'))
        self.six_button.setGeometry(QtCore.QRect(240, 70, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.six_button.setFont(font)
        self.six_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six_button.setAutoFillBackground(False)
        self.six_button.setObjectName("six_button")
        self.seven_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('7'))
        self.seven_button.setGeometry(QtCore.QRect(0, 0, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.seven_button.setFont(font)
        self.seven_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_button.setAutoFillBackground(False)
        self.seven_button.setObjectName("seven_button")
        self.one_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('1'))
        self.one_button.setGeometry(QtCore.QRect(0, 140, 121, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.one_button.setFont(font)
        self.one_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one_button.setAutoFillBackground(False)
        self.one_button.setObjectName("one_button")
        self.zero_button = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.press_it('0'))
        self.zero_button.setGeometry(QtCore.QRect(0, 210, 241, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.zero_button.setFont(font)
        self.zero_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero_button.setAutoFillBackground(False)
        self.zero_button.setObjectName("zero_button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
                                 "    background-color: rgb(32,32,32)\n"
                                 "}\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Calculator", "Calculator"))
        self.backspace_button.setText(_translate("MainWindow", "Backspace"))
        self.divide_button.setText(_translate("MainWindow", "÷"))
        self.multiply_button.setText(_translate("MainWindow", "x"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.input_line_edit.setText(_translate("MainWindow", "0"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.clear_all_button.setText(_translate("MainWindow", "CE"))
        self.inverse_button.setText(_translate("MainWindow", "1/x"))
        self.sq_button.setText(_translate("MainWindow", "x²"))
        self.sq_root_button.setText(_translate("MainWindow", "√x"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Standard"))
        self.input_line_edit.returnPressed.connect(self.equal_button.click)

    def press_it(self, pressed):
        if self.input_line_edit.text() in ['0', 'ERROR']:
            self.input_line_edit.setText(pressed)
        else:
            self.input_line_edit.setText(self.input_line_edit.text()+pressed)

    def clear(self):
        input = self.input_line_edit.text()
        try:
            float(input)
            self.input_line_edit.setText('0')
        except ValueError:
            for i in range(len(input) - 1, 0, -1):
                if not input[i].isdigit() or input[i] == '.':
                    continue
                else:
                    self.input_line_edit.setText(input[:i + 1])
                    break

    def clear_all(self):
        self.input_line_edit.setText('0')

    def backspace(self):
        input = self.input_line_edit.text()
        self.input_line_edit.setText(input[:len(input) - 1])

    def equal(self):
        obj = Cal(self.input_line_edit.text())
        self.input_line_edit.setText(obj.answer)


class Cal:
    def __init__(self, exp):
        try:
            self.exp = exp
            self.number, self.operator = self.separation()
            self.simplify()
            self.call()
            if len(self.operator) > 0:
                self.answer = 'ERROR'
            else:
                self.answer = str(self.number[0])
        except Exception:
            self.answer = 'ERROR'

    def separation(self):
        num = []
        operator = []
        temp = 0
        for i in range(len(self.exp)):
            char = self.exp[i]
            if char != '²' and char.isdigit():
                temp = temp * 10 + int(char)
            elif char == ' ':
                continue
            else:
                num.append(temp)
                temp = 0
                operator.append(self.exp[i])
        num.append(temp)
        return num, operator

    def simplify(self):
        op = ['%', '√', '²']
        for i in op:
            while i in self.operator:
                index = self.operator.index(i)
                if i == '√':
                    self.number[index - 1] = self.number[index - 1] ** 0.5
                    self.operator.pop(index)
                elif i == '²':
                    self.number[index] = self.number[index] ** 2
                    self.operator.pop(index)
                else:
                    self.number[index] = self.number[index] / 100
                    self.operator.pop(index)

    def calculate(self, symbol, freq):
        def delete_elements(index, res):
            self.number.pop(index)
            self.number.pop(index)
            self.number.insert(index, res)
            self.operator.pop(index)

        for _ in range(freq):
            index = self.operator.index(symbol)
            if symbol == '/':
                res = self.number[index] / self.number[(index + 1)]
                delete_elements(index, res)
            elif symbol == 'x' or symbol == '*':
                res = self.number[index] * self.number[(index + 1)]
                delete_elements(index, res)
            elif symbol == '+':
                res = self.number[index] + self.number[(index + 1)]
                delete_elements(index, res)
            elif symbol == '-':
                res = self.number[index] - self.number[(index + 1)]
                delete_elements(index, res)

    def call(self):
        def frequency(symbol):
            return self.operator.count(symbol)

        self.calculate('/', frequency('/'))
        self.calculate('x', frequency('x'))
        self.calculate('*', frequency('*'))
        self.calculate('-', frequency('-'))
        self.calculate('+', frequency('+'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
