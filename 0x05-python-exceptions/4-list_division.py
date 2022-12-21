#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("Out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("Divide by Zero")
            res = 0
        finally:
            result.append(res)
    return(result)
