end = "end"
lst = []
tmp = []
big_lst = []
res_lst = []
while lst != ['end']:
    lst = input().split(" ")
    big_lst.append(lst)
big_lst = big_lst[:-1]
for i in range(len(big_lst)):
    big_lst[i] = [int(j) for j in big_lst[i]]
for i in range(len(big_lst)):
    tmp.clear()
    for j in range(len(big_lst[i])):
        el = big_lst[(i - 1) % len(big_lst)][j % len(big_lst[i])] + big_lst[(i + 1) % len(big_lst)][j] + \
             big_lst[i % len(big_lst)][(j - 1) % len(big_lst[i])] + big_lst[i % len(big_lst)][(j + 1) % len(big_lst[i])]
        tmp.append(el)
    res_lst.append(tuple(tmp))
for i in range(len(res_lst)):
    for j in range(len(res_lst[i])):
        print(res_lst[i][j], end=" ")
    print()
