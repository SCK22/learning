# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


d = dict()
d[0] = 0
d[1] = 1


def fibonacci_number(n):
    for i in range(2, n+1):
        if i not in d:
            d[n] = fibonacci_number(n-1) + fibonacci_number(n-2)

    return d[n]


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if from_index > 61 or to_index > 61:
        return (fibonacci_number(to_index % 60 + 2) - fibonacci_number(from_index % 60 + 1)) % 10
    else:
        return (fibonacci_number(to_index + 2) - fibonacci_number(from_index + 1)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
