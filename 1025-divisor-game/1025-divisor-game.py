class Solution:
    def divisorGame(self, n: int) -> bool:
        for i in range(n):
            if n % 2 == 0:
                return True
        return False
        