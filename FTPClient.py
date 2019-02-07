from ftplib import FTP
from os import path
import asyncio
from config import Config

class FTPClient:
    def __init__(self, cwd: str, host: str, port: int):
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(Config.FTP_LOGIN, Config.FTP_PASSWD, Config.FTP_ACCT)
        self.ftp.cwd(cwd)  # replace with your directory

    def upload_file(self, upload: str, save_as: str):
        upload_file = path.split(upload)[::-1][0]
        # print(type(upload_file))
        # print(upload_file)
        how_name = save_as if save_as != '' else upload_file
        try:
            self.ftp.storbinary('STOR ' + how_name, open(upload, 'rb'))
            print('upload: ', upload, " save_ss:", how_name)
        except FileNotFoundError:
            print("not found: " + upload)
            pass

    async def upload_files(self, files: list, delay):
        await asyncio.sleep(delay)
        for i in files:
            # print(i)
            self.upload_file(i['path'], i['save_as'])
        self.ftp.quit()

    def download_file(self, download: str, save_as: str):
        local_file = open(save_as, 'wb')
        self.ftp.retrbinary('RETR ' + download, local_file.write, 1024)
        local_file.close()


if __name__ == '__main__':
    test = FTPClient(cwd="/", host="localhost", port=1026)
    test.upload_file('data.json', "thisis")
    test.ftp.quit()
