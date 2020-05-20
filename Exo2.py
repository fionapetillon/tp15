from PySide2.QtWidgets import *

class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)
        self.text = text

        layout = QHBoxLayout()

        label = QLabel(text)
        text_1 = QTextEdit()
        text_1.setMaximumHeight(20)

        layout.addWidget(label)
        layout.addWidget(text_1)

        self.setLayout(layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")
        self.setMinimumSize(300, 100)

        layout = QVBoxLayout()

        label_1 = LabeledTextField("IP address")
        label_2 = LabeledTextField("User")
        label_3 = LabeledTextField("Password")

        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)

        self.setLayout(layout)
