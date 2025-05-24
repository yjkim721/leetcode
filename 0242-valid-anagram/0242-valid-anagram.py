class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        for c in s:
            cnt = s_map.get(c, 0)
            cnt += 1
            s_map[c] = cnt
        s_r = sorted(s_map.items())

        t_map = {}
        for c in t:
            cnt = t_map.get(c, 0)
            cnt += 1
            t_map[c] = cnt
        
        t_r = sorted(t_map.items())

        if len(s_r) != len(t_r):
            return False

        for a, b in zip(s_r, t_r):
            if a != b:
                return False
        return True
        