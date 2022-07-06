class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        array = []
        for i in range(m):
            array.append(original[i*n:i*n + n])
        return array