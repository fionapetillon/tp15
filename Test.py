from Exo1 import *
from Exo2 import *

if __name__ == "__main__":
    app = QApplication([])
    win1 = SQLClientWindow()
    win2 = ConfigurationDialog()
    win1.show()
    win2.show()
    app.exec_()
