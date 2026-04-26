//Bucket Sort Solution: each indices has their own "bucket" 
// O(n) linear time if array is bounded, and this can happen only if we map the count each value could have (size of array) at worst all numbers are equal and thus one bucket is full, or all numbers are distinct and all buckets have one item.
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count; //hashmap to count occurances of each value

        for (int n:nums){
            count[n]++; //ex: {[1,1], [2,2], [3,3]} = (nums value, occurances)
        }
        /*
        for (int i=0; i<nums.size(); i++){
            count[nums[i]]++; //hashmap creates key:value pair if null, parsed by each integer from 0 to nums-1
        }
        */

        vector<vector<int>> freq(nums.size() + 1); //array of arrays, indexed by the frequency of each nums (limited by nums size(one single number can occur at max the size of the array)
        //freq vector of "num.size() + 1" empty vectors with no heap space used yet

        for (auto& pairs:count){ //count hashmap is parsed by each nums value and stores how many times each element occured
            freq[pairs.second].push_back(pairs.first); //freq[].push_back(); pushes (item) into [index] of vector freq, in this case the item is added into a vector
        }

        //we want top k elements
        vector<int> res;
        for (int i=freq.size()-1; i>=0; i--){ //descending order, most frequent
            for (int j=0; j<freq[i].size(); j++){ //each element of freq is a sublist that can be parsed to find either nothing or the numbers occuring i times
                res.push_back(freq[i][j]); //freq[i] is the bucket(vector) of numbers that appear i times, freq[i][j] accesses the jth number in that bucket
                if (res.size() == k) return res;
            }
        }
        return {}; //empty vector
    }
};
