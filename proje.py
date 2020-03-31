import random
import time
oyuncu=0
def basamak_pc(pcsayi):
    l=str(pcsayi)
    kontrol = True
    while kontrol:
        kontrol = False
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] == l[j] and i != j:
                    pcsayi = random.randint(1000, 9999)
                    l = str(pcsayi)
                    kontrol = True
    return int(l)
def basamak_oyuncu(sayi):
    while sayi< 1000 or sayi > 9999:
        sayi = int(input("Lütfen 4 haneli ve rakamları farklı bir sayi giriniz:"))
    l = str(sayi)
    kontrol = True
    while kontrol:
        kontrol = False
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] == l[j] and i != j:
                    sayi = int(input("Lütfen 4 haneli ve rakamları farklı bir sayi giriniz:"))
                    l = str(sayi)
                    kontrol = True
    return int(l)
def kullanici_tahmin(pc,t):
    kontrol = 0
    while kontrol < 4:
        while True:
            try:
                tahmin = int(input("Tahmin sayinizi giriniz: "))
                tahmin = basamak_oyuncu(tahmin)
                break
            except ValueError:
                print("Yanlış bir değer girdiniz!!!\n")
        str_tahmin = str(tahmin)
        kontrol = 0
        for m in range(len(pc)):
            for n in range(len(pc)):
                if pc[m] == str_tahmin[n] and m == n:
                    print("+")
                    kontrol += 1
                    t=1
                elif pc[m] == str_tahmin[n] and m != n:
                    print("-")
                    t=1
                else:
                    t=1
        return t,kontrol
def kullanici_start(sayi):
    while True:
        try:
            sayi = basamak_oyuncu(sayi)
            break
        except ValueError :
            print("Yanlış bir değer girdiniz!!!\n")
    return sayi
def pc_tahmin(kullanici,t):
    kontrol = 0
    while kontrol < 4:
        pc=random.randint(1000,9999)
        pc= basamak_pc(pc)
        st_pc=str(pc)
        kontrol=0
        print("Bilgisayar tahmin ediyor...")
        time.sleep(1)
        for m in range(len(kullanici)):
            for n in range(len(kullanici)):
                if kullanici[m] == st_pc[n] and m == n:
                    print("+")
                    kontrol += 1
                    t=0
                elif kullanici[m] == st_pc[n] and m != n:
                    print("-")
                    t=0
                else:
                    t=0
        return t,kontrol

#KULLANICADAN SAYI ALIP KONTROL EDİYORUZ!!
oyuncu=kullanici_start(oyuncu)

#BİLGİSAYARA RANDOM SAYI ATTIRIP KONTROL EDİYORUZ!!!
pc_sayi=random.randint(1000,9999)
pc_sayi=basamak_pc(pc_sayi)

#VERİ TİPİNİ DEĞİŞTİRİYORUZ
str_oyuncu=str(oyuncu)
str_pc=str(pc_sayi)

#KULLANICININ VE PC'NİN SAYIYI TAHMİN ETTİĞİ KISIM
print(str_oyuncu)
print(str_pc)
t=0
bitti=0
while bitti<4:
    bitti=0
    if bitti!=4:
        while t == 0:
            t,bitti=kullanici_tahmin(str_pc,t)
            if bitti==4:
                print("OYUNU KAZANDİNİZ..")
    if bitti!=4:
        while t == 1:
            t,bitti=pc_tahmin(str_oyuncu,t)
            if bitti==4:
                print("BİLGİSAYAR KAZANDİ..")