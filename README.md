Tugas 2
1. pertama Perlu membuat repository baru pada GitHub dengan nama folder repo yang dibebaskan. Lalu, buat repo lokal dengan nama yang sama dan masuk ke repo tersebut. Setelah itu, mengaktifkan virtual environment pada repo tersebut. Menyiapkan dependencies dan membuat proyek Django, melakukan konfigurasi environment variabel dan proyek, mengunggah proyek ke Repositori GitHub. Membuat aplikasi Main pada proyek, mengimplementasikan template, implementasikan Models, membuat dan mengaplikasikan migrasi model. Setelah melakukan itu semua, menghubungkan View dengan Template. mengonfigurasi routing URL pada Aplikasi Main. Lalu push semua kode tersebut ke dalam repository. dan yang terakhir menghubungkan repo github dan melakukan deployment melalui PWS.

2. https://www.canva.com/design/DAGygA4Da5M/Ts9pm4GIVXjM1a5I8m-i3w/edit?utm_content=DAGygA4Da5M&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Penjelasan : Secara ringkas, alur MVT pada Django dimulai saat pengguna meminta sebuah URL. Django, melalui urls.py, akan memetakan URL tersebut ke fungsi spesifik di views.py. Fungsi View ini kemudian bertindak sebagai jembatan yang memproses logika , dan jika dibutuhkan, ia akan mengambil atau mengolah data dari models.py (yang terhubung ke database). Terakhir, View akan menyajikan data tersebut menggunakan berkas Template (HTML) untuk menciptakan halaman web utuh yang dikirim kembali sebagai respons ke browser pengguna. 

3. berkas settings.py itu ibarat "otak" dari seluruh proyek Django. Semua konfigurasi dan pengaturan penting proyek web terletak pada berkas ini. Jadi, intinya, settings.py adalah berkas yang menyatukan semua bagian—aplikasi, database, keamanan, dan lainnya agar dapat bekerja sama sebagai satu kesatuan proyek web yang utuh.

4. database dapat dianggap sebagai sebuah rumah dan akan direnovasi. Proses migrasi di Django ada dua langkah. Pertama, menjalankan perintah makemigrations. Django bertugas untuk mengecek model rumahmu, dan menciptakan  blueprint atau "catatan renovasi" kebutuhan dari renovasi. Kedua, menjalankan migrate. ini memanggil Django lagi untuk mengerjakan renovasinya sesuai blueprint yang udah dibuat tadi, misalnya nambahin kamar baru (tabel) atau masang jendela (kolom) di rumahmu. Jadi, makemigrations itu bikin blueprintnya, migrate yang eksekusi rencananya.

5. Django adalah framework permulaan yang menyediakan keseimbangan ideal antar kesederhanaan, struktur yang jelas, dan kelengkapan fitur yang cocok untuk pembelajaran pengembangan perangkat lunak. Hal ini dapat membantu pemula memahami fokus pada konsep inti pengembangan web tanpa kesulitan konfigurasi.

Tugas 3
1. Dalam sebuah platform, pengiriman data itu penting agar data bisa sampai ke tujuan dengan cepat, aman, dan konsisten. Kalau tidak ada mekanisme yang jelas untuk mengirim data, informasi yang sudah terkumpul jadi tidak efisien. Data delivery juga bikin arus informasi jadi lancar, agar dapat mengikuti kebutuhan kalau datanya makin banyak, dan tetap ngejaga keamanan serta aturan yang berlaku. Ujung-ujungnya, ini bikin pengalaman pengguna lebih enak karena mereka selalu dapet info yang relevan.

2. JSON lebih populer dibanding XML karena strukturnya lebih sederhana, ringkas, dan mudah diproses oleh mesin maupun manusia. Selain itu, JSON terintegrasi baik dengan bahasa pemrograman modern, khususnya JavaScript, sehingga lebih efisien. XML masih berguna untuk skema data yang kompleks, tapi karena lebih ribet, JSON lebih banyak dipakai di web dan aplikasi sekarang.

3. Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form sudah sesuai dengan aturan validasi yang berlaku. Saat dipanggil, method ini akan mengecek setiap field, memastikan format data benar, dan menjalankan validasi tambahan jika ada. Jika semua data valid, is_valid() akan mengembalikan nilai True; sebaliknya, jika ada kesalahan, ia akan mengembalikan False dan menyimpan pesan error pada form.errors. Method ini penting karena memastikan data yang diproses atau disimpan ke database sudah benar dan aman, sehingga aplikasi bisa berjalan dengan lebih andal.

