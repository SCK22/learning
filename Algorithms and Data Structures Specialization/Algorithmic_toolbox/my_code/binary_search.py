# python3
import numpy as np

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4


    low = 0
    high = len(keys)
    if query > keys[-1]:
        return -1
    if query == keys[low]:
        return low
    if query == keys[-1]:
        return len(keys)
    # print("low", low)
    # print("high", high)
    while low <= high:
        # print("low", low)
        # print("high", high)
        mid = int(low + np.floor((high-low)/2))
        if mid > len(keys):
            return -1
        if query == keys[mid]:
            return mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return - 1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    print(input_keys, input_queries)
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
