
oyuncu=0
oyuncu1=0
def clr():
     print('\n' *20)
def basamak_oyuncu(sayi):
    while sayi< 1000 or sayi > 9999:
        sayi = int(input("Lütfen 4 haneli ve rakamları farklı bir sayi giriniz:\n"))
    l = str(sayi)
    kontrol = True
    while kontrol:
        kontrol = False
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] == l[j] and i != j:
                    sayi = int(input("Lütfen 4 haneli ve rakamları farklı bir sayi giriniz:\n"))
                    l = str(sayi)
                    kontrol = True
    return int(l)
def kullanici_tahmin(pc,t):
    kontrol = 0
    while kontrol < 4:
        while True:
            try:
                print("*****1.OYUNCU TAHMİN*****")
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
def kullanici1_tahmin(pc,t):
    kontrol = 0
    while kontrol < 4:
        while True:
            try:
                print("*****2.OYUNCU TAHMİN*****")
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
                    t=0
                elif pc[m] == str_tahmin[n] and m != n:
                    print("-")
                    t=0
                else:
                    t=0
        return t,kontrol
def kullanici_start(sayi):
    while True:
        try:
            sayi = basamak_oyuncu(sayi)
            break
        except ValueError :
            print("Yanlış bir değer girdiniz!!!\n")
    return sayi


#KULLANICADAN SAYI ALIP KONTROL EDİYORUZ!!
print("""************
  1.OYUNCU 
************""")
oyuncu=kullanici_start(oyuncu)
clr()
print("""************
  2.OYUNCU 
************""")
oyuncu1=kullanici_start(oyuncu1)
clr()

#VERİ TİPİNİ DEĞİŞTİRİYORUZ
str_oyuncu=str(oyuncu)
str_oyuncu1=str(oyuncu1)

#KULLANICININ VE KULLANİCİ1'İN SAYIYI TAHMİN ETTİĞİ KISIM
#print(str_oyuncu)
#print(str_oyuncu1)
t=0

bitti=0
while bitti<4:
    bitti=0
    if bitti!=4:
        while t == 0:
            t,bitti=kullanici_tahmin(str_oyuncu1,t)
            if bitti==4:
                print("""------------------
1.OYUNCU KAZANDİ..
------------------
""")
    if bitti!=4:
        while t == 1:
            t,bitti=kullanici1_tahmin(str_oyuncu,t)
            if bitti==4:
                print("""------------------
2.OYUNCU KAZANDİ..
------------------
""")