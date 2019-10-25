class Solution(object):
    
    def __init__(self):
        self.data = []
    
    def get_digits(self, num):
        digits = []
        while num>0:
            rem = num%10
            num = num/10
            digits.append(rem)
        return digits
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        for i in range(left,right+1):
            if i == 0:
                continue
            elif 1<=i<=9:
                self.data.append(i)
            else:
                reminders = self.get_digits(i)
                if 0 in reminders:
                    continue
                else:
                    status = True
                    for rem in reminders:
                        if i%rem != 0:
                            status = False
                            break
                    if status:
                        self.data.append(i)
        
        return self.data
        