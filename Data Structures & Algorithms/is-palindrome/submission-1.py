class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for c in s: #remove all whitespace and non-alphanumerical by only adding alphanumerical to output string
            if c.isalnum():
                output.append(c.lower()) #list are mutable, thus we are able to append and then later join to a string
            ostr = ''.join(output)
        return output == output[::-1] #is alphanumerical string a palindrome?
        #using strings to add onto is O(n) insertion, here its O(1), but space and time still O(n)