from abc import ABC, abstractmethod


class Admin:
    nama_sistem = "Sistem Scrim Mobile Legends"
    total_admin = 0

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        Admin.total_admin += 1

    def login(self, username, password):
        return self.username == username and self.__password == password

    def tampilkan_data(self):
        print("Admin:", self.username)

    def kelola_pertandingan(self, pertandingan):
        print(f"Admin {self.username} mengelola pertandingan {pertandingan.id_pertandingan}")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password:
            self.__password = password
        else:
            print("Password tidak boleh kosong")

    @classmethod
    def jumlah_admin(cls):
        print("Total admin:", cls.total_admin)

    @staticmethod
    def cek_username(username):
        return username.strip() != ""


class Pemain:
    nama_game = "Mobile Legends"
    total_pemain = 0

    def __init__(self, nama, id_pemain, role, umur=18):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.__umur = 18
        self.umur = umur
        Pemain.total_pemain += 1

    def tampilkan_data(self):
        print(f"{self.nama} | ID: {self.id_pemain} | Role: {self.role} | Umur: {self.__umur}")

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, umur):
        if umur < 13:
            print("Umur minimal 13 tahun; umur disetel ke 13.")
            self.__umur = 13
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
        if len(self._pemain) < self.maksimal_pemain:
            self._pemain.append(pemain)
            print(f"{pemain.nama} ditambahkan ke {self.nama_tim}.")
        else:
            print("Tim sudah memiliki 5 pemain.")

    def tampilkan_data(self):
        print(f"Tim: {self.nama_tim} | Kapten: {self.kapten}")
        if not self._pemain:
            print("  Belum ada pemain.")
        for pemain in self._pemain:
            print(f"  - {pemain.nama} | {pemain.role} | Umur {pemain.umur}")

    @property
    def jumlah_pemain(self):
        return len(self._pemain)

    def __len__(self):
        return len(self._pemain)

    def __str__(self):
        return f"{self.nama_tim} ({len(self)} pemain)"

    @classmethod
    def jumlah_tim(cls):
        print("Total tim:", cls.total_tim)

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""


class DetailPertandingan:
    def __init__(self, lokasi, tanggal):
        self.lokasi = lokasi
        self.tanggal = tanggal

    def tampilkan_detail(self):
        print("Lokasi:", self.lokasi)
        print("Tanggal:", self.tanggal)


class Pertandingan(ABC):
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

    @abstractmethod
    def validasi_pertandingan(self):
        pass

    @abstractmethod
    def proses_pertandingan(self, hasil):
        pass

    def jalankan(self, hasil):
        """Method konkret yang dipakai bersama oleh seluruh subclass."""
        if not self.validasi_pertandingan():
            print("Pertandingan tidak dapat diproses: data tim belum lengkap.")
            return
        self.proses_pertandingan(hasil)
        print("Proses pertandingan selesai.")

    def tampilkan_info(self):
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Status:", self._status)
        print("Hasil:", self.__hasil)
        self.detail.tampilkan_detail()

    def ubah_hasil(self, hasil):
        if hasil.strip() == "":
            print("Hasil tidak boleh kosong.")
            return False
        self.__hasil = hasil
        self._status = "Selesai"
        return True

    @property
    def hasil(self):
        return self.__hasil

    @classmethod
    def jumlah_pertandingan(cls):
        print("Total pertandingan:", cls.total_pertandingan)

    @staticmethod
    def cek_id(id_pertandingan):
        return id_pertandingan.strip() != ""


class ScrimKompe(Pertandingan):
    jenis = "Scrim Kompe"

    def __init__(self, id_pertandingan, tim1, tim2, lokasi, tanggal, format_game):
        super().__init__(id_pertandingan, tim1, tim2, lokasi, tanggal)
        self.format_game = format_game

    def validasi_pertandingan(self):
        return self.tim1.nama_tim.strip() != "" and self.tim2.nama_tim.strip() != ""

    def proses_pertandingan(self, hasil):
        if self.ubah_hasil(hasil):
            print(f"Hasil Scrim Kompe dicatat dengan format {self.format_game}.")

    def tampilkan_info(self):
        print("\n=== SCRIM KOMPETITIF ===")
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Format:", self.format_game)
        print("Status:", self._status)
        print("Hasil:", self.hasil)
        self.detail.tampilkan_detail()


class ScrimAnomali(Pertandingan):
    jenis = "Scrim Anomali"

    def __init__(self, id_pertandingan, tim1, tim2, lokasi, tanggal, aturan_khusus):
        super().__init__(id_pertandingan, tim1, tim2, lokasi, tanggal)
        self.aturan_khusus = aturan_khusus

    def validasi_pertandingan(self):
        return self.tim1.nama_tim.strip() != "" and self.tim2.nama_tim.strip() != ""

    def proses_pertandingan(self, hasil):
        if self.ubah_hasil(hasil):
            print(f"Hasil Scrim Anomali dicatat. Aturan khusus: {self.aturan_khusus}.")

    def tampilkan_info(self):
        print("\n=== SCRIM ANOMALI ===")
        print("ID:", self.id_pertandingan)
        print("Tim 1:", self.tim1.nama_tim)
        print("Tim 2:", self.tim2.nama_tim)
        print("Aturan:", self.aturan_khusus)
        print("Status:", self._status)
        print("Hasil:", self.hasil)
        self.detail.tampilkan_detail()



