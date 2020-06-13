from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        k, s, p = Counter(arr), 0, 0
        occurences = sorted(k.values(), reverse=True)
        ln = len(arr)
        
        #print(occurences, p)
        while s < (ln+1)//2:
            s += occurences[p]
            
            p+=1
        
        return p
        