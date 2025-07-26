class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = {}
        while n != 1:
            digits = []
            while n >= 1:
                d = n % 10
                n = n / 10
                digits.append(d * d)
            n = sum(digits)
            v = result.get(n, 0)
            if v == 0:
                result[n] = 1
            else:
                return False
        return True