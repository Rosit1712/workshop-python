# Minggu-09 #
- - - -
## Virtual Environts and Packages ##

* Python memnugkinkan dalam sebuah aplikasi nya bisa menggunakan library standart ataupun library dengan versi tertentu saja
* Yakni dengan menggunakan virtual environment (sebuah direktori mandiri yang berisi instalasi python untuk versi tertentu saja dan berisi package tambahan lainnya)
* Untuk membedakan environment setiap aplikasi mempunyai mempunyai virtual environment tersendiri
* venv : modul dengan fungsi untuk membuat dan mengatur virtual environment
* pip : program yang digunakan untuk menginstall (index website https://pypi.org), update, upgrade dan menghapus package

## Conda ##

* Merupakan salah tau package manager dan environment berbasis command line di windows, linux, macOs
* Untuk menjalankan conda setelah sudah diinstall di komputer, dengan mencari lewat search Anaconda ataupun melalui anaconda navigator
* conda --version : mengecek apakah conda di komputer sudah ada dan berjalan atau belum serta versinya
* conda update conda : perintah untuk mengupdate conda ke versi terbaru
* Mengatur Environment di conda menggunakan perintah dasar :
    1. conda create --name namaEnvironmentBaru namaPackage : buat environment
    2. conda activate : mengaktifkan environment
    3. conda info --envs : list semua environment yang ada
    4. activate : kembali ke default environment (base)
* Mengatur Python di conda menggunakan perintah dasar :
    1. conda create --name namaEnvironment python=versi (misal: 3.5) : buat environment
    2. conda activate namaEnvironment : aktifkan environment
    3. conda info --envs : cek environment bar sudah ada dan aktif atau belum
    4. python --version : mengecek versi python
    5. conda activate : menonaktifkan environmentBaru dan kembali ke default (base)
* Mengatur Package di conda menggunakan perintah dasar :
    1. conda search namaPackage (misal: beautifulsoup4) : cek package sudah terinstall atau belum
    2. conda install namaPackage (misal: beautifulsoup4) : install package kedalam environment baru. instalasi memerlukan komputer terkoneksi dengan internet
    3. conda list : melihat akan ada program yang terinstall di environment