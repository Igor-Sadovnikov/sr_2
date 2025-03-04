import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            '2025-12-01': [105, 54, 57, 288],
            '2034-04-25': [217, 106, 81, 219, 1, 112],
            '2018-03-05': [44, 168, 29],
            '2021-10-05': [13, 3, 17, 248, 21, 138]
        },
        {
            '2013-05-23': [7, 31, 230, 26, 98, 240, 222],
            '2019-11-21': [117, 56, 241, 1],
            '2001-06-02': [67, 223, 204, 71],
            '2018-04-09': [270, 17, 27, 18],
            '2021-10-09': [297, 94, 83, 67]
        }
    ]

    index = 0
    while (index := int(input('Введите номер примера: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
