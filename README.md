# Yapay-Zekali-Fitness-Antrenoru
Gerçek Zamanlı Yapay Zeka Fitness Antrenörü
 Kullanılan sistem özellikleri tablosu



İşlemci	Hız : 2.6 GHz 6 çekirdekli 4.5 GHz e kadar Turbo Boost ,
İş parçacığı sayısı: 12
Önbellek : 12 MB L3 önbellek
Veri Yolu Hız : 8 GT/s
TDP: 45W


Bellek	Boyut :16 GB
Tip :DDR4
Hız :2667 MHz

Grafik kartı	Tipi :GPU
Veri yolu : PCle
VRAM : 4GB
GPU bellek hızı :1750MHz




Ekran	Parlaklık :500 nit
Yenileme hızı : 60 Hz
Çözünürlük :3072 x 1920
IPS ve True Tone Teknolojisi
Boyut :16 inch



Depolama	Kapasite : 512GB
Dosya Sistemi : APFS
Tipi : SSD
Protokol : PCI- Express

Kamera	Çözünürlük :1280 x 720 piksel
İşletim Sistemi	MacOS Monterey Version 12.3.1





<img width="322" alt="image" src="https://user-images.githubusercontent.com/76569487/191975251-0fc6693c-e7d7-4376-adbf-efbf4b324fa2.png">
Özetle, Mediapipe in pozlama kısmından faydalanarak projemi gerçekleştirdim. Bu pozları sınıflandırarak onlara anlam kazandırdım. Vücudun eklem noktalarına önceden bahsedilen dönüm noktalarına (landmark)ını ekledim. Bunlara belirli kurallar yazarak pozlama ve hareket algılayabilecek döngüler ekledikten sonra geriye pipelineları üzerindeki açılara göre ekrana göstermek gereken kısımlar kaldı.


Programı yaparken kullanılan OpenCV, Mediapipe ve Numpy kütüphanelerden oldukça faydalandım ve kodumun en tepesine ekledim. İlk olarak, OpenCv ile Görüntü adında bir açılacak ekranı belirledim. Bu açılacak ekranın veriyi kameradan mı veya herhangi bir stok videodan ya da resimden mi alacağını belirledim. Denemelerimi yaparken ilk başta insan resimlerinden faydalandım. Bunu belirdikten sonra ikinci bir py uzantılı dosyayı açıp asıl koda import edileceği kısım olan PoseModule ü yazmaya başladım. Fps ayarlarını yapmak için time adlı kütüphaneyi import ettim ve belirli kodlamalarla fps  değerini ekranın sol üst kösesine yazdırdım. İkinci olarak, poseDetector adında bir sınıf oluşturup bunun içine gerekli kodlamaları yaptım. İnsan modelini düzgün çıkarmak için yaptığım ilk adım init fonksiyonu içine Mediapipe kütüphanesindeki pose kaynak kodlarındaki vücut pozlama oranlarını değerlerini self parametresi kullanarak init fonksiyonunun içine yazdım. Bir sonraki adımda ise findPose ve findPosition fonksiyonlarını ekledim. Bu fonksiyonlardan findPose u entegre ettikten sonra işlenen resim ve görüntüye landmarkaları çizmeye başladı. Bu noktaları ekranda gözüktükten sonra bunların arasına çizgi çekmeyi mümkün kılacak kodlamaları gerçekleştirildi


<img width="229" alt="image" src="https://user-images.githubusercontent.com/76569487/191975506-2b9d2171-9710-4936-9444-8c70b8df4528.png">
Şekil.3.1 Landmarkları ve pozisyon çizgileri çizilmiş görüntüsü

Programı yaparken kullanılan OpenCV, Mediapipe ve Numpy kütüphanelerden oldukça faydalandım ve kodumun en tepesine ekledim. İlk olarak, OpenCv ile Görüntü adında bir açılacak ekranı belirledim. Bu açılacak ekranın veriyi kameradan mı veya herhangi bir stok videodan ya da resimden mi alacağını belirledim. Denemelerimi yaparken ilk başta insan resimlerinden faydalandım. Bunu belirdikten sonra ikinci bir py uzantılı dosyayı açıp asıl koda import edileceği kısım olan PoseModule ü yazmaya başladım. Fps ayarlarını yapmak için time adlı kütüphaneyi import ettim ve belirli kodlamalarla fps  değerini ekranın sol üst kösesine yazdırdım. İkinci olarak, poseDetector adında bir sınıf oluşturup bunun içine gerekli kodlamaları yaptım. İnsan modelini düzgün çıkarmak için yaptığım ilk adım init fonksiyonu içine Mediapipe kütüphanesindeki pose kaynak kodlarındaki vücut pozlama oranlarını değerlerini self parametresi kullanarak init fonksiyonunun içine yazdım. Bir sonraki adımda ise findPose ve findPosition fonksiyonlarını ekledim. Bu fonksiyonlardan findPose u entegre ettikten sonra işlenen resim ve görüntüye landmarkaları çizmeye başladı. Bu noktaları ekranda gözüktükten sonra bunların arasına çizgi çekmeyi mümkün kılacak kodlamaları gerçekleştirildi
 
 
 
 <img width="149" alt="image" src="https://user-images.githubusercontent.com/76569487/191975626-3d36095a-0b4b-43e9-aeab-61d2ca87c623.png">  <img width="138" alt="image" src="https://user-images.githubusercontent.com/76569487/191975679-691efd09-8fb5-4692-b366-887f27d48d13.png">
          Şekil.3.2 Landmarkların çıktı değerleri öncesi ve sonrası

