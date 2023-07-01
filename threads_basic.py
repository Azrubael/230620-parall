#!/usr/bin/env python3

import threading

def print_numbers(srart, finish):
    for i in range(srart, finish):
        print(i)

# create concatenated threads
thread1 = threading.Thread(target=print_numbers, args=(0, 8))
thread1.start()
thread1.join()
print_numbers(50, 58)

# create concurrent threads
thread2 = threading.Thread(target=print_numbers, args=(100, 108))
thread2.start()
print_numbers(70, 78)