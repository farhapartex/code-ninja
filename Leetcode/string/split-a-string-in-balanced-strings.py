class Solution:
    def __init__(self, str):
        self.count = 0
        self.rval, self.lval = 0 , 0
        self.str = str

    def get_answer(self):
        for s in self.str:
            if s == "R":
                self.rval += 1
            else:
                self.lval += 1
        
            if self.rval == self.lval:
                self.count += 1
                self.rval, self.lval = 0 , 0

        return self.count


if __name__ == "__main__":
    str = Solution(input()).get_answer()
    print(str)
