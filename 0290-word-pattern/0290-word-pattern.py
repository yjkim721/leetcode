class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_map = {}
        for idx, p in enumerate(pattern):
            c = pattern_map.get(p, [])
            c.append(idx)
            pattern_map[p] = c
        ps = pattern_map.values()
        ps.sort(key=lambda x: x[0])
        
        word_map = {}
        words = s.split(" ")
        for idx, word in enumerate(words):
            c = word_map.get(word, [])
            c.append(idx)
            word_map[word] = c
        ws = word_map.values()
        ws.sort(key=lambda x: x[0])

        if len(ws) != len(ps):
            return False
        
        for p, w in zip(ps, ws):
            if p != w:
                return False
        return True