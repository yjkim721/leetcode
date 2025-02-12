class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        idx = len(s) - 1
        letter_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        while idx >= 0:
            if idx+1 < len(s) and s[idx:idx+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                ret -= letter_dict[s[idx]]
            else:
                ret += letter_dict[s[idx]]
            idx -= 1
        return ret