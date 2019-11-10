class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_word = False
        
class Trie:

    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return TrieNode()
    
    def _char_to_index(self,ch):
        return ord(ch)-ord('a')
        

    def insert(self, key: str) -> None:
        p_crawl = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
        
        p_crawl.is_end_word = True
        

    def search(self, key: str) -> bool:
        p_crawl = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]
        
        return p_crawl is not None and p_crawl.is_end_word 
        

    def startsWith(self, prefix: str) -> bool:
        p_crawl = self.root
        for level in range(len(prefix)):
            index = self._char_to_index(prefix[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]
        
        return True if p_crawl is not None else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)