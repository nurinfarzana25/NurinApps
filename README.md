Tautan menuju aplikasi Adaptable yang sudah di-deploy : https://nurinapps.adaptable.app/ atau https://nurinapps.adaptable.app/main/

Penjelasan mengenai cara mengimplementasikan checklist secara step=by-step :
    
    #Membuat proyek Django baru
        Setelah sebelumnya membuat direktori utama dan direktori proyek yang sudah terhubung dengan repositori di github dan menambahkan berkas requirments.txt yang berisikan beberapa dependencies serta menginstallnya, selanjutnya menjalankan command "django-admin startproject (nama_proyek) ." dan berhasillah dalam membuat proyek Django yang baru.
    
    #Membuat aplikasi main pada proyek
        Main akan ditambahkan ke dalam proyek lebih tepatnya pada direktori utama, yang nantinya akan menjadi direktori aplikasi. Yaitu dengan menjalankan command "python manage.py startapp main" dan mendaftarkannya ke dalam proyek dengan cara menambahkan 'main' pada berkas setting.py dalam direktori proyek. Pada aplikasi main ini lah yang akan dibuat direktori template yang berisikan main.html untuk membuat sebuah struktur untuk ditampilkan pada halaman web. 
    
    #Melakukan routing pada proyek agar dapat menjalankan aplikasi main
        Routing pada proyek ini digunakan agar aplikasi main dapat diakses melalui peramban web, yaitu dengan menambahkan beberapa kode pada berkas urls.py dalam direktori main. Kemudian menambahkan rute URL dalam urls.py yang ada pada proyek untuk menghubungkannya ke tampilan main, yaitu dengan melakukan impor fungsi include dari django.urls dan menambahkan rute url berupa(urlpatterns = [path('admin/', admin.site.urls),path('', include('main.urls')), ]) untuk mengarahkan ke tampilan main di dalam variabel urlpatterns. Setelah itu proyek Django dapat dijalankan dengan command "python manage.py runserver" dan kemudian membuka http://localhost:8000/main/ di perambanan web.
    
    #Membuat model pada aplikasi main dengan nama item
        Dalam direktori main yang ada pada direktori utama berisikan main.html ini, akan ditambahkan item yang memiliki atribut wajib seperti name(dengan tipe CharField), amount(dengan tipe IntegerField), dan description(dengan tipe TextField). models sebagai kelas dasar yang digunakan untuk mendefinisikan model dalam Django, dengan Item sebagai nama model yang didefinisikan. Setelah itu dilakukan migrasi, yaitu sebuah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode.Migrasi ini merupakan cara Django untuk melacak perubahan pada model basis data yang ada.
    
    #Membuat fungsi pada views.py
        Didalam aplikasi main, terdapat berkas views.py yang kemudian dapat ditambahkan fungsi yang akan dikembalikan ke dalam template html. Fungsi ini akan digunakan untuk menampilkan informasi yang direquest. Saya menambahkan nama-nama dari semua barang, berat setiap barang, harga setiap barang, dan jumlah ketersediaan/stok untuk setiap barang.
    
    #Mengatur routing aplikasi main
        Dan yang terakhir, perlu mengatur routing khusus untuk aplikasi "main", yaitu dnegan membuka berkas urls.py yang ada pada direktori main dan menambahkan beberapa kode : 
        from django.urls import path 
        from main.views import show_main 
        app_name = 'main'
        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    
    #Melakukan deployment ke Adaptable terhadap aplikasi
        Server Django dapat dijalankan dengan menggunakan command python manage.py runsurver dan kemudian membuka browser untuk mengakses http://localhost:8000/about. Setelah direktori lokal sudah terhubung ke repositori di github, kemudian login di Adaptable dengan akun github. Lalu menambahkan apps baru dengan repositori proyek yang akan dibangun. Selanjutnya mengikuti arahan untuk melakukan deployment, dan akhirnya berhasil untuk mendeploy aplikasi yang sudah dibangun. Terdapat link dengan keterangan domains, dan perlu menambahkan path /main/ pada akhir link tersebut untuk dapat mengakses aplikasi yang sudah dibuat sebelumnya. Namun, karena sebelumnya saya menggunakan image dengan file lokal maka foto-foto yang saya unggah tidak muncul, sehingga agar muncul maka saya menggunakan link address image dari internet untuk gambar-gambar yang saya gunakan.
    
    #Membuat sebuah README.md
        Yaitu dengan menambahkan file dengan nama README.md pada direktori utama. Setelah itu tinggal melakukan command add, commit, dan push.

        ![alt text](https://github.com/nurinfarzana25/NurinApps/blob/main/bagan.png?raw=true)
        
        *Menggunakan virtual environment 
            Virtual environment digunakan untuk mengisolasi lingkungan pengembangan aplikasi sehingga dependensi dan paket yang digunakan dalam proyek tidak akan berinteraksi dengan proyek lain atau sistem operasi secara global. Dengan virtual environment, maka dapat mengelola paket-paket Python yang diperlukan secara terisolasi untuk setiap proyek, yang membuatnya lebih bersih dan teratur. Tanpa menggunakan virtual environment, akan masih dapat membuat aplikasi web berbasis Django, tetapi dapat menjadi sulit mengelola dependensi dan mungkin menyebabkan konflik jika sedang bekerja pada beberapa proyek yang menggunakan versi paket yang berbeda.
        
        *MVC, MVT, dan MVVM
            
            -MVC (Model-View-Controller): Ini adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama. Model mewakili data dan logika aplikasi, View bertanggung jawab untuk tampilan, dan Controller mengatur interaksi antara Model dan View. Contoh framework yang menggunakan pola ini adalah Ruby on Rails.
            
            -MVT (Model-View-Template): Ini adalah varian dari MVC yang digunakan oleh Django. Model masih bertanggung jawab atas data dan logika bisnis, View menangani tampilan, dan Template berfungsi sebagai bagian yang mengendalikan bagaimana data ditampilkan dalam HTML. Controller dalam MVT digantikan oleh Django Framework itu sendiri.
            
            -MVVM (Model-View-ViewModel): Ini adalah pola desain yang digunakan terutama dalam pengembangan aplikasi berbasis frontend, seperti dengan framework Angular dan Vue.js. Model mewakili data dan logika, View menggambarkan tampilan, dan ViewModel berperan sebagai perantara antara Model dan View, mengatur logika tampilan.

