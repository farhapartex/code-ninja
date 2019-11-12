class Contact:
    def __init__(self):
        self.data = {}
    
    def insert(self,word):
        for i in range(1,len(word)+1):
            self.data[word[:i]] = self.data[word[:i]] +1 if word[:i] in self.data else 1
        

    def search(self,word):
        return self.data[word] if word in self.data else 0


if __name__ == "__main__":
    contact = Contact()
    for _ in range(int(input())):
        a,b = input().split()
        if a == "add":
            contact.insert(b)
        else:
            print(contact.search(b))
