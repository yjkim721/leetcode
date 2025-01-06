class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt, i = 0, 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                cnt += 1
                i += 1
        return cnt
