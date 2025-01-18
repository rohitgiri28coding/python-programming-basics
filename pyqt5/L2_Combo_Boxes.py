import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class ComboBoxes(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Combo Boxes')
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel('Hello World! What do you want to eat?')
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtBottom)
        my_combo.addItem('Cheese', 'something')
        my_combo.addItem('Roti', 2)
        my_combo.addItem('Chawal', qtw.QWidget)
        my_combo.addItem('Dal')
        my_combo.addItems(['batatapuri', 'panipuri'])
        my_combo.insertItem(1, 'Pizza')
        self.layout().addWidget(my_combo)

        def press_it():
            my_label.setText(f'Ordering {my_combo.currentText()}...')
            print(my_combo.currentData(), ', ', my_combo.currentIndex())
        my_button = qtw.QPushButton('Press me')
        my_button.clicked.connect(press_it)
        self.layout().addWidget(my_button)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication([])
    window = ComboBoxes()
    app.exec_()
