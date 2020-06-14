class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        flag = None
        #print(s1, " ", s2)
        for index, ch in enumerate(s1):
            if flag is None:
                if s1[index] < s2[index]:
                    flag = True
                elif s1[index] > s2[index]:
                    flag = False
            else:
                if flag and s1[index] > s2[index]:
                    return False
                elif flag == False and s1[index] < s2[index]:
                    return False
        
        return True
        