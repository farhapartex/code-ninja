class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_index = seats.index(1)
        right_index = len(seats)-1
        
        while right_index >0 and seats[right_index]==0:
            right_index -= 1
        
        zero, max_zero = 0, 0
        for i in range(left_index+1, right_index+1):
            if seats[i] == 0:
                zero += 1
                max_zero = max(zero, max_zero)
            else:
                zero = 0
        
        return max(left_index, len(seats)-1-right_index, (max_zero + 1) // 2)
        