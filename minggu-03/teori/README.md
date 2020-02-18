#Minggu 03

##Data Structures
___
1. Dalam python terdapat fungsi fungsi untuk dengan tipe list, sebagai berikut
    * list.append(x) : menambahkan item diakhir list (data terakhir) bermanfaat dalam pengaplikasian stack
    * list.extend(x) : memperbesar list dengan menambah semua item yang didefinisikan di perulangan
    * list.insert(i,x) : menambah item x diposisi ke i
    * list.remove(x) : menghapus item x yang pertama
    * list.pop([i]) : menghapus elemen pertama dari list yang sama dengan x kemudian dikemablikan hasilnya. bermanfaat dalam pengaplikasian stack
    * list.clear() : menghapus semua elemen yang ada di list
    * list.count(x) : mengembalikan nilai berupa berapa kali nilai x muncul dalam list
    * list.sort(key=None, reverse=False): mengurutkan item yang ada dalam list
    * list.reverse() : mengacak urutan semua yang elemen list
    * list.copy() : mengembalikan nilai dengan mengcopy elemen yang sama dengan a[:]
2. Statement del : untuk menghapus item/atau semua yang ada dalam list bisa menggunakan statement del. selain bisa menghapus item del bisa digunakan untuk menghapus variabel
3. Tuples and Sequences : dalam python ada beberapa urutan tipe data yang ditambahkan yaitu tuple
4. Sets : merupakan sebuah collection yang nantinya menyebabkan hasil tidak adanya elemen yang sama dalam sebuah list
5. Dictionaries : dictionaries ini di indekskan berdasarkan kunci yang mana nilai nya bersifat immutable (tidak bisa diubah). biasa nya string dan angka bisa dijadikan sebagai kunci, tuple bisa jika mengandung karakter string angka maupun tuple lagi. akan tetapi jika tuple mengandung objek mutable maka tidak bisa digunakan sebagai kunci, kita tidak bisa menggunakan list sebagai kunci, karena list bisa dimodifikasi ditempat menggunakan index penugasan
6. Teknik Looping: ketika melakukan iterasi dalam dictionaries digunakan fungsi items() agar nilai yang dihasilkan dapat ditampilkan secara bersamaan. kemudian saat ingin menampilkan posisi indeks dan nilai secara bersamaan digunakan fungsi enumerate(). untuk melakukan loop di lebih dari 2 penugasan digunakan zip(), terakhir reversed() digunakan untuk menampilkan loop secara acak 
7. Kondisi Selain While dan if: selain itu bisa digunakan operator comparasion seperti in, not in, <,>,<>,==,!=
8. Membandingkan Sequences dan tipe lain : objek sequences dapat dibandingkan dengan objek lain dengan tipe sequence yang sama, menggunakan lexicographical ordering yakni membandingkan 2 item pertama dan jika mereka berbeda maka akan menentukan hasil perbandingan, jika sama 2 item berikutnya akan dibandingkan kembali dan begitu seterusnya sampai salah satu sequence habis. jika dua item yang akan dibandingkan adalah dirinya sendiri dengan tipe yang sama, lexicographical comparasion akan dilakukan secara rekursif.