import multiprocessing
from tqdm import tqdm
import time

def worker():
    name = multiprocessing.current_process().name
    for i in range(10):
        print(f"{name} now")

def my_service():
    name = multiprocessing.current_process().name
    for i in range(10):
        print(f"{name} now")

if __name__ == '__main__':
    worker_1 = multiprocessing.Process(name='worker 1', target=my_service)
    worker_2 = multiprocessing.Process(name='worker 2', target=worker)

    worker_1.start()
    worker_2.start()