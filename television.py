import time

class Kumanda:

    def __init__(self,tv_durum = False,tv_ses = 0, kanal_listesi = ["TRT","KANAL D"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def __str__(self):
        return """
            ## Televizyon Bilgileri ##
            
            Marka : Samsung
            Model : IG-RE3419
            Durumu : {}
            
            ## Kanal Bilgileri ##
            
            Son Açık Kanal : {}
            Son Ses Seviyesi : {}
            
        """.format(self.tv_durum,self.kanal,self.tv_ses)

    def __len__(self):
        return len(self.kanal_listesi)

    def tv_kontrol(self):
        if(self.tv_durum == False):
            print("Televizyonunuz Açık Değil. Açmak İster misiniz ? ( E / H )")
            tv_open = input()
            if (tv_open == "e" or tv_open == "E"):
                self.tv_ac()
            else:
                print("Televizyonu açtıktan sonra tekrar deneyin")

    def tv_ac(self):
        if(self.tv_durum == True):
            print("Televizyon Zaten Açık")
        else:
            self.tv_durum = True
            print("Televizyon Açılıyor...")
            time.sleep(1)
            print("Televizyon {} kanalında, {} ses seviyesiyle açıldı".format(self.kanal,self.tv_ses))

    def tv_kapat(self):
        if (self.tv_durum == False):
            print("Televizyon Zaten Kapalı")
        else:
            self.tv_durum = False
            print("Televizyon Kapatıldı...")

    def ses_ayarlari(self):
        self.tv_kontrol()
        islem_durumu = False
        while (islem_durumu == False):
            print("Ses için ne yapmak istersiniz (seviye : {} )? ( Y / A ) : ".format(self.tv_ses))
            talep = input()
            print("Ne kadar ? :")
            miktar = input()

            if (talep == "Y" or talep == "y"):
                if (self.tv_ses + int(miktar) > 100):
                    self.tv_ses = 100
                else:
                    self.tv_ses += int(miktar)
                islem_durumu = True
            elif (talep == "A" or talep == "a"):
                if (self.tv_ses - int(miktar) < 0):
                    self.tv_ses = 0
                else:
                    self.tv_ses -= int(miktar)
                islem_durumu = True
            else:
                print("Hatalı Bir İşlem Kodu Girdiniz Tekrar Deneyiniz.")
            print("Ses Seviyesi : {}".format(self.tv_ses))
    def kanal_degistir(self):
        self.tv_kontrol()
        print("Lütfen kanal numarası giriniz :")
        acilacak_kanal = input()

        if(int(acilacak_kanal) > len(self.kanal_listesi) + 1):
            print("Hatalı Kanal, İşlem İptal Edildi")
        else:
            self.kanal = self.kanal_listesi[int(acilacak_kanal)-1]
            print("Kanal Değiştirildi, Yeni Kanal {} olarak ayarlandı".format(self.kanal))

    def list(self):
        i = 1
        for kanallar in self.kanal_listesi:
            print("{} - ) {}".format(i,kanallar))
            i += 1

    def kanal_ekle(self):
        self.tv_kontrol()
        print("Eklemek İstediğiniz Kanalın Adı : ")
        eklenecek_kanal = input()
        sira = 1
        ekleme = True
        for kanallar in self.kanal_listesi:
            if(kanallar.upper() == eklenecek_kanal.upper()):
                print("Bu kanal zaten {} numaralı sırada ekli".format(sira))
                ekleme = False
                break
            sira += 1

        if(ekleme == True):
            self.kanal_listesi.append(eklenecek_kanal.upper())
            print("Yeni kanal ekleniyor...")
            time.sleep(1)
            print("{} isimli kanal {} numaralı sıraya eklendi".format(eklenecek_kanal, sira))

    def otomatik_kapat(self):
        self.tv_kontrol()
        print("Televizyonunuzu kaç saniye sonra kapatmak istersiniz ? : ")
        otomatik_sayac = input()
        print("Süre Başlatıldı...")
        time.sleep(int(otomatik_sayac))
        print("Televizyon Kapatılıyor...")
        self.tv_kapat()

televizyon = Kumanda()

exit = False

while(exit == False):
    print("""
        ### İŞLEM SEÇİNİZ ###
        
        1-) TV Aç
        2-) Ses Ayarı Yap
        3-) Kanal Değiştir
        4-) Kanal Listesini Göster
        5-) TV Kapat
        6-) Kanal Ekle
        7-) Otomatik Kapat
        8-) Toplam Kanal Sayısı
        9-) Bilgiler
        10-) Çıkış
    """)
    secilen_islem = input()

    if(secilen_islem == "1"):
        televizyon.tv_ac()
        continue
    elif(secilen_islem == "2"):
        televizyon.ses_ayarlari()
        continue
    elif(secilen_islem == "3"):
        televizyon.kanal_degistir()
    elif(secilen_islem == "4"):
        televizyon.list()
    elif(secilen_islem == "5"):
        televizyon.tv_kapat()
        continue
    elif (secilen_islem == "6"):
        televizyon.kanal_ekle()
        continue
    elif (secilen_islem == "7"):
        televizyon.otomatik_kapat()
        continue
    elif (secilen_islem == "8"):
        print("Toplam Kanal Sayısı : {}".format(len(televizyon)))
        continue
    elif (secilen_islem == "9"):
        print(televizyon)
        continue
    elif(secilen_islem == "10"):
        exit = True
        print("Hoşçakalın....")
        break
    else:
        print("Hatalı İşlem Tekrar Deneyin")
        continue
