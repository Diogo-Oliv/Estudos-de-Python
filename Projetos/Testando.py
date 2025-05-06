import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criador de Arquivos")
        self.setGeometry(2500, 350, 500, 500)

        # Criação da label que mostrará o Cabeçalho do programa.
        labelHeader = QLabel("Programa para criação de arquivos", self)
        labelHeader.setFont(QFont("Arial", 15))
        labelHeader.setGeometry(0,0, 500, 100)
        labelHeader.setStyleSheet("background-color: gray;"
                                  "font-weight: bold;"
                                  "text-decorantion: underline;")
        labelHeader.setAlignment(Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()