#!/bin/python3

import math
import os
import random
import re
import sys


def getMinimum(quantity):
    tam = len(quantity)//2
    A = quantity[:tam+1]
    B = quantity[tam+1:]
    total_a = sum(A)
    total_b = sum(B)
    min_a = min(A)
    min_b = min(B)
    index_min_a = A.index(min(A))
    index_min_b = B.index(min(B))
    mov = 0
    print(A, B)
    print(f'index_A {index_min_a}: {min_a}\nindex_B {index_min_b}: {min_b}')
    dif = total_a - total_b
    print(f'dif: {dif}\nabs: {abs(dif)}')

    if dif > 0:
        # Significa que soma A > soma B
        while dif != 0:
            index_min_b = B.index(min(B))
            print(f'Antes:\nindex_min_b {index_min_b}: {min(B)}')
            B[index_min_b] += 1
            print(f'Depois:\nindex_min_b {index_min_b}: {min(B)}')
            dif = sum(A) - sum(B)
            mov += 1
            print('MOVE + 1, total:', mov)
            print(f'dif:{dif}')

    if dif < 0:
        # Significa que soma A < soma B
        while dif != 0:
            index_min_a = A.index(min(A))
            print(f'Antes:\nindex_min_a {index_min_a}: {min(A)}')
            B[index_min_a] += 1
            print(f'Depois:\nindex_min_a {index_min_a}: {min(A)}')
            dif = sum(A) - sum(B)
            mov += 1
            print('MOVE + 1, total:', mov)
            print(f'dif:{dif}')

    return mov
    print('final:', A, B, 'moves:', mov)


'''

    # print(f'Quantity:{quantity}\n A:{A}')

    for i in range(len(quantity)):
        total_a -= quantity[i]
        total_b += quantity[i]
        print(f'FOR[{i}]: {total_a} / {total_b}')

        A.append(quantity[i])

        if total_a == total_b:
            return A
    print(f'Quantity:{quantity}\n A:{A}')
    print(f'Final: {total_a}!={total_b}')
    '''


n = 3

quantity0 = [1, 4, 4]  # Moves: 1
quantity1 = [3, 3, 6, 3, 9]  # Moves: 0
quantity2 = [4, 5, 7]  # Moves: 2
quantity3 = [3, 4, 5, 7]  # Moves: 2
quantity4 = [3, 1, 4, 4]  # Moves: 1
quantity5 = [5, 3, 3, 6, 3, 9]  # Moves: 0
answ = [1, 0, 2, 2, 1, 0]
teste = []
quantity = [quantity0, quantity1, quantity2, quantity3, quantity4, quantity5]
# quantity5.sort()
# print(quantity5)
# print(getMinimum(quantity5))

for i in range(len(quantity)):
    if getMinimum(quantity[i]) == answ[i]:
        print(f'Passei!!\nMoves:{getMinimum(quantity[i])}')
    else:
        print(f'Reprovei no teste{i}!!\nMoves:{getMinimum(quantity[i])}')

# q = [1, 4, 4]
# add 1 in q[3] = [1, 4, 5]
# j = 2
# final: a = [1, 4] b = [5]
# moves n = 1
