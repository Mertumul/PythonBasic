class Araba():
    def __init__(self,model,renk,beygir_gücü,silindir,fiyat):
        print("İnit fonksiyonu çagrildi")
        self.model= model
        self.renk= renk
        self.beygir_gücü= beygir_gücü
        self.silindir= silindir
        self.fiyat=fiyat
    
    def bilgilerigoster(self):
        print("Arabannizin özellikleri\nModeli={}\nRenk={}\nBeygir Gücü={}\nSilindiri={}\nFiyati={}TL".format(self.model,self.renk,self.beygir_gücü,self.silindir,self.fiyat))
    
    def zam_yap(self,zam):
        print("Zam yapiliyor..")
        self.fiyat+=zam
        


araba1 = Araba("Ford Focus","Siyah",110,4,200000)
araba1.bilgilerigoster()
araba1.zam_yap(50000)
araba1.bilgilerigoster()

