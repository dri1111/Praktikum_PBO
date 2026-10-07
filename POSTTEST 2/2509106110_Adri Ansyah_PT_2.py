class Admin:
    nama_sistem = "Sistem Scrim Mobile Legends"
    total_admin = 0
    status = "Aktif"

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        Admin.total_admin += 1

    def login(self, username, password):
        return self.username == username and self.__password == password

    def tampilkan_data(self):
        print("Admin:", self.username)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == "":
            print("Password tidak boleh kosong")
        else:
            self.__password = password

    @classmethod
    def jumlah_admin(cls):
        print("Total admin:", cls.total_admin)

    @staticmethod
    def cek_username(username):
        return username != ""


class Pemain:
    nama_game = "Mobile Legends"
    total_pemain = 0
    status = "Aktif"

    def __init__(self, nama, id_pemain, role):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.__umur = 18
        Pemain.total_pemain += 1

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("ID:", self.id_pemain)
        print("Role:", self.role)
        print("Umur:", self.__umur)

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, umur):
        if umur < 13:
            print("Umur minimal 13 tahun")
        else:
            self.__umur = umur

    @classmethod
    def jumlah_pemain(cls):
        print("Total pemain:", cls.total_pemain)

    @staticmethod
    def cek_id(id_pemain):
        return id_pemain.isdigit()


class Tim:
    nama_game = "Mobile Legends"
    total_tim = 0
    maksimal_pemain = 5

    def __init__(self, nama_tim, kapten):
        self.nama_tim = nama_tim
        self.kapten = kapten
        self._pemain = []
        Tim.total_tim += 1

    def tambah_pemain(self, pemain):
        if len(self._pemain) < 5:
            self._pemain.append(pemain)
        else:
            print("Tim sudah memiliki 5 pemain")

    def tampilkan_data(self):
        print("Nama Tim:", self.nama_tim)
        print("Kapten:", self.kapten)

        for pemain in self._pemain:
            print("-", pemain.nama, "|", pemain.role)

    @property
    def jumlah_pemain(self):
        return len(self._pemain)

    @classmethod
    def jumlah_tim(cls):
        print("Total tim:", cls.total_tim)

    @staticmethod
    def cek_nama(nama):
        return nama != ""


class DetailPertandingan:
    def __init__(self, lokasi, tanggal):
        self.lokasi = lokasi
        self.tanggal = tanggal

    def tampilkan_detail(self):
        print("Lokasi:", self.lokasi)
        print("Tanggal:", self.tanggal)


class Pertandingan:
    nama_game = "Mobile Legends"
    total_pertandingan = 0

    def __init__(self, id_pertandingan, tim1, tim2, lokasi, tanggal):
        self.id_pertandingan = id_pertandingan
        self.tim1 = tim1
        self.tim2 = tim2
        self._status = "Terjadwal"
        self.__hasil = "Belum ada hasil"
        self.detail = DetailPertandingan(lokasi, tanggal)
        Pertandingan.total_pertandingan += 1

    def tampilkan_info(self):
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Status:", self._status)
        print("Hasil:", self.__hasil)
        self.detail.tampilkan_detail()

    def ubah_hasil(self, hasil):
        if hasil == "":
            print("Hasil tidak boleh kosong")
        else:
            self.__hasil = hasil
            self._status = "Selesai"

    @property
    def hasil(self):
        return self.__hasil

    @classmethod
    def jumlah_pertandingan(cls):
        print("Total pertandingan:", cls.total_pertandingan)

    @staticmethod
    def cek_id(id_pertandingan):
        return id_pertandingan != ""


class ScrimKompe(Pertandingan):
    jenis = "Scrim Kompe"

    def __init__(
        self,
        id_pertandingan,
        tim1,
        tim2,
        lokasi,
        tanggal,
        format_game
    ):
        super().__init__(
            id_pertandingan,
            tim1,
            tim2,
            lokasi,
            tanggal
        )
        self.format_game = format_game

    def tampilkan_info(self):
        print("\n=== SCRIM KOMPE ===")
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Format:", self.format_game)
        print("Status:", self._status)
        print("Hasil:", self.hasil)
        self.detail.tampilkan_detail()


