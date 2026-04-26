//using Systems.Collections.Generics

public class Solution
{
    public int[] TwoSum(int[] nums, int target){
        var pairs = new Dictionary<int, int>(); //value, index

        for (int i=0; i<nums.Length; i++){
            int complement = target - nums[i];
            if(pairs.TryGetValue(complement, out int j)) return new int[] {j, i};
            pairs[nums[i]] = i;
        }
        return new int[0];
    }
}