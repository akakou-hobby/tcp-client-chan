# coding:utf8
"""main_view.py
メイン画面のView
"""
import PyQt5.QtWidgets as qt


class View(qt.QMainWindow):
    """View Class."""

    def __init__(self):
        super().__init__()
        self.initUI()
        self.mainUI()
        # 表示
        self.show()

    def send_request(self):
        print("hello")

    def initUI(self):
        """Windowの基本情報のセット"""
        # ステータスバー
        self.statusBar().showMessage('Ready')
        # windowサイズ
        self.setGeometry(1000, 1000, 1000, 1000)
        # タイトル
        self.setWindowTitle('てぃーしーぴーくらいんとちゃん')

    def mainUI(self):
        """リクエストフォーム"""
        # Widget
        self.widget = qt.QWidget()

        # Layout
        layout_box = qt.QVBoxLayout()

        # URL Label
        url_label = qt.QLabel("ゆーあーるえる")
        layout_box.addWidget(url_label)

        # LineEdit
        self.textbox = qt.QLineEdit(self)
        layout_box.addWidget(self.textbox)

        # Request Label
        request_label = qt.QLabel("りくえすと")
        layout_box.addWidget(request_label)

        # EditText
        self.text_edit = qt.QTextEdit(self)
        layout_box.addWidget(self.text_edit)

        # CheckBox
        self.is_get_response = qt.QCheckBox('れすぽんすは受け取る？', self)
        layout_box.addWidget(self.is_get_response)

        # Button
        send_button = qt.QPushButton('そうしんっ！', self)
        send_button.clicked.connect(self.send_request)
        layout_box.addWidget(send_button)

        # Layout
        self.widget.setLayout(layout_box)
        self.setCentralWidget(self.widget)
