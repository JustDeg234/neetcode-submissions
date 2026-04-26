class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> counter; //each char will index frequency of instances

        for (int i=0; i<s.length(); i++){
            counter[s[i]] += 1; //if not in dict, char key will be added
        }

        for (char ch : t){
            if (counter.find(ch) == counter.end() || counter[ch] == 0){
                return false;
            }
            counter[ch] -= 1;
        }
        return true;
    }
};