class Notifikasi:
    def catat(self, pesan):
        print("[NOTIFIKASI]", pesan)


class LogAktivitas:
    def catat(self, pesan):
        print("[LOG AKTIVITAS]", pesan)


def kirim_pesan(komponen, pesan):
    """Duck typing: menerima objek apa pun yang memiliki method catat()."""
    komponen.catat(pesan)


def input_wajib(label):
    while True:
        nilai = input(label).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def buat_tim(nomor):
    print(f"\n=== DATA TIM {nomor} ===")
    nama_tim = input_wajib("Nama Tim: ")
    kapten = input_wajib("Nama Kapten: ")
    return Tim(nama_tim, kapten)


def buat_pemain(tim, nomor):
    print(f"\n=== DATA PEMAIN TIM {nomor} ===")
    nama = input_wajib("Nama pemain: ")
    while True:
        id_pemain = input_wajib("ID pemain (angka): ")
        if Pemain.cek_id(id_pemain):
            break
        print("ID pemain harus berupa angka.")
    role = input_wajib("Role: ")
    while True:
        umur_teks = input_wajib("Umur: ")
        if umur_teks.isdigit():
            break
        print("Umur harus berupa angka.")
    pemain = Pemain(nama, id_pemain, role, int(umur_teks))
    tim.tambah_pemain(pemain)


def demonstrasi_abstraksi():
    print("\n=== BUKTI ABSTRACT CLASS ===")
    try:
        Pertandingan("X", None, None, "Lokasi", "Tanggal")
    except TypeError as error:
        print("Pertandingan tidak bisa dibuat langsung karena bersifat abstract.")
        print("Bukti:", error)


def main():
    admin1 = Admin("adri", "110")
    admin2 = Admin("rina", "126")

    print("=" * 45)
    print("SISTEM SCRIM MOBILE LEGENDS")
    print("=" * 45)

    while True:
        username = input_wajib("Username: ")
        password = input_wajib("Password: ")
        if admin1.login(username, password):
            admin = admin1
            break
        if admin2.login(username, password):
            admin = admin2
            break
        print("Username atau password salah. Coba lagi.")

    print("\nLogin berhasil.")
    admin.tampilkan_data()

    tim1 = buat_tim(1)
    tim2 = buat_tim(2)
    buat_pemain(tim1, 1)
    buat_pemain(tim2, 2)

    print("\n=== DATA TIM ===")
    tim1.tampilkan_data()
    print(tim1)  
    tim2.tampilkan_data()
    print(tim2)

    print("\n=== PILIH JENIS SCRIM ===")
    print("1. Scrim Kompetitif")
    print("2. Scrim Anomali")
    while True:
        jenis = input_wajib("Pilih (1/2): ")
        if jenis in ("1", "2"):
            break
        print("Pilihan hanya 1 atau 2.")

    lokasi = input_wajib("Lokasi: ")
    tanggal = input_wajib("Tanggal: ")
    if jenis == "1":
        format_game = input_wajib("Format pertandingan: ")
        pertandingan = ScrimKompe("P001", tim1, tim2, lokasi, tanggal, format_game)
    else:
        aturan = input_wajib("Aturan khusus: ")
        pertandingan = ScrimAnomali("P002", tim1, tim2, lokasi, tanggal, aturan)

    admin.kelola_pertandingan(pertandingan)

    print("\n=== POLIMORFISME VIA PEWARISAN ===")
    daftar_pertandingan = [
        pertandingan,
        ScrimKompe("P003", tim1, tim2, lokasi, tanggal, "Best of 3"),
        ScrimAnomali("P004", tim1, tim2, lokasi, tanggal, "Tanpa jungler")
    ]
    for item in daftar_pertandingan:
        item.tampilkan_info()  

    print("\n=== JALANKAN PERTANDINGAN ===")
    hasil = input_wajib("Masukkan hasil pertandingan (contoh: Tim A menang 2-1): ")
    pertandingan.jalankan(hasil)

    print("\n=== DUCK TYPING ===")
    pesan = f"Data pertandingan {pertandingan.id_pertandingan} telah diperbarui."
    kirim_pesan(Notifikasi(), pesan)
    kirim_pesan(LogAktivitas(), pesan)

    demonstrasi_abstraksi()

    print("\n=== DATA AKHIR PERTANDINGAN ===")
    pertandingan.tampilkan_info()

    print("\n=== DATA JUMLAH ===")
    Admin.jumlah_admin()
    Pemain.jumlah_pemain()
    Tim.jumlah_tim()
    Pertandingan.jumlah_pertandingan()


if __name__ == "__main__":
    main()
