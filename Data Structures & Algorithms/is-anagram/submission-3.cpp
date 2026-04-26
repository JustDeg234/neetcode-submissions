class Solution{
    public:
        bool isAnagram(string s, string t){
            //base case, unequal lengths
            if(s.length() != t.length()){
                return false;
            }

            //use dictionary by keying each char and valueing their instances.
            unordered_map<char, int> counter;

            for(char ch:s){
                counter[ch] = counter[ch] + 1; //if not already in dict, its key is added automatically with initial value 0
            }
            //string s fully parsed and stored in counter

            for(char ch:t){
                if (counter.find(ch) == counter.end() || counter[ch] == 0) //logical operators evalute arguments safely
                    {return false;} //if the char from counter array isnt found or was never there when compared to t string, then no anagram 
                counter[ch] = counter[ch] - 1; //s already parsed and compared
            }
            //if successfully, yes anagram
            return true;
        }
};