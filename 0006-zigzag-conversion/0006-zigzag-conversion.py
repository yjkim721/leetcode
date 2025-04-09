import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        res = [{'x': 1, 'y': 1, 'value': s[0]}]
        x, y = 1, 1
        dir_x, dir_y = 0, 1
        max_x = 0
        for idx, c in enumerate(s[1:]):
            if y == numRows:
                dir_x, dir_y = 1, -1
            if y == 1:
                dir_x, dir_y = 0, 1
            x = x + dir_x
            y = y + dir_y
            max_x = max(x, max_x)
            res.append({'x': x, 'y': y, 'value': c})
        res.sort(key=lambda elem: elem['x'] + (elem['y'] - 1) * max_x)
        return ''.join([ e['value'] for e in res ])