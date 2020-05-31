class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words, res = sorted(words, key=len), []
        
        for index, word in enumerate(words):
            if index == len(words)-1:
                break
            for w in words[index+1:]:
                if word in w and word not in res:
                    res.append(word)
        
        return res
        