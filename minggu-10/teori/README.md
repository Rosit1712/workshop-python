# Minggu-10 #
- - - - 
## CockroachDB ##

* CockroachDB : Database berbasis SQL transaksional yang menggunakan penyimpanan key value (kunci penyimpanan)
* CockroachDB mampu melakukan scale terhadap cluster data secara horizontal tanpa perlu mengkonfigurasi ulang atau menambahkan arsitektur baru. Pengelolaan Cluster yang dilakukan :
    - Skala dengan hanya menambahkan node baru ke cluster CockroachDB
    - Otomatis menyeimbangkan dan distribusi rentang, bukan pecahan
    - Optimalkan pemanfaatan server secara merata di semua node
* Dalam pengeloaan database nya cockroach mempunyai 2 kategori cluster databse:
    1. Secure : seluruh proses dan transaksi beserta data terenkripsi. cert : mengenerate CA certificate dan key
    2. Insecure : seluruh proses dan transaksi beserta data tidak terenkripsi. insecure : cluster insecure
* CockroachDB untuk build python app menggunakan library :
    - psycopg2
    - SQLAlchemy
    - Django
    - PonyORM
    - peewee
* Cockroach Support PostgresSQL dengan client Go, Python, Ruby, Java, JavaScript (node.js),dll
* 3 langkah menambahkan Cluster cockroachDB :
    1. Tentukan mau berapa jumlah cluster yang akan digunakan
    2. Inisialisasi Cluster
    3. Sclae cluster dengan menambahkan nodes baru

## Psycopg ##

* adapter python untuk koneksi dengan PostGresSQL database
* instalasi : pip insgall psycopg2
## SQLAlchemy ##

* Python SQL toolkit dan Object Relational Mapper yang memberi pengembang aplikasi kekuatan penuh dan fleksibilitas SQL
* instalasi : pip install sqlalchemy sqlalchemy-cockroachdb
