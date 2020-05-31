class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
            
        data = {}
        for index, value in enumerate(list1):
            if value in list2:
                index_sum = index + list2.index(value)
                if index_sum in data:
                    data[index_sum].append(value)
                else:
                    data[index_sum] = [value]
        
        min_index = min(data.keys())
        return data[min_index]
            
        