dane = open("dane2.txt", "r")
do_usuniecia = "CCC"
lista = []

for x in dane:
    lista.append(x)

dane.close()
print(lista)

while do_usuniecia+"\n" in lista:
    for elem in lista:
        if elem.strip() == do_usuniecia:
            lista.remove(elem)
            break

dane = open("dane2.txt", "w")
dane.writelines(lista)
dane.close()

print(lista)


