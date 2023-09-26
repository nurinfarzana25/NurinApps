1. Django UserCreationForm adalah salah satu formulir bawaan (built-in form) yang disediakan oleh Django, sebuah kerangka kerja (framework) Python untuk pengembangan aplikasi web. Formulir ini digunakan untuk membuat dan mendaftarkan pengguna baru pada sebuah situs web yang menggunakan Django. Dalam konteks autentikasi pengguna, UserCreationForm digunakan bersama dengan model pengguna bawaan Django, yaitu User.

# Kelebihan UserCreationForm:

 - Mudah Digunakan: UserCreationForm telah siap pakai dan mudah digunakan. Pengguna hanya perlu mengimpor dan mengintegrasikannya ke dalam aplikasi Django Anda.
 - Validasi Otomatis: Form ini dilengkapi dengan validasi otomatis untuk memastikan bahwa pengguna memasukkan informasi yang sesuai, seperti memeriksa apakah kata sandi memenuhi kebijakan keamanan yang ditetapkan.
 - Konfigurasi yang Fleksibel: dapat menyesuaikan formulir ini sesuai kebutuhan proyek. Selain itu. dapat menambahkan atau menghapus bidang, menyesuaikan pesan kesalahan, atau menambahkan validasi tambahan.
 - Integrasi dengan Django Admin: Formulir ini dapat dengan mudah digunakan bersama dengan Django Admin untuk mengelola pengguna.

# Kekurangan UserCreationForm:

 - Tampilan Default: Tampilan dari UserCreationForm mungkin terlalu sederhana atau tidak sesuai dengan desain tampilan spesifik yang diinginkan oleh pengembang atau desainer web.
 - Kustomisasi yang Terbatas: Meskipun dapat menyesuaikan formulir ini, kustomisasi yang lebih lanjut, seperti menambahkan bidang kustom, dapat menjadi lebih rumit.
 - Bahasa Tertentu: Pesan kesalahan dan label pada formulir ini akan mengikuti bahasa yang diatur dalam pengaturan Django. Ini mungkin menjadi kendala jika Anda menginginkan formulir dalam bahasa yang berbeda.

 2. Perbedaan autentikasi dan otorisasi
 # Autentikasi
  Autentikasi adalah proses mengidentifikasi pengguna dan memastikan bahwa pengguna adalah mereka yang mereka klaim sebagai.
  Ini mencakup verifikasi identitas pengguna, biasanya dengan mengharuskan mereka memasukkan informasi login seperti nama pengguna (username) dan kata sandi (password).
  Autentikasi dapat mencakup mekanisme tambahan seperti autentikasi dua faktor (2FA), autentikasi dengan token, atau integrasi dengan pihak ketiga seperti OAuth.
  Tujuannya adalah untuk memastikan bahwa pengguna yang mencoba mengakses sistem adalah mereka yang sah.
  # Otorisasi
  Otorisasi adalah proses mengendalikan akses pengguna terotentikasi ke bagian-bagian tertentu dalam aplikasi berdasarkan peran (role) atau hak akses (permissions) yang mereka miliki.
  Ini berkaitan dengan apa yang diizinkan atau tidak diizinkan pengguna lakukan setelah mereka terautentikasi.
  Misalnya, pengguna dengan peran "Admin" dapat memiliki izin untuk mengelola pengguna lain, sedangkan pengguna biasa mungkin hanya diizinkan untuk melihat konten tetapi tidak dapat mengeditnya.
  Tujuannya adalah untuk memastikan bahwa pengguna hanya memiliki akses ke sumber daya yang sesuai dengan peran atau izin mereka.

