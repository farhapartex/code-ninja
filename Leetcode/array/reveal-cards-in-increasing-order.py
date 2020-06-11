class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck[:] = sorted(deck)
        ln, res = len(deck), []
        while len(deck) > 0:
            m = deck.pop()
            if len(res)>0:
                n = res.pop()
                res.insert(0,n)
            
            res.insert(0,m)
        
        return res
        