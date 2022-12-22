# import libraries
from collections import Counter
# import sys
# print(sys.version)


# necessary parameters
QUANTITY_OF_NUMBER_IN_CONSIDERATION = 55
N_LATEST_LINES = 10


# open number list file
file = open("number_list.txt", "r")
# lines = file.readlines()
lines = [line for line in file.readlines() if line.strip()]
# file.close()

file = open("number_list.txt", "r")
latest_lines = [l_lines for l_lines in file.readlines()[-N_LATEST_LINES:] if l_lines.strip()]
file.close()


# FUNCTIONS PART
def add_new_num_to_list():
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
    ALL_NUM = []
    JACKPOT_1 = []
    JACKPOT_2 = []

    ALL_NUM_LATEST = []
    JACKPOT_1_LATEST = []
    JACKPOT_2_LATEST = []
    
    A_n = J_1 = J_2 = 0
    
    # add new numbers or not
    add_new_num_to_list()
    

    # w, h = [int(x) for x in next(file).split()] # read first line

    for x in lines:
        ALL_NUM.extend(x.split())                  # ALL_NUM is the list of strings
        JACKPOT_1.extend(x.split()[:-1])                  # JACKPOT_1 is the list of strings
        JACKPOT_2.extend(x.split()[-1:])                  # JACKPOT_2 is the list of strings

    for y in latest_lines:
        ALL_NUM_LATEST.extend(y.split())           # ALL_NUM_LATEST is the list of strings
        JACKPOT_1_LATEST.extend(y.split()[:-1])           # ALL_NUM_LATEST is the list of strings
        JACKPOT_2_LATEST.extend(y.split()[-1:])           # ALL_NUM_LATEST is the list of strings

  
    len_all = len(ALL_NUM)
    len_j1 = len(JACKPOT_1)
    len_j2 = len(JACKPOT_2)

    # Iterating using while loop
    while A_n < len_all:
        ALL_NUM_int = ALL_NUM[A_n]
        A_n += 1

    while J_1 < len_j1:
        JACKPOT_1_int = JACKPOT_1[J_1]
        J_1 += 1

    while J_2 < len_j2:
        JACKPOT_2_int = JACKPOT_2[J_2]
        J_2 += 1
    

    try:
        ALL_NUM_list = [eval(i) for i in ALL_NUM_int]      # convert the list of STRING to the list of INTEGER
        JACKPOT_1_list = [eval(i) for i in JACKPOT_1_int]      # convert the list of STRING to the list of INTEGER
        JACKPOT_2_list = [eval(i) for i in JACKPOT_2_int]      # convert the list of STRING to the list of INTEGER
    except IndexError:
        print("Exception: Index out of range")


    # print("All number", ALL_NUM_list)
    # print("Jackpot", JACKPOT_1_list)
    # print("Jackpot 2nd", JACKPOT_2_list)

    # print()
    # print(ALL_NUM_list)
    # print(ALL_NUM)

    ALL_NUM_str_count = Counter(ALL_NUM)                 # ALL_NUM if the list of number in form of STRING
    JACKPOT_1_str_count = Counter(JACKPOT_1)                 # JACKPOT_1 if the list of number in form of STRING
    JACKPOT_2_str_count = Counter(JACKPOT_2)                 # JACKPOT_2 if the list of number in form of STRING

    # int_counter = Counter(ALL_NUM_list)             # ALL_NUM_list if the list of number in form of INTEGER

    ALL_NUM_str_count = ALL_NUM_str_count.most_common(QUANTITY_OF_NUMBER_IN_CONSIDERATION)       # counter for list of numbers but in form of string
    JACKPOT_1_str_count = JACKPOT_1_str_count.most_common(QUANTITY_OF_NUMBER_IN_CONSIDERATION)       # counter for list of numbers but in form of string
    JACKPOT_2_str_count = JACKPOT_2_str_count.most_common(QUANTITY_OF_NUMBER_IN_CONSIDERATION)       # counter for list of numbers but in form of string

    # int_counter = int_counter.most_common(10)       # counter for list of integer numbers

    print()
    print("\n" + str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of ALL NUMBERS (string): \n")
    for key_all, val_all in ALL_NUM_str_count:
        print(" ", key_all, " : ", val_all ,"times")
        # a = " ", key_all, " : ", val_all ,"times"

    print("\n" + str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of JACKPOT (string): \n")
    for key_jackpot, val_jackpot in JACKPOT_1_str_count:
        print(" ", key_jackpot, " : ", val_jackpot, " times")

    print("\n" + str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of JACKPOT 2 (string): \n")
    for key_JACKPOT_2, val_JACKPOT_2 in JACKPOT_2_str_count:
        print(" ", key_JACKPOT_2, " : ", val_JACKPOT_2, " times")

    # print(str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of ALL NUMBERS (string): \n", ALL_NUM_str_count, "\n")
    # print(str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of JACKPOT (string): \n", JACKPOT_1_str_count, "\n")
    # print(str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of JACKPOT 2 (string): \n", JACKPOT_2_str_count, "\n")

    # print("10 most frequent of ALL NUMBERS (integer): ", int_counter, "\n")
    # result_exporting()
    
    # def result_exporting():

    export_result = input("""\nExport result, [Y]es or [N]o?
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
            result.write(str(ALL_NUM_str_count))

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