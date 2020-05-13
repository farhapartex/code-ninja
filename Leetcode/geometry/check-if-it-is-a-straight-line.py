class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        previous_point, prev_slope = coordinates[0], "*"
        
        for index in range(1, len(coordinates)):
            current_point = coordinates[index]
            x = current_point[0] - previous_point[0]
            y = current_point[1] - previous_point[1]
            slop = "undefine" if x == 0 else ("0" if y/x == 0 else str(y/x))
            previous_point = current_point
            if prev_slope == "*":
                prev_slope = slop
            elif prev_slope != slop:
                return False
            else:
                prev_slope = slop
        
        return True