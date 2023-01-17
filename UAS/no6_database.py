# from sqlalchemy import create_engine

# # Membuat koneksi ke database
# engine = create_engine('sqlite:///mydb.db', echo=True)

from sqlalchemy import create_engine
from sqlalchemy.sql import select

# Membuat koneksi ke database
engine = create_engine('sqlite:///mydb.db', echo=True)

# Membuat objek koneksi
conn = engine.connect()

# Membuat perintah SELECT
stmt = select([testaja])

# Menjalankan perintah SELECT
result = conn.execute(stmt)

# Menampilkan hasil SELECT
for row in result:
    print(row)

# Menutup koneksi
conn.close()
