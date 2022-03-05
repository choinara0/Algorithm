import heapq
def solution(jobs):
    start = -1
    time_total, now, worked_job = 0, 0, 0
    jobs_heap = []
    while worked_job < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(jobs_heap, [job[1], job[0]])
        if jobs_heap:
            now_job = heapq.heappop(jobs_heap)
            start = now
            now += now_job[0]
            time_total += now - now_job[1]
            worked_job += 1
        else:
            now += 1
    time_avg = time_total // len(jobs)
    return time_avg

solution([[0, 3], [1, 9], [2, 6]]) #9