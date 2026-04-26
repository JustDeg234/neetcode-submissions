class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int curr = 0; //needs initial comparision

        for (int i=0; i<nums.size(); i++){
            curr = curr ^ nums[i];
        }
        return curr; //xor associative and commutative properties reveal the a ^ 0 = a while rest b ^ b = 0
    }
};
