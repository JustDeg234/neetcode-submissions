//max heap solution 
//O(n logn) time [heap] and O(n) space [bucket]

class Solution {
    public:
    vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int, int> count; //dict to key by number value and store frequency
        for(int n:nums){
            count[n]++;
        }

        //lambda function to redefine how priority queue chooses "greater" element for max heap creation
        auto comp = [](pair<int,int>&a, pair<int,int>&b){
            return a.second < b.second; //true means b has higher priority
        };
        priority_queue<pair<int,int>, vector<pair<int, int>>, decltype(comp)> heap(comp); //create a heap with instructions from comp

        for (auto& entry:count){ //O(nlogn) for adding elements to a heap O(logn) n times
            heap.push({entry.first, entry.second}); //push tuple onto max heap
        }

        vector<int> res;
        while(k-- > 0){
            res.push_back(heap.top().first);
            heap.pop(); //O(logm) k times = O(klogm + nlogn), space O(k)
        }

        return res;
    }
};