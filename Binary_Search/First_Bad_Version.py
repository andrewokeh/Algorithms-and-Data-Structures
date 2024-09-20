# https://leetcode.com/problems/first-bad-version/description/
# 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n

        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1

        return first
