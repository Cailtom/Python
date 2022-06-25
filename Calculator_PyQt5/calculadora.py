import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora PyQT5')
        self.setFixedSize(290, 330)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #fff; color: #333; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Botões da tela
        self.adicionar_botao(QPushButton('7'), 1, 0, 1, 1)
        self.adicionar_botao(QPushButton('8'), 1, 1, 1, 1)
        self.adicionar_botao(QPushButton('9'), 1, 2, 1, 1)
        self.adicionar_botao(QPushButton('+'), 1, 3, 1, 1)
        self.adicionar_botao(
            QPushButton('C'), 1, 4, 1, 1, 
            lambda: self.display.setText(''),
            'background: #d5580d; color: #fff;'
        )

        self.adicionar_botao(QPushButton('4'), 2, 0, 1, 1)
        self.adicionar_botao(QPushButton('5'), 2, 1, 1, 1)
        self.adicionar_botao(QPushButton('6'), 2, 2, 1, 1)
        self.adicionar_botao(QPushButton('-'), 2, 3, 1, 1)
        self.adicionar_botao(
            QPushButton('⬅'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'font-size: 10px;'
        )

        self.adicionar_botao(QPushButton('1'), 3, 0, 1, 1)
        self.adicionar_botao(QPushButton('2'), 3, 1, 1, 1)
        self.adicionar_botao(QPushButton('3'), 3, 2, 1, 1)
        self.adicionar_botao(QPushButton('/'), 3, 3, 1, 1)
        self.adicionar_botao(
            QPushButton('='), 3, 4, 2, 1, 
            self.botao_igualdade,
            'background: #228B22'
        )

        self.adicionar_botao(QPushButton('.'), 4, 0, 1, 1)
        self.adicionar_botao(QPushButton('0'), 4, 1, 1, 1)
        self.adicionar_botao(QPushButton('//'), 4, 2, 1, 1)
        self.adicionar_botao(QPushButton('*'), 4, 3, 1, 1)

        self.setCentralWidget(self.cw)

    def adicionar_botao(self, btn, row, col, rowspan, colspan, digito=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        btn.setStyleSheet(
            'font-weight: 700;'
        )

        if not digito:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(digito)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def botao_igualdade(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText(
                'Conta Inválida.'
            )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
