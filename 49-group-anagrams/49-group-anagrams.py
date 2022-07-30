class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result["".join(str(sorted(word)))].append(word)
        return result.values()