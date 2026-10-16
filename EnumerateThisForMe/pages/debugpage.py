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

class DebugPage(QWidget):
    output_ready = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # title
        self.title_label = QLabel("Debug paramaters")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.insertWidget(0, self.title_label)

        # add gap
        layout.addSpacing(50)

        # target input 
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("input target URL (demo.testfire.net to test)")
        self.input_field.setFixedSize(350, 36)

        input_row = QHBoxLayout()
        input_row.addStretch()
        input_row.addWidget(self.input_field)
        input_row.addStretch()

        # header and full scan buttons
        self.common_scan_checkbox = QCheckBox("Common scan")
        self.full_scan_checkbox = QCheckBox("Full scan (May take a while)")

        self.scan_group = QButtonGroup(self)
        self.scan_group.setExclusive(True)

        self.scan_group.addButton(self.common_scan_checkbox)
        self.scan_group.addButton(self.full_scan_checkbox)
        # add the buttons

        checkbox_row = QHBoxLayout()
        checkbox_row.addStretch()
        checkbox_row.addWidget(self.common_scan_checkbox)
        checkbox_row.addWidget(self.full_scan_checkbox)
        checkbox_row.addStretch()

        layout.addLayout(checkbox_row)
        layout.addLayout(input_row)

        # Run button
        self.run_button = QPushButton("Run")
        self.run_button.setFixedSize(240, 24)
        self.run_button.clicked.connect(self.on_run_clicked)

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(self.run_button)
        button_row.addStretch()

        layout.addLayout(button_row)

        # output box
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("")

        self.output_box.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)

        # add the box
        layout.addWidget(self.output_box, 1)

        self.output_ready.connect(self.output_box.setPlainText)

    def on_run_clicked(self):
        domain = self.input_field.text().strip()

        # check no input
        if not domain:
            self.output_box.setPlainText("Please enter some input.")
            return
        # code to run
        #check if specific types of scan
        common = str(self.common_scan_checkbox.isChecked())
        extensive = str(self.full_scan_checkbox.isChecked())

        # pass domain and options to dedicated nmap worker thread, then signalling changes from thread

        def scan_and_display(domain, common, extensive):
            module2 = subprocess.run([sys.executable, 'modules/module3.py', domain, common, extensive], capture_output=True, text=True)
            self.output_ready.emit(module2.stdout or module2.stderr)

        #start worker thread
        t = threading.Thread(target=scan_and_display, args = (domain, common, extensive))
        t.start()