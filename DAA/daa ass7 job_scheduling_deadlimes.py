def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline to create a schedule array
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [0] * (max_deadline + 1)

    total_profit = 0
    scheduled_jobs = []

    for job in jobs:
        deadline, profit = job[1], job[2]

        # Find the latest available slot for the job
        for i in range(deadline, 0, -1):
            if schedule[i] == 0:
                schedule[i] = job[0]
                total_profit += profit
                scheduled_jobs.append(job[0])
                break

    return scheduled_jobs, total_profit

# Example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
scheduled_jobs, total_profit = job_sequencing(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)


























# #explanation;
#
# explain me the code line by line
# ChatGPT
# Certainly! Here's a detailed explanation of the job sequencing code line by line:
#
# python
# Copy code
# def job_sequencing(jobs):
# This line defines a function named job_sequencing that takes a list of jobs as input.
#
# python
# Copy code
#     jobs.sort(key=lambda x: x[2], reverse=True)
# This line sorts the list of jobs in descending order based on the profit of each job (the third element in each job tuple).
#
# python
# Copy code
#     max_deadline = max(jobs, key=lambda x: x[1])[1]
# This line finds the job with the highest deadline and assigns it to max_deadline. It uses the max function with a key to extract the deadline (the second element in each job tuple) and then takes the deadline value.
#
# python
# Copy code
#     schedule = [0] * (max_deadline + 1)
# Here, we initialize a list called schedule with zeros. This list represents the time slots available for scheduling jobs. The length of the list is max_deadline + 1.
#
# python
# Copy code
#     total_profit = 0
#     scheduled_jobs = []
# We initialize total_profit to keep track of the total profit earned and an empty list scheduled_jobs to store the sequence of scheduled jobs.
#
# python
# Copy code
#     for job in jobs:
# This line starts a loop to iterate through the sorted list of jobs.
#
# python
# Copy code
#         deadline, profit = job[1], job[2]
# Inside the loop, we extract the deadline and profit from the current job.
#
# python
# Copy code
#         for i in range(deadline, 0, -1):
# This nested loop iterates from the job's deadline down to 1 (inclusive), searching for a time slot to schedule the job. It works backward to schedule jobs with earlier deadlines first.
#
# python
# Copy code
#             if schedule[i] == 0:
# Here, we check if the current time slot i is available (indicated by schedule[i] being 0).
#
# python
# Copy code
#                 schedule[i] = job[0]
# If the time slot is available, we schedule the current job by storing its ID (the first element of the job tuple) in the schedule list.
#
# python
# Copy code
#                 total_profit += profit
# We update the total profit by adding the profit of the current job.
#
# python
# Copy code
#                 scheduled_jobs.append(job[0])
# We add the job's ID to the scheduled_jobs list to keep track of the sequence in which jobs are scheduled.
#
# python
# Copy code
#                 break
# The break statement is used to exit the inner loop as soon as the job is scheduled.
#
# python
# Copy code
#     return scheduled_jobs, total_profit
# Finally, the function returns a tuple containing scheduled_jobs (the sequence of scheduled jobs) and total_profit (the total profit earned).
#
# The example usage provided at the end demonstrates how to use the job_sequencing function with a list of jobs, and it prints the scheduled jobs and the total profit.
