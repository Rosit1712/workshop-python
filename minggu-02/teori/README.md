Minggu 02

CONTROL FLOW TOOLS

if statements
    python tidak ada else if tapi menggunakan elif yang lebih singkat. blok else adalah optional, dan kondisi if, elif, elif digunakan untuk menggantikan peran switch case

for statement
    perulangan / loop for di python berbeda dengan bhs pemrograman lain, di python for mengulang sebanyak item yang di sebuah list / string

fungsi range()
    fungsi built in python yang menghasilkan rentang angka tertentu

break, continue dan else dalam perulangan
    break berfungsi menghentikan perulangan scr paksa, continue berfungsi mem bypass nilai tertentu, else dlm perulangan akan dieksekusi ketika perulangan terlalu panjang (for) atau ketika kondisi FALSE (while) tetapi tidak ketika perulangan di hentikan oleh break

pass statement
    statement yang fungsi tidak melakukan apapun, akan tetapi dapat digunakan ketika diperlukan syntax saat program tidak melakukan apapun

Mendefinisikan Fungsi
    diawali dengan keyword def, statement pertama dapat berupa string, fungsi dapata dipanggil dalam beberapa bentuk

keyword argument
    sebuah fungsi dapat dipanggil menggunakan argument keyword

parameter khusus
    secara default argument dapat lolos ke fungsi python sesuai posisi atau kata kunci. simbol /, * adalah optional akan tetapi ketika digunakan maka hal ini mengindikasikan bagai mana argument dapat masuk ke fungsi baik positional-only, positional-or-keyword, dan keyword-only (nama parameter)

arbitrary argument list
    digunakan untuk menspesifikan fungsi dapat dipanggil dengan angka arbitrary dari sebuah argument. biasa nya argument dalam bentuk tuple atau urutan-urutan

unpacking argument list
    terjadi ketika argument sudah berada didalam list atau tuple tapi perlu untuk di bongkar untuk pemanggilan fungsi yang memerlukan argument dengan posisi yang terpisah

lambda expressions 
    berfungsi untuk mengembalikan nilai dari hasil penjumlahan 2 argumen, lambda juga dapat digunakan kapanpunn objek fungsi diperlukan

dokumentasi string
    dalam penulisan dokumentasi baris pertama barus selalu singkat, langsung inti tujuan nya saja. jika memerlukan banyak dokumentasi baris kedua barus blank untuk menandakan kesimpulan dari deskripsi pertama. baris selanjutnya dapat berupa 1 atau lebih paragraf yang menjelaskan mengenai objek yang dibicarakan

fungsi annotaions
    fungsi opsional untuk keperluan informasi metadata mengenai tipe yang digunakan oleh user-defined function