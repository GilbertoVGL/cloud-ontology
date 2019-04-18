import pymongo
from sshtunnel import SSHTunnelForwarder
import pprint


class MongoConnection:

    _connection = None
    _server = None
    _db = None

    def __init__(self, host: str, username: str, password: str, db: str):
        self._db = db
        self._server = SSHTunnelForwarder(
            host,
            ssh_username=username,
            ssh_password=password,
            remote_bind_address=('127.0.0.1', 27017)
        )

    def __enter__(self):
        self._server.start()

        client = pymongo.MongoClient('127.0.0.1', self._server.local_bind_port)
        # server.local_bind_port is assigned local

        self._connection = client[self._db]
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._server.stop()
