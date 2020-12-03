with open('Day 1/Indata.txt','r') as file:
    rawData = file.read()
    list = list(map(int, rawData.splitlines()))

    for i in range(len(list)):
        for j in range(i, len(list)):
            for k in range(j, len(list)):

                if i == j or i == k or j == k:
                    continue
                if list[i] + list[j] + list[k] == 2020:
                    print("list[{}] = {}".format(i,list[i]))
                    print("list[{}] = {}".format(j,list[j]))
                    print("list[{}] = {}".format(k,list[k]))
                    print("sum: "+str((list[i]+list[j]+list[k])))
                    print("times: "+str((list[i]*list[j]*list[k])))
                    break
            else:
                continue
            break
        else:
            continue
        break
