class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        arr = []
        for i in range(len(s)):
            if s[i] in ('{','(','['):
                arr.append(s[i])
            elif s[i] in ('}',']',')'):
                if not arr or arr.pop() != d[s[i]]:
                    return False
        return not arr



