class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        pos, jump, jump_cnt = 0, nums[0], 1
        while True:
            max_pos = 0
            for idx in range(pos, pos+jump):
                if idx < len(nums) and max_pos < idx + nums[idx]:
                    max_pos = idx + nums[idx]
                if idx == len(nums)-1:
                    return jump_cnt
            jump_cnt += 1
            pos = max_pos