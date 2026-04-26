class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numbers; //set of unique elements, O(1) operation due to hashing
        for(auto num:nums){
            if (numbers.find(num) != numbers.end()) return true;

            numbers.insert(num);
        }
        return false;
    }
};