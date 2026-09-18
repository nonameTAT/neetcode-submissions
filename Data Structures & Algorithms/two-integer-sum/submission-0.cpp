class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> ht;
        for (int i = 0; i < nums.size(); i++) {
            if (ht.find(target-nums[i])!=ht.end()) {
                return {ht[target-nums[i]],i};
            } else {
                ht[nums[i]] = i;
            }
        }
        return {};
    }
};
