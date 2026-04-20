
from typing import List
from collections import Counter

def least_interval(tasks: List[str], n: int) -> int:

    task_count = Counter(tasks)
    max_count = 0
    max_freq = max(task_count.values())

    for freq in task_count.values():
        if freq == max_freq:
            max_count += 1

    framesize = (max_freq - 1) * (n+1) + max_count

    return max(len(tasks), framesize)


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2

    print(least_interval(tasks, n))
