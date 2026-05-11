from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wlen = len(s1)
        if wlen > len(s2):
            return False
        
        freq = Counter(s1)
        window = Counter(s2[:wlen])
        
        if window == freq:
            return True
        
        for r in range(wlen, len(s2)):
            # add new char on the right
            window[s2[r]] += 1
            # remove old char on the left
            window[s2[r - wlen]] -= 1
            if window[s2[r - wlen]] == 0:
                del window[s2[r - wlen]]
            
            if window == freq:
                return True
        
        return False