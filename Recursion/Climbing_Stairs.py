# O(2^n) time complexity, not optimal solution!! 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n-2) + self.climbStairs(n-1)

        # a = 0
        # b = 1
        # for i in range(n):
        #     c = a + b
        #     a = b
        #     b = c

        # return c
