class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        begin, end, mid = 0, len(letters)-1, 0
        
        while begin <= end:
            mid = (begin+end)//2
            if letters[mid] == target:
                begin = mid+1
            
            if letters[mid] > target:
                end = mid-1
            else:
                begin = mid+1
        
        return letters[0] if begin >= len(letters) else letters[begin]
        