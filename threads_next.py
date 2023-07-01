#!/usr/bin/env python3

import threading
import multiprocessing
import time

def print_numbers(srart, finish):
    for i in range(srart, finish):
        print(i)


def test_threads(n):
    threads = []
    for i in range(1, n):
        threads.append(threading.Thread(target=print_numbers,\
                                         args=(i*100, i*100+10)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def test_processes(n):
    procs = []
    for i in range(1, n):
        procs.append(multiprocessing.Process(target=print_numbers,\
                                         args=(i*100, i*100+10)))
    for t in procs:
        t.start()
    for t in procs:
        t.join()


if __name__ == '__main__':
    n = 100
    start = time.time()
    test_threads(n)
    # test_processes(n)
    finish = time.time()
    print(finish - start)

# Вывод: test_threads(n) - 0,035сек, test_processes(n) - 0,103сек
# Процессы обгонят потоки только на больших объемах процессорных нагрузок,
# которые будут обрабатываться разными ядрами процессора.
# Потоки выгодее использовать при наличии операций ввода-вывода