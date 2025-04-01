class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(' ')
        words.reverse()
        words = [ w for w in words if w] 
        return ' '.join(words)
        