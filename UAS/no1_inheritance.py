class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
        
    def jalan(self):
        print(f"Mobil {self.merk} ({self.tahun}) sedang berjalan.")
        
class MobilSport(Mobil):
    def __init__(self, merk, tahun, jenis):
        super().__init__(merk, tahun)
        self.jenis = jenis
        
    def jalan(self):
        print(f"Mobil sport {self.merk} ({self.tahun}) jenis {self.jenis} sedang berjalan.")
        
mobil1 = Mobil("Toyota", 2020)
mobil1.jalan()
# Output: Mobil Toyota (2020) sedang berjalan.

mobil2 = MobilSport("Porsche", 2022, "Coupe")
mobil2.jalan()
# Output: Mobil sport Porsche (2022) jenis Coupe sedang berjalan.
