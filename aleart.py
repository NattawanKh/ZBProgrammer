from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject ,Qt
from PyQt5.QtGui import QFont

class CustomAlertDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Notification")
        
        # Set fixed size for the dialog
        self.setFixedSize(300, 300)  # Adjust as needed

        # Set a larger font for the message
        font = QFont()
        font.setPointSize(15)

        # Create a label and set the message text
        label = QLabel(message)
        label.setFont(font)
        label.setWordWrap(True)

        # Create a button to close the dialog
        close_button = QPushButton("OK")
        close_button.clicked.connect(self.accept)

        # Conditionally apply background color
        if message.startswith("Process Finish") :
            label.setStyleSheet("background-color: green; color: white; font-size:30px")
            label.setAlignment(Qt.AlignCenter)
            close_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;  /* Green background */
                    color: white;  /* White text */
                    font-size: 26px;  /* Font size */
                    padding: 10px 20px;  /* Padding */
                    border-radius: 10px;  /* Rounded corners */
                }
                QPushButton:hover {
                    background-color: #45a049;  /* Darker green on hover */
                }
            """)
        elif message.startswith("Please Select Devices Type") :
            label.setStyleSheet("background-color: red; color: white; font-size:30px")
            label.setAlignment(Qt.AlignCenter)
            close_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;  /* Green background */
                    color: white;  /* White text */
                    font-size: 26px;  /* Font size */
                    padding: 10px 20px;  /* Padding */
                    border-radius: 10px;  /* Rounded corners */
                }
                QPushButton:hover {
                    background-color: #d32f2f;  /* Darker green on hover */
                }
            """)
        else :
            label.setStyleSheet("background-color: #FFBF00; font-size: 30px; color: white;")
            label.setAlignment(Qt.AlignCenter)
            close_button.setStyleSheet("""
                QPushButton {
                    background-color: #f86f15;  /* Green background */
                    color: white;  /* White text */
                    font-size: 26px;  /* Font size */
                    padding: 10px 20px;  /* Padding */
                    border-radius: 10px;  /* Rounded corners */
                }
                QPushButton:hover {
                    background-color: #fbee0f;  /* Darker green on hover */
                }
            """)
        # Set a stylesheet for the button

        # Arrange widgets in a layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(close_button)
        self.setLayout(layout)

class AlertHelper(QObject):
    show_alert_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def show_alert(self, message):
        # Use custom dialog instead of QMessageBox
        dialog = CustomAlertDialog(message)
        dialog.exec_()

alert_helper = AlertHelper()
alert_helper.show_alert_signal.connect(alert_helper.show_alert)