
# Sistem Scrim Mobile Legends

## Deskripsi Program

Sistem Scrim Mobile Legends merupakan program Python untuk mengelola admin, pemain, tim, dan pertandingan scrim. Program ini menerapkan konsep Object-Oriented Programming (OOP), enkapsulasi, inheritance, relasi UML, abstraksi, polimorfisme, duck typing, dan operator overloading.

# POSTTEST 1

## 1. Tema dan Class

Program menggunakan tema Sistem Scrim Mobile Legends dengan beberapa class utama:

- `Admin`: mengelola akun admin dan login.
- `Pemain`: menyimpan identitas dan role pemain.
- `Tim`: mengelola tim dan daftar pemain.
- `Pertandingan`: superclass untuk pertandingan.
- `ScrimKompe`: subclass pertandingan kompetitif.
- `ScrimAnomali`: subclass pertandingan dengan aturan khusus.
- `DetailPertandingan`: menyimpan lokasi dan tanggal pertandingan.
- `Notifikasi` dan `LogAktivitas`: mencatat informasi melalui duck typing.

## 2. Atribut

### Atribut kelas

Contoh atribut kelas yang digunakan:

- `Admin.nama_sistem`
- `Admin.total_admin`
- `Pemain.nama_game`
- `Pemain.total_pemain`
- `Tim.maksimal_pemain`
- `Pertandingan.total_pertandingan`

Atribut kelas digunakan bersama oleh objek dalam class yang sama.

### Atribut instance

Atribut instance dibuat menggunakan `__init__()` dan `self`, misalnya:

- `Admin.username`
- `Pemain.nama`
- `Pemain.id_pemain`
- `Tim.nama_tim`
- `Pertandingan.id_pertandingan`

### Hak akses atribut

- **Public:** `username`, `nama`, `role`, `nama_tim`.
- **Protected:** `_pemain` dan `_status`.
- **Private:** `__password`, `__umur`, dan `__hasil`.

Atribut private menggunakan name mangling Python untuk membatasi akses langsung dari luar class.

## 3. Jenis Method

### Instance method

Contoh:

- `Admin.login()`
- `Pemain.tampilkan_data()`
- `Tim.tambah_pemain()`
- `Pertandingan.tampilkan_info()`

Instance method digunakan untuk mengolah atau menampilkan data objek.

### Class method

Contoh:

- `Admin.jumlah_admin()`
- `Pemain.jumlah_pemain()`
- `Tim.jumlah_tim()`
- `Pertandingan.jumlah_pertandingan()`

Class method menggunakan decorator `@classmethod` dan parameter `cls`.

### Static method

Contoh:

- `Admin.cek_username()`
- `Pemain.cek_id()`
- `Tim.cek_nama()`
- `Pertandingan.cek_id()`

Static method menggunakan decorator `@staticmethod` untuk validasi tanpa parameter `self` atau `cls`.

## 4. Getter, Setter, dan Validasi

Program menggunakan `@property` sebagai getter dan `@nama_properti.setter` sebagai setter.

- `Admin.password`: menolak password kosong.
- `Pemain.umur`: memvalidasi umur minimal 13 tahun.
- `Pertandingan.hasil`: menyediakan akses untuk membaca hasil pertandingan.

Setter diuji dengan data valid dan tidak valid. Hasil pengujian dapat dilihat pada output program.

## 5. Pengujian Program

Program membuat beberapa objek, antara lain:

- Dua objek `Admin`.
- Dua objek `Tim`.
- Objek `Pemain` untuk setiap tim.
- Objek pertandingan dari subclass yang berbeda.

Program memperagakan instance method, class method, static method, getter, setter, dan validasi data.

# POSTTEST 2

## 1. Class Diagram UML

![Class Diagram Sistem Scrim Mobile Legends](class_diagram.png)

### Asosiasi

Relasi asosiasi terjadi antara `Pertandingan` dan `Tim`. Class `Pertandingan` menyimpan referensi objek tim melalui atribut `tim1` dan `tim2`, sedangkan objek tim dibuat secara terpisah.

### Agregasi

