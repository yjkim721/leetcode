class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for s in strs:
            print(prefix)
            if not prefix:
                return prefix
            prefix = self.common_prefix(s, prefix)
            
        return prefix

    def common_prefix(self, a, b):
        max_i = min(len(a), len(b))
        for i in range(max_i):
            if a[i] == b[i]:
                continue
            else:
                return a[:i]
        if len(a) < len(b):
            return a
        else:
            return b