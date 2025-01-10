class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = nums[0]
        n_cnt = 1
        i = 1
        k = 1

        if len(nums) <= 2:
            return len(nums)

        while i < len(nums):
            if nums[i] == n:
                n_cnt += 1
                if n_cnt == 2:
                    nums[k] = nums[i]
                    k += 1
            else:
                nums[k] = nums[i]
                n = nums[i]
                n_cnt = 1
                k += 1
            i += 1

        if k < len(nums):
            nums[k] = nums[-1]
        return k