4. csrf_token di Django berfungsi untuk mencegah serangan Cross-Site Request Forgery (CSRF), yaitu serangan ketika penyerang mengirimkan request palsu atas nama pengguna tanpa disadari. Dengan adanya token ini, setiap form yang dikirim harus membawa tanda unik yang sesuai dengan yang dibuat server, sehingga request bisa dipastikan benar-benar sah. Kalau kita tidak menambahkan csrf_token, aplikasi menjadi rentan. Penyerang bisa memanfaatkan celah ini dengan membuat form atau script tersembunyi yang otomatis mengirim request ke server menggunakan akun pengguna yang sedang login. Dampaknya bisa serius, mulai dari perubahan data, transaksi ilegal, hingga penghapusan informasi penting. Karena itu, csrf_token sangat penting untuk menjaga keamanan data dan melindungi pengguna dari manipulasi berbahaya.

5. Saya melakukan seperti yang di tutorial dengan memanipulasi atribut dari class yang ada di Models dan memanipulasi tampilan yang ada di main, product_view, dan create_product

Bukti Screenshot Postman --> https://drive.google.com/drive/folders/1eAc50-VmsGKUbWAA_vAdJoFYi9rV7tJO?usp=drive_link

Tugas4
1. AuthenticationForm adalah sebuah class bawaan dari Django yang dirancang untuk menangani proses autentikasi atau login pengguna. Formulir ini sudah terintegrasi dengan sistem bawaan pengguna Django. Kelebihan dari AuthenticationForm adalah keamanan terjamin, terintegrasi dengan Django, cepat dan mudah digunakan, dan validasi bawaan yang andal. Namun, Django juga memiliki kelemahan, yaitu kurang fleksibel untuk kustomisasi, Tampilan pesan kesalahan generik yang kurang ramah bagi pengguna, dan Ketergantungan pada django.contrib.auth

2. autentikasi adalah proses untuk membuktikan siapa Anda, sedangkan otorisasi adalah proses untuk menentukan apa yang boleh Anda lakukan. autentikasi seperti pengecekan kartu identitas yang memberikan akses masuk. sedangkan otorisasi seperti pengecekan akses mana saja yang dapat dilakukan oleh seseorang.
- Autentikasi itu dengan Django memastikan identitas pengguna melalui Model User yang menyediakan skema database username dan password yang di-hash. lalu, menempelkan objek pengguna atau request.user pada setiap request. otorisasi juga menyediakan form dan views siap pakai untuk login dan logout. Jadi, Django melakukan verifikasi identitas dan mengingat pengguna yang sudah login di seluruh situs.
- Otorisasi adalah sistem bawaan Django untuk mengontrol hak akses user melalui Flags dan Permissions pada setiap model. Serta melakukan Grouping terhadap akses grup dan decorator yang menyediakan batasan akses ke views. Jadi, Otorisasi Django menyediakan kerangka kerja berlapis untuk  memeriksa dan memberlakukan aturan hak akses bagi pengguna yang sudah terautentikasi.

3. Cookies menyimpan data di browser pengguna sehingga kelebihannya adalah cepat dan tidak memberatkan server, tapi tidak aman untuk data sensitif makanya yang biasanya dipake tuh buat info info yang ga sensitif. Sedangkan Session menyimpan data di server seperti akun akun facebook atau sosmed lainnya sehingga kelebihan dari session adalah sangat aman karena data pentingnya tidak keluar dari server, tapi membutuhkan memori di server.

4. Tidak, cookies tidak aman secara default, tapi Django membuatnya jadi aman. Cookies pada dasarnya rentan terhadap 3 risiko utama: Pencurian melalui JavaScript (serangan XSS),Pengintaian saat dikirim lewat koneksi tidak aman (HTTP), Pemalsuan Permintaan dari situs lain (serangan CSRF).Django secara default sudah melindungi Anda dengan cara: HttpOnly Flag, CSRF Token, Tanda Tangan Kriptografis, Mendukung HTTPS Django akan memastikan cookie hanya dikirim lewat koneksi aman. Jadi, Django sudah menyediakan perlindungan berlapis untuk keamanan yang ada pada cookies.

5. Dengan mengerjakan bertahap dengan tutorial dan melakukan penyesuaian atau modifikasi pada views, models, dan urls yang dibuat. sehingga dapat bekerja sesuai dengan rencana dan lepas dari error.

Tugas5
1. Jika ada beberapa CSS selector untuk satu elemen, prioritas ditentukan oleh spesifisitas: inline style punya prioritas tertinggi, lalu ID selector, kemudian class/atribut/pseudo-class, dan terakhir tag/elemen. Jika spesifisitas sama, aturan yang ditulis paling akhir yang dipakai.

2. Responsive design penting agar tampilan web menyesuaikan ukuran layar device, baik mobile maupun desktop. Misalnya, Instagram sudah menerapkan responsive design sehingga nyaman digunakan di HP maupun laptop, sedangkan website lama yang hanya didesain untuk desktop akan sulit digunakan di HP karena teks kecil dan layout berantakan.

3. Margin adalah jarak di luar elemen terhadap elemen lain, border adalah garis tepi elemen, sedangkan padding adalah ruang di dalam elemen antara konten dan bordernya. Misalnya: margin: 10px; border: 1px solid black; padding: 20px; akan memberi jarak luar 10px, garis tepi hitam, dan ruang dalam 20px.

