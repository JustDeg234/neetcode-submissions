public class Solution {
    public int[] TopKFrequent(int[] nums, int k){
        var cnt = new Dictionary<int, int>();
        foreach(var n in nums){
            cnt[n] = cnt.GetValueOrDefault(n) + 1;
        }

        // C#, like python or JS, priority queue is a min heap
        // simulate max heap property by negating frequency
        var heap = new PriorityQueue<int, int>();

        //populate with tuple
        foreach (var entry in cnt){
            heap.Enqueue(entry.Key, -entry.Value);
        } 

        var res = new List<int>();
        while(k-- > 0){
            res.Add(heap.Dequeue());
        }
        return res.ToArray(); //C# arrays are preferred: garbage-collected, safe, matches java return type
    }
}