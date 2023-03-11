def ikinci_deger_al(x):
    return x[1]


def atletleri_sirala(isimler, dereceler):
    liste = []
    for i in range(1, len(isimler) + 1):
        k = isimler[i - 1], dereceler[i - 1]
        liste.append(k)
    liste.sort(reverse=True, key=ikinci_deger_al)
    return liste


atlet_say = int(input("Yarışmaya katılan atlet sayısını giriniz"))
isim_liste = []
for i in range(1, atlet_say + 1):
    ad_soyad = input("Yarışmacı atletin adını soyadını giriniz:")
    isim_liste.append(ad_soyad)

liste_atis = []
birinci_atislar = []
for i in range(1,atlet_say+1):
    birinci_atis = float(input("1.eleme atış değerini giriniz:"))
    birinci_atislar.append(birinci_atis)
ikinci_atislar = []
for i in range(1,atlet_say+1):
    ikinci_atis = float(input("2. eleme atış değerini giriniz:"))
    ikinci_atislar.append(ikinci_atis)
ucuncu_atislar = []
for i in range(1,atlet_say+1):
    ucuncu_atis = float(input("3. eleme atış değerini giriniz:"))
    ucuncu_atislar.append(ucuncu_atis)
deger = []
for i in range(len(isim_liste)):
    deger.append(birinci_atislar[i])
    deger.append(ikinci_atislar[i])
    deger.append(ucuncu_atislar[i])
    liste_atis.append(max(deger))
print(liste_atis)
isim_liste = isim_liste[:8]
print(isim_liste)
atletleri_sirala(isim_liste, liste_atis)
for i in isim_liste:
    deger = isim_liste.index(i)
    atis = liste_atis[deger]
    if atis > 50 and i not in isim_liste:
        isim_liste.append(i)
        liste_atis.append(atis)
print(isim_liste)
print(liste_atis)
final_list_atis = []
dorduncu_atislar = []
for i in range(1,atlet_say+1):
        dorduncu_atis = float(input("4.final atış değerini giriniz:"))
        dorduncu_atislar.append(dorduncu_atis)
besinci_atislar = []
for i in range(1,atlet_say+1):
        besinci_atis = float(input("5. final atış değerini giriniz:"))
        besinci_atislar.append(besinci_atis)
altıncı_atislar = []
for i in range(1,atlet_say+1):
        altıncı_atis = float(input("6. final atış değerini giriniz:"))
        altıncı_atislar.append(altıncı_atis)
deger = []
for i in range(atlet_say):
    deger.append(dorduncu_atislar[i])
    deger.append(besinci_atislar[i])
    deger.append(altıncı_atislar[i])
    atılan=max(deger)
    onceki=liste_atis[i-1]
    if atılan > onceki:
        liste_atis[i-1]=atılan

atletleri_sirala(isim_liste, liste_atis)
print(liste_atis)
print(f"Altın madalyayı kazanan : {isim_liste[0]} mesafesi : {liste_atis[0]}")
print(f"Gümüş madalyayı kazanan : {isim_liste[1]} mesafesi : {liste_atis[1]}")
print(f"Gümüş madalyayı kazanan : {isim_liste[2]} mesafesi : {liste_atis[2]}")
