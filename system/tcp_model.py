# coding:utf-8
"""model.py
TCP送信＆受け取りを行う
"""
import socket


def sendTCP(host, port, request):
    response = ""
    # set
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    # connect
    client.connect((host, port))
    # send
    client.send(request.encode('utf-8'))
    # get
    while True:
        try:
            recv = client.recv(1024)
            response += recv.decode('utf-8')

        except socket.timeout:
            break
    # close
    client.close()

    # return
    return response
