class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        for idx in range(len(nums)):
            pos = idx + nums[idx]
            if pos == len(nums)-1:
                return True
        return False
