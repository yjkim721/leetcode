class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for idx, n in enumerate(nums):
            m[n] = idx
        
        for idx, n in enumerate(nums):
            remain_num = target - n
            remain_num_idx = m.get(remain_num, None)
            if remain_num_idx is None:
                continue
            if remain_num_idx == idx:
                continue
            else:
                return [idx, remain_num_idx]