import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Forms')

        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        label1 = qtw.QLabel('Enter your name')
        label1.setFont(qtg.QFont('Arial', 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        form_layout.addRow(label1)
        form_layout.addRow('First Name', f_name)
        form_layout.addRow('Last Name', l_name)

        button = qtw.QPushButton('Push Me!', clicked=lambda: self.press(f_name, l_name))
        form_layout.addRow(button)

        self.show()

    def press(self, f_name, l_name):
        qtw.QMessageBox.information(self, 'Message', f'Your name is {f_name.text().capitalize()} {l_name.text().capitalize()}')


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
