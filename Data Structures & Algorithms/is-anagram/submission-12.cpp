class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> cnt;

        for (char s_char : s){
            cnt[s_char] += 1; //creates entry if empty
        }

        for (char t_char : t){
            if (cnt.find(t_char) == cnt.end() || cnt[t_char] == 0) return false;
            cnt[t_char] -= 1;
        }

        return true;
    }
};
