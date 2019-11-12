class Dynamic_Array:
    def __init__(self):
        self.seq_list = {}
        self.last_answer=0
    
    def create_sequence(self,n):
        for i in range(n):
            self.seq_list[i] = []
    
    def xor(self,a,b):
        return 1 if (a or b) and not (a and b) else 0

    def first_query(self,x,y,n):
        index = (x^self.last_answer)%n
        self.seq_list[index].append(y)
    
    def second_query(self,x,y,n):
        index = (x^self.last_answer)%n
        seq = self.seq_list[index]
        self.last_answer = seq[y%len(seq)]
        print(self.last_answer)


if __name__ == "__main__":
    array = Dynamic_Array()
    n,q = list(map(int, input().split()))
    array.create_sequence(n)

    for i in range(q):
        a,x,y = list(map(int, input().split()))
        if a==1:
            array.first_query(x,y,n)
        elif a==2:
            array.second_query(x,y,n)


"""
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
"""