3. Cookies adalah potongan kecil data yang disimpan di sisi klien (pada browser pengguna) saat berinteraksi dengan situs web. Mereka digunakan untuk menyimpan informasi tentang sesi pengguna, preferensi, dan informasi lainnya. Dalam konteks aplikasi web, cookies sering digunakan untuk:

  - Mengelola Sesi Pengguna: Salah satu penggunaan utama cookies adalah untuk mengelola sesi pengguna. Ini memungkinkan server web untuk mengidentifikasi pengguna yang telah terautentikasi dan menyimpan informasi seperti ID sesi, yang kemudian dapat digunakan untuk mempertahankan keadaan sesi selama kunjungan berikutnya.

  - Melacak Preferensi Pengguna: Cookies dapat digunakan untuk menyimpan preferensi pengguna, seperti bahasa yang dipilih, tema situs web, atau pengaturan lainnya. Ini membantu dalam memberikan pengalaman yang disesuaikan dengan preferensi pengguna.

  - Pelacakan Analitik: Cookies dapat digunakan untuk melacak perilaku pengguna di situs web, seperti halaman yang dikunjungi, waktu yang dihabiskan di situs, dan interaksi lainnya. Ini membantu pemilik situs untuk menganalisis kinerja dan perilaku pengguna.

  - Iklan Target: Dalam iklan online, cookies digunakan untuk menyimpan data tentang perilaku pengguna dan digunakan untuk menampilkan iklan yang sesuai dengan minat pengguna.

4. Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang harus diwaspadai. Cookies adalah alat yang berguna untuk menyimpan informasi pada peramban pengguna, namun ada beberapa risiko yang terkait dengan penggunaannya:

  - Kehilangan Privasi Pengguna: Cookies dapat digunakan untuk melacak perilaku pengguna secara online, termasuk situs web yang mereka kunjungi dan preferensi mereka. Jika informasi ini disalahgunakan atau dibagikan tanpa izin, privasi pengguna dapat terancam.

  - Potensi Serangan Keamanan: Cookies yang tidak diamankan dengan baik dapat menjadi sasaran serangan, seperti serangan Cross-Site Scripting (XSS) di mana penyerang memasukkan kode berbahaya ke dalam halaman web yang dieksekusi oleh peramban pengguna. Hal ini dapat membahayakan data cookies.

  - Cross-Site Request Forgery (CSRF): Cookies juga dapat digunakan dalam serangan CSRF, di mana penyerang memaksa pengguna untuk melakukan tindakan tertentu tanpa izin saat mereka masuk ke situs web yang menggunakan cookies.

  - Cookie Theft: Jika cookies tidak diamankan dengan baik, mereka dapat dicuri oleh penyerang. Penyerang yang berhasil mencuri cookie sesi (session cookie) dapat mendapatkan akses ke akun pengguna yang bersangkutan.

  - Tracking dan Profiling: Cookies dapat digunakan oleh perusahaan untuk melacak dan membangun profil pengguna. Ini dapat menyebabkan masalah privasi dan perasaan pengawasan.

5. Implementasi checklist step-by-step
# Mengimplementasikan fungsi register, login, dan logout
  Yaitu dengan membuat fungsi baru yang bernamakan register, login_user, dan logout_user pada vberkas file views.py yang ada di subdirektori main. Kemudian menambahkan import redirect, UserCreationForm, dan messages pada bagian paling atas. Setelah itu melengkapi kode untuk semua fungsi register, login_user, dan logout_user. Pada folder main/templates, dibuat dua file html baru yang bernama register.html serta login.html. Untuk semua fungsi baru yang sudah dibuat, maka perlu melakukan import semua fungsi tersebut pada berkas urls.py yang ada di subdirektori main dan menambahkan path url ke dalam urlpatterns untuk dapat mengakses fungsi yang sudah diimport tersebut.
# Menghubungkan Item dengan User
  Melakukan import User pada berkas models.py, serta menambahkan program user = models.ForeignKey(User, on_delete=models.CASCADE) pada model Item untuk menghubungkan satu produk dengan satu user melalui sebuah relationship. Serta menambahkan beberapa potongan kode ke fungsi create_product di berkas views.py . Selain itu, juga perlu mengubah fungsi show_main untuk value dari name dalam context. Karena mengubah isi dari models, maka perlu melakukan migration.
