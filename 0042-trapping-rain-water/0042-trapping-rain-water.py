class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sorted_height_info = [(h, i) for i, h in enumerate(height)]
        sorted_height_info.sort(key=lambda x: -x[0])

        sorted_height = [ h for h, _ in sorted_height_info ]
        sorted_height_idxs = [ i for _, i in sorted_height_info ]
        
        cur_h = sorted_height[0]
        start_idx = sorted_height_idxs[0]
        end_idx = sorted_height_idxs[0]
        cnt = 0
        res = 0
        for h, idx in zip(sorted_height, sorted_height_idxs):
            if h == cur_h:
                start_idx = min(start_idx, idx)
                end_idx = max(end_idx, idx)
                cnt += 1
                continue
            if h != cur_h:
                res += ((end_idx - start_idx) - (cnt - 1)) * (cur_h - h)
                start_idx = min(start_idx, idx)
                end_idx = max(end_idx, idx)
                cur_h = h
                cnt += 1
        return res
