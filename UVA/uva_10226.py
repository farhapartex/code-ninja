test = int(input())
print("")
for i in range(test):
    data, counter = {}, 0
    while True:
        name = input()
        if len(name)==0 or name is None:
            break
        counter += 1
        if name in data:
            data[name] += 1
        else:
            data[name]=1
    
    for key in sorted(data):
        print("{0} {1:.4f}".format(key, (data[key]*100)/len(data)))
    print("")