from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)         # target character counts
        window = Counter()         # current window's character counts
        target_size = len(s1)
        left = 0
        
        for right in range(len(s2)):
            # 1. expand: add the new character on the right
            window[s2[right]] += 1
            
            # 2. shrink: if window is bigger than target, remove leftmost char
            if right - left + 1 > target_size:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            # 3. check: does the window match what we need?
            if window == need:
                return True
        
        return False