dane = open("ksiazki.txt", "r")

for x in dane:
    dane2 = x.strip().split(";")
    print(f"Autor {dane2[0]}, Tytuł {dane2[1]}, Rok {dane2[2]}.")

dane.close()

with open("ksiazki.txt") as dane:
    for x in dane:
        dane2 = x.strip().split(";")
        print(f"Autor {dane2[0]}, Tytuł {dane2[1]}, Rok {dane2[2]}.")

with open("dane2.txt", "w") as dane2:
    dane2.write("abcd")