4. Flexbox digunakan untuk mengatur elemen dalam satu dimensi (baris atau kolom) dengan fleksibel, cocok untuk alignment dan distribusi. Grid layout bekerja dua dimensi (baris dan kolom) sehingga lebih pas untuk layout kompleks seperti dashboard atau galeri.

5. Saya mulai dengan membuat struktur dasar navbar di HTML, lalu menambahkan style menggunakan Tailwind agar warnanya sesuai. Setelah itu, saya tambahkan menu desktop dan mobile dengan tombol hamburger. Lalu, saya buat event JavaScript sederhana untuk toggle menu mobile. Terakhir, saya tes di berbagai ukuran layar untuk memastikan tampilannya responsif.


Tugas 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
Perbedaan mendasar terletak pada bagaimana browser menangani proses tunggu (waiting).

Synchronous Request (Sinkron): Bekerja seperti panggilan telepon. Saat browser mengirim permintaan ke server, ia akan berhenti dan menunggu sampai server memberikan jawaban. Selama menunggu, pengguna tidak bisa melakukan interaksi apa pun dengan halaman web (UI menjadi frozen atau tidak responsif). Proses ini bersifat blocking.

Asynchronous Request (Asinkron): Bekerja seperti mengirim pesan chat. Browser mengirim permintaan ke server di "belakang layar" (background), dan tetap melanjutkan aktivitas lain tanpa harus menunggu jawaban. Pengguna bisa terus berinteraksi dengan halaman. Saat jawaban dari server tiba, hanya bagian tertentu dari halaman yang akan diperbarui sesuai data yang diterima. Proses ini bersifat non-blocking dan inilah prinsip yang digunakan oleh AJAX.

2. Alur kerja AJAX dalam konteks proyek Django ini adalah sebagai berikut:

Pemicu di Frontend: Pengguna melakukan aksi, misalnya menekan tombol "Publish News" pada modal. Aksi ini memicu sebuah fungsi JavaScript.

Request oleh JavaScript: Fungsi JavaScript menggunakan fetch() untuk mengirim permintaan (misalnya, POST) ke URL spesifik yang sudah terdaftar di urls.py Django (contoh: /create-product-ajax/). Request ini membawa data dari form dan juga header penting seperti X-CSRFToken untuk keamanan.

Routing oleh Django: urls.py menerima request dan mencocokkannya dengan view yang sesuai di views.py (contoh: create_product_ajax).

Pemrosesan di View: View di views.py menerima data, melakukan validasi (misalnya, menggunakan ProductForm), menyimpan data ke database, dan menyiapkan respons.

Response dalam Format JSON: Berbeda dengan render biasa yang mengembalikan file HTML, view ini mengembalikan JsonResponse. Isinya adalah data terstruktur (misalnya, {"status": "success", "message": "Product berhasil dibuat!"}).

Manipulasi DOM oleh JavaScript: JavaScript di frontend menerima respons JSON ini. Jika statusnya "success", JavaScript akan secara dinamis memperbarui halaman—misalnya, dengan menutup modal, menampilkan notifikasi toast, dan memuat ulang daftar produk—semua tanpa me-refresh halaman.

3. Pengalaman Pengguna (UX) yang Lebih Baik: Interaksi terasa lebih cepat, mulus, dan responsif seperti aplikasi desktop karena tidak ada flash putih atau jeda akibat reload halaman penuh.

Mengurangi Beban Server & Bandwidth: Server hanya mengirimkan paket data JSON yang berukuran kecil, bukan file HTML utuh yang lebih besar. Ini menghemat bandwidth dan sumber daya server.

Efisiensi: Hanya bagian halaman yang relevan yang diperbarui. Misalnya, saat menambah produk, hanya daftar produk yang di-refresh, bukan navbar atau footer.

4. Keamanan adalah prioritas utama, terutama untuk autentikasi. Berikut adalah langkah-langkah penting:

Gunakan CSRF Token: Semua permintaan POST, PUT, DELETE yang mengubah data, termasuk login dan register via AJAX, wajib menyertakan CSRF Token. Token ini dikirim melalui request header (X-CSRFToken) untuk memastikan permintaan berasal dari situs kita sendiri.

Validasi di Sisi Server: Jangan pernah percaya data yang dikirim dari frontend. Selalu lakukan validasi ulang di view Django menggunakan UserCreationForm dan AuthenticationForm untuk memastikan data bersih dan aman sebelum diproses.

Gunakan HTTPS: Seluruh komunikasi, terutama yang melibatkan pengiriman password, harus dienkripsi menggunakan HTTPS untuk mencegah serangan man-in-the-middle.

Otorisasi di Setiap Endpoint: Untuk fitur yang memerlukan login (seperti edit/hapus produk), setiap view AJAX harus selalu memeriksa apakah pengguna sudah diautentikasi (@login_required) dan memiliki hak akses yang sesuai (if product.user == request.user).

