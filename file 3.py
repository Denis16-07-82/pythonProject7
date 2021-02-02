str_1=[2,2,2,2,7,23,1,44,44,3,2,10,7,4,11]#задача 4 урок 4
new_str=[str_1[i] for i in range(len(str_1)) if str_1.count(str_1[i])==1]
print(new_str)