
class Solution{
    public:
    vector<vector<string>> groupAnagrams(vector<string>& strs){
        unordered_map<string, vector<string>> arr; //group anagrams by unique lexicographically sorted key

        for(string& s:strs){
            string key = s;
            sort(key.begin(), key.end());
            arr[key].push_back(s); //pushback to vector
        }

        vector<vector<string>> res;

        for(auto& entry:arr){
            res.push_back(entry.second); //grabs vectir if strings
        }
        return res;
    }
};
