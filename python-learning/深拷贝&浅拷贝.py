"""
@author: songchen
@contact: chloesong@tencent.com
@file: 深拷贝&浅拷贝.py
@time: 2023/11/7 15:31
@desc:
"""

import copy

if __name__ == '__main__':
    a = [1, 2, 3, ['a', 'b', 'c']]
    b = a
    c = a.copy()
    d = copy.deepcopy(a)

    a.append(5)
    a[3].append('d')
    print(a)
    print(b)
    print(c)
    print(d)
