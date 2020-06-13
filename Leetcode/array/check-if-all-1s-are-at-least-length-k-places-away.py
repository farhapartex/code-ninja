class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag, next_num = False, 0
        for index, num in enumerate(nums):
            if num ==1:
                if not flag:
                    current = index
                    flag = True
                else:
                    if next_num > index:
                        return False
                
                next_num = index + k +1
                
        
        return True
                    
        