class Solution:
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = {}, {}
        res = []
        
        for n in nums1:
            dict1[n] = dict1.get(n,0) + 1
        
        for n in nums2:
            dict2[n] = dict2.get(n,0) + 1
        
        
        for k in dict1.keys():
            res += [k] * min(dict1[k], dict2.get(k,0))
        
        
        return res
        