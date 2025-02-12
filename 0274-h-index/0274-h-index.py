class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted = citations.sort()
        idx = len(citations) - 1
        h_index = 0
        while idx >= 0:
            n = len(citations) - idx
            new_index = min(citations[idx], n)
            h_index = max(h_index, new_index)
            idx -= 1
        return h_index
