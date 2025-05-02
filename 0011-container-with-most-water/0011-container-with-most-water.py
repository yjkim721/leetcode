class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            print(area, left, right)
            if max_water < area:
                max_water = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water