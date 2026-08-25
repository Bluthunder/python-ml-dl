
import concurrent.futures
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as DummyPool
import numpy as np
import os


def do_something(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} seconds'


def concurrent_example():

    print('------ Runnning concurrent_example ------')
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        sec = [5, 4, 3, 2, 1]
        results = executor.map(do_something, sec)

        for r in results:
            print(r)
    finish = time.perf_counter()

    print(f'Finished in {finish - start} seconds')
    return None


def multiprocessing_example():
    print('------ Runnning multiprocessing_example ------')
    start = time.perf_counter()

    sec = [5, 4, 3, 2, 1]

    with Pool() as pool:
        results = pool.map(do_something, sec)

        for r in results:
            print(r)

    finish = time.perf_counter()
    print(f'Finished in {finish - start} seconds')


def thread_pool_executor_example():
    print('------ Runnning thread_pool_executor_example ------')
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        sec = [5, 4, 3, 2, 1]
        results = executor.map(do_something, sec)

        for r in results:
            print(r)
    finish = time.perf_counter()

    print(f'Finished in {finish - start} seconds')
    return None


def multiprocessing_dummy_example():
    print("--- Running multiprocessing.dummy.Pool ---")
    start = time.perf_counter()

    with DummyPool() as dummy_pool:
        sec = [5, 4, 3, 2, 1]
        results = dummy_pool.map(do_something, sec)

        for r in results:
            print(r)
    finish = time.perf_counter()

    print(f'Finished in {finish - start} seconds')
    return None


if __name__ == '__main__':

    print(f'Number of CPU {os.cpu_count()}')

    print(concurrent_example())

    print(multiprocessing_example())

    print(multiprocessing_dummy_example())

    print(thread_pool_executor_example())
