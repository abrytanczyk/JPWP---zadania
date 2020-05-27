import subprocess

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QPlainTextEdit, QDesktopWidget


class TopViewWindow(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(TopViewWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle(QtWidgets.QApplication.instance().applicationName() + ' - Top')

        self.text_box = QPlainTextEdit()
        self.text_box.setReadOnly(True)

        layout.addWidget(self.text_box)

        self.setLayout(layout)

        center_point = QDesktopWidget().availableGeometry().center()
        window_size = (800, 600)
        self.setGeometry(center_point.x() - window_size[0] // 2,
                         center_point.y() - window_size[1] // 2,
                         window_size[0],
                         window_size[1])

        self.show()

        self.action_timer = QTimer(self)
        self.action_timer.setSingleShot(False)
        self.action_timer.setInterval(1000)
        self.action_timer.timeout.connect(self.update_data)
        self.action_timer.start(1000)

    def update_data(self):
        try:
            output = subprocess.run(["top", "-b", "-n1"], capture_output=True)
            self.text_box.clear()
            self.text_box.setPlainText(output.stdout)
        except (ValueError, OSError, subprocess.SubprocessError) as e:
            self.action_timer.stop()
            QMessageBox.critical(self, "Error!", f"Program execution error: {str(e)}", QMessageBox.Ok)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()