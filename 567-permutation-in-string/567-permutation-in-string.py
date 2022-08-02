class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = Counter(s1)
        for i in range(len(s2)):
            sub = s2[i:i+len(s1)]
            s2Map = Counter(sub)
            if s1Map == s2Map:  
                return True
        return False
        