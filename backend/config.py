import os

LOCALHOST = '127.0.0.1'


class BaseConfig:

    def __init__(self, host=LOCALHOST, port=5000):
        self.HOST = host
        self.PORT = port

