class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            sub=(target-nums[i])
            if sub in nums and nums.index(sub)!=i:

                return [i,nums.index(sub)]
        return []        