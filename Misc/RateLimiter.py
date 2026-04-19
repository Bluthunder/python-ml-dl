from collections import deque
import time

class RateLimiter:

    def __init__(self, capacity:int, window:int):
        self.capacity = capacity
        self.window = window
        self.q = deque()

    def allow(self)->bool:
        now = time.time()

        # Remove old requests
        while self.q and self.q[0] <= now - self.window:
            self.q.popleft()

        if len(self.q) < self.capacity:
            self.q.append(now)
            return True

        return False
