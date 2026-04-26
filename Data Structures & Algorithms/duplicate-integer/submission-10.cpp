class Solution {
    public:
        bool hasDuplicate(vector<int> &nums){
            int n = nums.size(); //O(1), c++ STL container sequence like vector has size stored as integer member variabale within vector struct, updated on each operation 
            for(int i=0; i<n; i++){
                for(int j=i+1; j<n; j++){
                    if (nums[i]==nums[j]) return true;
                }
            }
            return false;
        }
};