//max heap solution 
//O(n logn) time [heap] and O(n) space [bucket]

class Solution{
    public: vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int,int> cnt; //key by element, value by frequency
        //populate dict
        for(int n:nums){
            cnt[n] += 1;
        }

        //create max heap
        auto comp = [](pair<int,int>& a, pair<int, int>& b){
            return a.second < b.second; //we want true to mean b has higher priority, otherwise a has default higher priority
        };
        priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(comp)> heap(comp); //create priority queue heap

        //populate max heap with each element from dict alongside its frequency, max heap sorts full array in nlogn time
        for (auto& entry:cnt){
            heap.push({entry.first, entry.second}); //tuple
        }

        vector<int> res;
        //return k most frequent elements
        while(k-- > 0){ //n * logn time
            res.push_back(heap.top().first);
            heap.pop(); //log n time
        }
        return res;
    }
};
