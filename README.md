# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jumlah dropout yang tinggi menjadi salah satu masalah yang besar sehingga Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.


### Cakupan Proyek
Untuk menjawab permasalahan bisnis tersebut, kita akan membuat sebuah sistem berbasis machine learning untuk mendeteksi siswa yang mungkin akan melakukan dropout serta membuat Dashboard untuk memonitor performa siswa. ***Proyek ini dilakukan dengan 3 tools, yaitu python, streamlit community cloud dan google looker studio***. 


### Persiapan

Sumber data: Adapun sumber data menggunakan <a href="https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv">Student Performance's</a> 

Setup environment:

Buka terminal atau PowerShell. Kemudian buat sebuah folder baru bernama proyek_students_performance dengan menjalankan perintah berikut.
```
mkdir proyek_students_performance

```
Kemudian pindah ke folder terbaru tersebut menggunakan perintah berikut.
```
cd proyek_students_performance

```
Kita buat sebuah virtual environment dengan menjalankan perintah berikut.
```
pipenv install

```
Aktifkan virtual environment dengan menjalankan perintah berikut.
```
pipenv shell

```
Instal semua library yang dibutuhkan menggunakan perintah berikut.
```
pip install -r requirements.txt

```
Buka jupyter-notebook dengan menjalankan perintah berikut.
```
jupyter-notebook .

```

## Business Dashboard
Dalam business dashboard yang telah dibuat, terdapat beberapa visualisasi yang membantu menganalisis faktor apa yang membuat tingginya Dropout siswa. Antara lain:
- Terdapat 4 KPI yaitu jumlah siswa lulus, jumlah siswa dropout, jumlah siswa aktif dan Dropout rate.
- Ditampilkan persentase status siswa
- Ditampilkan persentase gender siswa
- Bar chart Jumlah siswa berdasarkan course dan status 
- Bar chart terkait jumlah Dropout berdasarkan course yang diambil
- TOP 3 Course dengan dropout terbanyak 
- TOp 3 Course dengan gradute terbanyak
- Stacked bar chart berdasarkan status siswa & Penerima beasiswa
- Bar chart dari pekerjaan dan latar belakang pendidikan orang tua 

Adapun dashboard dapat dilihat pada link <a href="https://lookerstudio.google.com/reporting/0184b148-39ee-4c6c-9af7-bee3de2e134c">berikut </a>

## Menjalankan Sistem Machine Learning
Adapun untuk mengakses prototype yang telah dibuat secara online (streamlit community cloud) dapat dilihat pada link <a href="https://dropout-rate-analysis-lnsscrfvuaztk9bty5p4a8.streamlit.app/">berikut </a>

Jika anda ingin menjalankan prorotype secara lokal (via streamlit), maka berikut langkah-langkahnya:

```
Buka terminal di python/ anaconda prompt 
```
```
ketik streamlit run dropout_app.py
```
```
Isi/edit Data-data yang diperlukan
```
```
Klik "Predict"
```
```
Maka hasilnya prediksinya pun muncul ✨
```



## Conclusion
Terdapat beberapa kesimpulan yang dapat diambil dari dashboard dan model machine learning yang telah dibuat, diantaranya:
1. Mayoritas mahaiswa statusnya masih lajang.
2. 64% Siswa adalah perempuan sedangkan sisanya laki-laki
3. Siswa paling banyak berasal dari course Nursing (9500) sedangkan siswa paling sedikit dari course Biofuel Production Technologies (33)
4. Dari stacked bar chart diketahui bahwa siswa Dropout dari course Informatics Engineering (9119) lebih besar daripada siswa yang lulus.
5. TOP 3 course yang paling banyak Graduate adalah Nursing (9500), Social Services (9238) dan Journalism and Communication (9773).
6. TOP 3 course yang paling banyak dropout adalah Basic Education (9991), Management (9147) dan Nursing (9500).
7. Mayoritas orang tua siswa berprofesi sebagai "unskilled workers"
8. Mayoritas orang tua siswa hanya menempuh pendidikan selama 5-6 tahun (Hanya sampai setingkat SD saja)
9. Dilakukan prediksi menggunakan 3 algoritma machine learning yaitu decision tree, random forest dan gradientboosting
10. Algoritma yang paling baik akurasinya adalah random forest dengan akurasi sebesar 71%

### Rekomendasi Action Items
Oleh karena itu, saya merekomendasikan jaya-jaya institut melakukan hal-hal sebagai berikut:
- Melakukan pendampingan khusus terhadap siswa dari course Basic education, management, nursing dan informatic engineerring untuk meningkatkan status siswa "Graduate"
- Bisa menambah kuota penerima beasiswa, karena berdasarkan data hampir separuh siswa yang lulus adalah penerima beasiswa. Sehingga beasiswa ini sebagai pemacu kelulusan. Selain itu, adanya beasiswa meringkankan beban biaya bagi orang tua siswa dengan status "unskilled workers"
- Memberikan motivasi atau self development terhadap siswa yang memiliki orang lulusan setingkat SD. Hal ini dimungkinkan karena kurangnya dorongan dari keluarga untuk menyelesaikan Course
- Dapat menggunakan prototype aplikasi untuk mendeteksi siswa yang berpotensi Dropout 😁
