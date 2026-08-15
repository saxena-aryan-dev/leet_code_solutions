class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor_all = 0
        
        for num in nums:
            xor_all ^= num
        
        # Entire array works
        if xor_all != 0:
            return len(nums)
        
        # Need to remove one non-zero element
        for num in nums:
            if num != 0:
                return len(nums) - 1
        
        # All zeros
        return 0