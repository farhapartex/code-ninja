class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        data, temp = {}, []
        for n in arr1:
            if n in arr2:
                if n in data:
                    data[n] += 1
                    index = arr2.index(n)
                    arr2.insert(index, n)
                else:
                    data[n] = 1
            else:
                temp.append(n)
        
        arr2.extend(sorted(temp))
        return arr2
        