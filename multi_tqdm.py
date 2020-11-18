import multiprocessing
from tqdm import tqdm
import time

def worker():
    name = multiprocessing.current_process().name
    print(name, end='')
    for i in tqdm(range(100)):
        time.sleep(1)

def my_service():
    name = multiprocessing.current_process().name
    print('\n')
    print(name, end='')
    for i in tqdm(range(100)):
        time.sleep(2)

if __name__ == '__main__':
    worker_1 = multiprocessing.Process(name='my_service', target=my_service)
    worker_2 = multiprocessing.Process(name='worker 1', target=worker)

    start = time.time()
    worker_1.start()
    worker_2.start()

    if time.time() - start > 10:
        exit()