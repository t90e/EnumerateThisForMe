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

class OverviewPage(QWidget):
    domain_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # title
        self.title_label = QLabel("Overview")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.insertWidget(0, self.title_label)

        # add gap
        layout.addSpacing(20)

        # title 
        self.page_label = QLabel("NMAP Scans")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("Discover devices, services, and security flaws on a network")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)

        # title 
        self.page_label = QLabel("Direcory Bruteforce")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("A reconnaissance technique discovering hidden web directories and files by requesting paths from wordlists")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)
        
        # title 
        self.page_label = QLabel("Debug parameters")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("Appending flags like ?debug=1 and feeding malformed input to surface developer output or raw errors left live in production")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)
                
        # title 
        self.page_label = QLabel("All data entry points")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("Mapping every form, URL parameter, and header the app accepts input through")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)
        
        # title 
        self.page_label = QLabel("Map attack surface")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("Crawling the site to find every reachable page, link, and resource worth testing")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)
        
        # title 
        self.page_label = QLabel("Identify javascript files")
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.page_label)
                
        # summary 
        self.summary_label = QLabel("Finding JS files and extracting endpoint paths and parameters")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.summary_label)
        
        # me 
        self.summary_label = QLabel("Made by t90e :)")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setStyleSheet("font-size: 8px;")
        layout.addWidget(self.summary_label)
        