
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from window_ui import Ui_MainWindow


from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


def main():

    app = QApplication([])
    window = MainWindow()
    window.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    app.exec()    
    # ui_file_name = "main.ui"
    # app = QApplication([])

    # ui_file = QFile(ui_file_name)
    # loader = QUiLoader()
    # window = loader.load(ui_file)
    # ui_file.close()

    # window.show()
    app.exec()

if __name__ == '__main__':
    main()