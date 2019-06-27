pin = "1234"
giris = False
hak = 3
bakiye = 100

while True:
    if(hak < 1):
        print("Kartiniz bloke edilmistir, lutfen banka ile iletisime gecin")
        giris = False
        break
    print("Lutfen Sifrenizi Giriniz")
    girilen_pin = input()
    if(girilen_pin == pin):
        giris = True
        break
    else:
        giris = False
        hak -= 1
        print("Hatali sifre, {} deneme hakkiniz kaldi".format(hak))
        continue

if(giris == True):
    while True:
        print("""
                BANKAMIZA HOSGELDINIZ, LUTFEN ISLEM SECINIZ

                1-) Bakiye Goruntuleme
                2-) Hesaba Transfer
                3-) Cikis

            """)

        islem = input()

        if(islem == "3"):
            print("Hoscakalin, Kartinizi almayi unutmayin")
            break
        elif(islem == "1"):
            print("Hesabınızda bulunan toplam bakiye {} Turk Lirasidir.".format(bakiye))
            continue
        elif(islem == "2"):
            print("Transfer Yapacaginiz Hesabın IBAN Numarasini Giriniz")
            iban = input()
            print("Transfer Edilecek Ucreti Giriniz")
            eft = input()

            if(int(eft) > bakiye):
                print("Hesabınızda yeteri kadar bakiye bulunmuyor. Isleminiz iptal edildi.")
                continue
            else:
                print("{} IBAN numarasina {} TL gondermek istediginize emin misiniz ? ( E / H )".format(iban,eft))
                onay = input()
                if onay == "e" or onay == "E":
                    bakiye -= int(eft)
                    print("Transfer islemi gerceklesti, yeni bakiyeniz {} Turk Lirasidir".format(bakiye))
                    continue
                else:
                    print("Isleminiz Iptal Edildi")
                    continue
        else:
            print("Hatali Bir Islem Yaptiniz Lutfen Tekrar Deneyiniz")
            continue
