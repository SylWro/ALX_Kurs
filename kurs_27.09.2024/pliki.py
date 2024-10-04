plik = open("dane.txt", "r")        # read, write, append

# v1
# print(plik.readline())
# print(plik.readline())


# v2
# dane = plik.readlines()
# for x in dane:
#     print(x.strip())
#
# print("-----------------------------------")
#
# plik.seek(0)    # powrot kursora do znaku 1 linijki 1
# dane = plik.readlines()
# for x in dane:
#     print(x.strip())


# v3
for x in plik:
    print(x.strip())

plik.close()
txt = "aaa:ddd:asd:asdff"
x = txt.split(":")
print(x)


