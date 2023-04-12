import time as t


class Bilgisayar():

    def __init__(self, bilgisayar_durumu = "Kapalı", bilgisayar_ses = 0, yüklü_programlar = ["Chrome", "Visual Code"], yüklü_oyunlar = ["Lol", "Valorant"]):
        self.bilgisayar_durumu = bilgisayar_durumu
        self.bilgisayar_ses = bilgisayar_ses
        self.yüklü_programlar = yüklü_programlar
        self.yüklü_oyunlar = yüklü_oyunlar

    def bilgisayar_ac(self):
        if self.bilgisayar_durumu == "Açık":
            print("Bilgisayar zaten açık.")
        else:
            print("Bilgisayar açılıyor...")
            self.bilgisayar_durumu = "Açık"
        
    def bilgisayar_kapat(self):
        if self.bilgisayar_durumu == "Kapalı":
            print("Bilgisayar zaten kapalı.")
        
        else:
            print("Bilgisayar kapatılıyor...")
            self.bilgisayar_durumu = "Kapalı"

        
    def ses_ayarları(self):
        
        while True:
            if self.bilgisayar_durumu =="Kapalı":
                print("Önce bilgisayarı açınız.")
                break
            else:

                istek = input("Bilgisayarın sesini arttırmak için '>' tuşunu tıklayıp Enter'a basınız.\nBilgisayarın sesini azaltmak için '<' tuşuna basıp Enter'a tıklayınız.\nÇıkış yapmak için herhangi bir tuşa basıp Enter'a tıklayınız.\n")

                if istek == ">":
                    if self.bilgisayar_ses != 100:
                        self.bilgisayar_durumu += 1
                    print(f"Güncel ses: {self.bilgisayar_ses}")
                if istek == "<":
                    if self.bilgisayar_ses != 0:
                        self.bilgisayar_ses -= 1
                        print(f"Güncel ses: {self.bilgisayar_ses}")
                else:
                    print("Ana menüye dönülüyor...")
                    break
    
    def program_yükle(self, yüklenicek_program):
            print("Program(lar) yüklenir...")
            t.sleep(1)
            self.yüklü_programlar.append(yüklenicek_program)
            print("Program(lar) yüklendi.")

    def oyun_yükle(self, yüklenicek_oyun):
        print("Oyun(lar) yükleniyor...")
        t.sleep(1)
        self.yüklü_oyunlar.append(yüklenicek_oyun)
        print("Oyun(lar) yüklendi.")
    
    def __str__(self):
        return f"Bilgisayar Durumu: {self.bilgisayar_durumu}\nYüklü Programlar: {self.yüklü_programlar}\nYüklü Oyunlar: {self.yüklü_oyunlar}\n Ses Durumu: {self.bilgisayar_ses}"
    
bilgisayar = Bilgisayar()

print("""Basit Bilgisayar Uygulaması

1. Bilgisayar'ı Aç

2. Bilgisayar'ı Kapat

3. Program Yükle

4. Oyun Yükle

5. Bilgisayar Ses Ayarları

6. Bilgisayar Bilgileri

7. Çıkış için 'Q' harfine tıklayınız.


""")

while True:
   
   
   
   işlem = input("Lütfen bir işlem seçiniz: ")

   if işlem == "Q":
       print("Çıkış yapılıyor.")
       break
   
   elif işlem == "1":
       bilgisayar.bilgisayar_ac()
    
 
   elif işlem == "2":
       bilgisayar.bilgisayar_kapat()

   elif işlem == "3":
    
    if bilgisayar.bilgisayar_durumu == "Kapalı":
       print("Önce bilgisayarı açınız.")
       break

    else:
         
       programlar = input("Yüklenecek Programları aralarından ',' olacak şekilde giriniz: ").split(",")

       for i in programlar:
           bilgisayar.program_yükle(i)
   elif işlem == "4":
       
       oyunlar = input("Yüklenecek Oyunları aralarından ',' olacak şekilde giriniz: ").split(",")
       
       for i in oyunlar:
           bilgisayar.oyun_yükle(i)

   elif işlem == "5":
       bilgisayar.ses_ayarları()

   elif işlem == "6":
       print(bilgisayar)
