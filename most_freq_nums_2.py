# import libraries
from collections import Counter
# import sys
# print(sys.version)


# necessary parameters
QUANTITY_OF_NUMBER_IN_CONSIDERATION = 45
N_LATEST_LINES = 10

NUMBER_LIST = "number_list_2.txt"
RESULT_FILE = "result_2.txt"

# open number list file
file = open(NUMBER_LIST, "r")
# # lines = file.readlines()
# for count in enumerate(file):
#     if count % 2 == 0:
#         all_lines = [line for line in reversed(file.readlines()) if line.strip()]
# # file.close()
# print(all_lines)

# all_lines = [line.rstrip('\n') for count, line in enumerate(file, start=1) if count % 2 == 0]
all_lines = [' '.join(line[i:i+2].rstrip('\n') for i in range(0, len(line), 2)).rstrip() for count, line in enumerate(file, start=1) if count % 2 == 0 if line.strip()]
all_lines = list(reversed(all_lines))
file.close()
# print(all_lines)



file = open(NUMBER_LIST, "r")
# latest_lines = [line for line in file.readlines()[-N_LATEST_LINES:] if line.strip()]
latest_lines = all_lines[-N_LATEST_LINES:]
file.close()
# print(latest_lines)


# FUNCTIONS PART
def add_new_num_to_list():
    # add new numbers or not
    add_new_numbers = input("""Add number, [Y]es or [N]o? 
    [Y]es   :    Yes - Add new numbers
    else    :    No - Skip adding new numbers
        
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
        # n7 = input("    Enter number #7: ")
        new_num_set = n1 + " " + n2 + " " + n3 + " " + n4 + " " + n5 + " " + n6 # + " " + n7

        # Open the file in append & read mode ('a+')
        with open(NUMBER_LIST, "a+") as file:
            # Move read cursor to the start of file.
            file.seek(0)

            # If file is not empty then append '\n'
            data = file.read(100)
            if len(data) > 0:
                file.write("\n")

            # Append new content at the end of file
            file.write(new_num_set)

        file.close()
        print("\n\n    New added number set:\n      ", new_num_set, "\n")
        print("--------------------------------------------------------------------------------------\n")
        
    else:
        print("\nSkip adding new numbers. Proceed to checking...")
        print("--------------------------------------------------------------------------------------\n")


def check_frequent_numbers():
    # list of number in consideration
    ALL_NUM = []
    JACKPOT_1 = []
    JACKPOT_2 = []
    A_n = J_1 = J_2 = 0
    
    # add new numbers or not
    add_new_num_to_list()

    All_or_Latest_results = input("""Checking [A]ll results or """ + str(N_LATEST_LINES) + """ [L]atest results?
    [L]atest    :     Latest results
    else        :     All results

    Your choice: """)
    if All_or_Latest_results != "L":
        lines = all_lines
    else:
        lines = latest_lines

    print("--------------------------------------------------------------------------------------")
    for x in lines:
        ALL_NUM.extend(x.split())                  # ALL_NUM is the list of strings

    # Iterating using while loop
    len_all = len(ALL_NUM)
    while A_n < len_all:
        ALL_NUM_int = ALL_NUM[A_n]
        A_n += 1

    try:
        ALL_NUM_list = [eval(i) for i in ALL_NUM_int]      # convert the list of STRING to the list of INTEGER
    except IndexError:
        print("Exception: Index out of range")

    global ALL_NUM_str_count
    ALL_NUM_str_count = Counter(ALL_NUM)                 # ALL_NUM if the list of number in form of STRING
    ALL_NUM_str_count = ALL_NUM_str_count.most_common(QUANTITY_OF_NUMBER_IN_CONSIDERATION)       # counter for list of numbers but in form of string

    # int_counter = int_counter.most_common(10)       # counter for list of integer numbers

    print("--------------------------------------------------------------------------------------")
    print("\n" + str(QUANTITY_OF_NUMBER_IN_CONSIDERATION) + " most frequent of ALL NUMBERS (string): \n")
    for key_all, val_all in ALL_NUM_str_count:
        print(" ", key_all, " : ", val_all ,"times")
        # a = " ", key_all, " : ", val_all ,"times"

    print("--------------------------------------------------------------------------------------\n")

    # return ALL_NUM_str_count

def export_result():
    export_result = input(f"""\nExport result, [Y]es or [N]o?
    [Y]es   :   Export result to '{RESULT_FILE}'
    else    :   Skip exporting result

    Your choice: """)
    
    # if export_result == {"Y" | "YES" | "YEs" | "YeS" | "yES" | "Yes" | "yEs" | "yeS" | "yes" | "y"}:
    if export_result == "Y":
        with open(RESULT_FILE, "a+") as result:
            # Move read cursor to the start of file.
            result.seek(0)

            # If file is not empty then append '\n'
            data_result = result.read(100)
            if len(data_result) > 0:
                result.write("\n")

            # Append new content at the end of file
            result.write(str(ALL_NUM_str_count))

        result.close()

        print("\n Exported to '{}'.\n".format(RESULT_FILE))
        print("--------------------------------------------------------------------------------------\n")
    
    else:
        print("\n   No exportation!\n")
        print("--------------------------------------------------------------------------------------\n")

# CHEKING FREQUENT NUMBERS
check_frequent_numbers()
export_result()

# re-checking or not?
_continue = input("""Check again, [Y]es or [N]o?
    [Y]es   :   Re-do the checking process
    else    :   Stop checking
    
    Your choice: """)

while True:
    if _continue == "Y":
        print("\n--------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------\n")
        check_frequent_numbers()
    else:
        print("\n   Exiting...\n")
        break
    _continue = input("""Check again, [Y]es or [N]o?
    [Y]es   :   Re-do the checking process
    else    :   Stop checking
    
    Your choice: """)