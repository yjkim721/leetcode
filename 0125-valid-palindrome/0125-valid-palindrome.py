class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ''
        for c in s:
            if 'A' <= c and c <= 'Z':
                a += c.lower()
            elif 'a' <= c and c <= 'z':
                a += c
            elif '0' <= c and c <= '9':
                a += c
        len_a = len(a)
        for i in range(len_a):
            if a[i] != a[len_a - i -1]:
                return False
        return True