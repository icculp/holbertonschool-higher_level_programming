#!/usr/bin/python3
if __name__ != "__main__":
    def safe_print_list_integers(my_list=[], x=0):
        count = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                count += 1
            except ValueError:
                print(end='')
            except TypeError:
                print(end='')
        print()
        return count
