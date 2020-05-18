#!/usr/bin/python3
if __name__ != "__main__":
    def safe_print_list(my_list=[], x=0):
        count = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                count += 1
            except IndexError:
                print(end='')
        print()
        return count
