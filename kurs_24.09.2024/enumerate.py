# dane = ["adam", "piotr", "karina", "alx", "sylwia"]
#
# imie = "alx"
# noweImie = "robert"
#
# for x, i in enumerate(dane):
#     if i == imie:
#         dane[x] = noweImie
#
#
# print(dane)

dane = ["adam", "piotr", "karina", "alx", "sylwia", "alx", "janusz", "wojciech"]

imie = "alx"
list_of_alx = []

for x, i in enumerate(dane):
    if i == imie:
        list_of_alx.append(x)

index = list_of_alx[1]
dane[index] = "TEST"

print(dane)
