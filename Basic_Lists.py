short_names = ['Chris', 'Hank', 'Joel']
print(short_names)
short_names.append('Bruce') # Add to end of list
print('After append: ', short_names)
short_names.pop(3)          # Remove element at index
print('After .pop removal: ', short_names)
short_names.append('Rusty')
print('After append: ', short_names)
short_names.remove('Rusty') # Remove element with value 'x'
print('After .remove removal: ', short_names)
print(short_names[0])
print(short_names[1])
print(short_names[2])
short_names[2] = 'Junavae'
