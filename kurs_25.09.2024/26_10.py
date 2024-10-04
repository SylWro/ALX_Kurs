txt = "hobby"
wystąpienia = {}

for letter in txt:
    if letter not in wystąpienia:
        wystąpienia[letter] = 1
    else:
        wystąpienia[letter] += 1

print(wystąpienia)
