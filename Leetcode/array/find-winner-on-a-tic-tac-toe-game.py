class Solution:
    def vertical1(self, data, ch):
        if data[0][0]==ch and data[1][0]==ch and data[2][0]==ch:
            return True
        return False
    
    def vertical3(self, data, ch):
        if data[0][2]==ch and data[1][2]==ch and data[2][2]==ch:
            return True
        return False
    
    def vertical2(self, data, ch):
        if data[0][1]==ch and data[1][1]==ch and data[2][1]==ch:
            return True
        return False
    
    def horizontal1(self, data, ch):
        if data[0][0]==ch and data[0][1]==ch and data[0][2]==ch:
            return True
        return False
    
    def horizontal2(self, data, ch):
        if data[1][0]==ch and data[1][1]==ch and data[1][2]==ch:
            return True
        return False
    
    def horizontal3(self, data, ch):
        if data[2][0]==ch and data[2][1]==ch and data[2][2]==ch:
            return True
        return False
    
    def diagonal1(self, data, ch):
        if data[0][0]==ch and data[1][1]==ch and data[2][2]==ch:
            return True
        return False
    
    def diagonal2(self, data, ch):
        if data[0][2]==ch and data[1][1]==ch and data[2][0]==ch:
            return True
        return False
    
    
    def check(self, cordinate, data, ch):
        if cordinate[0]==0 and cordinate[1]==0:
            if self.vertical1(data, ch) or self.horizontal1(data, ch) or self.diagonal1(data,ch):
                return True
        elif cordinate[0]==0 and cordinate[1]==1:
            if self.vertical2(data, ch) or self.horizontal1(data, ch):
                return True
        elif cordinate[0]==0 and cordinate[1]==2:
            if self.vertical3(data, ch) or self.horizontal1(data, ch) or self.diagonal2(data,ch):
                return True
        
        elif cordinate[0]==1 and cordinate[1]==0:
            if self.vertical1(data, ch) or self.horizontal2(data, ch):
                return True
        elif cordinate[0]==1 and cordinate[1]==1:
            if self.vertical2(data, ch) or self.horizontal2(data, ch) or self.diagonal1(data,ch) or self.diagonal2(data,ch):
                return True
        elif cordinate[0]==1 and cordinate[1]==2:
            if self.vertical3(data, ch) or self.horizontal2(data, ch):
                return True
        elif cordinate[0]==2 and cordinate[1]==0:
            if self.vertical1(data, ch) or self.horizontal3(data, ch) or self.diagonal2(data,ch):
                return True
        elif cordinate[0]==2 and cordinate[1]==1:
            if self.vertical2(data, ch) or self.horizontal3(data, ch):
                return True
        elif cordinate[0]==2 and cordinate[1]==2:
            if self.vertical3(data, ch) or self.horizontal3(data, ch) or self.diagonal1(data,ch):
                return True
        else:
            return False
            
        
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        data = [ ["*"] * 3 for i1 in range(3) ]
        flag = True
        for cordinate in moves:
            if flag==True:
                data[cordinate[0]][cordinate[1]] = 'X'
                flag = False
                if self.check(cordinate, data, 'X'):
                    return 'A'
            else:
                data[cordinate[0]][cordinate[1]] = 'O'
                flag = True
                if self.check(cordinate, data, 'O'):
                    return 'B'
        return 'Draw' if len(moves)==9 else "Pending"
            
            
        
        
        