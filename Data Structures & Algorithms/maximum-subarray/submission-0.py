class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=mx_sum=nums[0]
        for num in nums[1:]:
            curr_sum=max(curr_sum+num,num)
            mx_sum=max(mx_sum,curr_sum)
        return mx_sum