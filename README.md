📚 About This Project – Kurallı Cümle Uygulaması
Kurallı Cümle, Türkçeyi öğrenmekte olan bireylerin doğru cümle yapılarını pekiştirmeleri için geliştirilmiş interaktif bir mobil uygulamadır. Bu uygulama, kullanıcıya karışık kelimelerden oluşan bir cümle sunar ve ondan bu kelimeleri doğru sıraya koyarak gramatik olarak kurallı hâle getirmesini bekler.

Uygulama; Kolay, Orta, Zor ve Çok Zor olmak üzere dört farklı zorluk seviyesinde cümleler içerir. Bu seviyeler, sentences.txt dosyasında tanımlanmış ve her bir cümle kendi etiketine göre ayrılmıştır.

🎯 Temel Amaç
Türkçe dil bilgisi ve cümle kurma becerilerini geliştirmek,

Doğru kelime sırasını öğrenmek,

Geri bildirimlerle öğrenmeyi desteklemek.

🧩 Uygulama Özellikleri
Kivy ile geliştirilen çok ekranlı arayüz (ScreenManager kullanılmıştır).

Cümleler rastgele olarak kelimelerine ayrılıp karıştırılır ve / işareti ile ekranda sunulur.

Kullanıcıdan doğru cümleyi elle yazması istenir.

difflib.SequenceMatcher algoritmasıyla yazdığı cümle ile doğru cümle karşılaştırılır ve benzerlik yüzdesi olarak geri bildirim verilir.

Eğer benzerlik oranı %85’in üzerindeyse cümle doğru kabul edilir ve arayüzde yeşil renk ile belirtilir, değilse kırmızı ile uyarılır.

Her zorluk seviyesinin kendine ait bir ekranı ve iş mantığı vardır.

📁 Dosya Yapısı
kuralli_cumle.kv → Kivy arayüz tanımı (.kv dosyası)

sentences.txt → Cümle veri kümesi (her satırda "kolay:", "orta:", "zor:", "çok zor:" etiketi ile başlayan cümleler)

main.py → Uygulamanın mantığını içeren Python dosyası (yukarıda verdiğin kod)

icon.png → Uygulama simgesi (varsayılan ikon dosyası)

⚙️ Zorluk Seviyeleri
Seviye	Açıklama
Kolay	Basit, günlük konuşmalarda geçen kısa cümleler
Orta	Birleşik yapılar ve bağlaçlar içeren cümleler
Zor	Sıfat-fiil, zarf-fiil gibi eklerle karmaşık hâle gelmiş cümleler
Çok Zor	Dil bilgisel olarak sınav düzeyinde, akademik veya uzun yapılara sahip
