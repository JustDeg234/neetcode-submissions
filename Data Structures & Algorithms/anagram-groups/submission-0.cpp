class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> ans; //group of anagrams parsed by lexicographically sorted key

        for(string& s:strs){
            string key = s;
            sort(key.begin(),key.end()); //string = array of chars that can be sorted
            ans[key].push_back(s); //if anagram, key will remain the same, push_back to append to vector (type consistency)
        }

        vector<vector<string>> res;
        for(auto& entry:ans){ //entry can refer to key or value in ans map
            res.push_back(entry.second);
        }
        return res;
    }
};
