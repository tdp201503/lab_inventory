from PyQt4 import QtGui
import sys
from controlador import LabInventoryController


def main():
    app = QtGui.QApplication(sys.argv)
    app_gui = LabInventoryController()
    app_gui.show()
    app.exec_()

if __name__ == "__main__":
    main()
