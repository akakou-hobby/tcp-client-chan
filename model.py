# coding:utf-8
"""model.py
TCP送信＆受け取りを行う
"""
import socket


def sendTCP(host, port, request):
    response = ""
    # set
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    client.connect((host, port))
    # send
    client.send(request.encode('utf-8'))
    # get
    while True:
        recv = client.recv(4096)
        response += recv
        if recv == "":
            break

    return response.decode('utf-8')
