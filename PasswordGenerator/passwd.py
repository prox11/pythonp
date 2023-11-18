import random
import string

lista1 = list(string.ascii_lowercase)
lista2 = list(string.ascii_uppercase)
lista3 = list(string.digits)
lista4 = list(string.punctuation)

print("Üdv a jelszó generáló programomban.")

db = input("Milyen hosszúságú legyen a jelszó: ")


while True:
    try:
        szam = int(db)
        if szam < 8:
            print("Legalább 8 karakter hosszúságú legyen.")
            db = input("Kérem adja meg a hosszúságot újra: ")
        elif szam >= 53:
            print("Kisebb legyen mint 53 karakter. ")
            db = input("Kérem adja meg a hosszúságot újra: ")
        else:
            break
    except:
        print("Nem megfelelő érték")
        db = input("Kérem adjon meg egy egész számot: ")

random.shuffle(lista1)
random.shuffle(lista2)
random.shuffle(lista3)
random.shuffle(lista4)

eredmeny = []

part1 = round(szam * (30/100))
part2 = round(szam * (20/100))

for i in range(part1):
    eredmeny.append(lista1[i])
    eredmeny.append(lista2[i])

for i in range(part2):
    eredmeny.append(lista3[i])
    eredmeny.append(lista4[i])

random.shuffle(eredmeny)

passwd = "".join(eredmeny)
print(f"Az eredmény: {passwd}")


