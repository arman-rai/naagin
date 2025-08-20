import threading, time

def worker(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")

t1 = threading.Thread(target=worker, args=("thread 1",))
t2 = threading.Thread(target=worker, args=("thread 2",))

t1.start()
t2.start()

