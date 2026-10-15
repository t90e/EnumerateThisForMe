import sys, subprocess, threading
from PySide6.QtCore import Signal
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
    QButtonGroup
)


class MainWindow(QMainWindow):
    output_ready = Signal(str)
    def __init__(self):
        super().__init__()
        # title and window size
        self.setWindowTitle("EnumerateItForMe")
        self.resize(1200, 800)


        central = QWidget()
        self.setCentralWidget(central)

        # main layout
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 10, 12, 12)
        layout.setSpacing(8)

        # title
        self.read_only_field = QLineEdit()
        self.read_only_field.setReadOnly(True)
        self.read_only_field.setPlaceholderText("Nmap scans")
        self.read_only_field.setFixedSize(270, 40)

        top_row = QHBoxLayout()
        top_row.addStretch()
        top_row.addWidget(self.read_only_field)
        top_row.addStretch()

        layout.addLayout(top_row)

        # add gap
        layout.addSpacing(50)

        # target input 
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("input target URL")
        self.input_field.setFixedSize(350, 36)

        input_row = QHBoxLayout()
        input_row.addStretch()
        input_row.addWidget(self.input_field)
        input_row.addStretch()

        # header and full scan buttons
        self.full_scan_checkbox = QCheckBox("Full scan")
        self.http_headers_checkbox = QCheckBox("HTTP headers")

        self.scan_group = QButtonGroup(self)
        self.scan_group.setExclusive(True)

        self.scan_group.addButton(self.full_scan_checkbox)
        self.scan_group.addButton(self.http_headers_checkbox)
        # add the buttons
        layout.addWidget(self.full_scan_checkbox)
        layout.addWidget(self.http_headers_checkbox)
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
        self.output_box.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
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
        fullscan = str(self.full_scan_checkbox.isChecked())
        headers = str(self.http_headers_checkbox.isChecked())

        # pass domain and options to dedicated nmap worker thread, then signalling changes from thread

        def scan_and_display(domain, fullscan, headers):
            module1 = subprocess.run([sys.executable, 'module1.py', domain, fullscan, headers], capture_output=True, text=True)
            self.output_ready.emit(module1.stdout or module1.stderr)

        #start worker thread
        t = threading.Thread(target=scan_and_display, args = (domain, fullscan, headers))
        t.start()


        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()