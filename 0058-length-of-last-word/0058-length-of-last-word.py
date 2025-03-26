class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        cur_cnt = 0
        for c in s:
            if c == ' ':
                cur_cnt = 0
            else:
                cur_cnt += 1
        return cur_cnt