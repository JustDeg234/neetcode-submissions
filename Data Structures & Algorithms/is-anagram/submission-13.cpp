class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> cnt;

        for (char s_char : s){
            cnt[s_char] += 1; //creates entry if empty
        }

        for (char t_char : t){
            if (--cnt[t_char] <0) return false;
        }

        return true;
    }
};
