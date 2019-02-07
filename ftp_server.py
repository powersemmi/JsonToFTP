from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from os import path


def ftp_server():
    server_path = path.abspath("server/")
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", server_path, perm="elradfmw")
    authorizer.add_anonymous(server_path, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1", 1026), handler)
    server.serve_forever()


if __name__ == '__main__':
    ftp_server()
