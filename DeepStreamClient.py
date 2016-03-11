from Connection import Connection
import json

class DeepStreamClient:

    def __init__(self, ip, port):

        self._connection = Connection(ip, port)

    def login(self, username, password):
        self._connection.open()
        credentials = json.dumps({"username": username, "password": password})
        print("Using credentials %s" % credentials)
        self._connection.authenticate(credentials)
