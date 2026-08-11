class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1] + 1:
                break
            total += nums[j]
        
        seen = set(nums)
        x = total
        while x in seen:
            x += 1
        return x