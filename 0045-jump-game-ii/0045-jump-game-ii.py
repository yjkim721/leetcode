class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        pos, jump, jump_cnt = 0, nums[0], 1
        while True:
            max_pos, new_pos = 0, 0
            print(pos, jump)
            for idx in range(pos, pos+jump+1):
                if idx < len(nums) and max_pos < idx + nums[idx]:
                    max_pos = idx + nums[idx]
                    new_pos = idx
                if idx == len(nums)-1:
                    return jump_cnt
            jump_cnt += 1
            pos = new_pos
            jump = nums[pos]