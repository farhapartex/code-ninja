class Solution:
    def __init__(self):
        self.data1=[]
        self.data2=[]
        self.result=[]
    
    def binary_search(self,target):
        bg, end = 0, len(self.data2)-1

        while bg <= end:
            mid = (bg+end)//2
            if self.data2[mid] == target:
                return True
            elif self.data2[mid] < target:
                bg = mid +1
            elif self.data2[mid] > target:
                end = mid-1
        
        return False

        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            self.data1 = nums1
            self.data2 = nums2   
        else:
            self.data1 = nums2
            self.data2 = nums1
            
        self.data2.sort()
        
        for num in self.data1:
            if num not in self.result:
                if self.binary_search(num):
                    self.result.append(num)
        
        return self.result