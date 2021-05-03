# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    # if the money is less tha 5, return as many 1 coins
    if money < 5:
        return money
    # else initialize a variable to store number of coins
    num_coins = 0
    # first give as many 10's as possible
    while money >= 10 and money % 10 >= 0:
        num_coins += 1
        # remove 10 for each 10 coin added
        money = money - 10
    # then give as many 5's as possible
    while money >= 5 and money % 5 >= 0:
        num_coins += 1
        # remove 5 for each 5 coin added
        money = money - 5
    # whatever is remaining, need to be 1's
    if money < 5:
        return num_coins + money


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
