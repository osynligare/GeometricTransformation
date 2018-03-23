# Program Transformasi Geometri
Simulasi untuk transformasi geometri 2 dimensi dengan menggunakan Antarmuka Pemrograman Aplikasi OpenGL

## Memulai
Buka folder bin lalu ketuk 2 kali pada file :
```
TransformasiGeometri.exe
```
*starting-up pada program agak lambat*
Lalu program akan menampilkan 2 buah jendela program.
Yang 1 adalah terminal dan 1 lagi adalah jendela untuk tampilan grafik.
Pada jendela terminal akan tertulis :
```
--------------SELAMAT DATANG---------------
Masukkan jumlah titik sudut :
```

### Pustaka yang digunakan
```
pyOpenGL
numpy
math
```

## Menggunakan Program
Berikut ini adalah cara menggunakan program :

### Memasukkan Titik Sudut
Contoh masukan :
```
Masukkan jumlah titik sudut : 3
(x1,y1) 100,100
(x2,y2) 300,100
(x3,y3) 250,250
Masukan fungsi :
```

### Perintah

Daftar perintah-perintah dasar:
Translasi objek searah x sejauh dx dan searah y sejauh dy.
```
translate dx dy
```

Dilatasi objek k kali.
```
dilate k
```

Rotasi objek deg derajat dengan poros (a,b).
```
rotate deg a b
```

Refleksi objek berdasarkan parameter <x, y, y=x, y=-x>.
```
reflect parameter
```

Menggusur objek searah param <x atau y> dengan faktor k.
```
shear param k
```

Meregangkan objek searah param <x atau y> dengan faktor k.
```
stretch param k
```

Transformasi objek dengan matrix bebas
a c
b d
```
custom a b c d
```

Melakukan transformasi sekaligus sebanyak n kali.
```
multiple n
command parameter
command parameter
.
.
.
```

Mengembalikan objek ke posisi awal.
```
reset
```

Keluar program.
```
exit
```

### Contoh penggunaan program :
```
--------------SELAMAT DATANG---------------
Masukkan jumlah titik sudut : 3
(x1,y1) 100,0
(x2,y2) 200,100
(x3,y3) 0,400
Masukan fungsi : rotate 90 0 0
Masukan fungsi : custom 1 2 2 1
Masukan fungsi : reset
Masukan fungsi : multiple 3
masukan fungsi ke-1 : dilate 0.5
masukan fungsi ke-2 : reflect y=-x
masukan fungsi ke-3 : shear x 2
Masukan fungsi : exit
SAMPAI JUMPA ;)
```