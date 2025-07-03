class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            ac = a.get(sorted_s, [])
            ac.append(s)
            a[sorted_s] = ac
        
        return a.values()