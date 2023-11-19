import hashlib
import base64

szoveg = input("Kérem adja meg a szöveget titkosításra: ")
titkositas = input("Kérem válasszon egy titkosítási formát az alábbiak közül\r\nsha-256 -> 1\r\nbase64 -> 2\r\nmd-5 -> 3\r\nválasz: ")


while True:
    try:
        szam = int(titkositas)
        if szam == 1:
            dekodsha = (hashlib.sha256(szoveg.encode('utf-8')).hexdigest())
            print(f"A sha-256 kódolt szöveged: {dekodsha}")
            break
        elif szam == 2:
            utfenc = szoveg.encode('utf-8')
            dekod64 = (base64.b64encode(utfenc))
            print(f"A base64-es kódolt szöveged: {dekod64}")
            break
        elif szam == 3:
            dekodmd5 = (hashlib.md5(szoveg.encode('utf-8')).hexdigest())
            print(f"Az md-5 kódolt szöveged: {dekodmd5}")
            break
        else:
            print("Nem megfelelő adat")
            titkositas = input("Kérem válasszon egy titkosítási formát az alábbiak közül\r\nsha-256 -> 1\r\nbase64 -> 2\r\nmd-5 -> 3\r\nválasz: ")
    except:
        print("Nem megfelelő típusú adat: ")
        titkositas = input("Kérem válasszon egy titkosítási formát az alábbiak közül\r\nsha-256 -> 1\r\nbase64 -> 2\r\nmd-5 -> 3\r\nválasz: ")


