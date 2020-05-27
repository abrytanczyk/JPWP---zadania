from typing import List

from PyQt5.QtGui import QIcon, QPixmap, QTransform
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout, QPushButton, QInputDialog, \
    QLineEdit, QMessageBox


# Bazowane na: https://doc.qt.io/archives/qq/qq11-stringlistedit.html
class StringListEditorWidget(QWidget):
    def __init__(self, string_list: List[str], parent=None):
        super().__init__(parent)

        self.string_list = string_list
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        buttons_layout = QVBoxLayout(self)

        self.list_widget = QListWidget(self)
        self.list_widget.itemSelectionChanged.connect(self.item_selection_changed)

        self.add_btn = QPushButton("", self)
        self.add_btn.setIcon(QIcon('icons/plus.png'))
        self.add_btn.clicked.connect(self.add_clicked)

        self.edit_btn = QPushButton("", self)
        self.edit_btn.setIcon(QIcon('icons/note.png'))
        self.edit_btn.clicked.connect(self.edit_clicked)

        self.remove_btn = QPushButton("", self)
        self.remove_btn.setIcon(QIcon('icons/rubbish.png'))
        self.remove_btn.clicked.connect(self.remove_clicked)

        self.up_btn = QPushButton("", self)
        self.up_btn.setIcon(QIcon('icons/upwards.png'))
        self.up_btn.clicked.connect(self.up_clicked)

        self.down_btn = QPushButton("", self)
        rotation_transform = QTransform()
        rotation_transform.rotate(180)
        self.down_btn.setIcon(QIcon(QPixmap('icons/upwards.png').transformed(rotation_transform)))
        self.down_btn.clicked.connect(self.down_clicked)

        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.edit_btn)
        buttons_layout.addWidget(self.remove_btn)
        buttons_layout.addWidget(self.up_btn)
        buttons_layout.addWidget(self.down_btn)
        buttons_layout.addStretch()

        layout.addWidget(self.list_widget)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        # Insert strings into list
        for item in self.string_list:
            self.list_widget.addItem(QListWidgetItem(item, self.list_widget))

    def update_buttons(self):
        any_items = self.list_widget.count() > 0

        self.edit_btn.setEnabled(any_items)
        self.remove_btn.setEnabled(any_items)

        current_item_idx = self.list_widget.currentRow()

        self.up_btn.setEnabled(any_items and current_item_idx > 0)
        self.down_btn.setEnabled(any_items and current_item_idx < (self.list_widget.count() - 1))

        self.update_list()

    def update_list(self):
        new_arguments = []
        for i in range(self.list_widget.count()):
            new_arguments.append(self.list_widget.item(i).text())

        self.string_list.clear()
        self.string_list.extend(new_arguments)

    def item_selection_changed(self, *args):
        self.update_buttons()

    def add_clicked(self):
        text, okPressed = QInputDialog.getText(self, "Add argument", "Argument:", QLineEdit.Normal, "")

        if okPressed and text != '' and not str.isspace(text):
            self.list_widget.addItem(QListWidgetItem(text, self.list_widget))
            self.list_widget.setCurrentRow(self.list_widget.count() - 1)
            self.list_widget.scrollToItem(self.list_widget.currentItem())

            self.update_buttons()

    def edit_clicked(self):
        current = self.list_widget.currentItem()
        original = current.text()
        if str.isspace(original) or original == '':
            self.add_clicked()
        else:
            text, okPressed = QInputDialog.getText(self, "Edit argument", "Argument:", QLineEdit.Normal, original)

            if okPressed and text != '' and not str.isspace(text):
                current.setText(text)
                self.update_buttons()

    def remove_clicked(self):
        current = self.list_widget.currentItem()
        original = current.text()

        if original == '' or \
            str.isspace(original) or \
            QMessageBox.question(self, "Remove", f"Remove argument: `{original}`",
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.Yes) == QMessageBox.Yes:
            self.list_widget.takeItem(self.list_widget.currentRow())
            self.update_buttons()

    def up_clicked(self):
        current_item_idx = self.list_widget.currentRow()
        if current_item_idx > 0:
            item = self.list_widget.takeItem(current_item_idx)
            self.list_widget.insertItem(current_item_idx - 1, item)
            self.list_widget.setCurrentRow(current_item_idx - 1)
            self.list_widget.scrollToItem(self.list_widget.currentItem())
            self.update_buttons()

    def down_clicked(self):
        current_item_idx = self.list_widget.currentRow()
        if current_item_idx < self.list_widget.count() - 1:
            item = self.list_widget.takeItem(current_item_idx)
            self.list_widget.insertItem(current_item_idx + 1, item)
            self.list_widget.setCurrentRow(current_item_idx + 1)
            self.list_widget.scrollToItem(self.list_widget.currentItem())
            self.update_buttons()
