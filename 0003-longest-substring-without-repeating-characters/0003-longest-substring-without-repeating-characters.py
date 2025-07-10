class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i = 0
        max_length = 1
        ans = ''
        while i < len(s):
            for j in range(i+1, len(s)):
                set_s = set(s[i:j+1])
                l = j - i + 1
                unique = len(set_s) == l
                if unique and l > max_length:
                    ans = s[i:j+1]
                    max_length = l
                elif not unique:
                    break
            i = i + 1
        return max_length
                
