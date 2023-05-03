class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("__init fonksiyonu__")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi
        self.tür=tür

    def __str__(self):
        return("İsim: {}\nYazar: {}\nSayfa Sayisi: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür))
    
    def __len__(self):
        return self.sayfa_sayisi
    
    def __del__(self):
        print("Kitap objesi siliniyor...")
        


kitap1=Kitap("Varolmanin Dayanilmaz Hafifligi","Milan Kundera",330,"Felsefik")
print(kitap1)
print(len(kitap1))
del kitap1
