import random
import string
import tkinter as ttk

def jelszo_gen():
    lista1 = list(string.ascii_lowercase)
    lista2 = list(string.ascii_uppercase)
    lista3 = list(string.digits)
    lista4 = list(string.punctuation)

    db = bevitel.get()

    while True:
        try:
            szam = int(db)
            if szam < 8:
                result_label.config(text="Legalább 8 karakter hosszú legyen.")
                return
            elif szam >= 53:
                result_label.config(text="Legfeljebb 52 karakter lehet.")
                return
            else:
                break
        except:
            result_label.config(text="Nem megfelelő érték")
            return

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
    result_label.config(text=f"A generált jelszó: {passwd}")


root = ttk.Tk()
root.title("Jelszó generátor ablak")
root.geometry("600x300")

root.configure(bg='#FFA500')

szoveg = ttk.Label(root, text="Üdv a jelszó generáló ablakban!\r\n Milyen hosszú legyen a jelszó?", bg='#FFA500', fg='black')
szoveg.pack()

bevitel = ttk.Entry(root)
bevitel.pack()

gomb = ttk.Button(root, text="Generálás", command=jelszo_gen, bg='black', fg='white')
gomb.pack(pady=10)

result_label = ttk.Label(root, text="", bg='#FFA500', fg='black')
result_label.pack()

root.mainloop()
