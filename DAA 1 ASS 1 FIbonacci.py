import timeit

def fibonacci(n):
    """Non-recursive Fibonacci function"""
    fib_list = [0] * (n + 1)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

def fibonacci_recursive(n):
    """Recursive Fibonacci function with memoization"""
    fib_recur_list = [-1] * (n + 1)

    if n == 0:
        return 0
    if n == 1:
        return 1
    if fib_recur_list[n] == -1:
        fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]

N = 200
RUNS = 100000
print(f"Given N = {N}\n{RUNS} runs")

# Measure time for the non-recursive Fibonacci function
print(
    "Fibonacci non-recursive:",
    fibonacci(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci(N)", setup="from __main__ import fibonacci, N", number=RUNS):.5f}',
    "O(n)\tSpace: O(n)",
)

# Measure time for the recursive Fibonacci function
print(
    "Fibonacci recursive:\t",
    fibonacci_recursive(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci_recursive(N)", setup="from __main__ import fibonacci_recursive, N", number=RUNS):.5f}',
    "O(n)\tSpace: O(n)",
)



















#code explanation----->
# explain the code line by line ...why used timelit ,what it do how it do and all~
#
# ChatGPT
# Certainly, let me explain the code line by line, including the purpose of using the timeit module and how it works.
#
# import timeit: This line imports the timeit module, which is used for measuring the execution time of code.
#
# def fibonacci(n):: This line defines a non-recursive Fibonacci function, fibonacci(n), that takes an integer n as an input parameter. It calculates the nth Fibonacci number using a non-recursive method.
#
# """Non-recursive Fibonacci function""": This is a docstring that provides a brief description of the fibonacci function.
#
# for i in range(2, n + 1):: This line starts a loop from 2 to n (inclusive) to calculate the Fibonacci numbers.
#
# fib_list[i] = fib_list[i - 1] + fib_list[i - 2]: In each iteration of the loop, this line calculates the ith Fibonacci number by summing the (i-1)th and (i-2)th Fibonacci numbers and stores it in the fib_list.
#
# return fib_list[n]: This line returns the nth Fibonacci number, which is stored in the fib_list.
#
# def fibonacci_recursive(n):: This line defines a recursive Fibonacci function with memoization, fibonacci_recursive(n), which takes an integer n as an input parameter.
#
# """Recursive Fibonacci function""": This is a docstring providing a brief description of the fibonacci_recursive function.
#
# if n = 0: and if n = 1:: These lines contain conditional statements with incorrect syntax. The correct syntax should use double equals, i.e., if n == 0: and if n == 1: to check if n is equal to 0 or 1.
#
# fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2): This line calculates the nth Fibonacci number using a recursive approach with memoization. It checks if the value has already been calculated and stores it in the fib_recur_list.
#
# N = 20: This line sets the value of N to 20, which represents the index of the Fibonacci number to be calculated.
#
# RUNS = 1000: This line sets the value of RUNS to 1000, indicating the number of times the code will run to measure execution time.
#
# print(f"Given N = {N}\n{RUNS} runs"): This line prints information about the value of N and the number of runs.
#
# fib_list = [0] * (N + 1): This line creates a list called fib_list with (N+1) elements, initialized to 0. This list will be used to store the non-recursive Fibonacci numbers.
#
# fib_list[0] = 0 and fib_list[1] = 1: These lines set the first two elements of fib_list to their initial values (0 and 1).
#
# print("Fibonacci non-recursive:", fibonacci(N), ...: This line calculates and prints the non-recursive Fibonacci number for N, along with its execution time using the timeit module. It also indicates the time complexity (O(n)) and space complexity (O(n)).
#
# fib_recur_list = [0] * (N + 1): This line creates a list called fib_recur_list with (N+1) elements, initialized to 0. This list will be used for memoization in the recursive Fibonacci function.
#
# fib_recur_list[0] = 0 and fib_recur_list[1] = 1: These lines set the first two elements of fib_recur_list to their initial values (0 and 1).
#
# print("Fibonacci recursive:\t", fibonacci_recursive(N), ...: This line calculates and prints the recursive Fibonacci number with memoization for N, along with its execution time using the timeit module. It also indicates the time complexity (O(n)) and space complexity (O(n)).
#
# Now, let's explain the purpose of using the timeit module and how it works:
#
# The timeit module is used to measure the execution time of a piece of code. In this code, it is used to measure the time taken by the fibonacci and fibonacci_recursive functions to calculate the Fibonacci numbers.
#
# timeit.timeit is a function provided by the timeit module. It takes two main arguments: a Python statement to be measured and a setup statement. It executes the statement multiple times (controlled by the number parameter) and returns the time taken to execute it.
#
# In this code, the timeit module is used to measure the execution time of the Fibonacci functions for a specified number of runs (1000 runs in this case).
#
# The setup parameter in timeit.timeit is used to provide any necessary setup code before measuring the time. It allows you to import the required functions and set any necessary variables.
#
# The execution time is printed along with the results of the Fibonacci calculations, providing a way to compare the performance of the two functions.
#
# The use of timeit helps obtain accurate and consistent timing results, which can be useful for benchmarking and profiling code to determine its efficiency.
#
# If you have more specific questions or need further clarification on any part of the code, please feel free to ask.




# questions on it___>
#
# Certainly! I'll provide a proper explanation of the code and then provide 20 questions along with their answers.
#
# Code Explanation:
# This code calculates Fibonacci numbers using both non-recursive and recursive methods. It also measures the execution time for each method and provides the time complexity and space complexity in the comments.
#
# Import the timeit module to measure the execution time.
#
# Define a non-recursive Fibonacci function, fibonacci(n), that calculates the Fibonacci number at index n. This function uses a list, fib_list, to store the Fibonacci numbers. It iterates through the list and calculates each Fibonacci number iteratively.
#
# Define a recursive Fibonacci function with memoization, fibonacci_recursive(n). It uses memoization to store previously calculated Fibonacci values to avoid redundant calculations. The fib_recur_list list is used for memoization.
#
# Set the value of N to 20, which represents the Fibonacci number you want to calculate, and RUNS to 1000, indicating the number of runs for measuring execution time.
#
# Print information about the value of N and the number of runs.
#
# Initialize fib_list with zeros and set the first two Fibonacci numbers.
#
# Measure the execution time and print the result for the non-recursive Fibonacci function.
#
# Initialize fib_recur_list with -1 to indicate uncalculated values and set the first two Fibonacci numbers.
#
# Measure the execution time and print the result for the recursive Fibonacci function with memoization.
#
# Provide comments with time and space complexities for both functions.
#
# Questions:
# What is the purpose of the timeit module in this code?
#
# Answer: The timeit module is used to measure the execution time of the Fibonacci functions.
# What is the purpose of the fibonacci function?
#
# Answer: The fibonacci function calculates Fibonacci numbers using a non-recursive method.
# How does the fibonacci function calculate Fibonacci numbers?
#
# Answer: It iteratively calculates Fibonacci numbers using a list to store the results.
# What is the N variable used for?
#
# Answer: The N variable represents the index of the Fibonacci number to be calculated.
# What is the purpose of the RUNS variable?
#
# Answer: RUNS indicates the number of times the code will run to measure execution time.
# How is memoization implemented in the fibonacci_recursive function?
#
# Answer: Memoization is implemented using the fib_recur_list list to store previously calculated Fibonacci numbers.
# What happens if n is equal to 0 in the fibonacci_recursive function?
#
# Answer: The function returns 0.
# What happens if n is equal to 1 in the fibonacci_recursive function?
#
# Answer: The function returns 1.
# Why is -1 used as an initial value in fib_recur_list?
#
# Answer: -1 indicates that a Fibonacci number at a given index has not been calculated yet.
# What is the time complexity of the non-recursive fibonacci function?
#
# Answer: The time complexity is O(n), where n is the index of the Fibonacci number.
# What is the space complexity of the non-recursive fibonacci function?
#
# Answer: The space complexity is O(n) because it uses a list to store the Fibonacci numbers.
# What is the time complexity of the recursive fibonacci_recursive function with memoization?
#
# Answer: The time complexity is O(n) because of memoization.
# What is the space complexity of the recursive fibonacci_recursive function with memoization?
#
# Answer: The space complexity is O(n) because it stores calculated Fibonacci numbers in a list.
# What is the result when N is set to 20 for both functions?
#
# Answer: Both functions calculate and return the 20th Fibonacci number, which is 6765.
# What is the purpose of using timeit for measuring execution time?
#
# Answer: timeit helps accurately measure the execution time of a function and allows for multiple runs to get a more reliable timing.
# How does the non-recursive Fibonacci function differ from the recursive one in terms of time complexity?
#
# Answer: The non-recursive function has a time complexity of O(n), while the recursive function has a time complexity of O(n) with memoization.
# What is the advantage of using memoization in the recursive Fibonacci function?
#
# Answer: Memoization reduces redundant calculations, making the recursive function more efficient.
# What are the primary limitations of the recursive Fibonacci function without memoization?
#
# Answer: It has exponential time complexity (O(2^n)), and it can be very slow for large values of n.
# What is the time complexity of the non-recursive Fibonacci function if N is increased?
#
# Answer: The time complexity remains O(n), regardless of the value of N.
# How would you modify this code to calculate and print the first N Fibonacci numbers rather than just the Nth Fibonacci number?
#
# Answer: You can modify the code to use a loop to calculate and print the first N Fibonacci numbers, storing them in a list or printing them directly within the loop.