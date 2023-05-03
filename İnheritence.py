class Calisan():
    def __init__(self,ad,soyad,maas,departman):
        print("Calisan init fonksiyonu::::")
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

    
    def bilgileri_goster(self):
        print("Çalisan sinifinin bilgileri ..........")
        print("Adi = {}\nSoyadi = {}\nMaasi = {}\nDepartmani = {}".format(self.ad,self.soyad,self.maas,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman

class Yonetici(Calisan):

    def __init__(self, ad, soyad, maas, departman,kisi_sayisi):
        print("yonetici init fonksiyonu::::")
        super().__init__(ad,soyad,maas,departman)
        self.kisi_Sayisi=kisi_sayisi
    
    def bilgileri_goster(self):
        print("Yonetici sinifinin bilgileri ..........")
        super().bilgileri_goster()
        print("Sorumlu oldugu kisi sayisi = ",self.kisi_Sayisi)


    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari




mudur=Yonetici("Ali","Kara",15000,"HR",10)
mudur.bilgileri_goster()





