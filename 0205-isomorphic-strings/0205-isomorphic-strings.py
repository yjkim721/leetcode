class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pos = {}
        for i, c in enumerate(s):
            l = s_pos.get(c,[])
            l.append(i)
            s_pos[c] = l
        s_items = s_pos.values()
        s_items.sort(key=lambda x: x[0])

        t_pos = {}
        for i, c in enumerate(t):
            l = t_pos.get(c,[])
            l.append(i)
            t_pos[c] = l
        t_items = t_pos.values()
        t_items.sort(key=lambda x: x[0])

        if len(t_items) != len(s_items):
            return False
        
        for t, s in zip(t_items, s_items):
            if t != s:
                return False
        return True
