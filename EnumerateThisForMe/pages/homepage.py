import sys, subprocess, threading
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QSizePolicy,
    QCheckBox,
    QButtonGroup,
    QStyle,
    QFrame,
    QStackedWidget,
    QLabel
)

class HomePage(QWidget):
    domain_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # title
        self.title_label = QLabel("Home Page")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.insertWidget(0, self.title_label)
        layout.addStretch(1)

        # add gap
        layout.addSpacing(20)

        # target input 
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("input target URL")
        self.input_field.setFixedSize(350, 36)

        input_row = QHBoxLayout()
        input_row.addStretch()
        input_row.addWidget(self.input_field)
        input_row.addStretch()
        
        self.input_label = QLabel("Enter the target URL to enumerate")
        self.input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.input_label)

        layout.addLayout(input_row)

        # submit domain
        self.submit_button = QPushButton("submit")
        self.submit_button.setFixedSize(240, 24)
        self.submit_button.clicked.connect(self.on_run_clicked)
        
        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(self.submit_button)
        button_row.addStretch()

        layout.addLayout(button_row)
        layout.addStretch(1)

    def on_run_clicked(self):
        domain = self.input_field.text().strip()

        if not domain:
            return
        self.domain_submitted.emit(domain)


