class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = '' #string init
        for s in strs:
            encoded_string += str(len(s)) + "@" + s
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        strs = [] #list init
        i = 0
        #WP: establish bounds at start and end of strings, then add to array
        #serialization framwork
        while i < len(s):
            j = i #upper bound = lower bound
            while s[j] != "@":
                j += 1
            length = int(s[i:j]) #from 0 to 1 to find the int length
            i = j + 1
            j = length + i
            strs.append(s[i:j])
            i = j #reset lower bound
        return strs
            