from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QListWidget, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class IntroPage(QWidget):
    def __init__(self, next_callback, cancel_callback):
        super().__init__()

        self.setWindowTitle("Simulation Configuration Wizard")
        self.resize(1000, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f8fa;
                font-family: 'Segoe UI';
                color: #2c2c2c;
            }
            QListWidget {
                background-color: #eef1f6;
                border-right: 1px solid #cfd4da;
                font-size: 14px;
                font-weight: 500;
            }
            QListWidget::item {
                padding: 8px 10px;
                border: none;
            }
            QListWidget::item:selected {
                background-color: #e0e7f9;
                color: #1a3d8f;
                font-weight: bold;
            }
            QLabel {
                font-size: 14px;
            }
            QPushButton {
                border: none;
                border-radius: 6px;
                padding: 8px 18px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton#next {
                background-color: #1a73e8;
                color: white;
            }
            QPushButton#next:hover {
                background-color: #155cc1;
            }
            QPushButton#cancel {
                background-color: #e5e5e5;
                color: #333;
            }
            QPushButton#cancel:hover {
                background-color: #dcdcdc;
            }
            QPushButton#closeWizard {
                background-color: #f0f0f0;
                color: #444;
                font-weight: 500;
            }
            QFrame#content_frame {
                background-color: white;
                border: 1px solid #d0d0d0;
                border-radius: 6px;
                padding: 30px;
            }
        """)

        # === Main Layout (Sidebar + Content) ===
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # === Sidebar ===
        sidebar = QListWidget()
        sidebar.setFixedWidth(200)
        sidebar.addItems([
            "Introduction",
            "Compounds",
            "Property Packages",
            "System of Units",
            "Behavior",
            "Undo/Redo"
        ])
        sidebar.setCurrentRow(0)
        main_layout.addWidget(sidebar)

        # === Content Frame ===
        content_frame = QFrame()
        content_frame.setObjectName("content_frame")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setSpacing(15)

        title = QLabel("<h2>Introduction</h2>")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        content_layout.addWidget(title)

        message = QLabel(
            "Welcome to the simulation configuration wizard.<br><br>"
            "In the next pages you will be able to add <b>compounds</b>, "
            "select <b>property packages</b>, set the <b>system of units</b>, "
            "and configure specific parameters for a new simulation.<br><br>"
            "Click <b>Next</b> to continue or <b>Cancel</b> to exit."
        )
        message.setWordWrap(True)
        message.setFont(QFont("Segoe UI", 12))
        content_layout.addWidget(message)
        content_layout.addStretch()

        # === Bottom Button Row ===
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignRight)

        btn_close = QPushButton("Close Wizard and go to the Simulation Configuration Window")
        btn_close.setObjectName("closeWizard")
        btn_close.clicked.connect(lambda: QMessageBox.information(
            self, "Close Wizard", "Returning to Simulation Configuration Window..."))
        btn_layout.addWidget(btn_close)
        btn_layout.addStretch()

        btn_cancel = QPushButton("Cancel")
        btn_cancel.setObjectName("cancel")
        btn_cancel.clicked.connect(cancel_callback)

        btn_next = QPushButton("Next >")
        btn_next.setObjectName("next")
        btn_next.clicked.connect(next_callback)

        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_next)
        content_layout.addLayout(btn_layout)

        main_layout.addWidget(content_frame)
        self.setLayout(main_layout)


# ==== Standalone Test Run ====
def launch_intro():
    app = QApplication(sys.argv)  # ✅ define app locally

    def on_next():
        QMessageBox.information(None, "Next", "Compound Selector Page should open here!")

    def on_cancel():
        QMessageBox.warning(None, "Exit", "Wizard cancelled by user.")
        app.quit()

    intro = IntroPage(on_next, on_cancel)
    intro.show()
    sys.exit(app.exec_())

