class Solution:
    def _is_leap_year(self, year: int)-> bool:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def dayOfYear(self, date: str) -> int:
        nums = [int(d)for d in date.split("-")]
        days = nums[2]
        
        for month in range(1,nums[1]):
            if month in [4,6,9,11]:
                days += 30
            elif month == 2:
                days += 28
                if self._is_leap_year(nums[0]):
                    days += 1
            else:
                days += 31
        
        return days
        