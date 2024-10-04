from random import randint

list1 = []
list2 = []

for i in range(10):
    list1.append(randint(1, 20))
    list2.append(randint(1, 20))


def find_common_highest_in_two_lists(list1, list2):
    common = []
    for elem in list2:
        if elem in list1 and elem not in common:
            common.append(elem)
    for n in range(len(common)):
        for i in range(len(common) - n - 1):
            if common[i] > common[i + 1]:
                common[i], common[i + 1] = common[i + 1], common[i]
    print(f"Najwieksza wspolna liczba to: {common[-1]}")

print(list1)
print(list2)
find_common_highest_in_two_lists(list1, list2)




