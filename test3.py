num_list_file = open("number_list.txt", "r")
lines = num_list_file.readlines()

num_list = []

for x in lines:
    num_list.extend(x.split())
    # num_list = int(num_list)
print(num_list)

num_list_file.close()


# for line in num_list_file:
#     list.extend(int(line.strip('\n')))
# print(list)
    

# f=open("number_list.txt","r")
# lines=f.readlines()
# result=[]
# for x in lines:
#     result.extend(x.split())

# print(result)
# f.close()
# with open("number_list.txt") as num_list:
#     w, h = [int(x) for x in next(num_list).split()]
#     array = []
#     for line in num_list:
#         array.append([int(x) for x in line.split()])