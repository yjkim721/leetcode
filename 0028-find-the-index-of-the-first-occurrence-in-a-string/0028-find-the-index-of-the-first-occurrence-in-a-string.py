class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_haystack = len(haystack)
        n_needle = len(needle)

        for i in range(n_haystack - n_needle + 1):
            substr = haystack[i:i+n_needle]
            print(substr)
            if substr == needle:
                return i

        return -1