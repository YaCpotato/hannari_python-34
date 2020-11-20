import multiprocessing
import time

def sender():
    print("Send------------->")

def sloth_receiver():
    time.sleep(2)
    print("Message received")

if __name__ == '__main__':
    sender = multiprocessing.Process(target=sender)
    sloth_receiver = multiprocessing.Process(target=sloth_receiver)

    sloth_receiver.start()
    sender.start()





