
/*
public class Solution {
    public bool hasDuplicate(int[] nums){
        int n = nums.Length; //nums.size(); in c++
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i]==nums[j]) return true;
            }
        }
        return false;
    }
}
*/

public class Solution {
    public bool hasDuplicate(int[] nums){
        
        HashSet<int> curr = new HashSet<int>(); //std::unordered_set<int> curr

        foreach (int num in nums) //for (num : nums)
        {
            if (curr.Contains(num)) return true; //if (curr.find(num) != curr.end()) return true;
            curr.Add(num); //curr.insert(num);
        }
        return false;
    }
}