class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            x[sorteds].append(s)
        return list(x.values())
            
