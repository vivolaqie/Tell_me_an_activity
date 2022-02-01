import random

Aktiviteler = ["Bisiklete binmek","Yüzmek","Yürüyüş Yapmak","Kitap Okumak","Bilgisayar Oynamak","Film İzlemek","Enstrünman Çalmak"]

print("Aktivite Pro Bu program canınız sıkıldığında veya ne yapacağınız konusunda kararsız kaldığınız zamanlarda seçtiğiniz aktiviteler içerisinden sizin için herhangi birini seçmek için vardır. Programın içinde varsayılan olarak sizin için hazırlanan aktivitiler bulunur. İstediğiniz durumda ekleyiniz  ")

print(Aktiviteler)

print(""""
      
      1: Aktivite dahil et.
      
      2: Yeni aktivite listesi oluştur.
    
      3: Benim için bir aktivite söyle.
      
      4: Çık
     
     
      """)


while True:
    secenek = input("Lütfen yönergelerden birini seçiniz:")
    if secenek == '1':
        aktivite = input("Dahil Etmek İstediğiniz Aktiviteyi Giriniz:")
        Aktiviteler.append(aktivite)
        print("Yeni Aktiviteler:",Aktiviteler)
    elif secenek == '2':
        print("Yeni Aktiviteleri Ekleyiniz. Tamamladıktan Soran Bitir Yazınız")
        while True:
            yeni_aktivite = input("Yeni Aktivite Giriniz:")
            olusturulan_aktiviteler = []
            yeni_aktivite.append(olusturulan_aktiviteler)
            
            if yeni_aktivite == "Bitir":
                break
    elif secenek == '3': 
        secilen_liste = str(input(""" Yeniden oluşturduğunuz listeden mi varsayılan listeden mi aktivite görmek istersiniz
        'Eski Liste' veya 'Yeni Liste' olarak cevaplandırın.                     
                              """))
        if secilen_liste == 'Eski Liste' or 'eski liste':
            a =random.choice(Aktiviteler)
            print(a)
        elif secilen_liste == 'Yeni Liste' or 'yeni liste':
            b =random.choice(olusturulan_aktiviteler)
            print(b)
    elif not secenek == '1'or'2'or'3'or'4':
        print("Lütfen geçerli bir değer girin.")
    elif secenek == '4':
        break
        
            






    
    