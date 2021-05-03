# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    d = dict()
    d[0] = 0
    d[1] = 1
    if n-1 not in d.keys():
        fibonacci_number(n-1)
    if n-2 not in d.keys():
        fibonacci_number(n-2)
    else:
        return d[n-1] + d[n-2]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
