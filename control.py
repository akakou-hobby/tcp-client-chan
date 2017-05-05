# coding:utf-8
"""control.py
コントロール
"""
import model
import collections


class SendTCPControl:
    """TCP送信コントロール"""
    def sendTCP(self, url, request):
        """メインメソッド:送信"""
        host_port = self.divide_url(url)
        model.sendTCP(host_port["host"], host_port["port"], request)

    def divide_url(self, url):
        """ポートとURLを分ける"""
        result = {
            "host": url,
            "port": 80
        }

        # コロンの数を探す
        char_list = collections.Counter(url)
        if char_list[":"] == 1:
            # => http://hogehogee:8000/spam/piyo
            general_divide = url.split(":")
            # => http://hogehogee
            #    8000/spam/piyo
            question_righter = general_divide[1].split("/")
            # => http://hogehogee
            #    8000
            #    spam
            #    piyo

            # ポート情報の含まれていないhost名を出す
            result["host"] = general_divide[0]
            count = 0
            for var in question_righter:
                if count != 0:
                    result["host"] += "/" + question_righter[1]
                count += 1
            # => https://hogehogee/spam/piyo
            #    8000

            # ポートの代入
            result["port"] = int(question_righter[0])

        return result
