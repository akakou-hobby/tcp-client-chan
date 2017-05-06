# coding: utf-8
"""てぃーしーぴのくらいんとちゃん
TCPを投げつけるのが得意なフレンズのプログラム
"""
from PyQt5.QtWidgets import QApplication
import request_view
import sys


def main():
    """Viewの呼び出し"""
    app = QApplication(sys.argv)
    request_view_ = request_view.View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
