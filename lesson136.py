data = ['a', 'ab', 'abc', 'abcd']
lengths = [len(element) for element in data]
print(lengths)

lengths = (len(element) for element in data)
print(lengths)
print(3 in lengths)



