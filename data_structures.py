
sample_list = [1, 2, 3, 4, 5]

print(sample_list)

sample_list.append(6)

print("\n6 added")
print(sample_list)

sample_list.insert(0, 99)

print("\n99 inserted")
print(sample_list)

# sample_list[0] = sample_list[0] + 1
sample_list[0] += 1

print("\n99 to 100")
print(sample_list)

# sample_list = sample_list + [10]
# sample_list.extend([10])
sample_list += [10]
print("\n10 added")
print(sample_list)

sample_list.remove(10)
print("\n10 removed")
print(sample_list)

sample_list.pop()
sample_list.pop(0)
print("\npopped and 0 popped")
print(sample_list)

# sample_list_joined = ' '.join(sample_list)
# print("\n10 removed")
# print(sample_list)

list_of_names = ['Ayo', 'Dele', 'Dami', 'Lola', 'Gbengene']
names_joined = '*'.join(list_of_names)
print("\nNames Joined")
print(names_joined)

print(tuple(sample_list))
