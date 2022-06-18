class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        array2D = list()
        for i in range(m):
            array2D.append(original[i*n: i*n + n])
        return array2D