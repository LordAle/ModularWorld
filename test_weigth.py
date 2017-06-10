import random

class w_item:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

item_list = [w_item('One',10000), w_item('Two',100), w_item('Three',50), w_item('Four',25), w_item('Five',1)]
result = {'One': 0, 'Two': 0, 'Three': 0, 'Four': 0, 'Five': 0}

total_w = 0
for item in item_list:
    total_w = total_w + item.weight


def select_random(s_list, weight):
    choice = random.randint(1, weight)
    for i in s_list:
        choice = choice - i.weight
        if choice <= 0:
            return i.name

for x in range(100000):
    selected = select_random(item_list, total_w)
    result[selected] += 1

print(result)

odds = [result['One']/100000, result['Two']/100000, result['Three']/100000, result['Four']/100000, result['Five']/100000]
expected = [10000/10176, 100/10176, 50/10176, 25/10176, 1/10176]

print(odds)
print(expected)

