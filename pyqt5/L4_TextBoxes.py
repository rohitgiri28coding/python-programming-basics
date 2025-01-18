import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Box')
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel('Type something below in the box')
        my_label.setFont(qtg.QFont('Times New Roman', 24))
        self.layout().addWidget(my_label)

        my_text = qtw.QTextEdit(self,
                                html='<center><h1><em>header tag with html</em></h1></center>',
                                acceptRichText=True,  # allows to do formatting in text while pasting
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText='Hello World!',
                                readOnly=False
                                )
        self.layout().addWidget(my_text)

        my_button = qtw.QPushButton('Press me!', clicked= lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'you have written {my_text.toPlainText()}')
            my_text.setPlainText('you pressed the button')


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
