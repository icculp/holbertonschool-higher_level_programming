#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    for i in d:
        if i[:2] != "__":
            print(i)
