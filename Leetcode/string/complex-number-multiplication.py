class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a.split("+")
        a1, a2 = int(a[0]), int(a[1].split("i")[0])
        b = b.split("+")
        b1, b2 = int(b[0]), int(b[1].split("i")[0])
        
        c = (a1*b1)-(a2*b2)
        d = (a1*b2 + a2*b1)
        return "{0}+{1}i".format(str(c), str(d))
        
        