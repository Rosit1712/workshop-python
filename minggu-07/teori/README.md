# Minggu-07 #
- - - -
## Kelas (Classes)

* Membuat kelas di python menggunakan syntax:
    class ClassName: 'Optional class documentation string' class_suite
* Obyek memiliki field berupa variabel obyek dan method berupa fungsi obyek. Keduanya disebut atribut obyek. Class juga dapat memiliki field class (variabel class) dan method class. Class didefinisikan dengan keyword class.
* Dalam deklarasi method pada class terdapat perbedaan yaitu ada parameter pertama yang harus ditambahkan pada parameter fungsi. Parameter ini diberi nama self, nilai dari parameter ini menunjuk ke obyek / instance itu sendiri. Nilai self ini disediakan oleh Python. Contoh, ada class ClassSaya yang mempunyai instance obyek obyeksaya. Ketika method dipanggil pada obyek obyeksaya.method(arg1, arg2), secara otomatis diubah oleh Python menjadi ClassSaya.method(obyeksaya, arg1, arg2).
* Method __init__ :   method ini akan dijalankan ketika obyek dibuat. Method ini berguna untuk melakukan inisialisasi. Perhatikan garis bawah dua kali di awal dan di akhir method (double underscore, dunder).
* Variabel class dan variabel objek (instance) : Variabel Class yaitu variabel yang dimiliki oleh class, sedangkan variabel obyek adalah variabel yang yang dimiliki oleh tiap-tiap obyek instance dari class.
* Inheritance : Salah satu keuntungan dari OOP adalan penggunaan ulang kode dan salah satu caranya yaitu menggunakan mekanisme inheritance / turunan.