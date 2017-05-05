# coding: utf-8
"""てぃーしーぴのくらいんとちゃん
TCPを投げつけるのが得意なフレンズのプログラム
"""
import sys
import view

from PyQt5.QtWidgets import QApplication


def main():
    """Viewの呼び出し"""
    app = QApplication(sys.argv)
    view_ = view.View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
