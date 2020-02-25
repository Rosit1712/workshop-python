# Minggu-04 #
- - - -
## Modules ##

* saat menggunakan python interpreter variabel atau fungsi yang dibuat pada sesi tersebut akan hilang ketika pengguna keluar dari interpreter tersebut. program yang dibuat disaran kan untuk di bagi menjadi beberapa file agar mudah dikendalikan pada saat maintenance.
* python mempunyai module  file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__.
*  fungsi penggunaan modul ini adalah definisi variabel, fungsi dan komponen-komponen lain yang ada di modul tersebut dapat dipergunakan baik difile lain atau di interpreter
* untuk meng import bisa digunakan 
    1. syntax standard: import namamodul
    2. syntax dengan alias: import module_name as alias
    3. syntax import salah satu bagian program saja: from ... import namabagian
    4.  syntax import semua isi modul: import *
* import bisa didefinisikan dalam IDLE python atau interperternya
* python punya modul-modul bawaan seperti math, os, sys, matplotlib, seaborn, dll. Modul-modul tersebut berada dalam direktori Lib
