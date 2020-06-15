class Solution:
    def search_word(self, word, products):
        res = []
        
        for product in products: #O(n)
            if len(word) <= len(product):
                #print(product[:len(word)-1])
                if word == product[:len(word)]:
                    if len(res) >= 3:
                        break
                    res.append(product)
        
        return res
    
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products = sorted(products) #nlog(n)
        
        for index, ch in enumerate(searchWord): #O(m)
            word = searchWord[:index+1]
            #print(word)
            ans = self.search_word(word, products)
            res.append(ans)
        
        return res
        