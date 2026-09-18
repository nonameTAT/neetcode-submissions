class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                curr_len=1
                while curr_len+num in num_set:
                    curr_len+=1
                longest=max(longest,curr_len)
        return longest