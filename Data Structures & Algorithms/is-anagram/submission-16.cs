public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var cnt = new Dictionary<char, int>();
        //Dictionary<char, int> cnt = new Dictionary<char, int>();

        foreach (var c in s)
            cnt[c] = cnt.GetValueOrDefault(c) + 1; //C# doesnt auto-create keys, avoids boilerplate code

        foreach(var c in t)
            if (!cnt.ContainsKey(c) || --cnt[c] < 0) return false; //Never touch dict[key] before proving the key exists.

        return true;
        
    }
}
