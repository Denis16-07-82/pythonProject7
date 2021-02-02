from itertools import count #задача 6 урок 4
from  itertools import cycle
my_list=[]
for i in count(3):
    if i < 11:
        my_list.append(i)
    else:
        break

print(my_list)
my_list_new=[]
n=1
for il in cycle(my_list):
    if n < 100:
        my_list_new.append(il)
        n+=1
    else:break
print(my_list_new)




