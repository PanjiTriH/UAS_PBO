class Mobil:
    def __init__(self, merk, tahun):
        self._merk = merk
        self._tahun = tahun
        
    def jalan(self):
        print(f"Mobil {self._merk} ({self._tahun}) sedang berjalan.")
        
    def get_merk(self):
        return self._merk
        
    def set_merk(self, merk):
        self._merk = merk

mobil = Mobil("Toyota", 2020)
print(mobil.get_merk()) # Output: Toyota
mobil.set_merk("Honda")
print(mobil.get_merk()) # Output: Honda
