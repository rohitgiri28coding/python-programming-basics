import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spin Box')
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel('Enter your choice')
        my_label.setFont(qtg.QFont('Times New Roman', 16))
        self.layout().addWidget(my_label)

        my_spin = qtw.QSpinBox(self,
                               value=10,
                               maximum=100,
                               minimum=0,
                               singleStep=5,  # we can use decimal numbers, but first we need to change QDoubleSpinBox
                               prefix='#',
                               suffix=' Order'
                               )
        my_spin.setFont(qtg.QFont('Times New Roman', 16))
        self.layout().addWidget(my_spin)

        my_button = qtw.QPushButton('Press Me!', clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'You Picked {my_spin.value()}')


app = qtw.QApplication([])
window = MainWindow()
app.exec_()
