class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_ptr, n_ptr = (0, 0)
        for _ in range(n):
            nums1.pop()

        while m_ptr < m and n_ptr < n:
            if nums1[m_ptr] >= nums2[n_ptr]:
                nums1.insert(m_ptr, nums2[n_ptr])
                n_ptr += 1
                m += 1
            else:
                m_ptr += 1

        if n_ptr < n:
            nums1 += nums2[n_ptr:]            
         