"""
LeetCode 933 - Number of Recent Calls

Implement RecentCounter that counts the number of recent requests
within a certain time frame.

    - RecentCounter()  -> Initializes with zero requests.
    - ping(t)          -> Adds a new request at time t and returns the
                          number of requests in the range [t-3000, t].

Example:
    rc = RecentCounter()
    rc.ping(1)      # -> 1
    rc.ping(100)    # -> 2
    rc.ping(3001)   # -> 3
    rc.ping(3002)   # -> 3  (request at t=1 is now outside the window)

Constraints:
    - 1 <= t <= 10^9
    - Each t is strictly larger than the previous.
    - At most 10^4 calls to ping.

Hint: Use a queue (deque). On each ping, add t and remove all entries
      that are < t - 3000.
"""

from collections import deque


class RecentCounter:

    def __init__(self):
        pass

    def ping(self, t: int) -> int:
        pass


rc = RecentCounter()
print(rc.ping(1))     # Expected: 1
print(rc.ping(100))   # Expected: 2
print(rc.ping(3001))  # Expected: 3
print(rc.ping(3002))  # Expected: 3
