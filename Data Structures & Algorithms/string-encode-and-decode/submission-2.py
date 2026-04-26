class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            #FP: use a unique identifier that allows for decoding of any sequence of unicode
            #WP: store each strings metadata by containing its int length followed by any character 
            encoded_string += str(len(s)) + "@" + s
        return encoded_string

    def decode(self, string: str) -> List[str]:
        strs = [] #list init
        i = 0
        #FP: 
        #WP: read in length of string until @ to signify start of string, then return string via encoded_string[lower bound:upperbound]
        while i < len(string):
            #step 1) start of length window
            j = i 
            while string[j] != '@':
                #step 2) end of length window
                j += 1
            #step 3) grab length of string in integer form
            length = int(string[i:j])
            #step 4) move lower bound
            i = j + 1
            j = i
            #step 5) move upper bound
            j += length
            #step 6) store string
            strs.append(string[i:j])
            #step 7) reset lower bound
            i = j
        return strs