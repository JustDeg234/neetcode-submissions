public class Solution {
    public bool hasDuplicate(int[] nums){
        
        HashSet<int> curr = new HashSet<int>();

        foreach (int num in nums)
        {
            if (curr.Contains(num)) return true;
            curr.Add(num);
        }
        return false;
    }
}