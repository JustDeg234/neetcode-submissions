/* 
Goal: if the array contains duplicates, return true
Inputs:
    vector of integers "nums"
Outputs:
    boolean indicating duplicate existance

class Solution
{
    public:
        bool hasDuplicate(vector<int> &nums)
        {
            int n = nums.size();

            for (int i = 0; i < n; ++i)
            {
                for (int j = i + 1; j < n; ++j)
                {
                    if (nums[i]==nums[j]) return true;
                }
            }
            return false;
        }
};
//Time Complexity: O(n^2)
//Space Complexity: O(1)

*/

/*
Use Sorting Algorithm (Time O(nlogn)) and use two pointer method (Space O(1))
*/
class Solution
{
    public:
        bool hasDuplicate(const std::vector<int> &nums) //address of num so the vector argument passed is in the same location throughout call and procedure
        {
            std::unordered_set<int> curr; //hashmap ds. allows for average-case constant-time O(1) lookups and insertions

            for (int num : nums) //goes through each element in the collection nums, storing the value in num each iteration
            {
                if (curr.find(num) != curr.end()) return true; //if find(num) returns end(), num is not present in the set, thus add into since its not a duplicate
                curr.insert(num);
            }
            return false;
        }
        
//Time Complexity: O(n)
//Space Complexity: O(n)
};


