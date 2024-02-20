# Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlangsung selama 5 minggu.
# Gaji yang diberikan adalah gaji per jam.
# Total pajak yang harus budi bayarkan dari penghasilannya selama bekerja adalah 14%.
# Setelah membayar pajak, budi menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan
# digunakan pada semester baru, dan 1% untuk membeli alat tulis.
# Setelah membeli baju, aksesoris dan alat tulis, Budi menggunakan 25% dari sisa uangnya untuk disedekahkan.
# Setiap Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim,
# dan sisanya akan diserahkan ke kaum dhuafa.
# Buatlah sebuah program, dengan input:
# 1. Gaji per jam yang anda inginkan
# 2. Jumlah jam kerja yang akan dilakukan dalam 1 minggu
# Output dari program adalah sebagai berikut :
# 1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak.
# 2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak.
# 3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris.
# 4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis.
# 5. Jumlah uang yang akan Budi sedekahkan.
# 6. Jumlah uang yang akan diterima anak yatim.
# 7. Jumlah uang yang akan diterima kaum dhuafa.

print("You will work for 5 weeks")
salary = int(input("Your demanded salary/hour (in Rp): "))
workhour = int(input("Your weekly work hour: "))

avsal = 5 * (salary*workhour)
print(f"Pendapatan sebelum pajak: {avsal}")

tax = round(avsal * (14/100))
avsal -= tax
print(f"Pendapatan setelah pajak: Rp {avsal}")

clacc = round(avsal * (10/100))
ut = round(avsal * (1/100))
avsal -= clacc
avsal -= ut
print(f"Uang untuk pakaian dan aksesoris: Rp {clacc}")
print(f"Uang untuk alat tulis: Rp {ut}")

cty = round(avsal * (25/100))
oph = round(cty * (30/100))
dhf = cty - oph
print(f"Uang untuk sedekah: Rp {cty}")
print(f"Uang untuk anak yatim: Rp {oph}")
print(f"Uang untuk kaum dhaufa: Rp {dhf}")