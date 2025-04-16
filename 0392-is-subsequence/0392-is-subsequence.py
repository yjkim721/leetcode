class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx = 0

        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        for t_idx in range(len(t)):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            if s_idx == len(s):
                break
        return s_idx == len(s)