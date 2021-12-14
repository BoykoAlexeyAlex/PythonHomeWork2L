def average (lst):
    sum1 =0
    for i in lst :
        sum1 += int(i)
    return str(round(sum1/len(lst),2))

def align (lst) :
    max_len = 0
    for element in lst :
        if len(element) > max_len :
            max_len = len(element)
    for i in range(len(lst)) :
        for j in range (max_len - len(lst[i])):
            lst[i] += ' '
    return lst



file_src = open('src_14.txt', encoding='utf-8')
file_res = open('src_res','w',encoding='utf-8')

lst_num= []
lst_names =[]
for line in file_src:
    lst_num.append(line[21:(len(line)-1)].split())
    lst_names.append(line[0:21])
lst_names = list(map(lambda x: x.split(),lst_names))
#print(lst_names)
lst_names = align(list(map(lambda x: str(x[0])+' '+ (x[1][0:1])+'.',lst_names)))
#lst_names = align(lst_names)
#print(lst_names)

for i in range (len(lst_names)):

    file_res.write(lst_names[i]+'  ')
    file_res.write(average(lst_num[i]))
    file_res.write('\n')

file_res.close()
file_src.close()