# Menggunakan data dari cookies
  Karena sebelumnya sudah dilakukan import HttpResponseRedirect dan reverse pada berkas views.py, maka hanya tinggal melakukan import datetime. Kemudian menambahkan fungsi yang dapat menambahkan cookie yang bernama last_login pada fungsi login_user. Fungsi ini digunakan untuk melihat waktu terakhir kali pengguna melakukan login, yaitu dengan mengubah beberapa potongan kode di fungsi login_user. Pada fungsi show_main juga perlu ditambahkan potongan kode dengan key last login yang berisikan request.COOKIES['last_login']. Serta mengubah fungsi logout_user dengan menambahkan response.delete_cookie('last_login'). Pada main.html juga ditambahkan potongan kode agar dapat menampilkan last login.
  
#########################################################

1. Membuat input form untuk menambahkan objek model app sebelumnya.
  Form ini akan digunakan sebagai perantara untuk melakukan input data barang pada aplikasi yang kemudian dapat menambahkan data baru tersebut untuk dapat ditampilkan ke halaman utama. Pertama, dengan membuat berkas baru pada direktori main dengan format penamaan form.py yang kemudian ditambahkan kode-kode berupa import ModelForm dan Item dari django.forms dan main.models. Dibuat sebuah kelas dengan nama ProductForm yang didalamnya terdapat kelas lagi dengan nama meta. Dalam kelas Meta ini, terdapat variable model yang berisikan Item dan fields yang terdiri dari "name", "price", "description", "amount", "category", dan "image". Pada berkas views.py ditambahkan import HttpResponseRedirect, ProductForm, dan reserve. Pada berkas ini, ditambahkan juga suatu fungsi dengan nama create_product yang menerima parameter request serta kode untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika ditambahkan pada form. Fungsi ini akan diimport pada file urls.py serta ditambahkan path url pada urlpatterns. Kemudian dibuat berkas baru bernama create_product.html sebagai kerangka dari tampilan halaman utama. Di file main.html juga ditambahkan kode-kode untuk menampilkan item-item yang sudah ditambahkan, dengan meliputi nama produk, harga, deskripsi, stok, kategori, dan tanggal ditambahkan.

2. Menambahkan 5 views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
  # HTML
  Untuk tampilan HTML, maka program tersebut dapat diakses dengan menjalankan perintah "python manage.py runserver" dan membuka local host  "http://localhost:8000". Dengan tersebut, maka tampilan proyek akan muncul di halaman utama serta dapat menambahkan item-item ke dalam aplikasi dan menampilkannya di halaman utama.
  # XML
  Untuk dapat mengakses dengan tampilan XML, maka perlu menambahkan import HttpResponse dan Serializer pada berkas views.py, kemudian menambahkan fungsi baru bernama show_xml dengan parameter request yang berisikan data=Item.object.all() dan mereturnya dengan return HttpResponse(serializers.serialize("xml", data), content_type="application/xml"). Selanjutnya perlu melakukan import show_xml tersebut di berkas url.py serta menambahkan path url ke dlaam urlpatterns agar dapat mengakses fungsi yang sudah dibuat tersebut dengan path('xml/', show_xml, name='show_xml'),. Program dengan tampilan xml dapat diakses dengan menjalankan command python manage.py runserver dan membuka localhost  http://localhost:8000/xml.

  # JSON
  Untuk dapat mengakses dengan tampilan JSON, maka langkah-langkah yang perlu dilakukan mirip dengan langkah-langkah untuk mengakses dengan tampilan XML. Bedanya pada fungsi, yaitu bernama show_json dan return HttpResponse(serializers.serialize("json", data), content_type="application/json"). Pada urls.py juga dilakukan import show_json dan path url yang ditambahkan ke dalam urlpatterns yaitu path('json/', show_json, name='show_json'),. Program dengan tampilan json dapat diakses dengan menjalankan command python manage.py runserver dan membuka localhost  http://localhost:8000/json.

  # XML dan JSON by ID
  Sedangkan untuk akses bentuk xml dengan id, maka juga perlu menambahan fungsi show_xml_by_id dan show_json_by_id.Bedanya dengan yang sebelumnya, pada variable dalam fungsi terdapat sebuah query yang nantinya akan disimpan dengan id tertentu yaitu data=Item.objects.filter(pk=id). Selanjutnya dilakukan juga return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") serta return HttpResponse(serializers.serialize("json", data), content_type="application/json"). Kedua fungsi tersebut juga diimport pada berkas url.py serta menambahkan path url kedalam urlpatterns untuk akses pada fungsi tersebut dengan path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),. Untuk menjalankan proyek tersebut maka jalankan command python manage.py runserver dan mengakses nya melalui http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id]. Sebagai contoh  http://localhost:8000/xml/1/ atau http://localhost:8000/json/1/.

