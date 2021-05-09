# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops = [0] + stops + [d]  # coz we don't refill at starting position
    n = len(stops)
    num_refills = 0  # initialize the number of refills to 0
    current_refill = 0  # initialize the current refills to 0
    iteration = 1
    # as long as the current refill at most the last refill
    while current_refill <= n:  # only the stops, ignoring the destination
        # print("iteration", iteration)
        # set the last refill to current refill
        last_refill = current_refill
        # print("current_refill", current_refill)
        # print("last_refill", last_refill)
        # print("num_refills", num_refills)
        # print("#"*10)
        # print(len(stops))
        # if the current refill is not last and the next refill can be reached by the car
        while current_refill < n and stops[current_refill + 1] - stops[last_refill] <= m:
            # print("next refill dist", stops[current_refill + 1] - stops[last_refill])
            # print("go to" , stops[current_refill + 1])
            # print("from", stops[last_refill])
            current_refill = current_refill + 1
            # print("current_refill", current_refill)
            # print("last_refill", last_refill)
            # print("num_refills", num_refills)
            # print("-"*50)
            if current_refill >= n-1: # redundant condition
                break
        if current_refill == last_refill:
            return -1
        if current_refill < n-1:
            num_refills = num_refills + 1
        # print("num_refills", num_refills)
        # print("#" * 50)
        iteration +=1
        if current_refill >= n-1:  # redundant condition
            break
    return num_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))

    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
