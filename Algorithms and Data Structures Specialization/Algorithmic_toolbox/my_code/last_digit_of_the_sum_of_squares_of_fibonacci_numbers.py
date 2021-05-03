# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

d = dict()
d[0] = 0
d[1] = 1


def fibonacci_number(n):
    for i in range(2, n+1):
        if i not in d:
            d[n] = fibonacci_number(n-1) + fibonacci_number(n-2)

    return d[n]


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    # https://www.geeksforgeeks.org/sum-of-squares-of-fibonacci-numbers/

    if n > 2:
        if n > 61:
            return (fibonacci_number(n % 60) * fibonacci_number((n % 60) +1)) % 10
        else:
            return (fibonacci_number(n) * fibonacci_number(n + 1)) % 10

    if n <= 2:
        return n


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
