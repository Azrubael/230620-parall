#!/usr/bin/env python3

import threading

def print_numbers(srart, finish):
    for i in range(srart, finish):
        print(i)

threads = []
for i in range(1, 8):
    threads.append(threading.Thread(target=print_numbers,\
                                    args=(i*10, (i+1)*10)))
for t in threads:
    t.start()

# for t in threads:
#     t.join()