3. Perbedaan antara form POST dan form GET dalam Django.
  # Metode pengiriman data :
  Form POST: Ketika menggunakan metode POST dalam formulir Django, data yang diisi dalam formulir dikirimkan sebagai bagian dari badan permintaan HTTP. Data ini tidak terlihat dalam URL dan tidak ter-cache oleh peramban web. Oleh karena itu, metode POST lebih cocok digunakan untuk pengiriman data sensitif atau data yang besar.
  Form GET: Dalam metode GET, data yang diisi dalam formulir ditambahkan ke URL sebagai query string. Ini membuat data terlihat dalam URL dan dapat terlihat oleh pengguna serta ter-cache oleh peramban web. Metode GET umumnya digunakan untuk mengambil data dari server tanpa mengubahnya, seperti pencarian atau filter.
  # Kapasitas data :
  Metode POST dapat digunakan untuk mengirimkan data yang lebih besar karena data dikirimkan dalam badan permintaan HTTP. 
  Metode GET memiliki batasan pada jumlah data yang dapat dikirimkan melalui URL. Karena data ditambahkan ke URL sebagai query string, terdapat batasan panjang URL di beberapa peramban web. 

4. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data.
  # XML 
  XML dirancang untuk merepresentasikan dan menukar data yang struktural dan sangat terstruktur. Sehingga sering digunakan untuk mengirim data antara sistem yang berbeda dan digunakan dalam berbagai aplikasi seperti SOAP (Simple Object Access Protocol) dalam layanan web. XML menggunakan tag yang mendefinisikan elemen dan atribut untuk merepresentasikan data, yaitu memiliki sintaks yang lebih terstruktur dengan struktur hirarkis yang kuat. XML mendukung dokumen parsial, yang berarti  dapat membagi dan mengirim hanya sebagian dari dokumen XML yang lebih besar. Parsing XML biasanya memerlukan lebih banyak kode dan bisa lebih rumit, terutama untuk dokumen yang lebih besar dan terstruktur. XML dapat digunakan dalam berbagai bahasa pemrograman dan memiliki dukungan yang luas.
  # JSON
  JSON diciptakan untuk pertukaran data ringan dan sederhana antara browser web dan server, serta dalam lingkungan bahasa pemrograman berbasis JavaScript. Ini sering digunakan dalam API REST (Representational State Transfer). JSON menggunakan pasangan nama/kunci dan nilai, yang biasanya dalam format objek atau array. Sintaksisnya lebih ringkas dan mudah dibaca oleh manusia dibandingkan dengan XML. JSON juga mendukung pengiriman data parsial, dan dapat memilih bagian tertentu dari objek JSON untuk dikirim. JSON memiliki parsing yang lebih mudah karena hampir semua bahasa pemrograman modern memiliki dukungan langsung untuk JSON. JSON adalah format yang alami bagi bahasa pemrograman berbasis objek seperti JavaScript, tetapi juga memiliki dukungan luas di berbagai bahasa pemrograman.
  # HTML
  HTML digunakan untuk mengatur tampilan dan struktur konten halaman web. Meskipun dapat mengandung data, fokus utamanya adalah pada presentasi dan tampilan. HTML juga menggunakan tag, tetapi fokusnya adalah pada struktur tampilan dan hyperlinking, sehingga memiliki elemen dan atribut khusus untuk tujuan tersebut. HTML biasanya digunakan dalam halaman web lengkap, dan membagi-bagi halaman web umumnya tidak praktis. HTML juga memiliki parsing yang relatif mudah karena diinterpretasikan oleh peramban web. HTML adalah bahasa yang digunakan dalam pengembangan web dan dapat diinterpretasikan oleh peramban web, dan biasanya tidak digunakan secara langsung untuk pertukaran data antar sistem.

5. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
  - Ringkas dan mudah dibaca: JSON memiliki sintaks yang sederhana dan mudah dibaca oleh manusia. Ini menggunakan struktur objek atau array yang intuitif, membuatnya mudah dipahami oleh pengembang dan bahkan dapat dibaca secara langsung dalam kode JavaScript.
  - Pengiriman data yang efisien: JSON adalah format data yang ringan, artinya data yang dihasilkan dalam format JSON relatif kecil dalam ukuran. Ini mengurangi beban jaringan saat mengirim data melalui internet, yang penting dalam lingkungan web yang mengutamakan kinerja.
  - Format yang konsisten: JSON memiliki format yang konsisten, dengan aturan yang jelas tentang bagaimana data harus diatur. Ini meminimalkan ambiguitas dan meningkatkan interoperabilitas antara berbagai aplikasi.
  - Dukungan untuk struktur data yang rumit: JSON dapat digunakan untuk merepresentasikan data dengan struktur yang kompleks, termasuk objek bersarang dan array multidimensi. Ini membuatnya sesuai untuk data yang lebih kompleks dalam aplikasi web modern.

6. Akses kelima URL dengan Postman
  Untuk mengakses menggunakan Postman, maka perlu menjalankan perintah python manage.py runserver, dan melakukan request baru dengan method GET dan url http://localhost:8000/xml atau http://localhost:8000/json atau juga http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] untuk mengetes fungsi pengambilan data produk berdasarkan ID. Berikut hasil dari akses kelima url tersebut melalui postman.
