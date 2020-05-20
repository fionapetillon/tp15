from Exo1 import *
from Exo2 import *

if __name__ == "__main__":
    app = QApplication([])
    win_1 = SQLClientWindow()
    win_2 = ConfigurationDialog()
    win_1.show()
    win_2.show()
    app.exec_()
