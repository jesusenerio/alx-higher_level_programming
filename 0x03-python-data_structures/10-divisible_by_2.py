#!/usr/bin/python3
def divisible_by_2(my_list=[]):
# iterate through the list
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            return(my_list[i])
        else:
            return None
# then check if the element in that position is divisible by 2
# if yes return true 
# else return false
