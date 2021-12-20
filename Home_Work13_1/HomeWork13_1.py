def average (lst):
    sum1 =0
    for i in lst :
        sum1 += int(i)
    return str(round(sum1/len(lst),2))

def align (lst) :
    for i in range(21+len(lst[-1]) - len(''.join(lst))):
        lst.insert(4,' ')

    return lst


file_src = open('src_14.txt', encoding='utf-8')
file_res = open('src_res.txt','w',encoding='utf-8')

line_num = 0
av_sum = 0

for line in file_src:
    l = line.split()
    file_res.write(''.join(align([l[1],' ',l[0][0],'.',average(l[2:])]))+'\n')
    if float(average(l[2:])) < 5:
        print(''.join(align([l[1],' ',l[0][0],'.',average(l[2:])])))
    av_sum += float(average(l[2:]))
    line_num +=1

print('Средний балл группы ', round(av_sum/line_num,2))


file_res.close()
file_src.close()