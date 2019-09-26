class BinarySearch:
    def __init__(self):
        self.data = []
    
    def insert_data(self, data):
        self.data.append(data)
    
    def search(self, data):
        """
        data must be sorted for binary search algorithm
        """
        self.data.sort()

        beg, end = 0, len(self.data)

        while beg <= end:
            mid = int((beg+end)/2)
            if self.data[mid] == data:
                return True
            elif self.data[mid] < data:
                beg = mid+1
            elif self.data[mid] > data:
                end = mid-1
        return False


if __name__ == "__main__":
    bsearch = BinarySearch()

    bsearch.insert_data(10)
    bsearch.insert_data(12)
    bsearch.insert_data(5)
    bsearch.insert_data(8)
    bsearch.insert_data(20)
    bsearch.insert_data(22)
    bsearch.insert_data(19)
    bsearch.insert_data(15)
    bsearch.insert_data(1)

    print("Data found") if bsearch.search(10) else print("Data not found")
    print("Data found") if bsearch.search(13) else print("Data not found")
    print("Data found") if bsearch.search(1) else print("Data not found")
    print("Data found") if bsearch.search(18) else print("Data not found")
    print("Data found") if bsearch.search(22) else print("Data not found")