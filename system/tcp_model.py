# coding:utf-8
"""tcp_model.py
TCP送信＆受け取りを行う
"""
import socket


class TCPModel():
    """TCP通信のモデル"""
    def __init__(self, host, port, request):
        """TCPの接続と送信"""
        # set
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1)
        # connect
        self.client.connect((host, port))
        # send
        self.client.send(request.encode('utf-8'))

    def get_response(self):
        """TCPレスポンスの受け取り"""
        response = ""
        # get
        while True:
            try:
                recv = self.client.recv(1024)
                response += recv.decode('utf-8')

            except socket.timeout:
                break
        # return
        return response
