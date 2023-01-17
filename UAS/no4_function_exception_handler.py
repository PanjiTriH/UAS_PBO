#####Contoh1#####
def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan 0.")
        hasil = None
    return hasil

hasil = bagi(10, 2)
print(hasil) # Output: 5.0

hasil = bagi(10, 0)
print(hasil) # Output: Tidak bisa membagi dengan 0. None



# #####Contoh2#####
# def cek_umur(umur):
#     if umur < 0:
#         raise ValueError("Umur tidak boleh kurang dari 0")
#     print("Umur yang dimasukkan valid")

# try:
#     cek_umur(-1)
# except ValueError as e:
#     print(e)

# # Output: Umur tidak boleh kurang dari 0



# #####Contoh3#####
# def konversi_ke_bilangan(input_str):
#     try:
#         bilangan = float(input_str)
#     except ValueError:
#         bilangan = None
#     return bilangan

# print(konversi_ke_bilangan("2")) # Output : 2.0
# print(konversi_ke_bilangan("dua")) # Output : None



# #####Contoh4#####
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number!")

