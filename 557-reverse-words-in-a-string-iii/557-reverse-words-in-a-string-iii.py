class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for word in range(0,len(words)):
            words[word] = words[word][::-1]
        return " ".join(words)
            
        
            
        