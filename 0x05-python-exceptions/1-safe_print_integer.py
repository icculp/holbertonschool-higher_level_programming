#!/usr/bin/python3
if __name__ != "__main__":
    def safe_print_integer(value):
        try:
            print("{:d}".format(value))
            return True
        except:
            return False
