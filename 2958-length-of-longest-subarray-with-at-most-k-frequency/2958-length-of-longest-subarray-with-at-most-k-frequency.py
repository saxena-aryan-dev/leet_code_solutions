from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            count[x] += 1
            while count[x] > k:          # only x can be the offender
                count[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans