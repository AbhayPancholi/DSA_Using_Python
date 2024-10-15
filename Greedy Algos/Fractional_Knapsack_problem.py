"""
The fractional knapsack problem is an optimization problem where the goal is to maximize the total value of items 
that can be put into a knapsack with a fixed weight capacity. Unlike the traditional 0/1 knapsack problem, in the 
fractional knapsack problem, you can take fractions of an item rather than having to include the whole item or 
exclude it entirely.

Problem Statement:
Given n items, each with a weight w[i] and a value v[i], determine the maximum value that can be obtained by placing
items in a knapsack with a capacity W.
Fractions of items can be included in the knapsack.

"""

"""
Steps to Solve the Fractional Knapsack Problem:

1. Calculate the value-to-weight ratio (v[i]/w[i]) for each item.

2. Sort the items in descending order based on their value-to-weight ratio.

3. Select items in sorted order:
    a. If the weight of the current item is less than or equal to the remaining capacity, include the entire item.
    b. If the weight exceeds the remaining capacity, include as much of the item as possible (i.e., take a fraction
       of the item to fill the knapsack).

Example:
Let's consider an example with three items and a knapsack with a capacity of 50 units:

Item 1: Weight = 10, Value = 60
Item 2: Weight = 20, Value = 100
Item 3: Weight = 30, Value = 120
Knapsack Capacity, W = 50

Step 1: Calculate the Value-to-Weight Ratio
Item 1: 60/10 = 6
Item 2: 100/20 = 5
Item 3: 120/30 = 4

Step 2: Sort Items by Value-to-Weight Ratio
Sorted order: Item 1 (6), Item 2 (5), Item 3 (4)

Step 3: Select Items to Maximize Value
Include Item 1 (weight 10): Remaining capacity = 50 - 10 = 40; Total value = 60
Include Item 2 (weight 20): Remaining capacity = 40 - 20 = 20; Total value = 60 + 100 = 160
Include a fraction of Item 3 (weight 20 out of 30): Fraction = 20/30; Value added = 120 * (20/30) = 80

"""
