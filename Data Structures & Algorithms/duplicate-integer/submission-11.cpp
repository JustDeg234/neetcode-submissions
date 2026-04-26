class Solution{
    public:
        bool hasDuplicate(vector<int> &nums){
            std::unordered_set<int> curr;
            for (int i=0; i<nums.size(); i++) { //num = nums[i] in cpp: for(int num:nums)
                if (curr.find(nums[i]) != curr.end()) return true;
                curr.insert(nums[i]);
            }
            return false;
        }
};