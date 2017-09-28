
''' page/request/control.py
イベントがあった時にこっちに飛ばされる。

'''
import os
import configparser
from lib.http_client import http_client

class Event():
    def __init__(self, view):
        '''Viewのインスタンスを取ってくる'''
        self.view = view

    def button_clicked(self):
        '''リクエストボタンが押されたとき'''
        ### 各UIの持ってる値を持ってくる
        edit_text_plain = self.view.text_edit.toPlainText()
        line_edit_plain = self.view.line_edit.text()

        ### レスポンス作成
        line_text_split = line_edit_plain.split(':')
        request = {
            'host': line_text_split[0],
            'port': int(line_text_split[1]),
            'header': edit_text_plain,
            'encode': 'utf-8'
        }

        ### 通信
        client = http_client.LowLayerHTTPClient(request=request)
        client.connect()
        client.send()
        response = client.get_response()
        client.close()

        print(client.response['all'])

        ### 設定ファイルの読み込み
        inifile = configparser.SafeConfigParser()
        inifile.read('config.ini')
        editor = inifile.get('General', 'text_editer')
        count = inifile.get('General', 'count')
        count = int(count)
        count += 1
        inifile.set('General', 'count', str(count))

        ### ファイル保存
        f = open(str(count) + '.html', 'w')
        f.write(client.response['all'])
        f.close()


        ### メモ帳の起動
        os.system(editor + ' ' + str(count) + '.html')

        ### 終了
        exit()
