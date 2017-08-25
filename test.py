
a_string = 'one, two'

new = a_string.split(',')
for index, item in enumerate(new):
    print(index)
    new[index] = new[index].strip()

print(new)

if 'w' in a_string:
    print('Ok')
