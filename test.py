import itertools

a_string = 'One, Two,Three, Four,Five'

a_list = a_string.split(', ')
for index, value in enumerate(a_list):
    split = value.split(',')
    a_list[index] = split

a_list = list(itertools.chain.from_iterable(a_list))

print(a_list)
