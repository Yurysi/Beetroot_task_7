from random import randint

"""
    Task 3

    List comprehension exercise

    Use a list comprehension to make a list containing tuples (i, j) where
    `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""

num_list = []
tpl = []
for k in range(25):
    i = randint(1, 10)
    j = i ** 2
    tpl = [i, j]
    tpl = tuple(tpl)
    num_list.append(tpl)
num_list.append(tpl)

print(num_list)
a = [(i, i ** 2) for i in range(1, 11)]
print(a)
