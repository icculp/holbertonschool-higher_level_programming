#!/usr/bin/python3
if __name__ != "__main__":
    def raise_exception_msg(message=""):
        class NameError(Exception):
            def __init__(self, message):
                self.message = message
        raise NameError(message)
