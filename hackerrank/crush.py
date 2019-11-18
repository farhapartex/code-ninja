def get_max_num(data,n):
    mx_num, temp = 0,0
    for i in range(n):
        temp += data[i]
        if temp > mx_num:
            mx_num = temp
    return mx_num
    

def update_array(D,a,b,k):
    D[a-1] += k
    if b < len(D):
        D[b] -= k

if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    data, current_max = [0]*n, 0
    # D = init_diff_array(data)
    for _ in range(m):
        a,b,k = list(map(int, input().split()))
        current_max = update_array(data,a,b,k)
    
    print(get_max_num(data,n))