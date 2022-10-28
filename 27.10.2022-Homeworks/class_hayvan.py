class Hayvan():
    def __init__(self,isim,tur,yas,kilo,boy,cinsiyet,beslenme):
       self.isim = isim
       self.tur=tur
       self.yas = yas
       self.kilo = kilo
       self.boy=boy
       self.cinsiyet=cinsiyet
       self.beslenme=beslenme

    def bilgileri_goster(self):
        print("Hayvan sınıfının bilgileri...")
        print("Hayvanın ismi: {}\nHayvanın türü: {}\nHayvanın yaşı: {}\nHayvanın kilosu: {}\nHayvanın boyu: {}\nHayvanın cinsiyeti: {}\nHayvanın beslenme şekli: {}\n".format(self.isim,self.tur,self.yas,self
.kilo,self.boy,self.cinsiyet,self.beslenme))

class Dinazor(Hayvan):
    def __init__(self,isim,tur,yas,kilo,boy,cinsiyet,beslenme,ozellik):
        super().__init__(isim,tur,yas,kilo,boy,cinsiyet,beslenme)
        self.ozellik=ozellik
Ceratosaurus = Dinazor("Dinazor","Ceratosaurus",100,1000,200,"Dişi","Etçil","Kuyruklu")
print(Ceratosaurus.bilgileri_goster())


Triceratops= Dinazor("Dinazor","Triceratops",120,700,250,"Erkek","Yarı Etçil","3 Boynuzlu")
print(Triceratops.bilgileri_goster())


class Orkinos(Hayvan):
     def __init__(self,isim,tur,yas,kilo,boy,cinsiyet,beslenme,hız):
        super().__init__(isim,tur,yas,kilo,boy,cinsiyet,beslenme)
        self.hız=hız
SarıKanatOrkinos=Orkinos("Orkinos","Sarı Kanat Orkinosu",40,300,250,"Dişi","Etçil","75km/h")
print(SarıKanatOrkinos.bilgileri_goster())


class Kartal(Hayvan):
      def __init__(self,isim,tur,yas,kilo,boy,cinsiyet,beslenme,renk):
        super().__init__(isim,tur,yas,kilo,boy,cinsiyet,beslenme)
        self.renk=renk
Harpy=Kartal("Kartal","Harpy",25,5,100,"Erkek","Etçil","Siyah-Beyaz")
print(Harpy.bilgileri_goster())


class Ceylanlar(Hayvan):
    def __init__(self,isim,tur,yas,kilo,boy,cinsiyet,beslenme,Familya):
        super().__init__(isim,tur,yas,kilo,boy,cinsiyet,beslenme)
        self.familya=Familya
GrantininCeylani=Ceylanlar("Ceylan","Grantinin Ceylanı",15,75,80,"Dişi","Otçul","Çift Boynuzlular")
print(GrantininCeylani.bilgileri_goster())


