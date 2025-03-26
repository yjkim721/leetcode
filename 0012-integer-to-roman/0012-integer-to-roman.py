class Solution(object):
    def intToRoman(self, num):
        m = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        s = ''
        dividers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        div_idx = 0
        while num != 0:
            while num >= dividers[div_idx]:
                num -= dividers[div_idx]
                s += m[dividers[div_idx]]
            div_idx += 1
        return s
        
        