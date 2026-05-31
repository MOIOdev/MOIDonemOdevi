# Sorumlu Yapay Zeka ve Etik Analiz

Bu projede CDC BRFSS 2024 veri seti kullanılarak metabolik sağlık ve diyabet tahmini yapılmıştır. Modelin amacı, bireyleri kesin olarak “hasta” veya “sağlıklı” şeklinde etiketlemek değil; diyabet açısından risk faktörlerini analiz etmek ve yüksek risk taşıyan grupları belirlemeye yardımcı olmaktır.

## 1. Örnekleme Yanlılığı

BRFSS veri seti anket temelli bir veri setidir. Bu nedenle veriler, ankete katılan kişilerin verdiği cevaplara dayanmaktadır. Bazı grupların ankete katılım oranı daha düşük olabilir. Örneğin düşük gelirli bireyler, teknolojiye erişimi sınırlı kişiler veya belirli yaş grupları veri setinde yeterince temsil edilmemiş olabilir. Bu durum modelin bazı grupları daha az doğru tahmin etmesine yol açabilir.

## 2. Ölçüm Yanlılığı

Veri setindeki bazı değişkenler kişilerin kendi beyanlarına dayanmaktadır. Örneğin kilo, boy, fiziksel aktivite, alkol tüketimi veya genel sağlık durumu gibi bilgiler bireylerin kendileri tarafından bildirilmiştir. Bu tür cevaplarda hatırlama hatası, yanlış beyan veya sosyal olarak kabul edilebilir cevap verme eğilimi olabilir. Bu nedenle model sonuçları tamamen klinik ölçüm gibi değerlendirilmemelidir.

## 3. Tarihsel Yanlılık

Sağlık hizmetlerine erişim, gelir düzeyi, eğitim seviyesi ve yaş gibi faktörler geçmişten gelen toplumsal eşitsizlikleri yansıtabilir. Bu durum modelin sadece biyolojik riskleri değil, aynı zamanda sosyal ve ekonomik eşitsizlikleri de öğrenmesine neden olabilir. Bu nedenle model sonuçları yorumlanırken sağlık eşitsizlikleri dikkate alınmalıdır.

## 4. Hassas Değişkenler

Projede yaş, gelir ve eğitim gibi değişkenler diyabet riskini etkileyebilecek önemli faktörlerdir. Ancak bu değişkenler aynı zamanda hassas veya dolaylı hassas özellikler olarak değerlendirilebilir. Bu yüzden model çıktıları bireyleri etiketlemek veya dışlamak için değil, risk faktörlerini anlamak için kullanılmalıdır.

## 5. Mahremiyet ve Veri Güvenliği

Kullanılan BRFSS veri seti anonimleştirilmiş bir veri setidir. Projede kişisel isim, telefon numarası, adres veya kimlik bilgisi gibi doğrudan kişisel veriler kullanılmamıştır. Bu nedenle bireylerin doğrudan kimliklerinin tespit edilmesi amaçlanmamaktadır.

## 6. Damgalama Riski

Diyabet tahmini yapan modeller, yanlış yorumlandığında bireyleri “hasta”, “sağlıksız” veya “riskli kişi” gibi damgalayabilir. Bu nedenle proje sonuçları kesin tanı olarak değil, yalnızca istatistiksel risk tahmini olarak değerlendirilmelidir. Sağlıkla ilgili kesin kararlar için uzman hekim değerlendirmesi gereklidir.

## 7. Etik Sonuç

Bu proje, diyabet riskini etkileyen faktörleri makine öğrenmesi yöntemleriyle analiz etmeyi amaçlamaktadır. Model çıktıları karar verme sürecine yardımcı olabilir; ancak tek başına tıbbi tanı, tedavi veya bireysel sağlık kararı için kullanılmamalıdır. Proje, sorumlu yapay zeka ilkeleri doğrultusunda mahremiyet, adalet, açıklanabilirlik ve sınırlılık bilinciyle değerlendirilmelidir.
