from collections import Counter


quantity_of_number_in_consideration = 55


# FUNCTIONS PART
def new_num_to_list():
    # add new numbers or not
    add_new_numbers = input("""Add number, [Y]es or [N]o? 
    Y: Yes - Add new numbers
    N: No - Skip adding new numbers
        
    Your choice: """)

    if add_new_numbers == "Y":
        # input new numbers
        print("\nEnter the new number set:")
        n1 = input("    Enter number #1: ")
        n2 = input("    Enter number #2: ")
        n3 = input("    Enter number #3: ")
        n4 = input("    Enter number #4: ")
        n5 = input("    Enter number #5: ")
        n6 = input("    Enter number #6: ")
        n7 = input("    Enter number #7: ")
        
        new_num_set = n1 + " " + n2 + " " + n3 + " " + n4 + " " + n5 + " " + n6 + " " + n7


        # Open the file in append & read mode ('a+')
        with open("number_list.txt", "a+") as file:
            # Move read cursor to the start of file.
            file.seek(0)

            # If file is not empty then append '\n'
            data = file.read(100)
            if len(data) > 0:
                file.write("\n")

            # Append new content at the end of file
            file.write(new_num_set)

        file.close()

    else:
        print("Skip adding new numbers. Proceed to checking...")


def check_frequent_numbers():
    # list of number in consideration
    all_num = []
    jackpot_1 = []
    jackpot_2 = []

    # add new numbers or not
    new_num_to_list()
    

    # open number list file
    file = open("number_list.txt", "r")
    # lines = file.readlines()
    lines = [line for line in file.readlines() if line.strip()]
    file.close()

    # w, h = [int(x) for x in next(file).split()] # read first line

    for x in lines:
        all_num.extend(x.split())                  # all_num is the list of strings
        jackpot_1.extend(x.split()[:-1])                  # jackpot_1 is the list of strings
        jackpot_2.extend(x.split()[-1:])                  # jackpot_2 is the list of strings


    a = j1 = j2 = 0
    len_all = len(all_num)
    len_j1 = len(jackpot_1)
    len_j2 = len(jackpot_2)

    # Iterating using while loop
    while a < len_all:
        all_num_int = all_num[a]
        a += 1

    while j1 < len_j1:
        jackpot_1_int = jackpot_1[j1]
        j1 += 1

    while j2 < len_j2:
        jackpot_2_int = jackpot_2[j2]
        j2 += 1
    

    try:
        all_num_list = [eval(i) for i in all_num_int]      # convert the list of STRING to the list of INTEGER
        jackpot_1_list = [eval(i) for i in jackpot_1_int]      # convert the list of STRING to the list of INTEGER
        jackpot_2_list = [eval(i) for i in jackpot_2_int]      # convert the list of STRING to the list of INTEGER
    except IndexError:
        print("Exception: Index out of range")


    # print("All number", all_num_list)
    # print("Jackpot", jackpot_1_list)
    # print("Jackpot 2nd", jackpot_2_list)

    # print()
    # print(all_num_list)
    # print(all_num)

    all_num_str_count = Counter(all_num)                 # all_num if the list of number in form of STRING
    jackpot_1_str_count = Counter(jackpot_1)                 # all_num if the list of number in form of STRING
    jackpot_2_str_count = Counter(jackpot_2)                 # all_num if the list of number in form of STRING

    # int_counter = Counter(all_num_list)             # all_num_list if the list of number in form of INTEGER

    all_num_str_count = all_num_str_count.most_common(quantity_of_number_in_consideration)       # counter for list of numbers but in form of string
    jackpot_1_str_count = jackpot_1_str_count.most_common(quantity_of_number_in_consideration)       # counter for list of numbers but in form of string
    jackpot_2_str_count = jackpot_2_str_count.most_common(quantity_of_number_in_consideration)       # counter for list of numbers but in form of string

    # int_counter = int_counter.most_common(10)       # counter for list of integer numbers

    print()
    print("\n" + str(quantity_of_number_in_consideration) + " most frequent of ALL NUMBERS (string): \n")
    for key_all, val_all in all_num_str_count:
        print(" ", key_all, " : ", val_all ,"times")
        # a = " ", key_all, " : ", val_all ,"times"

    print("\n" + str(quantity_of_number_in_consideration) + " most frequent of JACKPOT (string): \n")
    for key_jackpot, val_jackpot in jackpot_1_str_count:
        
        print(" ", key_jackpot, " : ", val_jackpot, " times")

    print("\n" + str(quantity_of_number_in_consideration) + " most frequent of JACKPOT 2 (string): \n")
    for key_jackpot_2, val_jackpot_2 in jackpot_2_str_count:
        print(" ", key_jackpot_2, " : ", val_jackpot_2, " times")
            
    # print(str(quantity_of_number_in_consideration) + " most frequent of ALL NUMBERS (string): \n", all_num_str_count, "\n")
    # print(str(quantity_of_number_in_consideration) + " most frequent of JACKPOT (string): \n", jackpot_1_str_count, "\n")
    # print(str(quantity_of_number_in_consideration) + " most frequent of JACKPOT 2 (string): \n", jackpot_2_str_count, "\n")

    # print("10 most frequent of ALL NUMBERS (integer): ", int_counter, "\n")
    # result_exporting()
    
    # def result_exporting():

    export_result = input("""Export result, [Y]es or [N]o?
    [Y]es :  Export result to result.txt
    [N]o  :  Skip exporting result

    Your choice: """)
    
    if export_result == "Y":
        with open("result.txt", "a+") as result:
            # Move read cursor to the start of file.
            result.seek(0)

            # If file is not empty then append '\n'
            data_result = result.read(100)
            if len(data_result) > 0:
                result.write("\n")

            # Append new content at the end of file
            result.write(str(all_num_str_count))

        result.close()
    
    else:
        print("\n   No exportation!\n")



# CHEKING FREQUENT NUMBERS
check_frequent_numbers()

# re-checking or not?
_continue = input("""Check again, [Y]es or [N]o?
    [Y]es :  Re-do the checking process
    [N]o  :  Stop checking
    
    Your choice: """)

while True:
    if _continue == "Y":
        check_frequent_numbers()
    else:
        print("\n   Exiting...\n")
        break
    _continue = input("Enter 1 to check again, 0 to escape: ")