Son olarak, devamında ise yukardaki değerleri x y değerlerini x’i genişlikle çarpıp y’yi ise uzunlukla çarptıktan sonra buna kanal diyoruz sonrasında çıktıya landmarkın id si ardından cx değeri ve cy değerini çıktı olarak ekrana bastırıyoruz. Yukardaki resimde 14 numaralı yani sağ dirseğin konum değerlerini görmekteyiz. PoseModule kısmını bu şekilde bitirmiş oluyoruz. 
Programın asıl hareketleri tanımlama kısımlarına geldiğimizde ise ilk başta çalışacağımız çözünürlüğü belirlemek oluyor 1280 x 720 olarak belirledik. Daha önce belirlediğimiz findPose ve findPosition objelerini fitness uygulamasına import ederek çalıştıracağız. Pozu kodumuza ekledikten sonra resimde poz modulunde gördüğümüz gibi görürüz sonrasında da önemli olan kısım bu iki pipiline bir landmark arasında kalacak açıyı aciBul fonksiyonu olarak adlandırdığımız kısmı yazıyoruz. Bu bölümde spesifik olarak hangi landmarkların kullanıldığını göstermiş olacağız. Bu belirlenen kısımları sağ kol için 12, 14, 16  sol kol için 11 , 13 , 15 sağ bacak için ise 24 , 26 , 28 ve sol bacak için 23,  25, 27 numaralandırılmış landmarkların vücut poz modülünde hem renk boyut olarak karışmaması için öne çıkaracak farklı renk ve büyüklük ayarlıyoruz. (Şekil 2.2.3) Ayrışan kısımları da açı ve hareket tanımlarını yaparak bir nevi kenara ayırıyoruz. Sonrasında açı ayarlarını yapmak için Numpy kütüphanesinden birkaç modüle çağırıyoruz. Tanjant kullanarak eğim değerini aldıktan sonra bu bizim açı değerimiz olmuş oluyor. Eklem yerinden oynarken yaptığı açıyı 90’dan küçükse 360 ekleyerek değerini veriyoruz.  Bu işlemin aynısını bacaklardaki diz açısına göre de ayarlıyoruz burada 90’dan küçük olduğu değeri saydırıyoruz ve görüntülerin üzerine gerçek zamanlı olarak ekliyoruz. Yapılan hareketin doğruluk oranlarını belirlemek için açını belirli aralıklarda yüzde oranı veriyoruz. Bu verdiğimiz yüzde ise ekranın sağında bulundan barı dolduruyor ve hareket tamamlandığında rengi değişiyor. Son haline gelmeden birkaç adım önce ekranın sol altına da kaç kez yaptığımızı gösteren sayacı yerleştirdim. Sayaç belirlediğin yon değişkenleri 0 durumundan 1’e giderken sayacı 0.5 arttırıp 1’den 0’a giderken de aynı oranda arttırıyor hareket tamamlandığında ekranın sol altındaki rakam artmış oluyor. Yüzde kısmına geldiğimizde ise per3 adında değişken tanımlıyoruz eğer per3 kısmı 100 ise yon 0 sonrasında per3 kısmı 0 olduğunda yön kısmı 1 olması barın yukarda %100 aşağıda %0 olmasını sağlıyor.

<img width="333" alt="image" src="https://user-images.githubusercontent.com/76569487/191975861-366f1829-4169-4bac-90b6-7de0e3f0d7ef.png">
 Şekil3.3 Çalışan son halinin ekran görüntüsü
 
 Yukardaki resimde dumbell curl hareketini görmekteyiz sol üst köşede fps bulunmakta ve sağ taraftaki yeşil barda %51 oranında hareketin doğru yapıldığını görmekteyiz.
Sadece dumbell curl hareketi değil birçok hareketi de bünyesinde barındırıyor. Bacaktaki lan markları algılayarak yapılan squat hareketi:


<img width="402" alt="image" src="https://user-images.githubusercontent.com/76569487/191975964-75309c08-893c-4c18-845d-0b40b12cd0b0.png">
Şekil.3.4 Squat hareketi



