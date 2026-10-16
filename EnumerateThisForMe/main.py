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

from pages.homepage import HomePage
from pages.overviewpage import OverviewPage
from pages.nmappage import NmapPage
from pages.bruteforcepage import BruteforcePage
from pages.debugpage import DebugPage

class SideBarBase(QWidget):
    page_requested = Signal(int) 
    def __init__(self, parent = None):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.Shape.Box)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(3)
        self.layout.addWidget(self.frame)

        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)       

class SideBarCollapsed(SideBarBase):
    def __init__(self, parent = None):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.button = QPushButton()

        #add icon
        self.button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogOkButton))
        self.frame_layout.addWidget(self.button)
        self.frame_layout.addStretch(1)

class SideBarExpanded(SideBarBase):
    def __init__(self, parent = None):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.home_button = QPushButton("Home")
        #set icon for the home button
        self.home_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogOkButton))
        self.home_button.clicked.connect(lambda: self.page_requested.emit(0))
        self.frame_layout.addWidget(self.home_button)
        
        self.overview_button = QPushButton("Overview")
        self.overview_button.clicked.connect(lambda: self.page_requested.emit(1))
        self.frame_layout.addWidget(self.overview_button)
        self.frame_layout.addStretch(1)

        self.nmap_button = QPushButton("Nmap")
        self.nmap_button.clicked.connect(lambda: self.page_requested.emit(2))
        self.frame_layout.addWidget(self.nmap_button)
        self.frame_layout.addStretch(1)

        self.bruteforce_button = QPushButton("Bruteforce Dir")
        self.bruteforce_button.clicked.connect(lambda: self.page_requested.emit(3))
        self.frame_layout.addWidget(self.bruteforce_button)
        self.frame_layout.addStretch(1)

        self.debug_button = QPushButton("Debug")
        self.debug_button.clicked.connect(lambda: self.page_requested.emit(4))
        self.frame_layout.addWidget(self.debug_button)
        self.frame_layout.addStretch(1)

class MainWindow(QMainWindow):

    output_ready = Signal(str)

    def __init__(self):
        super().__init__()
        # title and window size
        self.setWindowTitle("EnumerateItForMe")
        self.resize(1200, 800)

        self.layouts = {}

        central = QWidget()
        self.setCentralWidget(central)
             
        # menu label
        self.menu_label = QLabel("Menu")
        self.menu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_label.setStyleSheet("font-size: 16px;")

        # layouts setup, main window, submain for sidebar and content being side by side, everything else inside content window on right side..
        self.layouts['main'] = QVBoxLayout(central)
        self.layouts['main'].setContentsMargins(12, 10, 12, 12)
        self.layouts['main'].setSpacing(8)

        self.layouts['submain'] = QHBoxLayout()
        self.layouts['main'].addLayout(self.layouts['submain'])

        self.layouts['sidebar_column'] = QVBoxLayout()
        self.layouts['sidebar_column'].setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layouts['submain'].addLayout(self.layouts['sidebar_column'])

        self.layouts['sidebar_column'].insertWidget(0, self.menu_label)

        self.pages = QStackedWidget()
        self.layouts['submain'].addWidget(self.pages)

        self.home_page = HomePage()
        self.overview_page = OverviewPage()
        self.nmap_page = NmapPage()
        self.bruteforce_page = BruteforcePage()
        self.debug_page = DebugPage()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.overview_page)
        self.pages.addWidget(self.nmap_page)
        self.pages.addWidget(self.bruteforce_page)
        self.pages.addWidget(self.debug_page)


        # automatically fill domain
        self.home_page.domain_submitted.connect(self.nmap_page.input_field.setText)
        self.home_page.domain_submitted.connect(self.bruteforce_page.input_field.setText)
        self.home_page.domain_submitted.connect(self.debug_page.input_field.setText)

        self.init_ui()

    def init_ui(self):
        self.sidebar_expanded = SideBarExpanded()
        self.layouts['sidebar_column'].addWidget(self.sidebar_expanded)

        self.config_sidebar()

        self.sidebar_expanded.page_requested.connect(self.pages.setCurrentIndex)

    def config_sidebar(self):
        self.sidebar_expanded.setFixedWidth(150)
        self.sidebar_expanded.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()