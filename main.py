from io import TextIOWrapper
from threading import Thread
from os.path import isfile
import requests


def get_status(index: int, fp: TextIOWrapper) -> None:
    base_url = "https://news.walla.co.il/item/"

    request = requests.head(f"{base_url}{index}")
 
    fp.write(f"{index},{request.status_code}\n")
    fp.flush()

def run(start: int) -> None:
    if isfile(f"{start}-{start + 100000}.csv") == False:
        with open(f"{start}-{start + 100000}.csv", "w") as fp:
            fp.write("index,status\n")
            fp.flush()
            for index in range(start, start + 100000):
                get_status(index, fp)
        return

    appendStart = 0

    with open(f"{start}-{start + 100000}.csv", "ab+") as fp:
        index = -2
        good = None
        while True:
            fp.seek(index,2)
            isgood = fp.readline().decode()
            if isgood.startswith("\n") == True:
                break
            good = isgood
            index = index + -1
        good = good

        appendStart = int(good.split(",")[0]) + 1
    
    with open(f"{start}-{start + 100000}.csv", "a") as fp:
        for index in range(appendStart, start + 100000):
            get_status(index, fp)

def main():
    threads = []

    for x in range(0, 40):
        threads.append(Thread(target=run, args=(x * 100000,)))

    for th in threads:
        th.start()

    for th in threads:
        th.join()

if __name__ == "__main__":
    main()