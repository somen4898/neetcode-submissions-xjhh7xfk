from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_size = len(s1)
        if target_size > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:target_size])
        
        if window == need:
            return True
        
        for right in range(target_size, len(s2)):
            entering = s2[right]
            leaving = s2[right - target_size]
            
            # slide: add entering char, remove leaving char
            window[entering] += 1
            window[leaving] -= 1
            if window[leaving] == 0:
                del window[leaving]
            
            if window == need:
                return True
        
        return False