#!/usr/bin/python3
"""
    Task 10
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}'
                     .format(sys.argv[2], sys.argv[1]))
    j = r.json()
    cur = j.get('commits_url')
#   print(cur)
    cur = cur.replace('{/sha}', "")
    com = requests.get(cur)
#   print(dir(com))
    b = com.json()
    ind = 0
    for bi in b:
        big = bi
        sha = big.get('sha')
        aname = big.get('commit').get('author').get('name')
        print("{}: {}".format(sha, aname))
        ind = ind + 1
        if ind == 10:
            break
'''
    print(big.keys())
    print("------------")
    print(big.get('sha'))
    print("-------------")
    print(big.get('commit').get('author').get('name'))
'''
