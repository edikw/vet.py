print "Selamat datang di App VET version 1.0"
print
operasi = """1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian"""

print "Daftar Jenis Pengoperasian : "
print operasi

saklar = True


def kalkulator():

	input_operasi =raw_input("pilih jenis operasi : ")
	while input_operasi.isdigit() is False:
		print "hanya dengan angka"
	input_operasi = raw_input("pilih jenis operasi : ")
	if input_operasi > "4":
		print "pilihan hanya 1 sampai 4"
		input_operasi = raw_input("pilih jenis operasi : ")
	else: 
		print "anda bisa lanjut"

	angka1 = raw_input ("masukkan angka pertama :")
	while angka1.isdigit() is False:
		print "hanya dengan angka"
		angka1 = raw_input ("masukkan angka pertama :")

	angka2 = raw_input ("masukkan angka kedua :")
	while angka2.isdigit() is False:
		print "hanya dengan angka"
		angka2 = raw_input ("masukkan angka kedua :")

	def penjumlahan ():
		jumlah1 = int(angka1) + int(angka2)
		print jumlah1

	def pengurangan ():
		jumlah2 = int(angka1) - int(angka2)
		print jumlah2

	def perkalian ():
		jumlah3 = int(angka1) * int(angka2)
		print jumlah3

	def pembagian ():
		jumlah4 = int(angka1) / int(angka2)
		print jumlah4

	if input_operasi == "1" :
		penjumlahan()

	elif input_operasi == "2" :
		pengurangan()

	elif input_operasi == "3" :
		perkalian()

	elif input_operasi == "4" :
		pembagian()

	else :
		print "Pilihan Hanya 1 sampai 4"

#kalkulator()

def tanya ():
	tanya = raw_input ("apakah ingin menghitung kembali? Y/T : ")
	if tanya == "Y" or tanya == "y":
		return True

	elif tanya == "T" or tanya == "t":
		return False

	else:
		return False
	
while saklar :
	if saklar == True:
		kalkulator()
		saklar = tanya ()
	
	else:
		saklar = False
		print "Terimaksih Telah Menggunakan App ini"
