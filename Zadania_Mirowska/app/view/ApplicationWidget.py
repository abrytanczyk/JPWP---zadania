import subprocess

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMessageBox

from app.data.ConfigurationManager import ConfigurationManager
from app.model.ApplicationData import ApplicationData
from app.view.ApplicationSettingsWidget import ApplicationSettingsWidget
import os


class ApplicationWidget(QWidget):
    def __init__(self, app_data: ApplicationData, parent):
        super(ApplicationWidget, self).__init__(parent)

        self.app_data = app_data
        self.initUI()

    def initUI(self):

        grid = QGridLayout(self)
        self.setLayout(grid)
        self.setMinimumHeight(100)

        self.label = QLabel(self.app_data.name, self)
        self.label2 = QLabel(self.app_data.description, self)

        settings_btn = QPushButton('', self)
        settings_btn.setIcon(QIcon('icons/nature.png'))
        settings_btn.pressed.connect(self.application_open_setting)

        run_btn = QPushButton('Run', self)
        run_btn.pressed.connect(self.run_clicked)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(settings_btn, 0, 1, QtCore.Qt.AlignRight)
        grid.addWidget(run_btn, 2, 0)

        self.show()

    def update_vew(self):
        self.label.setText(self.app_data.name)
        self.label2.setText(self.app_data.description)

    def application_open_setting(self):
        settings_window = ApplicationSettingsWidget(self.app_data)

        if settings_window.exec_():
            self.app_data = settings_window.app_data
            self.update_vew()
            ConfigurationManager.save_configuration()

    def run_clicked(self):
        try:
            subprocess.Popen(executable=str(self.app_data.path),
                             args=self.app_data.arguments,
                             cwd=self.app_data.work_dir,
                             startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.DETACHED_PROCESS))
        except (ValueError, OSError, subprocess.SubprocessError) as e:
            QMessageBox.critical(self, "Error!", f"Program execution error: {str(e)}", QMessageBox.Ok)
