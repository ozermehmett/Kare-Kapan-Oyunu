import sys
import time

tahta = []
MIN_YATAY = 3
MAX_YATAY = 7
HARFLER = ["A","B","C","D","E","F","G","H"]
hamle = ""


def kapat():   #oyun bitiminde kodu sonlandırma fonksiyonu
    print("""
                UYGULAMA KAPATILIYOR....
              """)
    time.sleep(3)
    sys.exit()
    

def tahtaKontrol(yatay):    #verilen yatay çizgi sayısı şartımızı sağlıyor mu diyw kontrol ettik
    if yatay <= 7 and yatay >= 3:
        return True
    else:
        return False


def ekle(yatay,HARFLER,hamle,renk):     #yeni taş ekleme fonksiyonu
    j = int(hamle[1]) - 1   #yatay indexi aldık
    for i in range(len(HARFLER)):  #harf indexini aldık
        if hamle[0] == HARFLER[i]:
          break
    tahta[j][i] = renk
    goruntule(yatay,HARFLER)


def cikar(yatay,HARFLER,hamle):    # taş çıkarma fonksiyonu
    j = int(hamle[1]) - 1   #yatay indexi aldık
    for i in range(len(HARFLER)):  #harf indexini aldık
        if hamle[0] == HARFLER[i]:
          break 
    tahta[j][i] = " "
    goruntule(yatay,HARFLER)


def konumDegistir(yatay,HARFLER,yerDegistir):   #bir taşın konumunu değiştirme fonksiyonu
    j = int(yerDegistir[1]) - 1   # yer degstircek olan yatay indexi aldık
    for i in range(len(HARFLER)):  #yer degstircek olan  harf indexini aldık
        if yerDegistir[0] == HARFLER[i]:
          break
    x = int(yerDegistir[4]) - 1   #yeni konumunun yatay indexi aldık
    for y in range(len(HARFLER)):  #yeni konumunun harf indexini aldık
        if yerDegistir[3] == HARFLER[y]:
          break
    tahta[x][y] = tahta[j][i]  # yeni konumuna ekledik
    hamle = yerDegistir[0] + yerDegistir[1]  # matrixden silmek için eski konumu aldık
    cikar(yatay,HARFLER,hamle)    # matrixden sildik
    goruntule(yatay,HARFLER)   


def kareKontrol(yatay,tahta,bKare,sKare):  #oluşan karelerin sayısını döndürür
    for i in range(yatay - 1):
        for j in range(yatay):
            if tahta[i][j] == tahta[i][j+1] == tahta[i+1][j] == tahta[i+1][j+1]:
                if tahta[i][j] == "B":
                    bKare += 1
                elif tahta[i][j] == "S":
                    sKare += 1
    return bKare,sKare


def yeniKare(yatay,tahta,hamle):    #konumu değişen taşın yeni kare oluşturup oluşturmadığını kontrol eden fonksiyon
    x = int(hamle[4]) - 1   #yeni konumunun yatay indexi aldık
    for y in range(len(HARFLER)):  #yeni konumunun harf indexini aldık
        if hamle[3] == HARFLER[y]:
          break
    if yatay-1 > x and yatay > y:   #eğer ki taşın konumu sınırlarda değilse etraftaki 4 alanı kontrol eder
        if tahta[x][y] == tahta[x+1][y] == tahta[x+1][y+1] == tahta[x][y+1]:  #sağ alt
            return True
        if tahta[x][y] == tahta [x-1][y] == tahta[x-1][y+1] == tahta[x][y+1]: #sağ üst
            return True
        if tahta[x][y] == tahta [x-1][y-1] == tahta[x-1][y] == tahta[x][y-1]: #sol üst 
            return True
        if tahta[x][y] == tahta [x][y-1] == tahta[x+1][y-1] == tahta[x+1][y]: #sol alt
            return True
    if x == 0 and y > 0:    #eğer taş [0][i] i>0 indeksindeyse kontrol eder
        if tahta[x][y] == tahta [x][y-1] == tahta[x+1][y-1] == tahta[x+1][y]:
            return True
    if x == 0 and y < yatay:  #eğer taş [0][i] i<max indeksindeyse kontrol eder
        if tahta[x][y] == tahta [x+1][y] == tahta[x][y+1] == tahta[x+1][y+1]:
            return True
    if x == yatay-1 and y > 0:  #eğer taş [i][j] i = max, j>0 indeksindeyse kontrol eder
        if tahta[x][y] == tahta [x][y-1] == tahta[x-1][y-1] == tahta[x-1][y]:   
            return True
    if x == yatay-1 and y < yatay:  #eğer taş [i][j] i = max, j < max indeksindeyse kontrol eder
        if tahta[x][y] == tahta [x-1][y] == tahta[x][y+1] == tahta[x-1][y+1]:
            return True
        

def goruntule(yatay,HARFLER):   #oyun tahtasını görüntülememizi sağlayan fonksiyon
    araSatir = "|" + ("   "+"|")*yatay
    HARFLER = HARFLER[:yatay+1]
    print("  ", end='')  #A harfiden önce2 bosluk
    for harf in HARFLER:  # harfler yazdı
        print(f"{harf:3} ",end='')
    print()  #alt satıra gectı
    for i in range(yatay):   #orta kısıma matrixleri yazdırdık
        print(f"{i+1}","---".join(tahta[i]),f"{i+1}")
        if i == yatay-1:
            break
        print(f"  {araSatir}")
    print("  ",end='')  #A harfiden önce2 bosluk
    for harf in HARFLER:  # harflerı yazdık
        print(f"{harf:4}",end='')
    print("\n\n")  # alt satıra gectı

