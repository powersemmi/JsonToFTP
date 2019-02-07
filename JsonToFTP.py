import json
import asyncio
import time

from FTPClient import FTPClient


def parse_json(data_file: str):
    with open(data_file, "r") as read_file:
        data = json.load(read_file)
    return data


def split_list(seq: list, num: int):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


async def main():
    parsed_json = parse_json("data.json")
    # print(parsed_json)
    json1, json2 = split_list(parsed_json, 2)
    ftp1 = FTPClient(cwd="/", host="localhost", port=1026)
    ftp2 = FTPClient(cwd="/", host="localhost", port=1026)
    task1 = asyncio.create_task(
        ftp1.upload_files(json1, 0.0001)
    )
    task2 = asyncio.create_task(
        ftp2.upload_files(json2, 0.0002)
    )

    # print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    # print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main(), debug=False)





