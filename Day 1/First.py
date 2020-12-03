with open('Day 1/Indata.txt','r') as file:
    rawData = file.read()
    list = list(map(int, rawData.splitlines()))

    for i in range(len(list)):
        for j in range(i, len(list)):
            # print("i: {0}, j: {1}".format(i,j))
            if i == j:
                continue
            if list[i] + list[j] == 2020:
                print("list[{}] = {}".format(i,list[i]))
                print("list[{}] = {}".format(j,list[j]))
                print("sum: "+str((list[i]+list[j])))
                print("times: "+str((list[i]*list[j])))
                break
        else:
            continue
        break
