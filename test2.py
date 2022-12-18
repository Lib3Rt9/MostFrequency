from collections import Counter

number_list = []

# new_num = input("Enter new number:")

num_list_file = open("number_list.txt", "r")
file_content = num_list_file.read()

print("The file content are:\n", file_content)

number_list.extend(file_content)
print("The file content are:\n", number_list)