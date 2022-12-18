from collections import Counter

num_list=["1","2","3","4","5"] 

new_num = input("Enter new number:")
num_list.extend(new_num)

# print(num_list)
c = Counter(num_list)
a = c.most_common(10)

print(a)

# file = open("test1.py", "a")
# file.write(new_num)

# file.close()