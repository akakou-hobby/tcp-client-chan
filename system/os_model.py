"""os_model.py
他プロセス関連やファイルの保存等に用いる
"""
import threading
import subprocess


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


class OpenCromium(threading.Thread):
    """chromiumでパケットを開く"""
    def __init__(self):
        super(OpenCromium, self).__init__()

    def run(self, file_path):
        subprocess.Popen(["chromium " + file_path], shell=True)
