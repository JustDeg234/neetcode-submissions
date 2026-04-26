public class Solution{
    public List<List<string>> GroupAnagrams(string[] strs){
        var arr = new Dictionary<string, List<string>>();

        foreach(string s in strs){
            //string key = s;
            //Array.Sort(key); doesnt work on immutable strings in csharp, plus strings arent even char arrays
            char[] chars = s.ToCharArray();
            Array.Sort(chars);
            string key = new string(chars);
            
            if (!arr.ContainsKey(key)) arr[key] = new List<string>();
            arr[key].Add(s);
            //arr[key] = arr.GetValueOrDefault(s) + 1; only works for string not list of strings
        }

        List<List<string>> res = new List<List<string>>();
        foreach(var group in arr.Values){
            res.Add(group);
        }

        return res;
    }
}
