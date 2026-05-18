# About_page.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette, QLinearGradient, QBrush
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
import os


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()

        # 🌈 Background gradient
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1080)
        gradient.setColorAt(0.0, QColor("#1e3c72"))
        gradient.setColorAt(1.0, QColor("#2a5298"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 🌟 Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setContentsMargins(100, 60, 100, 60)
        self.setLayout(main_layout)

        # 🧊 Content card (glass effect)
        content_card = QWidget()
        content_card.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 20px;
            }
        """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 0, 0, 120))
        shadow.setOffset(0, 8)
        content_card.setGraphicsEffect(shadow)

        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setContentsMargins(80, 60, 80, 60)
        content_layout.setSpacing(25)
        content_card.setLayout(content_layout)
        main_layout.addWidget(content_card)

        # 🧪 Logo
        logo_label = QLabel()
        logo_path = r"C:\Users\koyan\Chemical-Simulator-GUI\src\main\resources\base\icons\logoo.png"
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(logo_label)

        # 🏷️ Title
        title = QLabel("Chemical Simulator GUI")
        title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #1e3c72; letter-spacing: 1px;")
        content_layout.addWidget(title)

        # 🌿 Description
        desc = QLabel(
            "An open-source chemical process simulator designed for learning, "
            "research, and experimentation in chemical engineering."
        )
        desc.setFont(QFont("Segoe UI", 18))
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #333333;")
        desc.setWordWrap(True)
        content_layout.addWidget(desc)

        # Separator
        line = self.create_separator()
        content_layout.addWidget(line)

        # ⚙️ Features section
        features_label = QLabel("""
            <b style="font-size:20px; color:#1e3c72;">Key Features</b><br><br>
            <ul style="font-size:16px; color:#333333; line-height:1.8;">
                <li>Simulate unit operations like Heaters, Mixers, Flash, Distillation Columns</li>
                <li>Interactive input and output visualization</li>
                <li>Multi-language support</li>
                <li>Export simulation results to Excel and PDF</li>
                <li>Open-source and easy to extend</li>
            </ul>
        """)
        features_label.setTextFormat(Qt.RichText)
        features_label.setAlignment(Qt.AlignLeft)
        features_label.setWordWrap(True)
        content_layout.addWidget(features_label)

        # Separator
        content_layout.addWidget(self.create_separator())

        # 🧑‍💻 Developer Info
        dev_label = QLabel("""
            <b style="color:#1e3c72;">Developed by:</b> FOSSEE, IIT Bombay<br>
            <b>Version:</b> 1.0 &nbsp; | &nbsp; <b>License:</b> MIT<br><br>
            <a href='https://github.com/FOSSEE/Chemical-Simulator-GUI' style='color:#2a5298; text-decoration:none;'>
                🔗 GitHub Repository
            </a>
        """)
        dev_label.setFont(QFont("Segoe UI", 16))
        dev_label.setAlignment(Qt.AlignCenter)
        dev_label.setTextFormat(Qt.RichText)
        dev_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        dev_label.setOpenExternalLinks(True)
        dev_label.setStyleSheet("""
            QLabel:hover { color: #1e3c72; }
        """)
        content_layout.addWidget(dev_label)

        # Separator
        content_layout.addWidget(self.create_separator())

        # 🕊️ Footer
        footer = QLabel("© 2025 FOSSEE, IIT Bombay  •  All Rights Reserved")
        footer.setFont(QFont("Segoe UI", 14))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #555555; margin-top: 10px;")
        content_layout.addWidget(footer)

        # 🌸 Fade-in animation
        self.fade_in_animation()

    # 🔹 Helper for creating separators
    def create_separator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #cccccc;")
        return line

    # 🔹 Fade-in animation for smooth entry
    def fade_in_animation(self):
        self.setWindowOpacity(0)
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(1200)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.start()
