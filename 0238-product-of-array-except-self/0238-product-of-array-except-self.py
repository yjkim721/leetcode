class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        p = 1
        s = 1
        for i in range(0, len(nums)):
            p *= nums[i]
            s *= nums[len(nums)-i-1]
            if i+1 < len(nums):
                output[i+1] *= p
            if len(nums)-i-2 >= 0:
                output[len(nums)-i-2] *= s
        return output
        