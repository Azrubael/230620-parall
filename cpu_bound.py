
"""
When you run the code with different interpreters the results may differ
markedly (for example PyPy or CPython).
As a consequence of the work of GIL (the global interpreter lock), the execution time is practically independent of the number of threads
"""

import threading
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def calculate_fibonacci(start, end, result):
    fib_sequence = []
    for i in range(start, end):
        fib_sequence.append(fibonacci(i))
    result.extend(fib_sequence)


def main():
    num_terms = 30                 # let's calculate the thirty first numbers
    num_threads = 1                # let's start with one thread
    chunk_size = num_terms // num_threads
    threads = []
    result = []

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i+1)*chunk_size if i != num_threads-1 else num_terms
        thread = threading.Thread(target=calculate_fibonacci, args=(start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    finish_time = time.time()

    print(result)
    print("Threads were started:", num_threads)
    print("Eexecution took time:", finish_time-start_time)


if __name__ == '__main__':
    main()
