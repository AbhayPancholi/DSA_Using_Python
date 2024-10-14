## Problem Definition: -
"""
In this problem we have been provided with coins of different denominations say: {1, 2, 5, 10, 20, 50, 100, 1000}
and total amount of money. We have to find the minimun number of coins to make up the given amount.
Note: There is infinite supply of denominations.

Example 1:
Total amount: 70
Answer: 2 -> 50 + 20 = 70

Example 2:
Total amount: 122
Answer: 3 -> 100 + 20 + 2 = 122

"""

## Approach to solve the problem: -
"""
Step 1: find the biggest coin that is less than given amount.

Step 2: Add coin to the result and substract coin from the given amount.

step 3: if given amount is equal to zero:
            print result.
        else:
            repeat steps.

"""


def coinChange(amount, coins):
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]

        if coinValue <= amount:
            print(coinValue)
            amount -= coinValue

        if coinValue > amount:
            index -= 1

        if amount == 0:
            break


coins = [1, 2, 5, 10, 20, 50, 100]
coinChange(201, coins)
