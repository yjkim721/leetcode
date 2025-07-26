class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i, n in enumerate(nums):
            l = m.get(n, [])
            l.append(i)
            m[n] = l

        for i, n in enumerate(nums):
            m_idxs = m.get(n)
            for m_i in m_idxs:
                if abs(m_i - i) > 0 and abs(m_i - i) <= k:
                    return True
        
        return False
