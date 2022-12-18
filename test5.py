# Program to find most frequent
# element in a list
 
def ten_most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,12, 1, 2, 2, 1, 3, 2,3,4,5,6,7,8,9,2,2,2]
print(ten_most_frequent(List))