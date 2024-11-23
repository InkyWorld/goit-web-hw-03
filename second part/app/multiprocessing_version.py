import time
import multiprocessing

from synchronous_version import get_factors


def parallel_factorize(numbers):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    result = pool.map(get_factors, numbers)
    pool.close()
    pool.join()
    return result


def main():
    data = [
        128,
        255,
        99999,
        10651060,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
    ]
    start_time = time.time()
    parallel_factorize(data)
    end_time = time.time()
    print(f"Паралельне виконання: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    main()
