class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> pairs; //curr nums element, curr index because we want to find the index it was originally

        for(int i=0; i<nums.size();i++){ //key is to return index tuple
            if(pairs.find(target-nums[i]) != pairs.end()) return {pairs[target-nums[i]], i};
            pairs[nums[i]] = i;
        }
        return {};
    }
};
