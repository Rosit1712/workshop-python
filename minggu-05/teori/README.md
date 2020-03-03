#Minggu-04#
- - - -
##Input dan Output##

1. untuk menampilkan output dengan format tertentu
    * keyword f atau F sebelum tanda quotes ' didalam string, nantinya bisa menuliskan/memasukan nilai ekspresi { dan } yang berarti nilai dalam { } merujuk pada variabel atau nilai literal
    * str.format(): fungsi string yg penggunaan masih dengan { dan } sebagai penanda dimana variaabel akan diganti dan bisa menyediakan detail format yang diinginkan.
    * konversi segala nilai string:
        - str() mengembalikan nilai hasil yang bisa dibaca oleh manusia
        - repr() menghasilkan nilai yang bisa dibaca oleh interpreter / ditutup secara paksa jika tidak ada syntax yang ekuivalen
    * tanda { dan } merujuk pada posisi objek yang dilewatkan kedalam fungsi str.format()
    * jika string terlalu panjang dan tidak ingin dipisahkan maka bisa digunakan [] yang berfungsi untuk mereferensi variabel yang akan diformat berdasarkan nama bukan posisi. bisa juga menggunakan notasi **
    * pengolahan string terakhir secara manual dengan operasi slicing dan concat utuk membuat layout baru. fungsi rjust() membuat string rata kanan dengan lebar kearah kiri, begitu pula dengan str.ljust() dan str.center() sama-sama untuk marginnnya. str.zfill() mengenerate string dengan 0 (mendeteksi plus atau minus)
    * pemformatan string model lama menggunakan operator %, dimana ia meninterpretasikan argumen disebelah kiri seperti sprintf()string format-gaya untuk diterapkan pada argumen yang benar, dan mengembalikan string yang dihasilkan dari operasi pemformatan
    * fungsi open() digunakan untuk membaca file dengan mengembalikan dalam bentuk objek. format open(filename, mode)
    * fungsi read() digunakan untuk membaca data yang dalam file
    * fungsi readline() digunakan untuk membaca data ditiap baris file
    * format JSON umumnya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah terbiasa dengannya, yang menjadikannya pilihan yang baik untuk interoperabilitas