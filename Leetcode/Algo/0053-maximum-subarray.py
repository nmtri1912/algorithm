class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            if num > num + cur_sum:
                cur_sum = num
            else:
                cur_sum+=num
            max_sum = max(max_sum, cur_sum)
        return max_sum
