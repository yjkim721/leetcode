class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for r in ransomNote:
            if r in magazine:
                idx = magazine.index(r)
                magazine[idx] = 1
            else:
                return False
        return True