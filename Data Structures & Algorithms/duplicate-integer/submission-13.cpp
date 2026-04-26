class Solution {
public:
    bool hasDuplicate(vector<int> &nums) {
                //once passed to a function, arrays lose knowledge of their size, only a pointer
        unordered_set<int> numbers;
        for (int i=0; i<nums.size(); i++){
            if (numbers.find(nums[i]) != numbers.end()) return true; //duplicate found
            //otherwise add on
            numbers.insert(nums[i]);
        }
        return false;
    }
};