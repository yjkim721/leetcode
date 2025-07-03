class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i, j, k = (0, 1, 2)
        
        m = {}

        for idx, n in enumerate(nums):
            m[n] = idx

        ret = set()
        for idx1 in range(len(nums)-2):
            i = idx1
            for idx2 in range(i+1, len(nums)-1):
                j = idx2
                last_num = 0 - nums[idx1] - nums[idx2]
                last_num_idx = m.get(last_num, None)
                if last_num_idx != None and last_num_idx > j:
                    k = last_num_idx
                    sorted_e = sorted([nums[i], nums[j], nums[k]])
                    ret.add(tuple(sorted_e))

        real_ret = []
        for e in ret:
            real_ret.append(list(e))
        
        return real_ret