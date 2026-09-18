class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map <int,int> hsm;
        for (int i = 0; i<nums.size();i++) {
            if (hsm.find(nums[i]) != hsm.end()) return true;
            hsm[nums[i]]=i;
        }
        return false;
    }
};