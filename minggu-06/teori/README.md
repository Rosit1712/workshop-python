# MINGGU-06 #
- - - -

## Error dan Exception ##

* Exception adalah sebuah peristiwa yang terjadi selama pelaksanaan program yang mengganggu aliran normal instruksi program 
* handling exception atau penanganan saat exception muncul dapat dilakukan di python
* Macam Exception standart : Exception, StopIteration, SystemExit, StandardError ArithmeticError, OverFlowError,TypeError, dll
* untuk handling exception ini digunakan statement try...except, dengan urutan yang dilakukan:
    1. statement didalam klausa try yang pertama kali dieksekusi 
    2. jika tidak ada exception yang terjadi statement except akan diskip tidak dikerjakan
    3. tetapi jika exception muncul dalam klausa try, maka statemnt sisa didalam try tidak akan dikerjakan dan akan berlanjut ke klausa except dengan mencari apakah ada tipe exception yang terjadi
    4. jika exception muncul dan tidak ditemukan exception yang cocok di klausa except maka program akan mempass ke statement diluar klausa try. jika handler exception tidak ditemukan eksekusi akan dihentikan dengan menampilkan pesan
* sebuah statement try dapat mempunyai lebih dari 1 klausa except dengan tipe exception yang berbeda
* keyword raise digunakan mengeluarkan error atau exception secara disengaja
* selain menggunakan exception bawaan kita bisa mendeklarasikan nama exception sesuai kebutuhan. kelas baru exception yang dibuat ini berasal dari kelas Exception
* selain klausa try...except kedua harus ada (try 1, except bisa lebih dari 1) juga bisa ditambahkan klausa optional yaitu finally dengan fungsi untuk mengeksekusi sebuah statement setelah try entah exception terjadi atau pun tidak 