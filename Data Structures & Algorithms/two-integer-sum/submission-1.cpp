class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pairIDx;

        for(int i=0; i<nums.size(); i++){
            int num = nums[i]; //current element
            if (pairIDx.find(target - num) != pairIDx.end()) return {pairIDx[target - num], i};//checks if the other opperand exists within the list.
            pairIDx[num] = i; //<key: element, value: index> so we can parse the operand value for the index
            //i will always be > than the pairIDx[target-num] due to insertation after check, and pairIDx holding only values < i.
        }
        return {};
    }
};
