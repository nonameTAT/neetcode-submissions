class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        seen={}
        for i in range(0,len(nums)):
            needed = target - nums[i]
            if needed not in seen:
                seen[nums[i]]=i
            else:
                return [seen[needed],i]
