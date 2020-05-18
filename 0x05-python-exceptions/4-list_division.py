#!/usr/bin/python3
if __name__ == "__main__":
    def list_division(my_list_1, my_list_2, list_length):
        c = [None] * list_length
        for i in range(len(my_list_2)):
            try:
                c[i] = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                c[i] = 0
            except TypeError:
                print("wrong type")
                c[i] = 0
            except IndexError:
                print("out of range")
                c[i] = 0
        return c
