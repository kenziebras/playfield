Nama : Kenzie Nibras Tradezqi

NPM : 2406414776

Kelas : PBP D

Hobi : Tidur

Jurusan : Sistem Informasi

1. pertama Perlu membuat repository baru pada GitHub dengan nama folder repo yang dibebaskan. Lalu, buat repo lokal dengan nama yang sama dan masuk ke repo tersebut. Setelah itu, mengaktifkan virtual environment pada repo tersebut. Menyiapkan dependencies dan membuat proyek Django, melakukan konfigurasi environment variabel dan proyek, mengunggah proyek ke Repositori GitHub. Membuat aplikasi Main pada proyek, mengimplementasikan template, implementasikan Models, membuat dan mengaplikasikan migrasi model. Setelah melakukan itu semua, menghubungkan View dengan Template. mengonfigurasi routing URL pada Aplikasi Main. Lalu push semua kode tersebut ke dalam repository. dan yang terakhir menghubungkan repo github dan melakukan deployment melalui PWS.

2. https://www.canva.com/design/DAGygA4Da5M/Ts9pm4GIVXjM1a5I8m-i3w/edit?utm_content=DAGygA4Da5M&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Penjelasan : Secara ringkas, alur MVT pada Django dimulai saat pengguna meminta sebuah URL. Django, melalui urls.py, akan memetakan URL tersebut ke fungsi spesifik di views.py. Fungsi View ini kemudian bertindak sebagai jembatan yang memproses logika , dan jika dibutuhkan, ia akan mengambil atau mengolah data dari models.py (yang terhubung ke database). Terakhir, View akan menyajikan data tersebut menggunakan berkas Template (HTML) untuk menciptakan halaman web utuh yang dikirim kembali sebagai respons ke browser pengguna. 

3. berkas settings.py itu ibarat "otak" dari seluruh proyek Django. Semua konfigurasi dan pengaturan penting proyek web terletak pada berkas ini. Jadi, intinya, settings.py adalah berkas yang menyatukan semua bagian—aplikasi, database, keamanan, dan lainnya agar dapat bekerja sama sebagai satu kesatuan proyek web yang utuh.

4. database dapat dianggap sebagai sebuah rumah dan akan direnovasi. Proses migrasi di Django ada dua langkah. Pertama, menjalankan perintah makemigrations. Django bertugas untuk mengecek model rumahmu, dan menciptakan  blueprint atau "catatan renovasi" kebutuhan dari renovasi. Kedua, menjalankan migrate. ini memanggil Django lagi untuk mengerjakan renovasinya sesuai blueprint yang udah dibuat tadi, misalnya nambahin kamar baru (tabel) atau masang jendela (kolom) di rumahmu. Jadi, makemigrations itu bikin blueprintnya, migrate yang eksekusi rencananya.

5. Django adalah framework permulaan yang menyediakan keseimbangan ideal antar kesederhanaan, struktur yang jelas, dan kelengkapan fitur yang cocok untuk pembelajaran pengembangan perangkat lunak. Hal ini dapat membantu pemula memahami fokus pada konsep inti pengembangan web tanpa kesulitan konfigurasi.