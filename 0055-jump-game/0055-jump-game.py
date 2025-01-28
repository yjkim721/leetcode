class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        jump = nums[0]
        for pos in range(len(nums)):
            print(pos, jump)
            if pos >= len(nums)-1:
                return True
            if jump < nums[pos]:
                jump = nums[pos]
            if jump == 0:
                return False
            jump -= 1
        return False
