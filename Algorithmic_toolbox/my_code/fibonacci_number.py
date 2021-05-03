# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


d = dict()
d[0] = 0
d[1] = 1


def fibonacci_number(n):
    for i in range(1, n+1):
        if i not in d:
            d[n] = fibonacci_number(n-1) + fibonacci_number(n-2)
    return d[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
