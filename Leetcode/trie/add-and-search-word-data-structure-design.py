from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)
        self.is_end_word = False


class Trie:
    
    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return TrieNode()
    
    def _char_to_index(self,ch):
        return ord(ch)-ord('a') 
        

    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = self.get_node()
            root = root.children[w]
        root.is_end_word = True

    def search(self, root, word):
        for i in range(len(word)):
            if word[i] != '.':
                if word[i] not in root.children:
                    return False
                root = root.children[word[i]]
            else:
                visit_all = root.children
                for child in visit_all:
                    if self.search(root.children[child], word[i+1:]):
                        return True
                return False
        return (root.is_end_word == True)


class WordDictionary:
    
    def __init__(self):
        self.trie = Trie()
        self.root = self.trie.root
    
    
    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        return self.trie.search(self.root, word)
        