![HTML 1](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/html.png)
![HTML 2](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/html%20(2).png)
![XML](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/xml.png)
![JSON](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/json.png)
![XML BY ID](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/xml%20by%20id.png)
![JSON BY ID](https://github.com/nurinfarzana25/NurinApps/blob/main/foto/json%20by%20id.png)

############################################################

Tautan menuju aplikasi Adaptable yang sudah di-deploy : https://nurinapps.adaptable.app/ atau https://nurinapps.adaptable.app/main/

Penjelasan mengenai cara mengimplementasikan checklist secara step-by-step :
    
    #Membuat proyek Django baru
        Setelah sebelumnya membuat direktori utama dan direktori proyek yang sudah terhubung dengan repositori di github yang dalam prosesnya disarankan untuk membuat lingkungan virtual Python untuk proyek Django agar dapat mengisolasi dependensi proyek yaitu dengan menjalankan command 'python -m venv env' dan diaktifkan dengan 'env\Scripts\activate.bat'. Dan kemudian menambahkan berkas requirments.txt yang berisikan beberapa dependencies serta menginstallnya dengan menjalankan command 'pip install django', selanjutnya menjalankan command "django-admin startproject (nama_proyek) ." dan berhasillah dalam membuat proyek Django yang baru.
    
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

        *Penjelasan bagan :
            - Client Request
              Client (misalnya, peramban web seperti Chrome) melakukan permintaan ke aplikasi web Django dengan mengakses URL tertentu, seperti http://example.com/myapp/page1/.
            - urls.py
              File urls.py merupakan bagian dari proyek Django yang menghubungkan URL yang diminta oleh client dengan tindakan (views) yang akan diambil. Ini berisi peta URL yang mengarahkan permintaan klien ke fungsi tampilan (views) yang sesuai.
            - views.py
              File views.py berisi fungsi-fungsi tampilan yang akan mengelola permintaan dari client. Ketika URL cocok dengan pola yang didefinisikan di urls.py, fungsi tampilan yang sesuai akan dipanggil. Fungsi tampilan ini akan melakukan logika bisnis, mengambil data dari model jika diperlukan, dan mempersiapkan respons.
            - models.py
              File models.py merupakan bagian dari proyek Django yang berisi definisi model-data, seperti tabel database atau objek Python yang mewakili entitas dalam aplikasi. Model ini digunakan untuk berinteraksi dengan database dan mengambil atau menyimpan data.
            - HTML template
              Berkas HTML Template adalah berkas yang digunakan untuk menghasilkan tampilan HTML yang akan dikirimkan sebagai respons ke client. Dalam berkas ini, Anda dapat menggunakan sintaks template Django untuk menyisipkan data yang diperoleh dari model ke dalam tampilan.
            - HTTP Respone
              Setelah tampilan (views) selesai memproses permintaan dan merender HTML, hasilnya dikirimkan sebagai respons HTTP ke client. Respons ini mungkin berisi HTML, CSS, JavaScript, atau data lain yang diperlukan oleh klien untuk menampilkan halaman web.
            Jadi, dalam rangkaian ini, urls.py mengarahkan permintaan klien ke fungsi tampilan yang sesuai di views.py. Fungsi tampilan ini dapat mengakses model-data dari models.py jika diperlukan dan menggunakan template HTML untuk merender tampilan yang dikirimkan kembali ke klien sebagai respons HTTP. Semua komponen ini berkolaborasi untuk menyajikan halaman web yang diinginkan oleh klien.
        
        *Menggunakan virtual environment 
            Virtual environment digunakan untuk mengisolasi lingkungan pengembangan aplikasi sehingga dependensi dan paket yang digunakan dalam proyek tidak akan berinteraksi dengan proyek lain atau sistem operasi secara global. Dengan virtual environment, maka dapat mengelola paket-paket Python yang diperlukan secara terisolasi untuk setiap proyek, yang membuatnya lebih bersih dan teratur. Tanpa menggunakan virtual environment, akan masih dapat membuat aplikasi web berbasis Django, tetapi dapat menjadi sulit mengelola dependensi dan mungkin menyebabkan konflik jika sedang bekerja pada beberapa proyek yang menggunakan versi paket yang berbeda.
        
        *MVC, MVT, dan MVVM
            
            -MVC (Model-View-Controller): Ini adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama. Model mewakili data dan logika aplikasi, View bertanggung jawab untuk tampilan, dan Controller mengatur interaksi antara Model dan View. Contoh framework yang menggunakan pola ini adalah Ruby on Rails.
            
            -MVT (Model-View-Template): Ini adalah varian dari MVC yang digunakan oleh Django. Model masih bertanggung jawab atas data dan logika bisnis, View menangani tampilan, dan Template berfungsi sebagai bagian yang mengendalikan bagaimana data ditampilkan dalam HTML. Controller dalam MVT digantikan oleh Django Framework itu sendiri.
            
            -MVVM (Model-View-ViewModel): Ini adalah pola desain yang digunakan terutama dalam pengembangan aplikasi berbasis frontend, seperti dengan framework Angular dan Vue.js. Model mewakili data dan logika, View menggambarkan tampilan, dan ViewModel berperan sebagai perantara antara Model dan View, mengatur logika tampilan.

