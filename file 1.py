str_1=[3,7,5,6,8,9,19,13,14,11]#задача 2 урок 4
new_str=[str_1[i+1] for i in range(len(str_1)-1) if str_1[i+1]>str_1[i]]
print(new_str)
