# boarding_tele
Script untuk boardcast telegram
instalasi module python 3.12

pkg update && pkg upgrade

pkg install git 

git clone https://github.com/RyotaXD/boarding_tele

cd boarding_tele

pip install -r requirements.txt

python boarding_tele.py


Langkah-langkah Mendapatkan API Keys
Login ke Portal My Telegram
1. Buka browser Anda dan akses laman resmi di https://my.telegram.org/auth.

2. Verifikasi Nomor Telepon

Masukkan nomor telepon akun Telegram Anda dalam format internasional (contoh: +62812xxxxxx).

Klik Next. Anda akan menerima kode verifikasi yang dikirimkan langsung melalui chat di aplikasi Telegram (bukan lewat SMS).

3. Salin kode tersebut, tempelkan di kolom "Confirmation code", lalu klik Sign In.

4. Pilih Menu API Development Tools
Setelah berhasil masuk, Anda akan melihat beberapa opsi. Klik pada tautan API development tools.

5. Isi Formulir Aplikasi
Jika ini pertama kalinya Anda mendaftar, Anda akan diminta mengisi formulir singkat:

App title: Nama aplikasi Anda (bebas, contoh: "Skrip Saya").

Short name: Nama pendek (bebas, hanya huruf dan angka).

URL: Bisa dikosongkan atau isi dengan alamat web apa saja.

Platform: Pilih platform yang sesuai (misalnya: Android, iOS, atau Desktop).

Description: Deskripsi singkat aplikasi Anda.

Salin API ID dan API Hash
Klik Create application. Setelah itu, sistem akan menampilkan detail aplikasi Anda. Di sana Anda akan melihat:

App api_id = 120299332

App api_hash = 'pelerkodok'