def sayi_mi(yatay):    #girilen yatay çizgi sayısının integer türünde olup olmadığını kontrol eder ve
    try:               #değilse yeniden input alır
        yatay = int(yatay)
        return yatay
    except:
        main()


def kontrol1(yatay,HARFLER,bKare,sKare,durumS,durumB,hamle):   #taş çıkarma ve konum değiştirme fonksiyonu
    while bKare+sKare > 0:                                     # bir oyun sonu burada konrtol ediliyor
        first = False
        if bKare > 0:
            hamle = input("Lütfen çıkarmak istediğiniz siyah taşın konumunu giriniz: ")
            hamle = hamle.upper()
            if len(hamle) == 2:    
                cikar(yatay,HARFLER,hamle)
                durumB = True
                first = True
                bKare -= 1
            else:
                print("Lütfen geçerli bir hamle giriniz!!")
            
        elif sKare > 0:
            hamle = input("Lütfen çıkarmak istediğiniz beyaz taşın konumunu giriniz: ")
            hamle = hamle.upper()
            if len(hamle) == 2:    
                cikar(yatay,HARFLER,hamle)
                durumS = True
                first = True
                sKare -= 1
            else:
                print("Lütfen geçerli bir hamle giriniz!!")
        else:
            break
    else:        
        print("Hiç kare oluşmadığı için taş çıkarma sırası beyazda")
        hamle = input("Lütfen çıkarmak istediğiniz taşın konumunu giriniz: ")
        hamle = hamle.upper()
        while True:
            if len(hamle) == 2:    
                cikar(yatay,HARFLER,hamle)
                durumB = True
                break
            else:
                print("Lütfen geçerli bir hamle giriniz!!")    
    return durumS,durumB


def oyunSonu(yatay,tahta):   #oyunun bitip bitmediğini kontrol eden fonksiyon
    bSayac = 0
    sSayac = 0
    for i in range(yatay-1):
        for j in range(yatay):
            if tahta[i][j] == "B":
                bSayac += 1
            if tahta[i][j] == "S":
                sSayac += 1    
    if sSayac == 3:
        print("Kazanan Beyaz")
        kapat()
    if bSayac == 3:
        print("Kazanan Siyah")
        kapat()

    
def main():      #oyunun akışını sağlayan ana fonksiyon
    durumB = False 
    durumS = False
    bKare = 0
    sKare = 0
    renk = "B"
    yatay = input("Lütfen yatay çizgi sayısını giriniz: ")
    yatay = sayi_mi(yatay)
    if type(sayi_mi(yatay)) == int:
        if not tahtaKontrol(yatay):
            main()

    for i in range(yatay):     #matris olusturduk
        tahta.append((yatay+1)*[" "])      

    goruntule(yatay,HARFLER)
    beyazTas = int((yatay*(yatay+1))/2)
    siyahTas = int((yatay*(yatay+1))/2)
    

    while siyahTas+beyazTas > 0:   #tüm taşları yerleştirmeye yarayan döngü
        hamle = input("Lütfen hamle giriniz: ")
        hamle = hamle.upper()
        if len(hamle) == 2:    
            ekle(yatay,HARFLER,hamle,renk)
            if renk == "B":
                beyazTas -= 1
                renk = "S"
            else:
                beyazTas -= 1
                renk = "B"
        else:
            print("Lütfen geçerli bir hamle giriniz!!")
    bKare,sKare = kareKontrol(yatay,tahta,bKare,sKare)   #oluşan karelerin sayısını döndüren fonksiyonu çağırır
    durumS,durumB = kontrol1(yatay,HARFLER,bKare,sKare,durumS,durumB,hamle)  #taş çıkarma ve konum değiştirmeye yarayan fonksiyonu çağırır

    
    while True:   #oyun sonunun gelip gelmediğini kontrol eden döngü
        if durumB:
            hamle = input("Lütfen konumunu değiştirmek istediğiniz taşın mevcut konumu boşluk yeni konumunu giriniz: ")
            hamle = hamle.upper()
            if len(hamle) == 5:    
                konumDegistir(yatay,HARFLER,hamle)
                if yeniKare(yatay,tahta,hamle):
                    hamle = input("Lütfen çıkarmak istediğiniz siyah taşın konumunu giriniz: ")
                    hamle = hamle.upper()
                    cikar(yatay,HARFLER,hamle)
                    durumB = False
            else:
                print("Lütfen geçerli bir hamle giriniz!!")
        if durumS:
            hamle = input("Lütfen konumunu değiştirmek istediğiniz taşın konumunu giriniz: ")
            hamle = hamle.upper()
            if len(hamle) == 5:    
                konumDegistir(yatay,HARFLER,hamle)
                if yeniKare(yatay,tahta,hamle):
                    hamle = input("Lütfen çıkarmak istediğiniz beyaz taşın konumunu giriniz: ")
                    hamle = hamle.upper()
                    cikar(yatay,HARFLER,hamle)
                    durumB = False      
            else:
                print("Lütfen geçerli bir hamle giriniz!!")

        oyunSonu(yatay,tahta)

main()

