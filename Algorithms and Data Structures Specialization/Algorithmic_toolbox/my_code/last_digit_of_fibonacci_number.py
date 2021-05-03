# python3

#
# def last_digit_of_fibonacci_number_naive(n):
#     assert 0 <= n <= 10 ** 7
#
#     if n <= 1:
#         return n
#
#     return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10

d = dict()
d[0] = 0
d[1] = 1


def fibonacci_number(n):
    for i in range(1, n+1):
        if i not in d:
            d[n] = fibonacci_number(n-1) + fibonacci_number(n-2)
    return d[n]


def last_digit_of_fibonacci_number(n):
    # https://stackoverflow.com/questions/40094796/python-calculate-the-last-digit-of-a-large-fibonacci-number-with-less-time
    if n >61:
        return fibonacci_number(n%60) % 10
    else:
        return fibonacci_number(n) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