class ScrimAnomali(Pertandingan):
    jenis = "Scrim Anomali"

    def __init__(
        self,
        id_pertandingan,
        tim1,
        tim2,
        lokasi,
        tanggal,
        aturan_khusus
    ):
        super().__init__(
            id_pertandingan,
            tim1,
            tim2,
            lokasi,
            tanggal
        )
        self.aturan_khusus = aturan_khusus

    def tampilkan_info(self):
        print("\n=== SCRIM ANOMALI ===")
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Aturan:", self.aturan_khusus)
        print("Status:", self._status)
        print("Hasil:", self.hasil)
        self.detail.tampilkan_detail()


admin1 = Admin("adri", "110")
admin2 = Admin("rina", "126")

print("=" * 40)
print("SISTEM SCRIM MOBILE LEGENDS")
print("=" * 40)

while True:
    username = input("Username: ")
    password = input("Password: ")

    if admin1.login(username, password):
        admin = admin1
        break
    elif admin2.login(username, password):
        admin = admin2
        break
    else:
        print("Username atau password salah")

print("\nLogin berhasil")
admin.tampilkan_data()

print("\n=== DATA TIM 1 ===")
nama_tim1 = input("Nama Tim: ")
kapten1 = input("Nama Kapten: ")

if not Tim.cek_nama(nama_tim1) or kapten1 == "":
    print("Data tim tidak boleh kosong")
else:
    tim1 = Tim(nama_tim1, kapten1)

print("\n=== DATA TIM 2 ===")
nama_tim2 = input("Nama Tim: ")
kapten2 = input("Nama Kapten: ")

if not Tim.cek_nama(nama_tim2) or kapten2 == "":
    print("Data tim tidak boleh kosong")
else:
    tim2 = Tim(nama_tim2, kapten2)


print("\n=== DATA PEMAIN TIM 1 ===")

nama = input("Nama pemain: ")
id_pemain = input("ID pemain: ")
role = input("Role: ")

if Pemain.cek_id(id_pemain) and nama != "" and role != "":
    pemain1 = Pemain(nama, id_pemain, role)

    umur = input("Umur: ")

    if umur.isdigit():
        pemain1.umur = int(umur)
        tim1.tambah_pemain(pemain1)
    else:
        print("Umur harus berupa angka")
else:
    print("Data pemain tidak valid")


print("\n=== DATA PEMAIN TIM 2 ===")

nama = input("Nama pemain: ")
id_pemain = input("ID pemain: ")
role = input("Role: ")

if Pemain.cek_id(id_pemain) and nama != "" and role != "":
    pemain2 = Pemain(nama, id_pemain, role)

    umur = input("Umur: ")

    if umur.isdigit():
        pemain2.umur = int(umur)
        tim2.tambah_pemain(pemain2)
    else:
        print("Umur harus berupa angka")
else:
    print("Data pemain tidak valid")


print("\n=== DATA TIM ===")

tim1.tampilkan_data()
print()
tim2.tampilkan_data()


print("\n=== PILIH JENIS SCRIM ===")
print("1. Scrim Kompe")
print("2. Scrim Anomali")

jenis = input("Pilih: ")

lokasi = input("Lokasi: ")
tanggal = input("Tanggal: ")

if jenis == "1":
    format_game = input("Format pertandingan: ")

    pertandingan = ScrimKompe(
        "P001",
        tim1,
        tim2,
        lokasi,
        tanggal,
        format_game
    )

elif jenis == "2":
    aturan = input("Aturan khusus: ")

    pertandingan = ScrimAnomali(
        "P001",
        tim1,
        tim2,
        lokasi,
        tanggal,
        aturan
    )

else:
    print("Jenis scrim tidak tersedia")
    pertandingan = None


if pertandingan is not None:

    admin.kelola_pertandingan(pertandingan) \
        if hasattr(admin, "kelola_pertandingan") else None

    print("\n=== DATA PERTANDINGAN ===")
    pertandingan.tampilkan_info()

    print("\n=== HASIL PERTANDINGAN ===")
    hasil = input("Masukkan hasil: ")

    pertandingan.ubah_hasil(hasil)

    print("\n=== DATA SETELAH PERTANDINGAN ===")
    pertandingan.tampilkan_info()

    print("\n=== DATA JUMLAH ===")
    Admin.jumlah_admin()
    Pemain.jumlah_pemain()
    Tim.jumlah_tim()
    Pertandingan.jumlah_pertandingan()