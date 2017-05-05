# coding:utf8
"""main_view.py
メイン画面のView
"""
from PyQt5.QtWidgets import QMainWindow


class View(QMainWindow):
    """View Class."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ステータスバー
        self.statusBar().showMessage('Ready')
        # windowサイズ
        self.setGeometry(1000, 1000, 1000, 1000)
        # タイトル
        self.setWindowTitle('てぃーしーぴーくらいんとちゃん')
        # 表示
        self.show()
