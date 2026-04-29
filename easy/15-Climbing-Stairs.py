class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        first, second = 1, 2

        for i in range(3, n + 1):
            first, second = second, first + second

        return second
