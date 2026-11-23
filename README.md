# Kalite Kontrol ve Hata Takip Sistemi

Güncel Yazılım Geliştirme Süreçleri ve DevOps dersi kapsamında geliştirilen bireysel web uygulaması.

## Problem ve hedef kullanıcı
Küçük üretim işletmelerinde kalite kontrol sırasında bulunan hatalar dağınık notlarda tutulduğunda takip ve analiz zorlaşabilir. Bu uygulama kalite kontrol personelinin hata kaydı oluşturmasını, üretim sorumlularının hangi hata türlerinin öne çıktığını görmesini sağlar.

## Teknolojiler
- Python
- Streamlit (web arayüzü)
- SQLite (yerel, kalıcı veritabanı)
- Git/GitHub (sürüm kontrolü)
- GitHub Issues ve Projects (iş takibi)

## İlk sürümdeki iki çalışan özellik
1. **Hata kaydı oluşturma (#1):** Ürün adı, hata türü, açıklama ve hata adedi girip kaydedebilirsiniz. Bilgiler SQLite veritabanına yazılır.
2. **Hata analizi (#2):** Kayıtlar hata türlerine göre gruplanır. Grafik ve tabloda tür bazında toplam hata adedi görünür.

İleriki sürüme bırakılan işler: kayıt filtreleme (#3), hata durumunu güncelleme (#4), CSV dışa aktarma (#5).

## Kurulum ve çalıştırma
Bilgisayarda Python 3.10 veya üzeri kurulu olmalıdır.

1. Bu depoyu **Code > Download ZIP** ile indirin ve ZIP'i çıkartın; veya Git ile klonlayın:
   ```bash
   git clone https://github.com/senakatip74/kalite-kontrol-hata-takip.git
   cd kalite-kontrol-hata-takip
   ```
2. Proje klasöründe terminal açıp bağımlılıkları kurun:
   ```bash
   python -m pip install -r requirements.txt
   ```
   Windows'ta `python` komutu çalışmıyorsa `py` komutunu kullanabilirsiniz.
3. Uygulamayı başlatın:
   ```bash
   python -m streamlit run app.py
   ```
4. Açılan tarayıcı sayfasını kullanın (genellikle http://localhost:8501).

**Veriler:** İlk çalıştırmada `data/quality.db` dosyası otomatik oluşturulur. Veriler bilgisayarınızda saklanır; veritabanı GitHub'a gönderilmemelidir.

## İki özelliği nasıl deneyebilirsiniz?
### 1. Hata kaydı oluşturma
- Ürün adı: `Metal Parça A`, hata türü: `Çizik`, açıklama: `Yüzeyde çizik`, hata adedi: `2` girin.
- **Kaydı ekle** düğmesine basın. Başarı mesajını ve kaydı **Kaydedilen hatalar** tablosunda görün.
- Uygulamayı kapatıp tekrar başlatın. Kayıt hâlâ görünmelidir.
- Ürün adını boş bırakıp kayıt yapmayı deneyin: hata mesajı görünmelidir.

### 2. Hata analizi ve grafik
- Yukarıdaki kayda ek olarak `Çizik` türünde **3**, `Ölçü hatası` türünde **4**, `Renk hatası` türünde **1** adet hata kaydı oluşturun.
- **Hata analizi** bölümünde şu toplamları kontrol edin: Çizik = **5**, Ölçü hatası = **4**, Renk hatası = **1**; genel toplam = **10**.
- Yeni kayıt eklediğinizde grafik ve analiz tablosu güncellenmelidir.

## Streamlit Community Cloud üzerinden çalıştırma (Python kurulumu gerektirmez)

1. https://share.streamlit.io/ adresine gidin ve GitHub hesabınızla giriş yapın.
2. **Create app / New app** seçeneğini açın; **Deploy a public app from GitHub** yolunu seçin.
3. Depo: `senakatip74/kalite-kontrol-hata-takip`, dal: `main`, ana dosya: `app.py` olarak ayarlayın.
4. İsteğe bağlı bir uygulama adresi seçip **Deploy** düğmesine basın.
5. Uygulama açılınca yukarıdaki iki özelliği tarayıcıda deneyin.

**Bulut ortamı veri uyarısı:** Uygulama SQLite verilerini çalıştığı sunucudaki yerel dosyada saklar. Bu kayıtlar aynı çalışan örnekte oturumlar arasında görülebilir; ancak Streamlit Cloud sunucusu yeniden başlatılırsa veya yeniden dağıtılırsa **kalıcı olmaları garanti edilmez**. Bu nedenle bulut ortamındaki verileri örnek/test verisi olarak kullanın. Kalıcı bulut depolaması için ileride harici veritabanı gereklidir. Uygulamanın yerel Python kurulumunda SQLite verileri disk üzerinde kalıcıdır.

**Canlı uygulama bağlantısı:** Yayımlandıktan sonra buraya eklenecek.

## Otomatik testler
```bash
python -m unittest discover -s tests -v
```
Testler geçerli kayıt ekleme, kalıcılık, geçersiz girişleri reddetme ve üç farklı hata türünün doğru analizini kapsar.

## Görevler ve pano
- [Görev 1 – Hata kaydı oluşturma](https://github.com/senakatip74/kalite-kontrol-hata-takip/issues/1)
- [Görev 2 – Hata analizi](https://github.com/senakatip74/kalite-kontrol-hata-takip/issues/2)
- [Görev 3 – Filtreleme](https://github.com/senakatip74/kalite-kontrol-hata-takip/issues/3)
- [Görev 4 – Durum güncelleme](https://github.com/senakatip74/kalite-kontrol-hata-takip/issues/4)
- [Görev 5 – CSV indirme](https://github.com/senakatip74/kalite-kontrol-hata-takip/issues/5)

**GitHub Projects pano bağlantısı:** Pano oluşturulup depo ile ilişkilendirildikten sonra buraya eklenecek.

## Geliştirme notu
İş kartlarındaki kabul kriterleri ve kod commit'leri, yazılım geliştirme sürecinin takibi için kullanılmaktadır.
