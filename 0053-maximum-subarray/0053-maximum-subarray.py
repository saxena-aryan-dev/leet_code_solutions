class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        total = 0
        for x in nums:
            total = max(x, total + x)
            maxi = max(maxi, total)
        return maxi