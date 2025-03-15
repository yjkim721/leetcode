class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [ gas[i] - cost[i] for i in range(0, len(gas)) ]
        sorted_indices = sorted(range(len(diff)), key=lambda i: diff[i], reverse=True)
        for max_idx in sorted_indices:
            tank = 0
            success = True
            for i in range(0, len(gas)):
                new_idx = max_idx + i if max_idx + i < len(gas) else max_idx + i - len(gas)
                tank +=  gas[new_idx] - cost[new_idx]
                if tank < 0:
                    success = False
                    break
            if success:
                return max_idx
        return -1