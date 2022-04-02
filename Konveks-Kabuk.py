#Konveks Kabuk algoritması
#Noktaların sınıf olarak tanımlanması
import matplotlib.pyplot as plt

class Nokta:
    #Sınıfta apsis ve ordinatı tanımladık
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y

#Sıralama algoritması olarak bubblesort algoritması kullanacağım.
#Bu algoritma parametre olarak liste alacak.
def bubbleSort(liste):
  for i in range(len(liste)):
    for j in range(0, len(liste) - i - 1):
      if liste[j].x > liste[j + 1].x:
        temp = liste[j]
        liste[j] = liste[j+1]
        liste[j+1] = temp
    return liste

def donus_yonu(p,q,r):
    deger = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    '''
    0 ==> p, q ve r lineerdir.
    1 ==> Saat yönünde dönüş yapıyor.
    2 ==> Saat yönünün tersine dönüş yapıyor.
    '''
    if deger == 0:
        return 0

    elif deger > 0:
        return 1

    else:
        return 2


def konveks_kabuk(liste):
    L_ust = list()
    L_alt = list()
    #Programa verdiğimiz listeyi x ekseni değerlerine göre sıraladık.
    sirali_liste = bubbleSort(liste)
    #Üst kabuktan başladık ilk iki elemanı ekledik.
    L_ust.append(sirali_liste[0])
    L_ust.append(sirali_liste[1])
    #L_ust = [ sirali_liste[0],sirali_liste[1]]

    for nkt_indis in range(2,len(liste)):
        L_ust.append(sirali_liste[nkt_indis])
        while(len(L_ust)>2 and donus_yonu(L_ust[-3],L_ust[-2],L_ust[-1])!=1):
            L_ust.remove(L_ust[-2])
    #Üst kabuk tamamlandı.
    #Alt kabuk hesaplanacak.

    L_alt = [ sirali_liste[-1],sirali_liste[-2]]

    for nkt_indis_ in range(len(sirali_liste)-2,1,-1):
        L_alt.append(sirali_liste[nkt_indis_])
        while(len(L_alt)>2 and donus_yonu(L_alt[-3],L_alt[-2],L_alt[-1])!=1):
            L_alt.remove(L_alt[-2])
    L_alt.remove(L_alt[0])
    L_alt.remove(L_alt[-1])
    L = L_ust + L_alt
    return L

noktalar = []
noktalar.append(Nokta(1, 1))
noktalar.append(Nokta(1.5, 2))
noktalar.append(Nokta(1, 3))
noktalar.append(Nokta(2, 2.5))
noktalar.append(Nokta(2, 3))
noktalar.append(Nokta(3, 2))
noktalar.append(Nokta(3, 2))
noktalar.append(Nokta(4, 2))
noktalar.append(Nokta(4, 1))
noktalar.append(Nokta(2, 1))
liste_ = konveks_kabuk(noktalar)

for eleman_ in noktalar:
    plt.plot(eleman_.x,eleman_.y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
for eleman in liste_:
    plt.plot(eleman.x,eleman.y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="blue")
    print(str(eleman.x) +","+str(eleman.y))
    
plt.show()

