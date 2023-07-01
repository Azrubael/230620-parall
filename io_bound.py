"""
An example of effective threading in case of input-output operations
The interpreter essentially waived responsibility and thread safety when working with files, this issue is dealt with directly by Linux.
"""

import threading
import time


def write_to_file(file_path, start, end):
    for i in range(start, end):
        with open(file_path, 'a') as file:  #the file opening is placed inside the loop intentionally 
            file.write(f"Line {i}\n")

def main():
    file_path = 'output.txt'
    num_lines = 10000                       #let's calculate the thirty first numbers 
    num_threads = 7                         #the optimum is near 7 thread
    chunk_size = num_lines // num_threads

    threads = []

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else num_lines
        thread = threading.Thread(target=write_to_file, args=(file_path, start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    finish_time = time.time()

    print("Done!")
    print("Threads were started:", num_threads)
    print("Eexecution took time:", finish_time-start_time)


if __name__ == '__main__':
    main()