Relasi agregasi terjadi antara `Tim` dan `Pemain`. Class `Tim` menyimpan kumpulan objek pemain melalui atribut `_pemain`, tetapi objek pemain dapat dibuat secara terpisah dari tim.

### Komposisi

Relasi komposisi terjadi antara `Pertandingan` dan `DetailPertandingan`. Objek `DetailPertandingan` dibuat di dalam konstruktor `Pertandingan` dan menjadi bagian dari data pertandingan.

## 2. Inheritance

Program memiliki superclass `Pertandingan` dan dua subclass:

- `ScrimKompe`
- `ScrimAnomali`

Kedua subclass memanggil konstruktor superclass menggunakan `super().__init__(...)`.

Setiap subclass memiliki atribut unik:

- `ScrimKompe`: `format_game`.
- `ScrimAnomali`: `aturan_khusus`.

Kedua subclass juga melakukan method overriding pada `tampilkan_info()`, `validasi_pertandingan()`, dan `proses_pertandingan()`.

## 3. Abstraksi

Class `Pertandingan` merupakan abstract base class yang menggunakan `ABC`.

Abstract method yang digunakan:

- `validasi_pertandingan()`
- `proses_pertandingan()`

Kedua method wajib diimplementasikan oleh subclass konkret.

Method `jalankan()` merupakan method konkret yang digunakan bersama oleh subclass untuk memvalidasi dan menjalankan pertandingan.

Program juga mencoba membuat objek `Pertandingan` secara langsung menggunakan `try-except TypeError`. Proses tersebut gagal karena abstract method belum diimplementasikan.

## 4. Polimorfisme

### Polimorfisme melalui inheritance

Class `ScrimKompe` dan `ScrimAnomali` mengimplementasikan method `tampilkan_info()` dengan perilaku berbeda.

Keduanya dipanggil melalui satu loop yang berisi objek pertandingan berbeda.

### Duck typing

Class `Notifikasi` dan `LogAktivitas` tidak saling mewarisi, tetapi mempunyai method yang sama, yaitu `catat()`.

Keduanya dipanggil melalui fungsi `kirim_pesan()` tanpa memeriksa tipe objek.

### Operator overloading

Class `Tim` menerapkan:

- `__len__()` untuk menghitung jumlah pemain menggunakan `len(tim)`.
- `__str__()` untuk menampilkan informasi tim melalui `print(tim)`.

Program tidak membedakan perilaku polimorfik dengan pemeriksaan `type()` atau rantai `if/elif` berdasarkan jenis objek.

## 5. Prinsip SOLID

Program menerapkan konsep **Open/Closed Principle (OCP)**. Jenis pertandingan baru dapat ditambahkan dengan membuat subclass baru dari `Pertandingan` dan mengimplementasikan abstract method yang diwajibkan.

Dengan demikian, perilaku pertandingan dapat diperluas melalui class baru tanpa harus mengubah kontrak superclass.

# Screenshot Output Program

## 1. Login Berhasil

![Login berhasil](SS-Login.png)

## 2. Data Tim

![Data tim](SS-Data-Tim.png)

## 3. Data Pemain

![Data pemain](SS-Data-Pemain.png)

## 4. Pemilihan Jenis Scrim

![Pemilihan scrim](SS-pertandingan.png)

## 5. Detail Pertandingan dan Polimorfisme

![Detail pertandingan](SS-tim.png)

## 6. Proses Menjalankan Pertandingan

![Proses pertandingan](SS-Total-Pertandingan.png)

## 7. Hasil Akhir

![Hasil akhir](SS-penentu-pemenang.png)

## 8. Bukti Duck Typing

Sisipkan screenshot output yang menunjukkan:

- `[NOTIFIKASI]`
- `[LOG AKTIVITAS]`

![Bukti duck typing](SS-Duck-typing.png)

## 9. Bukti Abstract Class

Sisipkan screenshot output `TypeError` saat program mencoba menginstansiasi class `Pertandingan`.

![Bukti abstract class](SS-Abstrack.png)

## 10. Bukti Validasi Setter

Sisipkan screenshot pengujian setter dengan data valid dan tidak valid.

![Bukti validasi eror login](SS-Eror-Login.png,SS-Eror-ID.png,SS-Pilihan)
