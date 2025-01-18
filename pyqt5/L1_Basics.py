import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import *


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello world')  # add a title
        self.setLayout(qtw.QVBoxLayout())  # sets vertical layout

        l1 = qtw.QLabel('Hello World')
        l1.setFont(QFont('Helvetica', 22))  # sets font size
        self.layout().addWidget(l1)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name')
        my_entry.setText('')
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton('Push me!',
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()

        def press_it():
            l1.setText(f'Hello {my_entry.text().capitalize()}')
            my_entry.setText('')


app = qtw.QApplication([])
mw = MainWindow()

app.exec()
