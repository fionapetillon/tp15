from PySide2.QtWidgets import *

class LabeledTextField(QWidget):

    def __init__(self, text):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()


        self.text = text
        self.label = QLabel(text)
        self.textedit = QTextEdit()
        self.textedit.setMaximumHeight(20)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textedit)

        self.setLayout(self.layout)



class ConfigurationDialog(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration ")
        self.setMinimumSize(300, 100)

        self.layout = QVBoxLayout()

        self.label1 = LabeledTextField("IP address")
        self.label2 = LabeledTextField("User")
        self.label3 = LabeledTextField("Password")

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label3)

        self.setLayout(self.layout)

