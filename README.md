# 8 Vezir Problemi

8 satranç veziri, iki vezirin birbirini tehdit etmemesi şartıyla bir satranç tahtasına nasıl yerleştirilir?

(2 vezir aynı sütun, satır veya köşegen üzerinde olmamalıdır)

8 Vezir problemi ilk olarak 1848'de satranç oyuncusu **Max Bezzel** tarafından ileri sürüldü. Gauss ve Georg Cantor gibi birçok matematikçi tarafından da incelendi. İlk çözüm, 1850'de Franz Nauck tarafından önerildi ve aynı zamanda “8 Vezir Problemini” gündeme getirdi.

Her n x n satranç tahtası için maksimum vezir sayısının ne kadar yerleştirilebileceği bilgisine sahibiz. Hiçbiri diğerine saldırmaz, n'ye eşittir. Klasik kombinatoryal problemlerden biri, bir satranç tahtası gibi 8 x 8'lik bir tahtaya sekiz vezir yerleştirme yöntemi olan ve her biri başka bir vezir ile **_çakışmayan_** (**_saldıramayan_**) sekiz vezir problemidir. 8 vezir problemi, vezirler birbirlerine saldırmamaları için _n_ sayıda vezir yerleştirilerek genelleştirildi. En son n = 26 değeri için çözüm bulundu. Çok yüksek hesaplama gücüne gereksinim duyulduğundan n = 27 için çözüm henüz bulunamamıştır.

8 Vezir problemini çözmek için **birden fazla** yöntem gösterilebilir. Bunlardan bazıları Brute Force, Genetik Algoritma, Yokuş Tırmanma, Rastgele Yürüme ve GBF/A yöntemleridir. 8x8’lik bir tabloda 96 farklı çözüm çıkacaktır.

