#!/usr/bin/python3
if __name__ != "__main__":
    def raise_exception_msg(message=""):
        try:
            raise NameError(message)
        except NameError:
            print(message)
