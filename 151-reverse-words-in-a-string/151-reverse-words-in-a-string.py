class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = reversed(words)
        return " ".join(reverse)
        