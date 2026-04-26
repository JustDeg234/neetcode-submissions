class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pairs; //<nums element, index>

        for(int i=0; i<nums.size(); i++){
            if(pairs.find(target - nums[i]) != pairs.end()) return {pairs[target-nums[i]],i};
            pairs[nums[i]] = i;
            
        }
        return {};
    }
};
