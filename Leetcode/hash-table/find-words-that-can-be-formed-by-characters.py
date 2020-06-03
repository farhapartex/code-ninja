class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        n = 0
        for word in words:
            y = chars
            flag = False
            for w in word:
                if w in y:
                    y = y.replace(w,"",1)
                else:
                    flag = True
                    break
            
            if not flag:
                n += len(word)
        
        
        return n
                    
        