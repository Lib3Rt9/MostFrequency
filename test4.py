from collections import Counter

# num_list_file = open("number_list.txt", "r")

# file_content = num_list_file.read()
# print("The file content are: ", file_content)

# # content_list = file_content.split()

# # print("The list is: ", content_list)

# # num_list_file.write(new_num)
# # new_num = input("Enter new number:")
# # num_list.extend(new_num)

# with open('number_list.txt') as f:
#     lis=list(map(int,x.split()) for x in f if x.strip())  # if x.strip() to skip blank lines

#    #use list(map(int,x.split()))  in case of python 3.x

# print(lis)

# num_list=[] 

# poly_shape = []

# with open('number_list.txt', 'r') as handle:
#     for line in handle:
#         if not line.strip():
#             continue  # This skips blank lines

#         values = map(int, line.split())
#         poly_shape.append(values)

# num_list_file.close()

f = open('number_list.txt') 
d = f.read() 
print(d)

new_num = d

number_list = []
number_list.extend(new_num)

print(number_list)

f.close() 