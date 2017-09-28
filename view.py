# coding:utf8
"""request_view.py
リクエスト作成画面のView
"""
import PyQt5.QtWidgets as qt
import os, sys

import event


class View(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.event = event.Event(self)
        self.setWindow()
        self.setUI()

        self.show()

    def setWindow(self):
        '''ウィンドウ等の設定'''
        # ステータスバー
        self.statusBar().showMessage('Ready')

        # windowサイズ
        self.setGeometry(1000, 1000, 1000, 1000)

        # タイトル
        self.setWindowTitle('てぃーしーぴーくらいんとちゃん -りくえすと-')


    def setUI(self):
        '''UIの設定'''
        # Widget
        widget = qt.QWidget()

        # Layout
        layout_box = qt.QVBoxLayout()

        # URL Label
        url_label = qt.QLabel("ほすと：ぽーと")
        layout_box.addWidget(url_label)

        # LineEdit
        self.line_edit = qt.QLineEdit(self)
        layout_box.addWidget(self.line_edit)

        # Request Label
        request_label = qt.QLabel("りくえすと")
        layout_box.addWidget(request_label)

        # EditText
        self.text_edit = qt.QTextEdit(self)
        layout_box.addWidget(self.text_edit)

        # Button
        send_button = qt.QPushButton('そうしんっ！', self)
        send_button.clicked.connect(self.event.button_clicked)
        layout_box.addWidget(send_button)

        # Layout
        widget.setLayout(layout_box)
        self.setCentralWidget(widget)
