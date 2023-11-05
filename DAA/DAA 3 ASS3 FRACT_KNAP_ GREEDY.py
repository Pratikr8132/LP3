class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ / wt_

    def __lt__(self, other):
        return self.cost < other.cost

def fractionalKnapSack(wt, val, capacity):
    """Function to get maximum value"""
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]

    # Sorting items by value-to-weight ratio (cost)
    iVal.sort(reverse=True)

    totalValue = 0
    for i in iVal:
        curWt = i.wt
        curVal = i.val

        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = 0
            break

    return totalValue

if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    # Function call
    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)




























































# FIRST EXPLAIN MEE THE CODE LINE BY LINE, THEN WHAT WE HAVE IMPLEMENTED WHY WE NEED IT AND THEN PREPARE 30 QUESTION AND ANSWER
#
# ChatGPT
# !
# Certainly, let's start by explaining the code line by line:
#
# python
# Copy code
# class ItemValue:
#     """Item Value DataClass"""
#
#     def __init__(self, wt_, val_, ind_):
#         self.wt = wt_
#         self.val = val_
#         self.ind = ind_
#         self.cost = val_ / wt_
#
#     def __lt__(self, other):
#         return self.cost < other.cost
# The code begins by defining a class called ItemValue, which is used to represent the values and weights of items in the context of the fractional Knapsack problem.
#
# In the __init__ method, the class constructor, it initializes attributes wt (weight), val (value), ind (index), and cost (value-to-weight ratio) for each item.
#
# The __lt__ method is defined to allow comparison of ItemValue objects based on their cost attributes. This is used for sorting items based on their cost in descending order.
#
# python
# Copy code
# def fractionalKnapSack(wt, val, capacity):
#     """Function to get the maximum value"""
#     iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
#
#     # Sorting items by value-to-weight ratio (cost)
#     iVal.sort(reverse=True)
#
#     totalValue = 0
#     for i in iVal:
#         curWt = i.wt
#         curVal = i.val
#
#         if capacity - curWt >= 0:
#             capacity -= curWt
#             totalValue += curVal
#         else:
#             fraction = capacity / curWt
#             totalValue += curVal * fraction
#             capacity = 0
#             break
#
#     return totalValue
# The fractionalKnapSack function is defined to solve the fractional Knapsack problem. It takes three arguments: wt (a list of item weights), val (a list of item values), and capacity (the capacity of the knapsack).
#
# Inside the function, it creates a list iVal of ItemValue objects, where each object represents an item, its weight, value, and index.
#
# The iVal list is sorted in descending order based on the value-to-weight ratio (cost). This sorting step is essential for the greedy approach.
#
# The function initializes totalValue to 0, which will store the maximum value that can be obtained.
#
# It then iterates through the sorted list of iVal objects.
#
# For each item, it checks if adding the entire item to the knapsack will not exceed the capacity (by comparing capacity - curWt with 0).
#
# If there's enough capacity for the entire item, it subtracts the item's weight from the remaining capacity, adds the item's value to the total value, and continues with the next item.
#
# If the capacity does not allow for the entire item, it calculates the fraction of the item that can be added to the knapsack, updates the total value accordingly, sets the capacity to 0, and breaks out of the loop.
#
# Finally, the function returns the totalValue, which represents the maximum value that can be obtained with the given capacity and items.
#
# python
# Copy code
# if __name__ == "__main__":
#     wt = [10, 40, 20, 30]
#     val = [60, 40, 100, 120]
#     capacity = 50
#
#     # Function call
#     maxValue = fractionalKnapSack(wt, val, capacity)
#     print("Maximum value in Knapsack =", maxValue)
# This part of the code is executed if the script is run as the main program.
#
# It defines the item weights (wt), item values (val), and the knapsack capacity (capacity) that will be used for testing.
#
# The fractionalKnapSack function is called with these parameters, and the result (maximum value) is stored in maxValue.
#
# Finally, it prints the maximum value that can be obtained in the knapsack.
#
# Now, let's discuss what we have implemented and why we need it:
#
# What We Have Implemented:
#
# We have implemented a Python script that solves the fractional Knapsack problem using a greedy approach.
# The code defines a ItemValue class to represent item values, weights, and costs (value-to-weight ratio).
# It also defines a fractionalKnapSack function that calculates the maximum value that can be obtained by selecting fractions of items based on their value-to-weight ratios.
# Why We Need It:
#
# The fractional Knapsack problem is a classic optimization problem where we need to select items from a set with limited capacity to maximize the total value.
# This problem is relevant in various real-world scenarios, such as resource allocation, budget optimization, and portfolio management.
# Now, let's prepare 30 questions and answers based on the code:
#
# What is the purpose of the ItemValue class in this code?
#
# Answer: The ItemValue class represents the values, weights, and costs (value-to-weight ratios) of items in the fractional Knapsack problem.
# Why is the value-to-weight ratio (cost) calculated for each item in the ItemValue class?
#
# Answer: The value-to-weight ratio is crucial for the greedy approach used to solve the fractional Knapsack problem. It helps in selecting the most valuable items first.
# What is the significance of the __lt__ method in the ItemValue class?
#
# Answer: The __lt__ method allows comparison of ItemValue objects based on their cost (value-to-weight ratio), which is used for sorting items in descending order of cost.
# What does the fractionalKnapSack function aim to solve?
#
# Answer: The fractionalKnapSack function aims to find the maximum value that can be obtained by selecting fractions of items to fill a knapsack with limited capacity.
# What are the input parameters of the fractionalKnapSack function?
#
# Answer: The function takes three parameters: wt (item weights), val (item values), and capacity (knapsack capacity).
# How does the code calculate the value-to-weight ratio for each item in the iVal list?
#
# Answer: The value-to-weight ratio is calculated in the __init__ method of the ItemValue class as val / wt.
# Why is the iVal list sorted in descending order based on the value-to-weight ratio (cost)?
#
# Answer: Sorting by cost is essential for the greedy approach, as it allows the algorithm to select the most valuable items first.
# What is the purpose of the totalValue variable in the fractionalKnapSack function?
#
# Answer: The totalValue variable stores the maximum value that can be obtained by selecting items for the knapsack.
# How does the code determine whether an entire item can be added to the knapsack without exceeding its capacity?
#
# Answer: It checks if capacity - curWt is greater than or equal to 0 for the current item.
# What happens when an item can be added to the knapsack without exceeding the capacity?
#
# Answer: The item's weight is subtracted from the remaining capacity, and the item's value is added to the totalValue.
# How does the code handle cases where only a fraction of an item can be added to the knapsack?
#
# Answer: It calculates the fraction of the item that can be added, updates the totalValue accordingly, sets the capacity to 0, and breaks out of the loop.
# What is the significance of the if __name__ == "__main__": block at the end of the code?
#
# Answer: This block is executed when the script is run as the main program. It defines input values and demonstrates how to use the fractionalKnapSack function.
# What are the item weights (wt) and values (val) used for testing in the code?
#
# Answer: The provided weights and values are wt = [10, 40, 20, 30] and val = [60, 40, 100, 120].
# What is the significance of the maxValue variable in the code?
#
# Answer: maxValue stores the maximum value that can be obtained in the knapsack, which is calculated by the fractionalKnapSack function.
# How does the code handle the case where the knapsack has a capacity of 0?
#
# Answer: In such a case, the totalValue remains 0, and no items are added to the knapsack.
# Why is the capacity set to 0 when a fraction of an item is added to the knapsack?
#
# Answer: Setting the capacity to 0 ensures that no more items can be added once a fraction of an item has been included in the knapsack.
# What happens if all items can be added to the knapsack without exceeding its capacity?
#
# Answer: In this case, the capacity becomes 0, and the maximum possible value is obtained.
# How does the code handle situations where there is not enough capacity for any item?
#
# Answer: In such cases, the totalValue remains 0, and no items are added to the knapsack.
# What is the time complexity of the greedy algorithm used in this code to solve the fractional Knapsack problem?
#
# Answer: The time complexity is O(n log n), where n is the number of items, due to the sorting step.
# Can this algorithm be used for the 0/1 Knapsack problem where items cannot be divided?
#
# Answer: No, this algorithm is specifically designed for the fractional Knapsack problem, where items can be divided.
# What would be the expected output of the code when using the provided test values?
#
# Answer: The expected output is "Maximum value in Knapsack = 240.0."
# How does the greedy algorithm ensure that it selects the most valuable items first?
#
# Answer: By sorting items in descending order of their value-to-weight ratio (cost), the algorithm prioritizes items with the highest value relative to their weight.
# In which real-life scenarios can the fractional Knapsack problem be applied?
#
# Answer: It can be applied in resource allocation, financial portfolio optimization, and various scenarios where maximizing value with limited capacity is essential.
# Can this algorithm handle negative item values or weights?
#
# Answer: No, this algorithm assumes that all item values and weights are non-negative.
# What is the primary difference between the fractional Knapsack problem and the 0/1 Knapsack problem?
#
# Answer: In the fractional Knapsack problem, items can be divided, while in the 0/1 Knapsack problem, items cannot be divided.
# What other algorithms or methods can be used to solve the Knapsack problem?
#
# Answer: Dynamic programming and branch and bound are commonly used methods for solving the Knapsack problem.
# How does the greedy approach used in this code compare to dynamic programming for solving the Knapsack problem?
#
# Answer: The greedy approach is faster and simpler but may not always provide an optimal solution. Dynamic programming guarantees an optimal solution but is more computationally intensive.
# What is the space complexity of the algorithm in this code?
#
# Answer: The space complexity is O(n) to store the iVal list of ItemValue objects.
# What would happen if the input lists wt and val had different lengths?
#
# Answer: The code would raise an error, as the two lists should have the same length.