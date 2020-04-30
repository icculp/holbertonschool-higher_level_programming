#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    elif (sys.argv[2][0] not in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                  sys.argv[3], c.add(int(sys.argv[1]), int(sys.argv[3]))))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                  sys.argv[3], c.sub(int(sys.argv[1]), int(sys.argv[3]))))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                  sys.argv[3], c.mul(int(sys.argv[1]), int(sys.argv[3]))))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                  sys.argv[3], c.div(int(sys.argv[1]), int(sys.argv[3]))))
