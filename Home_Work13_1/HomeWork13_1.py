def average (lst):
    sum1 =0
    for i in lst :
        sum1 += int(i)
    return str(round(sum1/len(lst),2))

def align (lst) :
    max_len = 0
    for element in lst :
        if len(element[0]) > max_len :
            max_len = len(element[0])
    for i in range(len(lst)) :
        for j in range (max_len - len(lst[i][0])):
            lst[i].insert(4,' ')
        lst[i].insert(4,'  ')
    return lst


file_src = open('src_14.txt', encoding='utf-8')
file_res = open('src_res','w',encoding='utf-8')

lst = []

for line in file_src:
    lst.append(line.split())

lst = align(list(map(lambda x: [x[0],' ', x[1][0],'.',average(x[2:])],lst)))

for i in range (len(lst)):
    file_res.write(''.join(lst[i])+'\n')


file_res.close()
file_src.close()
