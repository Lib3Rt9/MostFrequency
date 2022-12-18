n1 = input("Enter n1: ")
n2 = input("Enter n2: ")
n3 = input("Enter n3: ")
n4 = input("Enter n4: ")
n5 = input("Enter n5: ")
n6 = input("Enter n6: ")

n = n1 + " " + n2 + " " + n3 + " " + n4 + " " + n5 + " " + n6

with open("test6.txt", "a+") as file:
        # Move read cursor to the start of file.
        file.seek(0)

        # If file is not empty then append '\n'
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")

        # Append new content at the end of file
        file.write(n)

file.close()