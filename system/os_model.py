"""os_model.py
他プロセス関連やファイルの保存等に用いる
"""
import threading
import subprocess
import configparser


class FileModel():
    """ファイルに関するクラスの作成"""
    def write(fname, resonse):
        """ファイルの保存"""
        if fname[0]:
                # open
                file_ = open(fname[0], "w")
                # write
                file_.write(resonse)
                # close
                file_.close()


class OpenBrowser(threading.Thread):
    """ブラウザでパケットを開く"""
    def __init__(self):
        super(OpenBrowser, self).__init__()

    def check_browser(self):
        """ブラウザがどれか設定ファイルから読み込む"""
        inifile = configparser.SafeConfigParser()
        inifile.read('./system/config.ini')
        self.browser = inifile.get('General', 'browser')

    def run(self, file_path):
        subprocess.Popen([self.browser + ' ' + file_path], shell=True)
