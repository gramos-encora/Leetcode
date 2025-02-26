from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        reversed_dict = {}
        pairs = 0

        for i,word in enumerate(words):
            if word in reversed_dict:
                print(f"match: {word}")
                pairs += 1
            
            reversed_dict[word[::-1]] = i 
        
        return pairs