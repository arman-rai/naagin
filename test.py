# multiprocessing
# threads are limited so multi process and profit

from multiprocessing import Process

def compute_square(x):
    print(f"{x}^2 = {x*x}")

processes = [Process(target=compute_square, args=(i,)) for i in range(5)]

for p in processes: p.start()
for p in processes: p.join()
