# coding:utf8
"""request_view.py
リクエスト作成画面のView
"""
import PyQt5.QtWidgets as qt
import model_control
import response_view


class View(qt.QMainWindow):
    """View Class"""

    def __init__(self):
        super().__init__()
        self.initUI()
        self.mainUI()
        # 表示
        self.show()

    def request_button_clicked(self):
        """リクエストボタンが押されたとき、widgetから入力を受け取って、Contralに投げ込む"""
        edit_text_plain = self.text_edit.toPlainText()
        line_edit_plain = self.line_edit.text()
        is_get_response = self.check_get_response_box.isChecked()

        controler = model_control.SendTCPControl()
        response = controler.sendTCP(line_edit_plain, edit_text_plain)

        response_view.View(response)

    def initUI(self):
        """Windowの基本情報のセット"""
        # ステータスバー
        self.statusBar().showMessage('Ready')
        # windowサイズ
        self.setGeometry(1000, 1000, 1000, 1000)
        # タイトル
        self.setWindowTitle('てぃーしーぴーくらいんとちゃん -りくえすと-')

    def mainUI(self):
        """リクエストフォーム"""
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

        # CheckBox
        self.check_get_response_box = qt.QCheckBox('れすぽんすは受け取る？', self)
        layout_box.addWidget(self.check_get_response_box)

        # Button
        send_button = qt.QPushButton('そうしんっ！', self)
        send_button.clicked.connect(self.request_button_clicked)
        layout_box.addWidget(send_button)

        # Layout
        widget.setLayout(layout_box)
        self.setCentralWidget(widget)
