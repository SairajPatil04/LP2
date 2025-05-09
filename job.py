def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    result = [None] * n
    slot = [False] * n
    total_profit = 0  

    for job in jobs:
        job_id, deadline, profit = job
        for j in range(min(deadline, n) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job
                total_profit += profit  
                break

    print("Scheduled Jobs:")
    for job in result:
        if job:
            print(job)
    print("Total Profit:", total_profit)

# Example input
jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
job_scheduling(jobs)