![enter image description here](https://i.ibb.co/MVxk9PM/tahta.png)

Genetik algoritma yönteminde sol üstteki ilk sütundan başlayıp, ardından ikinci sütuna bir vezir yerleştirecek ve ilk sütunda vezirin saldıramayacağı bir yer bulana kadar onu hareket ettirecek recursive (özyinelemeli) bir metod kullanılacaktır.
![enter image description here](https://i.ibb.co/tmV44w3/gorsellestirme.png)

# Single Point Crossover

Ebeveyn dizisinde bir geçiş noktası seçilir. Organizma dizisindeki bu noktanın ötesindeki tüm veriler, iki ebeveyn arasında değiştirilir. Çaprazlama noktaları, _Konumsal Önyargı (Positional Bias)_ ile seçilir. <br>

![enter image description here](https://i.ibb.co/brWzh2M/tekNokta.jpg)
![enter image description here](https://i.ibb.co/6P12bMv/tek-Nokta-2.jpg)
# Two Point Crossover

Bu, N-noktası Çaprazlama tekniğinin özel bir durumudur. Kromozomlar (şeritler) üzerinde rastgele iki nokta seçilir ve bu noktalarda genetik materyal değiştirilir.
<br>
![enter image description here](https://i.ibb.co/hsDxMF9/2Nokta.jpg)
![enter image description here](https://i.ibb.co/XW0c6gg/2Nokta-2.jpg)
## 8 Vezir probleminin Genetik Algoritma ile çözümü

Öncelikle tahta boyutuna göre popülasyon boyutu bulunur. İlk popülasyon rastgele bir şekilde oluşturulur. Ardından, ortaya çıkan kromozom adayları değerlendirilir. Değerlendirme sonrasında bir sonraki jenerasyon için çalışmaya başlanır. Buradaki amaç, mevcut kromozomların arasından en iyi olduğu düşünülenlerin seçilmesidir. Seçim yapıldıktan sonra program başlangıcında kullanıcı girdisine göre önceden belirlenmiş olan tek nokta veya çift nokta çaprazlaması uygulanır. Bu sırada ortaya çıkan yeni çıktılara (çocuk, offspring) **mutasyon** uygulanır. En iyi jenerasyon bulunana (yani satranç tahtasında birbirine saldırabilir konumda olmayan vezirlerin bulunduğu jenerasyon tespit edilene kadar) veya maksimum iterasyon sayısı tamamlanana kadar tekrarlanır.

## Nasıl Kullanılır?

**Programın çalışabilmesi için NumPy kütüphanesi gereklidir. Terminalde** **“pip install numpy”** **komutu kullanarak kurulabilir.** [**Detaylı bilgi NumPy’ın sitesinden alınabilir.**](https://numpy.org/install/)

Program (Script) başlatıldığında tahta boyutu, çaprazlama türü (tek nokta/çift nokta,) mutasyon kullanımı yapılıp yapılmayacağı ve maksimum yapılabilecek iterasyon sayısı sorulacaktır.

Bunlar için **önerilen değerler aşağıdaki gibidir:**

Tahta boyutu: **8**  
Çaprazlama türü: **1**  
Mutasyon kullanımı: **e**  
Maksimum iterasyon: **2000**

Parametreler sistem özelliklerini göz önünde bulundurarak verilmelidir, aksi takdirde işlem çok uzun sürebilir. Örnek olarak tahta boyutu 32 olarak verildiğinde ve iterasyon sayısı yüksek tutulduğunda bilgisayarın işlemi tamamlaması (mevcut kod ile) time complexity bakımından uygulanabilir olamayacaktır.

Ardından program verilmiş olan parametrelere uyarak ilk popülasyonu oluşturarak 8 Vezir problemini çözmeye çalışmaya başlayacaktır.
![enter image description here](https://i.ibb.co/NnrDMcb/8-Vezir-Initial.jpg)
Jenerasyonların Fitness (uygunluk) durumunu her jenerasyonda ekrana basacak ve işlem tamamlandığında:

**Eğer problem maksimum iterasyon sayısına ulaşılmadan çözülebilmişse:**

Birbirine saldırmayan (yani çakışmayan) vezirlerin bulunduğu jenerasyonu ve toplam iterasyon sayısını görüntüleyecektir.

**Eğer problem maksimum iterasyon sayısına ulaşılmadan çözülememişse:**

Toplam yapılan iterasyon sayısını görüntüleyecektir.

Enter tuşu ile programdan çıkabilirsiniz.



https://user-images.githubusercontent.com/105719360/171736613-f979408b-2b46-4079-9372-d757ced8b470.mp4



## Deney ve Sonuçları

Bu çalışmada 2 farklı çeşit teknik ile deney yapılmıştır. Bunlar **Single Point Crossover** (Tek Nokta Çaprazlaması) ve **Two Point Crossover** (Çift Nokta Çaprazlaması) yöntemleridir. Bu iki teknikten hangisinin 8 Vezir problemini genetik algoritmalar ile çözme konusunda daha efektif olduğu saptanmaya çalışılmıştır.

**Deneyin yapıldığı şartlar:**

***8* Tahta Boyutu seçeneği için:**

**CPU**: Intel(R) Core(TM) i5-8300H CPU @ 2.30GHz

**İşletim Sistemi**: Windows 10 Pro 21H2 (Build Numarası 19044.1706)

**İşlemci Mimarisi**: 64-Bit (x86-64)

**Kullanılan Python Sürümü**: Python 3.10

**Python için Ayrılan RAM Miktarı**: 12GB

**NumPy kütüphane sürümü:** numpy-1.22.4-cp310-cp310-win_amd64.whl

<br>

***16* Tahta Boyutu seçeneği için:**

**CPU**: AMD Ryzen 9 5950X 16-Çekirdek CPU @ 3.40GHz

**İşletim Sistemi**: Windows Server 2019

**İşlemci Mimarisi**: 64-Bit (x86-64)

**Kullanılan Python Sürümü**: Python 3.10

**Python için Ayrılan RAM Miktarı**: 3GB

**NumPy kütüphane sürümü:** numpy-1.22.4-cp310-cp310-win_amd64.whl

Tüm testler için maksimum iterasyon değeri 2000 verilmiştir.

Tüm testlerde mutasyon özelliği kullanılmıştır.

![enter image description here](https://i.ibb.co/gyv29KX/8-Vezir-Sonuclar.jpg)


**Sonuç olarak, Tek Nokta Çaprazlama tekniğinin 8 Vezir problemi özelinde daha iyi sonuç verdiği saptanmıştır. Bu sonuca ulaşmak için her bir çaprazlama türünde test en az 5 kere tekrarlanmıştır.**
