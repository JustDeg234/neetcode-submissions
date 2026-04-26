class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for c in s: #remove all whitespace and non-alphanumerical by only adding alphanumerical to output string
            if c.isalnum():
                output += c.lower() #add char to string (string immutability leads to creation of string each time)
        return output == output[::-1] #is alphanumerical string a palindrome?