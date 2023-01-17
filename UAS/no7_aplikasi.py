import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('mydb.db')

# Membuat objek cursor
cursor = conn.cursor()

# Membuat tabel
cursor.execute("""CREATE TABLE testajaa (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    salary REAL)""")

# Menambahkan data ke tabel
cursor.execute("INSERT INTO testaja VALUES (1, 'namaorang', 10000)")
cursor.execute("INSERT INTO testaja VALUES (2, 'buahnaga', 12000)")
cursor.execute("INSERT INTO testaja VALUES (3, 'sayurbayam', 15000)")
cursor.execute("INSERT INTO testaja VALUES (4, 'kopi', 25000)")

# Menyimpan perubahan
conn.commit()

# Menampilkan data dari tabel
cursor.execute("SELECT * FROM testaja")

for row in cursor.fetchall():
    print(row)

# Menutup koneksi
conn.close()
