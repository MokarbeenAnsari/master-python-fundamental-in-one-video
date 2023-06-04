# for loop through List
from itertools import count


float_list = [ 12, 13.9, 7, 78, 3, 45.9, 67.12, 30, 5, 3, 2]

for i in range(len(float_list)):
    float_list[i] = 2 * float_list[i]

print(float_list)

count_num = 0
for num in float_list:
    if num > 10:
        count_num = count_num + 1
        
print(count_num)