//max heap solution 
//O(n logn) time [heap] and O(n) space [bucket]
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for(int n:nums){
            count[n]++; // (nums value, occurrences)
        }

        auto comp = [](pair<int, int>& a, pair<int, int>& b){ //lambda
            return a.second < b.second; //max heap of frequencies
        };
        priority_queue<pair<int, int>, vector<pair<int,int>>, decltype(comp)> heap(comp); //use priority queue to create max heap

        for (auto& entry:count){ //O(nlogn) for adding heap O(logn) n times
            heap.push({entry.first, entry.second});//push tuple onto max heap
        }

        vector<int> res;
        while(k-- > 0){
            res.push_back(heap.top().first);
            heap.pop(); //O(logm) k times = O(klogm), space O(k)
        }
        return res;
    }
};
