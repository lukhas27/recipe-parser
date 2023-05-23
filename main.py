import sys

from PyQt5.QtWidgets import QApplication

from lib.parser_app import ParserApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ParserApp()
    ex.show()
    sys.exit(app.exec_())