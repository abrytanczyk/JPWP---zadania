from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QFileDialog, QDialogButtonBox, QLabel, \
    QHBoxLayout

from app.model.ApplicationData import ApplicationData
from pathlib import Path

from app.view.StringListEditorWidget import StringListEditorWidget


class ApplicationSettingsWidget(QDialog):
    def __init__(self, app_data: ApplicationData):
        super().__init__()

        self.app_data = app_data
        self.initUI(app_data)

    def initUI(self, app_data):
        self.setWindowTitle(QtWidgets.QApplication.instance().applicationName() + ' - ' + app_data.name +' - Settings')

        layout = QFormLayout()
        self.setLayout(layout)

        self.name_field_edit = QLineEdit()
        self.name_field_edit.setText(app_data.name)

        self.description_field_edit = QLineEdit()
        self.description_field_edit.setText(app_data.description)

        self.path_field_edit = QLineEdit()
        self.path_field_edit.setText(str(app_data.path))
        path_button = QPushButton()
        path_button.setIcon(QIcon('icons/folder.png'))
        path_button.pressed.connect(self.showFilePath)

        path_hbox = QHBoxLayout()
        path_hbox.addWidget(self.path_field_edit)
        path_hbox.addWidget(path_button)

        self.work_dir_field_edit = QLineEdit()
        self.work_dir_field_edit.setText(str(app_data.work_dir))
        work_dir_butt = QPushButton()
        work_dir_butt.setIcon(QIcon('icons/folder.png'))
        work_dir_butt.pressed.connect(self.showWorkDirPath)

        work_dir_hbox = QHBoxLayout()
        work_dir_hbox.addWidget(self.work_dir_field_edit)
        work_dir_hbox.addWidget(work_dir_butt)

        button_box = QDialogButtonBox(QDialogButtonBox.Apply | QDialogButtonBox.Cancel)
        button_box.button(QDialogButtonBox.Apply).clicked.connect(self.get_data_and_accept)
        button_box.rejected.connect(self.reject)

        layout.addRow(QLabel("Name:"), self.name_field_edit)
        layout.addRow(QLabel("Description:"), self.description_field_edit)
        layout.addRow(QLabel('Application path:'), path_hbox)
        layout.addRow(QLabel('Application working directory:'), work_dir_hbox)
        layout.addRow(QLabel('Arguments:'), StringListEditorWidget(self.app_data.arguments, self))
        layout.addWidget(button_box)

    def showFilePath(self):

        file_path = QFileDialog.getOpenFileName(self, 'Open file', str(Path.home()))

        if file_path[0]:
            self.path_field_edit.setText(file_path[0])

    def showWorkDirPath(self):

        work_dir_path = QFileDialog.getExistingDirectory(self, 'Open directory', self.work_dir_field_edit.text())

        if work_dir_path[0]:
            self.work_dir_field_edit.setText(work_dir_path[0])

    def get_data_and_accept(self):
        self.app_data.name = self.name_field_edit.text()
        self.app_data.description = self.description_field_edit.text()
        self.app_data.path = Path(self.path_field_edit.text())
        self.app_data.work_dir = Path(self.work_dir_field_edit.text())

        self.accept()
