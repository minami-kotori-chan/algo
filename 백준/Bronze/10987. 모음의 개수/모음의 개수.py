c = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0
sentence = input()
for s in sentence:
    if s in c:
        count += 1
print(count)