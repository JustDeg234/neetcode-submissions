class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }

        unordered_map<char, int> cnt;

        for(int i=0; i<s.size(); i++){
            cnt[s[i]] += 1;
        }

        for(int j=0; j<t.size(); j++){
            if (cnt.find(t[j]) == cnt.end() || cnt[t[j]] == 0) return false;
            cnt[t[j]] -= 1;
        }
        return true;
    }
};
