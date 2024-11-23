import time


def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def factorize(numbers):
    result = []
    for num in numbers:
        result.append(get_factors(num))
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
    factorize(data)
    end_time = time.time()
    print(f"Синхронне виконання: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    main()
