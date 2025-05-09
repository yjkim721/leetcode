class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while numbers[i] + numbers[j] != target:
            print(i, j)
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

        return [i+1, j+1]