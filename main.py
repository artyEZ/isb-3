import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QApplication, QFileDialog, QMessageBox


class CryptoSystemGUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.are_settings_loaded = False
        self.setWindowTitle('Task')
        self.setGeometry(100, 100, 600, 300)  
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.settings_file_label = QLabel('Settings file:', self.central_widget)
        self.settings_file_label.setGeometry(50, 50, 150, 30)  
        self.load_settings_file_button = QPushButton('Load', self.central_widget)
        self.load_settings_file_button.setGeometry(200, 50, 100, 30)  
        # self.load_settings_file_button.clicked.connect(self.init_settings)
        
        self.key_length_label = QLabel('Length key (in bits):', self.central_widget)
        self.key_length_label.setGeometry(50, 100, 150, 30)  
        self.key_length_input = QLineEdit(self.central_widget)
        self.key_length_input.setGeometry(200, 100, 100, 30)  
        self.load_keys_file_button = QPushButton('Load', self.central_widget)
        self.load_keys_file_button.setGeometry(310, 100, 100, 30)  
        # self.load_keys_file_button.clicked.connect(self.generate_keys)
        
        self.encrypt_button = QPushButton('Encrypt', self.central_widget)
        self.encrypt_button.setGeometry(50, 150, 100, 30)  
        # self.encrypt_button.clicked.connect(self.encrypt_text)
        
        self.decrypt_button = QPushButton('Decrypt', self.central_widget)
        self.decrypt_button.setGeometry(160, 150, 100, 30)  
        # self.decrypt_button.clicked.connect(self.decrypt_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CryptoSystemGUI()
    win.show()
    sys.exit(app.exec_())        
