import random
import timeit


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_deterministic(arr, low, high):
    if low < high:
        pivot_index = deterministic_pivot(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        partition_index = partition(arr, low, high)

        quicksort_deterministic(arr, low, partition_index - 1)
        quicksort_deterministic(arr, partition_index + 1, high)


def deterministic_pivot(arr, low, high):
    # Choose the middle element as the pivot
    mid = (low + high) // 2
    return mid


def quicksort_randomized(arr, low, high):
    if low < high:
        pivot_index = randomized_pivot(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        partition_index = partition(arr, low, high)

        quicksort_randomized(arr, low, partition_index - 1)
        quicksort_randomized(arr, partition_index + 1, high)


def randomized_pivot(arr, low, high):
    # Choose a random pivot within the range [low, high]
    return random.randint(low, high)


if __name__ == "__main__":
    # IF U WANT TO give input use following

    # arr = [int(x) for x in input("Enter space-separated integers: ").split()]
    # IF U WANT TO USE RANDOM 1,10000 ARRAY
    # USE
    # arr = [random.randint(1, 100) for _ in range(1000)]
    arr = [1, 99, 53, 57, 63, 61, 46, 63, 94, 28, 23, 28, 46, ]

    # Test deterministic Quick Sort
    arr_copy_deterministic = arr.copy()
    start_time = timeit.default_timer()
    quicksort_deterministic(arr_copy_deterministic, 0, len(arr_copy_deterministic) - 1)
    deterministic_time = timeit.default_timer() - start_time

    # Print the sorted array
    print("Sorted array (Deterministic):", arr_copy_deterministic)

    # Test randomized Quick Sort
    arr_copy_randomized = arr.copy()
    start_time = timeit.default_timer()
    quicksort_randomized(arr_copy_randomized, 0, len(arr_copy_randomized) - 1)
    randomized_time = timeit.default_timer() - start_time

    # Print the sorted array
    print("Sorted array (Randomized):", arr_copy_randomized)

    print("Deterministic Quick Sort Time: {:.6f} seconds".format(deterministic_time))
    print("Randomized Quick Sort Time: {:.6f} seconds".format(randomized_time))










































# Sure, let's go through the provided code line by line and explain each part.
#
# python
# Copy code
# import random
# import timeit
# These lines import the necessary libraries for the code. random is used for generating random numbers, and timeit is used to measure the time it takes for specific code sections to execute.
#
# python
# Copy code
# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
# Here, a partition function is defined. It takes an array arr and two indices low and high as parameters. The purpose of this function is to select a pivot element (usually the last element of the array), and then rearrange the elements in the array such that all elements less than or equal to the pivot are on the left, and all elements greater than the pivot are on the right.
#
# python
# Copy code
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
# This part of the function iterates through the elements in the range [low, high-1]. If an element arr[j] is less than or equal to the pivot, it increments i and swaps arr[i] and arr[j]. This effectively moves smaller elements to the left side of the pivot.
#
# python
# Copy code
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
# After the loop, it swaps the pivot element arr[high] with the element at position i + 1. This ensures that all elements to the left of i + 1 are less than or equal to the pivot, and all elements to the right are greater than the pivot. Finally, it returns the index of the pivot.
#
# python
# Copy code
# def quicksort_deterministic(arr, low, high):
#     if low < high:
#         pivot_index = deterministic_pivot(arr, low, high)
#         arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
#         partition_index = partition(arr, low, high)
# The quicksort_deterministic function is a deterministic version of the quicksort algorithm. It takes an array arr and the indices low and high. If low is less than high, it selects a pivot index using the deterministic_pivot function, swaps the pivot element with the last element of the subarray, and then partitions the array using the partition function.
#
# python
# Copy code
#         quicksort_deterministic(arr, low, partition_index - 1)
#         quicksort_deterministic(arr, partition_index + 1, high)
# It then recursively applies quicksort to the left and right subarrays.
#
# python
# Copy code
# def deterministic_pivot(arr, low, high):
#     # Choose the middle element as the pivot
#     mid = (low + high) // 2
#     return mid
# The deterministic_pivot function simply chooses the middle element of the subarray as the pivot. This is a deterministic choice, meaning the pivot is always in the middle.
#
# python
# Copy code
# def quicksort_randomized(arr, low, high):
#     if low < high:
#         pivot_index = randomized_pivot(arr, low, high)
#         arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
#         partition_index = partition(arr, low, high)
# The quicksort_randomized function is a randomized version of the quicksort algorithm. It works similarly to quicksort_deterministic but chooses a random pivot using the randomized_pivot function.
#
# python
# Copy code
# def randomized_pivot(arr, low, high):
#     # Choose a random pivot within the range [low, high]
#     return random.randint(low, high)
# The randomized_pivot function generates a random pivot index within the range [low, high].
#
# python
# Copy code
# if __name__ == "__main":
#     arr = [111, 888, 12313, 12, 14, 115, 23, 21, 9, 8, 7, 6, 5, 3, 2, 1111, 243242, 2342342]
# This code block is the main section of the program. It initializes an array arr with some sample values.
#
# python
# Copy code
#     # Test deterministic Quick Sort
#     arr_copy_deterministic = arr.copy()
#     start_time = timeit.default_timer()
#     quicksort_deterministic(arr_copy_deterministic, 0, len(arr_copy_deterministic) - 1)
#     deterministic_time = timeit.default_timer() - start_time
# Here, it tests the deterministic quicksort by creating a copy of the original array, measuring the time it takes to sort it using quicksort_deterministic, and recording the time taken.
#
# python
# Copy code
#     # Test randomized Quick Sort
#     arr_copy_randomized = arr.copy()
#     start_time = timeit.default_timer()
#     quicksort_randomized(arr_copy_randomized, 0, len(arr_copy_randomized) - 1)
#     randomized_time = timeit.default_timer() - start_time
# Similarly, it tests the randomized quicksort using a copy of the original array and records the time taken.
#
# python
# Copy code
#     print("Deterministic Quick Sort Time: {:.6f} seconds".format(deterministic_time))
#     print("Randomized Quick Sort Time: {:.6f} seconds".format(randomized_time))
# Finally, it prints out the time taken for both the deterministic and randomized quicksort methods.
#
# Now, let's address the problem statement:
#
# Problem Statement:
# The code you provided implements two versions of the quicksort algorithm: deterministic and randomized pivot selection. The problem is to compare the performance of these two versions in terms of execution time on a given array.
#
# Brief Description:
# The code defines functions for partitioning and two quicksort algorithms: deterministic and randomized pivot selection. It then applies both algorithms to the same input array and measures the time it takes for each algorithm to sort the array. This is done to compare the efficiency of these pivot selection methods in terms of runtime.
#
# Now, let's prepare 30 questions and answers related to the code:
#
# What is the purpose of the partition function in the code?
#
# The partition function rearranges elements in an array so that all elements less than or equal to the pivot are on the left, and all elements greater than the pivot are on the right.
# What does the deterministic_pivot function do?
#
# The deterministic_pivot function selects the middle element of a subarray as the pivot for quicksort.
# How is the pivot selected in the randomized_pivot function?
#
# The randomized_pivot function selects a random pivot within the range [low, high] of the subarray.
# What is the primary difference between quicksort_deterministic and quicksort_randomized functions?
#
# quicksort_deterministic uses a deterministic pivot selection (middle element), while quicksort_randomized uses a random pivot selection.
# Why might you choose to use a randomized pivot selection in quicksort?
#
# Randomized pivot selection helps prevent worst-case scenarios and improves the average performance of quicksort.
# What is the main purpose of the if __name__ == "__main__": block in the code?
#
# This block is the main execution section of the code, where the sorting algorithms are tested and their performance is measured.
# What is the sample input array used for testing in the code?
#
# The sample input array contains integers: [111, 888, 12313, 12, 14, 115, 23, 21, 9, 8, 7, 6, 5, 3, 2, 1111, 243242, 2342342].
# What does the start_time variable measure in the code?
#
# The start_time variable records the start time before executing a section of code, which is later used to calculate the elapsed time.
# Why is the arr_copy_deterministic array created before testing the deterministic quicksort?
#
# It is created to keep a copy of the original array, as quicksort modifies the input array in place. This copy allows testing without altering the original data.
# How is the time taken for sorting with deterministic quicksort recorded in the code?
#
# The deterministic_time variable stores the time taken for sorting using the deterministic quicksort algorithm.
# Why does the code use the len(arr_copy_deterministic) - 1 as the high index when calling quicksort_deterministic?
#
# This ensures that the high index corresponds to the last element of the array, as quicksort is typically applied to a subarray of the original array.
# What is the primary purpose of the quicksort_randomized function in the code?
#
# The quicksort_randomized function implements the quicksort algorithm with a randomized pivot selection strategy.
# How is the time taken for sorting with randomized quicksort recorded in the code?
#
# The randomized_time variable stores the time taken for sorting using the randomized quicksort algorithm.
# Why is a copy of the original array created before testing the randomized quicksort?
#
# Similar to the deterministic quicksort test, the copy is created to avoid modifying the original array during testing.
# What are the advantages of using randomized pivot selection in quicksort?
#
# Randomized pivot selection helps prevent worst-case scenarios and makes quicksort more robust against specific input data patterns.
# In the code, what does "deterministic" mean in the context of the quicksort algorithm?
#
# "Deterministic" means that the pivot selection method is consistent and not based on randomness. It selects the middle element as the pivot.
# How does the code ensure that the pivot is always in the middle in the deterministic version of quicksort?
#
# The deterministic_pivot function chooses the middle element as the pivot by calculating the middle index as (low + high) // 2.
# What is the time complexity of the quicksort algorithm in the best-case scenario?
#
# The best-case time complexity of quicksort is O(n*log(n)), where n is the number of elements to be sorted.
# How does quicksort achieve its best-case time complexity?
#
# Quicksort achieves its best-case time complexity by selecting well-balanced pivots, resulting in balanced partitions.
# What is the worst-case time complexity of quicksort?
#
# The worst-case time complexity of quicksort is O(n^2), which occurs when the pivot selection strategy consistently chooses the smallest or largest element.
# How does the randomized pivot selection strategy help avoid the worst-case scenario in quicksort?
#
# Randomized pivot selection introduces randomness, making it highly unlikely to consistently choose the worst pivot, thus avoiding the worst-case scenario.
# What does the "partition_index" represent in the code?
#
# The partition_index is the index where the pivot element is correctly positioned after the partitioning step in the quicksort algorithm.
# Why does quicksort have better average-case performance compared to some other sorting algorithms?
#
# Quicksort has better average-case performance because it is efficient in partitioning and sorting elements on average, leading to O(n*log(n)) time complexity.
# What is the purpose of the if __name__ == "__main__": block in a Python script?
#
# The if __name__ == "__main__": block is used to specify the code that should run when the script is executed directly, as opposed to when it is imported as a module into another script.
# What is the significance of measuring and comparing the execution times of different sorting algorithms?
#
# Measuring execution times helps assess the efficiency and performance of sorting algorithms, enabling the selection of the most suitable algorithm for specific use cases.
# What other factors, besides pivot selection, can influence the performance of the quicksort algorithm?
#
# The distribution of data, input size, and the choice of sorting algorithm variations (e.g., three-way quicksort) can influence the performance of quicksort.
# What are some scenarios where quicksort might be the preferred sorting algorithm?
#
# Quicksort is preferred when sorting large datasets, especially when average-case performance is critical. It is also suitable for in-place sorting.
# Can quicksort be stable, and what does "stable sorting" mean?
#
# Quicksort is not stable by default. Stable sorting means that equal elements maintain their relative order after sorting. Quicksort may change the order of equal elements.
# Why is it important to make a copy of the original array for testing in the code?
#
# Making a copy ensures that the original data is preserved, allowing for multiple tests without modifying the input array.
# How does quicksort compare to other sorting algorithms like merge sort or bubble sort in terms of efficiency?
#
# Quicksort is generally more efficient than bubble sort and has similar average-case efficiency to merge sort, but it is often more memory-efficient due to its in-place nature. However, the choice of sorting algorithm depends on the specific requirements and characteristics of the data to be sorted.








#lab manual content

#
# Title: Write a program for analysis of quick sort by using deterministic and randomized variant.
#
# Objective: To analyze time and space complexity of quick sort by using deterministic and randomized
# variant.
#
# Theory:
# What is a Randomized Algorithm?
# • An algorithm that uses random numbers to decide what to do next anywhere in its logic is
# called Randomized Algorithm..
# • For example, in Randomized Quick Sort, we use random number to pick the next pivot (or we
# randomly shuffle the array).
# • Typically, this randomness is used to reduce time complexity or space complexity in other
# standard algorithms.
# • Randomized algorithm for a problem is usually simpler and more efficient than its
# deterministic counterpart.
# • The output or the running time are functions of the input and random bits chosen .
#
# Department of Computer Engineering Laboratory Practice III
#
# A.Y. 2023-24
#
# Types of Randomized Algorithms
# 1. Las Vegas Algorithms
# ● These algorithms always produce correct or optimum result.
# ● Time complexity of these algorithms is based on a random value and time complexity is
# evaluated as expected value.
# ● For example, Randomized QuickSort always sorts an input array and expected worst case time
# complexity of QuickSort is O(nLogn).
# ● A Las Vegas algorithm fails with some probability, but we can tell when it fails. In particular,
# we can run it again until it succeeds, which means that we can eventually succeed with
# probability 1.
# ● Alternatively, we can think of a Las Vegas algorithm as an algorithm that runs for an
# unpredictable amount of time but always succeeds
# 2. Monte Carlo Algorithms
# ● Produce correct or optimum result with some probability.
# ● These algorithms have deterministic running time and it is generally easier to find out worst
# case time complexity.
# ● For example Karger’s Algorithm produces minimum cut with probability greater than or equal to
# 1/n2
# (n is number of vertices) and has worst case time complexity as O(E).
# ● A Monte Carlo algorithm fails with some probability, but we can’t tell when it fails.
# ● The polynomial equality-testing algorithm in an example of a Monte Carlo algorithm
# Randomized Quick Sort Algorithm:
#
# Department of Computer Engineering Laboratory Practice III
#
# A.Y. 2023-24
#
# Applications of Randomized Algorithms
# ● Randomized algorithms have huge applications in Cryptography.
# ● Load Balancing.
# ● Number-Theoretic Applications: Primality Testing
# ● Data Structures: Hashing, Sorting, Searching, Order Statistics and Computational
# Geometry.
# ● Algebraic identities: Polynomial and matrix identity verification. Interactive proof systems.
# ● Mathematical programming: Faster algorithms for linear programming, Rounding linear
# program solutions to integer program solutions
#
# Analysis of Randomized Quick sort
# The running time of quicksort depends mostly on the number of comparisons performed in all calls to
# the Randomized-Partition routine. Let X denote the random variable counting the number of
# comparisons in all calls to Randomized-Partition.
# Let zi denote the i-th smallest element of A[1..n].
# Thus A[1..n] sorted is <z1, z2, ... , zn >.
# Let Zij = {zi, ..., zj} denote the set of elements between zi and zj, including these elements.
# Xij = I{ zi is compared to zj}.
# Thus, Xij is an indicator random variable for the event that the i-thv smallest and the j-th smallest
# elements of A are compared in an execution of quicksort.
# Number of Comparisons
# Since each pair of elements is compared at most once by quicksort, the number X of comparisons is
# given by
#
# Therefore, the expected number of comparisons is
#
# Expected Number of Comparisons
#
# Department of Computer Engineering Laboratory Practice III
#
# A.Y. 2023-24
#
# It follows that the expected running time of Randomized- Quicksort is O(n log n).
# It is unlikely that this algorithm will choose a terribly unbalanced partition each time, so the
# performance is very good almost all the time.
# Assignment Questions:
# 1. Explain difference between quick sort and randomized quick sort? What is deterministic quick
# sort?
# 2. Comment on why randomized quick sort is more preferable to normal quick sort? Write
# pseudo code for randomized quick sort.
# 3. Discuss in details complexity analysis of randomized quick sort. What is overall Time
# Complexity in Worst Case? Comment on stability of the same.
# 4. Discuss advantages of randomized algorithm? How to analyze Randomized Algorithms?
# 5. Which is better randomized quick sort and/or merge sort? Why?
#
# Conclusion: In this way we have explored Concept of quick sort by using deterministic and
# randomized variant.