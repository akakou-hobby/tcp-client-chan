# coding:utf8
"""response_view.py
レスポンス閲覧画面のView
"""
import PyQt5.QtWidgets as qt


class View(qt.QWidget):
    """View Class"""

    def __init__(self, response_text, parent=None):
        self.window = qt.QDialog(parent)

        self.response_text = response_text

        super().__init__()
        self.initUI()
        self.mainUI()
        self.window.exec_()

    def save_file(self):
        """ファイルへ保存する"""
        pass

    def browse_chromium(self):
        """Chromium経由でファイルを見る"""
        pass

    def initUI(self):
        """Windowの基本情報のセット"""
        # windowサイズ
        self.setGeometry(1000, 1000, 1000, 1000)
        # タイトル
        self.setWindowTitle('てぃーしーぴーくらいんとちゃん -れすぽんす-')

    def mainUI(self):
        """レスポンス閲覧画面"""
        # Layout
        layout_box = qt.QVBoxLayout()

        # Request Label
        request_label = qt.QLabel("れすぽんす")
        layout_box.addWidget(request_label)

        # EditText
        self.text_edit = qt.QTextEdit(self)
        self.text_edit.setText(self.response_text)
        layout_box.addWidget(self.text_edit)

        # Button
        save_button = qt.QPushButton('ほぞん', self)
        save_button.clicked.connect(self.save_file)
        layout_box.addWidget(save_button)

        # Button
        chromium_button = qt.QPushButton('ほぞんしてくろみあむでみる', self)
        chromium_button.clicked.connect(self.browse_chromium)
        layout_box.addWidget(chromium_button)

        # Layout
        self.window.setLayout(layout_box)
