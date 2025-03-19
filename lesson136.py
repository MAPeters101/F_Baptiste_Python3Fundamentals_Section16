data = ['a', 'ab', 'abc', 'abcd']
lengths = [len(element) for element in data]
print(lengths)

lengths = (len(element) for element in data)
print(lengths)
print(3 in lengths)
print('-'*80)

def my_len(x):
    return len(x)

lengths = (my_len(element) for element in data)
print(list(lengths))

lengths = map(len, data)
print(lengths)
print(list(lengths))
print(list(lengths))
