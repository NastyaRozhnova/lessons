a = 5
b = '5'

#            0           1          2
fridge = ['fruits', 'vegetables', 'milk', 'sugar', 'bread']
#                                            -2       -1
# print(fridge[1])

# print(type(a))
# print(type(b))
# print(type(fridge))

get = input('Что достать?\n')

while get not in fridge:
    print('не в холодильнике')
    get = input('Что достать?\n')

print('в холодильнике')

for el in fridge[1:]:
    print(el)