# coding: utf-8
"""てぃーしーぴのくらいんとちゃん
TCPを投げつけるのが得意なフレンズのプログラム
"""
import sys
from PyQt5.QtWidgets import QApplication

import view


def main():
    """Viewの呼び出し"""
    app = QApplication(sys.argv)
    _view = view.View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
