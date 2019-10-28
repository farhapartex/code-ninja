def show_result(data,data_in):
    for n in data_in:
        print("{0} {1}".format(n, data[n]))


if __name__ == "__main__":
    try:
        data, data_in = {}, []
        while True:
            nums = input()
            if nums is None or len(nums) == 0:
                show_result(data,data_in)
                break
            nums = list(map(int, nums.split(" ")))
            print(nums)
            
            for n in nums:
                if n in data:
                    data[n] += 1
                else:
                    data[n] = 1
                    data_in.append(n)
        
    except:
        pass