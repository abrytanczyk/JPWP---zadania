import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from app.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Application Manager')
    app.setWindowIcon(QIcon('icons/plane.png'))
    ex = MainWindow()
    sys.exit(app.exec_())
