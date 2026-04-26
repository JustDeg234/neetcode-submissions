class Solution:
    def isValid(self, s: str) -> bool:
        while "[]" in s or "()" in s or "{}" in s:
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            s = s.replace("()", "")#brute force: string immutability causes new string creation every iteration
        return s == "" #if true, every pair is validated