from PySide6.QtWidgets import QApplication
from login_window import loginWindow

if __name__ == "__main__":
    app = QApplication([])
    window = loginWindow()
    window.show()
    app.exec()

