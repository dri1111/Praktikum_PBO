class Pemain:
    nama_game = "ML"
    total_pemain = 0
    status = "Aktif"

    def __init__(self, nama, id_pemain, role):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.__umur = 18
        Pemain.total_pemain += 1

    def tampilkan_data(self):
        print(self.nama, self.id_pemain, self.role, self.__umur)

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, nilai):
        if nilai < 13:
            print("Umur tidak valid")
        else:
            self.__umur = nilai

    @classmethod
    def jumlah_pemain(cls):
        print("Total pemain:", cls.total_pemain)

    @staticmethod
    def validasi_id(id_pemain):
        return id_pemain.isdigit()


class Tim:
    nama_game = "ML"
    total_tim = 0
    maksimal_anggota = 5

    def __init__(self, nama_tim, kapten, asal):
        self.nama_tim = nama_tim
        self.kapten = kapten
        self.asal = asal
        self.__jumlah_anggota = 0
        Tim.total_tim += 1

    def tampilkan_data(self):
        print(self.nama_tim, self.kapten, self.asal, self.__jumlah_anggota)

    @property
    def jumlah_anggota(self):
        return self.__jumlah_anggota

    @jumlah_anggota.setter
    def jumlah_anggota(self, jumlah):
        if jumlah < 0 or jumlah > 5:
            print("Jumlah anggota tidak valid")
        else:
            self.__jumlah_anggota = jumlah

    @classmethod
    def jumlah_tim(cls):
        print("Total tim:", cls.total_tim)

    @staticmethod
    def validasi_nama(nama):
        return len(nama) >= 3


class Pertandingan:
    nama_game = "ML"
    total_pertandingan = 0
    status = "Belum Dimulai"

    def __init__(self, id_pertandingan, tim1, tim2, tanggal):
        self.id_pertandingan = id_pertandingan
        self.tim1 = tim1
        self.tim2 = tim2
        self.tanggal = tanggal
        self.__hasil = "Belum Ada Hasil"
        Pertandingan.total_pertandingan += 1

    def tampilkan_data(self):
        print(self.id_pertandingan, self.tim1.nama_tim,
              "vs", self.tim2.nama_tim, self.tanggal, self.__hasil)

    @property
    def hasil(self):
        return self.__hasil

    @hasil.setter
    def hasil(self, nilai):
        if nilai == "":
            print("Hasil tidak boleh kosong")
        else:
            self.__hasil = nilai

    @classmethod
    def jumlah_pertandingan(cls):
        print("Total pertandingan:", cls.total_pertandingan)

    @staticmethod
    def validasi_id(id_pertandingan):
        return len(id_pertandingan) > 0


class ScrimKompe(Pertandingan):
    jenis = "Scrim Kompe"

    def tampilkan_aturan(self):
        print("Scrim Kompe: pertandingan kompetitif dan serius")


class ScrimAnomali(Pertandingan):
    jenis = "Scrim Anomali"

    def tampilkan_aturan(self):
        print("Scrim Anomali: pertandingan dengan aturan khusus")


class Admin:
    nama_sistem = "Sistem Scrim ML"
    total_admin = 0
    status = "Aktif"

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        Admin.total_admin += 1

    def tampilkan_data(self):
        print("Username:", self.username)
        print("Password: ******")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nilai):
        if len(nilai) < 3:
            print("Password tidak valid")
        else:
            self.__password = nilai

    @classmethod
    def jumlah_admin(cls):
        print("Total admin:", cls.total_admin)

    @staticmethod
    def validasi_username(username):
        return len(username) >= 4


pemain1 = Pemain("Dan", "1", "Jungler")
pemain2 = Pemain("Cad", "2", "Gold Lane")

tim1 = Tim("ONIC", "Kay", "Samarinda")
tim2 = Tim("RRQ", "Zenn", "Samarinda")

tim1.jumlah_anggota = 5
tim2.jumlah_anggota = 5

pertandingan1 = Pertandingan("P1", tim1, tim2, "23-09-2026")
pertandingan2 = Pertandingan("P2", tim2, tim1, "24-09-2026")

kompe1 = ScrimKompe("K1", tim1, tim2, "25-09-2026")
kompe2 = ScrimKompe("K2", tim2, tim1, "26-09-2026")

anomali1 = ScrimAnomali("A1", tim1, tim2, "27-09-2026")
anomali2 = ScrimAnomali("A2", tim2, tim1, "28-09-2026")

admin1 = Admin("adri", "110")
admin2 = Admin("sabrina", "126")

pemain1.umur = 20
pemain1.tampilkan_data()
pemain2.tampilkan_data()

tim1.tampilkan_data()
tim2.tampilkan_data()

pertandingan1.hasil = "RRQ menang 2-1"
pertandingan1.tampilkan_data()
pertandingan2.tampilkan_data()

kompe1.tampilkan_aturan()
anomali1.tampilkan_aturan()

admin1.tampilkan_data()
admin2.tampilkan_data()

Pemain.jumlah_pemain()
Tim.jumlah_tim()
Pertandingan.jumlah_pertandingan()
Admin.jumlah_admin()

print(Pemain.validasi_id("1001"))
print(Tim.validasi_nama("RRQ"))
print(Admin.validasi_username("adri"))

pemain1.umur = 10
pertandingan1.hasil = ""
admin1.password = "1"