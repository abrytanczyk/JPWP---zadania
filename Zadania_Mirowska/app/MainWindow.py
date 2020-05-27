import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QDesktopWidget, QHBoxLayout, QPushButton, \
    QAction, QMainWindow, QSizePolicy

from app.data.ConfigurationManager import ConfigurationManager
from app.model.ApplicationData import ApplicationData
from app.view.ApplicationSettingsWidget import ApplicationSettingsWidget
from app.view.ApplicationWidget import ApplicationWidget
from app.view.TopViewWindow import TopViewWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.top_window = None

        ConfigurationManager.load_configuration()
        self.initUI()

    def initUI(self):
        center_point = QDesktopWidget().availableGeometry().center()
        window_size = (300, 600)
        self.setGeometry(center_point.x() - window_size[0] // 2,
                         center_point.y() - window_size[1] // 2,
                         window_size[0],
                         window_size[1])
        self.setWindowTitle(QtWidgets.QApplication.instance().applicationName())

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        scrollContent = QWidget()
        scrollContent.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        scroll.setWidget(scrollContent)

        self.scrollLayout = QVBoxLayout(scrollContent)
        self.scrollLayout.setSpacing(0)
        scrollContent.setLayout(self.scrollLayout)

        self.create_apps_list()

        self.setCentralWidget(scroll)

        self.create_menubar()

        self.show()

    def create_apps_list(self):
        # clear
        for i in range(self.scrollLayout.count()):
            self.scrollLayout.itemAt(0).widget().setParent(None)

        for item in ConfigurationManager.get_configuration().applications_list:
            widget = ApplicationWidget(item, self)
            widget.setMaximumHeight(widget.minimumHeight())
            self.scrollLayout.addWidget(widget, 0)

    def create_menubar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        newAct = QAction('New', self)
        newAct.setIcon(QIcon('icons/plus.png'))
        newAct.triggered.connect(self.add_new_launcher)

        toolsMenu = menubar.addMenu('Tools')

        topAct = QAction('Top', self)
        topAct.triggered.connect(self.show_top_window)

        fileMenu.addAction(newAct)
        toolsMenu.addAction(topAct)

    def closeEvent(self, event):
        ConfigurationManager.save_configuration()
        event.accept()

    def add_new_launcher(self):
        app_data = ApplicationData()
        settings_window = ApplicationSettingsWidget(app_data)

        if settings_window.exec_():
            app_data = settings_window.app_data
            ConfigurationManager.get_configuration().applications_list.append(app_data)
            self.create_apps_list()

    def show_top_window(self):
        if self.top_window is None:
            self.top_window = TopViewWindow()
            self.top_window.closed.connect(self.top_window_closed)
        else:
            self.top_window.focusWidget()

    def top_window_closed(self):
        self.top_window = None