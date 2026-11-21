# ============================================================
#  Türkçe Akademi – Kengaytirilgan Ma'lumotlar bazasi
# ============================================================

# ============================================================
# MAVZULAR RO'YXATI (Topics)
# ============================================================
TOPICS = {
    "sifatlar": "🎨 Sifatlar (Adjectives)",
    "sonlar": "🔢 Sonlar (Numbers)",
    "ranglar": "🌈 Ranglar (Colors)",
    "oziq_ovqat": "🍎 Oziq-ovqat (Food)",
    "hayvonlar": "🐾 Hayvonlar (Animals)",
    "jism": "🧍 Tana a'zolari (Body)",
    "oila": "👨‍👩‍👧 Oila (Family)",
    "kasb": "💼 Kasblar (Jobs)",
    "transport": "🚗 Transport",
    "shahar": "🏙️ Shahar (City)",
    "tabiat": "🌿 Tabiat (Nature)",
    "vaqt": "⏰ Vaqt (Time)",
    "kunlar": "📆 Kunlar va Oylar",
    "hissiyot": "😊 Hissiyotlar (Feelings)",
    "sport": "⚽ Sport",
    "kiyim": "👕 Kiyim-kechak (Clothes)",
    "uy": "🏠 Uy (Home)",
    "maktab": "🏫 Maktab (School)",
    "salomatlik": "🏥 Salomatlik (Health)",
    "sayohat": "✈️ Sayohat (Travel)",
    "texnologiya": "💻 Texnologiya",
    "taom": "🍽️ Taom atamalari (Meal)",
    "savdo": "🛒 Savdo (Shopping)",
    "tarix": "📜 Turkiya haqida",
}

# ============================================================
# BARCHA SIFATLAR (200+ ta)
# ============================================================
ADJECTIVES = [
    # O'lcham
    {"tr": "Büyük", "uz": "Katta", "category": "o'lcham", "example": "Büyük bir ev – Katta bir uy"},
    {"tr": "Küçük", "uz": "Kichik", "category": "o'lcham", "example": "Küçük bir çocuk – Kichik bir bola"},
    {"tr": "Uzun", "uz": "Uzun", "category": "o'lcham", "example": "Uzun bir yol – Uzun yo'l"},
    {"tr": "Kısa", "uz": "Qisqa", "category": "o'lcham", "example": "Kısa saç – Qisqa soch"},
    {"tr": "Geniş", "uz": "Keng", "category": "o'lcham", "example": "Geniş bir oda – Keng xona"},
    {"tr": "Dar", "uz": "Tor", "category": "o'lcham", "example": "Dar bir sokak – Tor ko'cha"},
    {"tr": "Yüksek", "uz": "Baland", "category": "o'lcham", "example": "Yüksek bir bina – Baland bino"},
    {"tr": "Alçak", "uz": "Past", "category": "o'lcham", "example": "Alçak tavan – Past ship"},
    {"tr": "Derin", "uz": "Chuqur", "category": "o'lcham", "example": "Derin bir göl – Chuqur ko'l"},
    {"tr": "Sığ", "uz": "Sayoz", "category": "o'lcham", "example": "Sığ bir nehir – Sayoz daryo"},
    {"tr": "Kalın", "uz": "Qalin", "category": "o'lcham", "example": "Kalın bir kitap – Qalin kitob"},
    {"tr": "İnce", "uz": "Ingichka", "category": "o'lcham", "example": "İnce bir kağıt – Ingichka qog'oz"},
    {"tr": "Ağır", "uz": "Og'ir", "category": "o'lcham", "example": "Ağır bir çanta – Og'ir sumka"},
    {"tr": "Hafif", "uz": "Yengil", "category": "o'lcham", "example": "Hafif bir kutu – Yengil quti"},

    # Sifat/Ko'rinish
    {"tr": "Güzel", "uz": "Chiroyli", "category": "korinish", "example": "Güzel bir kız – Chiroyli qiz"},
    {"tr": "Çirkin", "uz": "Xunuk", "category": "korinish", "example": "Çirkin hava – Yomon havo"},
    {"tr": "Yakışıklı", "uz": "Kelishgan", "category": "korinish", "example": "Yakışıklı bir adam – Kelishgan erkak"},
    {"tr": "Şık", "uz": "Zamonaviy/Did bilan kiyingan", "category": "korinish", "example": "Şık bir elbise – Zamonaviy ko'ylak"},
    {"tr": "Temiz", "uz": "Toza", "category": "korinish", "example": "Temiz bir ev – Toza uy"},
    {"tr": "Kirli", "uz": "Iflos", "category": "korinish", "example": "Kirli eller – Iflos qo'llar"},
    {"tr": "Düzgün", "uz": "Tartibli", "category": "korinish", "example": "Düzgün saç – Tartibli soch"},
    {"tr": "Dağınık", "uz": "Tartibsiz", "category": "korinish", "example": "Dağınık oda – Tartibsiz xona"},
    {"tr": "Parlak", "uz": "Yaltiroq/Yorqin", "category": "korinish", "example": "Parlak bir yıldız – Yorqin yulduz"},
    {"tr": "Mat", "uz": "Lopsiz", "category": "korinish", "example": "Mat boya – Lopsiz bo'yoq"},

    # His-tuyg'u / Ruhiyat
    {"tr": "Mutlu", "uz": "Xursand", "category": "hissiyot", "example": "Mutlu bir çocuk – Xursand bola"},
    {"tr": "Üzgün", "uz": "Xafa", "category": "hissiyot", "example": "Üzgün bir yüz – Xafa yuz"},
    {"tr": "Kızgın", "uz": "G'azablangan", "category": "hissiyot", "example": "Kızgın bir adam – G'azablangan odam"},
    {"tr": "Sakin", "uz": "Tinch/Sokin", "category": "hissiyot", "example": "Sakin bir kişi – Tinch odam"},
    {"tr": "Heyecanlı", "uz": "Hayajonlangan", "category": "hissiyot", "example": "Heyecanlı bir çocuk – Hayajonlangan bola"},
    {"tr": "Korkmuş", "uz": "Qo'rqqan", "category": "hissiyot", "example": "Korkmuş bir kedi – Qo'rqqan mushuk"},
    {"tr": "Şaşkın", "uz": "Hayron", "category": "hissiyot", "example": "Şaşkın bir ifade – Hayron ifoda"},
    {"tr": "Yorgun", "uz": "Charchagan", "category": "hissiyot", "example": "Yorgun bir işçi – Charchagan ishchi"},
    {"tr": "Enerjik", "uz": "Energiyali", "category": "hissiyot", "example": "Enerjik bir sporcu – Energiyali sportchi"},
    {"tr": "Neşeli", "uz": "Quvnoq", "category": "hissiyot", "example": "Neşeli bir müzik – Quvnoq musiqa"},
    {"tr": "Sıkılmış", "uz": "Zerikkan", "category": "hissiyot", "example": "Sıkılmış görünüyor – Zerikkan ko'rinadi"},
    {"tr": "Meraklı", "uz": "Qiziquvchan", "category": "hissiyot", "example": "Meraklı bir öğrenci – Qiziquvchan o'quvchi"},
    {"tr": "Utangaç", "uz": "Uyatchan", "category": "hissiyot", "example": "Utangaç bir kız – Uyatchan qiz"},
    {"tr": "Cesur", "uz": "Jasur", "category": "hissiyot", "example": "Cesur bir kahraman – Jasur qahramon"},

    # Sifat/Xarakter
    {"tr": "İyi", "uz": "Yaxshi/Mehribon", "category": "xarakter", "example": "İyi bir insan – Yaxshi inson"},
    {"tr": "Kötü", "uz": "Yomon", "category": "xarakter", "example": "Kötü haber – Yomon xabar"},
    {"tr": "Akıllı", "uz": "Aqlli", "category": "xarakter", "example": "Akıllı bir öğrenci – Aqlli o'quvchi"},
    {"tr": "Aptal", "uz": "Ahmoq", "category": "xarakter", "example": "Aptal bir karar – Ahmoqona qaror"},
    {"tr": "Nazik", "uz": "Muloyim/Xushmuomala", "category": "xarakter", "example": "Nazik bir hanım – Muloyim xonim"},
    {"tr": "Kaba", "uz": "Qo'pol", "category": "xarakter", "example": "Kaba bir adam – Qo'pol odam"},
    {"tr": "Dürüst", "uz": "Halol/To'g'ri", "category": "xarakter", "example": "Dürüst bir insan – Halol inson"},
    {"tr": "Yalancı", "uz": "Yolg'onchi", "category": "xarakter", "example": "Yalancı bir kişi – Yolg'onchi odam"},
    {"tr": "Cömert", "uz": "Saxiy", "category": "xarakter", "example": "Cömert bir komşu – Saxiy qo'shni"},
    {"tr": "Cimri", "uz": "Xasis", "category": "xarakter", "example": "Cimri bir adam – Xasis odam"},
    {"tr": "Çalışkan", "uz": "Mehnatsevar", "category": "xarakter", "example": "Çalışkan bir öğrenci – Mehnatsevar o'quvchi"},
    {"tr": "Tembel", "uz": "Dangasa", "category": "xarakter", "example": "Tembel bir kişi – Dangasa odam"},
    {"tr": "Sabırlı", "uz": "Sabr-toqatli", "category": "xarakter", "example": "Sabırlı bir anne – Sabr-toqatli ona"},
    {"tr": "Sabırsız", "uz": "Sabrsiz", "category": "xarakter", "example": "Sabırsız bir müşteri – Sabrsiz mijoz"},
    {"tr": "Güvenilir", "uz": "Ishonchli", "category": "xarakter", "example": "Güvenilir bir dost – Ishonchli do'st"},
    {"tr": "Güvenilmez", "uz": "Ishonchsiz", "category": "xarakter", "example": "Güvenilmez biri – Ishonchsiz biri"},

    # Jismoniy holat
    {"tr": "Sağlıklı", "uz": "Sog'lom", "category": "holat", "example": "Sağlıklı bir insan – Sog'lom inson"},
    {"tr": "Hasta", "uz": "Kasal", "category": "holat", "example": "Hasta bir çocuk – Kasal bola"},
    {"tr": "Güçlü", "uz": "Kuchli", "category": "holat", "example": "Güçlü bir sporcu – Kuchli sportchi"},
    {"tr": "Zayıf", "uz": "Kuchsiz/Ozg'in", "category": "holat", "example": "Zayıf bir ses – Kuchsiz ovoz"},
    {"tr": "Şişman", "uz": "Semiz", "category": "holat", "example": "Şişman bir kedi – Semiz mushuk"},
    {"tr": "Genç", "uz": "Yosh", "category": "holat", "example": "Genç bir adam – Yosh erkak"},
    {"tr": "Yaşlı", "uz": "Keksa", "category": "holat", "example": "Yaşlı bir kadın – Keksa ayol"},
    {"tr": "Aç", "uz": "Och", "category": "holat", "example": "Aç bir çocuk – Och bola"},
    {"tr": "Tok", "uz": "To'q", "category": "holat", "example": "Tok hissediyorum – To'q his qilyapman"},
    {"tr": "Susuz", "uz": "Chanqagan", "category": "holat", "example": "Çok susuz – Juda chanqadim"},

    # Muhit/Havo
    {"tr": "Sıcak", "uz": "Issiq", "category": "muhit", "example": "Sıcak hava – Issiq havo"},
    {"tr": "Soğuk", "uz": "Sovuq", "category": "muhit", "example": "Soğuk bir kış günü – Sovuq qish kuni"},
    {"tr": "Ilık", "uz": "Iliq", "category": "muhit", "example": "Ilık bir bahar günü – Iliq bahor kuni"},
    {"tr": "Yağmurlu", "uz": "Yomg'irli", "category": "muhit", "example": "Yağmurlu bir gün – Yomg'irli kun"},
    {"tr": "Güneşli", "uz": "Quyoshli", "category": "muhit", "example": "Güneşli bir hava – Quyoshli havo"},
    {"tr": "Bulutlu", "uz": "Bulutli", "category": "muhit", "example": "Bulutlu bir gök – Bulutli osmon"},
    {"tr": "Rüzgarlı", "uz": "Shamolли", "category": "muhit", "example": "Rüzgarlı bir gün – Shamolли kun"},
    {"tr": "Karlı", "uz": "Qorli", "category": "muhit", "example": "Karlı dağlar – Qorli tog'lar"},

    # Sifat/Narsa
    {"tr": "Yeni", "uz": "Yangi", "category": "narsa", "example": "Yeni bir araba – Yangi mashina"},
    {"tr": "Eski", "uz": "Eski", "category": "narsa", "example": "Eski bir kitap – Eski kitob"},
    {"tr": "Ucuz", "uz": "Arzon", "category": "narsa", "example": "Ucuz bir ürün – Arzon mahsulot"},
    {"tr": "Pahalı", "uz": "Qimmat", "category": "narsa", "example": "Pahalı bir telefon – Qimmat telefon"},
    {"tr": "Hızlı", "uz": "Tez", "category": "narsa", "example": "Hızlı bir araba – Tez mashina"},
    {"tr": "Yavaş", "uz": "Sekin", "category": "narsa", "example": "Yavaş bir bilgisayar – Sekin kompyuter"},
    {"tr": "Sert", "uz": "Qattiq", "category": "narsa", "example": "Sert bir tahta – Qattiq yog'och"},
    {"tr": "Yumuşak", "uz": "Yumshoq", "category": "narsa", "example": "Yumuşak bir yastık – Yumshoq yostiq"},
    {"tr": "Düz", "uz": "Tekis", "category": "narsa", "example": "Düz bir yol – Tekis yo'l"},
    {"tr": "Eğri", "uz": "Qiyshiq", "category": "narsa", "example": "Eğri bir çizgi – Qiyshiq chiziq"},
    {"tr": "Keskin", "uz": "O'tkir", "category": "narsa", "example": "Keskin bir bıçak – O'tkir pichoq"},
    {"tr": "Künt", "uz": "To'mtoq", "category": "narsa", "example": "Künt bir kalem – To'mtoq qalam"},
    {"tr": "Tatlı", "uz": "Shirin", "category": "narsa", "example": "Tatlı bir meyve – Shirin meva"},
    {"tr": "Acı", "uz": "Achchiq", "category": "narsa", "example": "Acı biber – Achchiq qalampir"},
    {"tr": "Ekşi", "uz": "Nordon", "category": "narsa", "example": "Ekşi limon – Nordon limon"},
    {"tr": "Tuzlu", "uz": "Sho'r", "category": "narsa", "example": "Tuzlu yemek – Sho'r taom"},
    {"tr": "Lezzetli", "uz": "Mazali", "category": "narsa", "example": "Lezzetli bir yemek – Mazali taom"},
    {"tr": "Tatsız", "uz": "Mazasiz", "category": "narsa", "example": "Tatsız çorba – Mazasiz sho'rva"},
    {"tr": "Kokulu", "uz": "Xushbo'y", "category": "narsa", "example": "Kokulu bir gül – Xushbo'y atirgul"},
    {"tr": "Kokuşmuş", "uz": "Hidli/Sasigan", "category": "narsa", "example": "Kokuşmuş balık – Sasigan baliq"},
    {"tr": "Gürültülü", "uz": "Shovqinli", "category": "narsa", "example": "Gürültülü bir şehir – Shovqinli shahar"},
    {"tr": "Sessiz", "uz": "Jim/Sokin", "category": "narsa", "example": "Sessiz bir gece – Jim tun"},

    # Rang/Ko'rinish qo'shimcha
    {"tr": "Renkli", "uz": "Rangli", "category": "rang", "example": "Renkli bir resim – Rangli rasm"},
    {"tr": "Renksiz", "uz": "Rangsiz", "category": "rang", "example": "Renksiz bir hayat – Rangsiz hayot"},
    {"tr": "Açık", "uz": "Och (rang)", "category": "rang", "example": "Açık mavi – Och ko'k"},
    {"tr": "Koyu", "uz": "To'q (rang)", "category": "rang", "example": "Koyu kırmızı – To'q qizil"},

    # Miqdor/Ko'p-oz
    {"tr": "Çok", "uz": "Ko'p", "category": "miqdor", "example": "Çok para – Ko'p pul"},
    {"tr": "Az", "uz": "Kam/Oz", "category": "miqdor", "example": "Az zaman – Oz vaqt"},
    {"tr": "Yeterli", "uz": "Yetarli", "category": "miqdor", "example": "Yeterli para – Yetarli pul"},
    {"tr": "Yetersiz", "uz": "Yetarsiz", "category": "miqdor", "example": "Yetersiz bilgi – Yetarsiz bilim"},
    {"tr": "Tam", "uz": "To'liq/Aynan", "category": "miqdor", "example": "Tam olarak – Aynan shunday"},
    {"tr": "Yarım", "uz": "Yarim", "category": "miqdor", "example": "Yarım ekmek – Yarim non"},
    {"tr": "Boş", "uz": "Bo'sh", "category": "miqdor", "example": "Boş bir oda – Bo'sh xona"},
    {"tr": "Dolu", "uz": "To'la", "category": "miqdor", "example": "Dolu bir bardak – To'la stakan"},
]

# ============================================================
# MAVZU BO'YICHA SO'ZLAR (Topic Words)
# ============================================================
TOPIC_WORDS = {
    "sifatlar": ADJECTIVES,

    "sonlar": [
        {"tr": "Bir", "uz": "1 – Bir", "example": "Bir elma – Bir olma"},
        {"tr": "İki", "uz": "2 – Ikki", "example": "İki çocuk – Ikki bola"},
        {"tr": "Üç", "uz": "3 – Uch", "example": "Üç gün – Uch kun"},
        {"tr": "Dört", "uz": "4 – To'rt", "example": "Dört mevsim – To'rt fasl"},
        {"tr": "Beş", "uz": "5 – Besh", "example": "Beş dakika – Besh daqiqa"},
        {"tr": "Altı", "uz": "6 – Olti", "example": "Altı ay – Olti oy"},
        {"tr": "Yedi", "uz": "7 – Yetti", "example": "Yedi gün – Yetti kun"},
        {"tr": "Sekiz", "uz": "8 – Sakkiz", "example": "Sekiz saat – Sakkiz soat"},
        {"tr": "Dokuz", "uz": "9 – To'qqiz", "example": "Dokuz yıl – To'qqiz yil"},
        {"tr": "On", "uz": "10 – O'n", "example": "On lira – O'n lira"},
        {"tr": "Yirmi", "uz": "20 – Yigirma", "example": "Yirmi kişi – Yigirma kishi"},
        {"tr": "Otuz", "uz": "30 – O'ttiz", "example": "Otuz yaşında – O'ttiz yoshda"},
        {"tr": "Kırk", "uz": "40 – Qirq", "example": "Kırk dakika – Qirq daqiqa"},
        {"tr": "Elli", "uz": "50 – Ellik", "example": "Elli lira – Ellik lira"},
        {"tr": "Altmış", "uz": "60 – Oltmish", "example": "Altmış saniye – Oltmish soniya"},
        {"tr": "Yetmiş", "uz": "70 – Yetmish", "example": "Yetmiş kilo – Yetmish kilo"},
        {"tr": "Seksen", "uz": "80 – Sakson", "example": "Seksen yıl – Sakson yil"},
        {"tr": "Doksan", "uz": "90 – To'qson", "example": "Doksan gram – To'qson gram"},
        {"tr": "Yüz", "uz": "100 – Yuz", "example": "Yüz lira – Yuz lira"},
        {"tr": "Bin", "uz": "1000 – Ming", "example": "Bin kişi – Ming kishi"},
        {"tr": "Birinci", "uz": "Birinchi", "example": "Birinci sıra – Birinchi qator"},
        {"tr": "İkinci", "uz": "Ikkinchi", "example": "İkinci kat – Ikkinchi qavat"},
        {"tr": "Üçüncü", "uz": "Uchinchi", "example": "Üçüncü kapı – Uchinchi eshik"},
        {"tr": "Son", "uz": "Oxirgi", "example": "Son ders – Oxirgi dars"},
    ],

    "ranglar": [
        {"tr": "Kırmızı", "uz": "Qizil", "example": "Kırmızı elma – Qizil olma"},
        {"tr": "Mavi", "uz": "Ko'k", "example": "Mavi gökyüzü – Ko'k osmon"},
        {"tr": "Yeşil", "uz": "Yashil", "example": "Yeşil yaprak – Yashil barg"},
        {"tr": "Sarı", "uz": "Sariq", "example": "Sarı güneş – Sariq quyosh"},
        {"tr": "Beyaz", "uz": "Oq", "example": "Beyaz bulut – Oq bulut"},
        {"tr": "Siyah", "uz": "Qora", "example": "Siyah gece – Qora tun"},
        {"tr": "Turuncu", "uz": "To'q sariq/Apelsin rangi", "example": "Turuncu portakal – To'q sariq apelsin"},
        {"tr": "Mor", "uz": "Binafsha", "example": "Mor çiçek – Binafsha gul"},
        {"tr": "Pembe", "uz": "Pushti", "example": "Pembe elbise – Pushti ko'ylak"},
        {"tr": "Kahverengi", "uz": "Jigarrang", "example": "Kahverengi toprak – Jigarrang tuproq"},
        {"tr": "Gri", "uz": "Kulrang", "example": "Gri bulut – Kulrang bulut"},
        {"tr": "Altın", "uz": "Oltin rang", "example": "Altın renk saç – Oltin rang soch"},
        {"tr": "Gümüş", "uz": "Kumush rang", "example": "Gümüş yüzük – Kumush uzuk"},
        {"tr": "Lacivert", "uz": "To'q ko'k", "example": "Lacivert deniz – To'q ko'k dengiz"},
        {"tr": "Bej", "uz": "Krем rangi", "example": "Bej renkli duvar – Krem rangli devor"},
        {"tr": "Açık mavi", "uz": "Och ko'k", "example": "Açık mavi gökyüzü – Och ko'k osmon"},
        {"tr": "Koyu yeşil", "uz": "To'q yashil", "example": "Koyu yeşil orman – To'q yashil o'rmon"},
    ],

    "oziq_ovqat": [
        {"tr": "Ekmek", "uz": "Non", "example": "Taze ekmek – Yangi non"},
        {"tr": "Et", "uz": "Go'sht", "example": "Koyun eti – Qo'y go'shti"},
        {"tr": "Tavuk", "uz": "Tovuq go'shti", "example": "Tavuk yemeği – Tovuq taomi"},
        {"tr": "Balık", "uz": "Baliq", "example": "Izgara balık – Qovurilgan baliq"},
        {"tr": "Pirinç", "uz": "Guruch", "example": "Pirinç pilavı – Guruch palovi"},
        {"tr": "Makarna", "uz": "Makaron", "example": "Domates soslu makarna – Pomidor sosli makaron"},
        {"tr": "Çorba", "uz": "Sho'rva", "example": "Mercimek çorbası – Yasmiq sho'rvasi"},
        {"tr": "Salata", "uz": "Salat", "example": "Mevsim salatası – Fasl salatasi"},
        {"tr": "Peynir", "uz": "Pishloq", "example": "Beyaz peynir – Oq pishloq"},
        {"tr": "Yoğurt", "uz": "Qatiq", "example": "Türk yoğurdu – Turk qatiği"},
        {"tr": "Yumurta", "uz": "Tuxum", "example": "Haşlanmış yumurta – Qaynatilgan tuxum"},
        {"tr": "Süt", "uz": "Sut", "example": "Taze süt – Yangi sut"},
        {"tr": "Tereyağı", "uz": "Sariyog'", "example": "Tereyağlı ekmek – Sariyog'li non"},
        {"tr": "Bal", "uz": "Asal", "example": "Çiçek balı – Gul asali"},
        {"tr": "Zeytin", "uz": "Zaytun", "example": "Siyah zeytin – Qora zaytun"},
        {"tr": "Domates", "uz": "Pomidor", "example": "Kırmızı domates – Qizil pomidor"},
        {"tr": "Salatalık", "uz": "Bodring", "example": "Taze salatalık – Yangi bodring"},
        {"tr": "Soğan", "uz": "Piyoz", "example": "Kuru soğan – Quruq piyoz"},
        {"tr": "Sarımsak", "uz": "Sarimsoq", "example": "Sarımsak ezmesi – Sarimsoq ezma"},
        {"tr": "Biber", "uz": "Qalampir", "example": "Kırmızı biber – Qizil qalampir"},
        {"tr": "Elma", "uz": "Olma", "example": "Kırmızı elma – Qizil olma"},
        {"tr": "Muz", "uz": "Banan", "example": "Sarı muz – Sariq banan"},
        {"tr": "Portakal", "uz": "Apelsin", "example": "Taze portakal suyu – Yangi apelsin sharbati"},
        {"tr": "Üzüm", "uz": "Uzum", "example": "Siyah üzüm – Qora uzum"},
        {"tr": "Çilek", "uz": "Qulupnay", "example": "Taze çilek – Yangi qulupnay"},
        {"tr": "Karpuz", "uz": "Tarvuz", "example": "Tatlı karpuz – Shirin tarvuz"},
        {"tr": "Kavun", "uz": "Qovun", "example": "Sarı kavun – Sariq qovun"},
        {"tr": "Şeker", "uz": "Shakar", "example": "Beyaz şeker – Oq shakar"},
        {"tr": "Tuz", "uz": "Tuz", "example": "Sofra tuzu – Dasturxon tuzi"},
        {"tr": "Yağ", "uz": "Yog'", "example": "Zeytinyağı – Zaytun yog'i"},
    ],

    "hayvonlar": [
        {"tr": "Kedi", "uz": "Mushuk", "example": "Beyaz kedi – Oq mushuk"},
        {"tr": "Köpek", "uz": "It", "example": "Büyük köpek – Katta it"},
        {"tr": "At", "uz": "Ot", "example": "Hızlı at – Tez ot"},
        {"tr": "İnek", "uz": "Sigir", "example": "Sütlü inek – Sutli sigir"},
        {"tr": "Koyun", "uz": "Qo'y", "example": "Beyaz koyun – Oq qo'y"},
        {"tr": "Keçi", "uz": "Echki", "example": "Dağ keçisi – Tog' echkisi"},
        {"tr": "Tavuk", "uz": "Tovuq", "example": "Çiftlik tavuğu – Ferma tovuği"},
        {"tr": "Horoz", "uz": "Xo'roz", "example": "Sabah horozu – Ertalab xo'rozi"},
        {"tr": "Ördek", "uz": "O'rdak", "example": "Sarı ördek – Sariq o'rdak"},
        {"tr": "Aslan", "uz": "Sher", "example": "Güçlü aslan – Kuchli sher"},
        {"tr": "Kaplan", "uz": "Yo'lbars", "example": "Çizgili kaplan – Chiziqli yo'lbars"},
        {"tr": "Ayı", "uz": "Ayiq", "example": "Kahverengi ayı – Jigarrang ayiq"},
        {"tr": "Kurt", "uz": "Bo'ri", "example": "Gri kurt – Kulrang bo'ri"},
        {"tr": "Tilki", "uz": "Tulki", "example": "Kırmızı tilki – Qizil tulki"},
        {"tr": "Tavşan", "uz": "Quyon", "example": "Beyaz tavşan – Oq quyon"},
        {"tr": "Fare", "uz": "Sichqon", "example": "Küçük fare – Kichik sichqon"},
        {"tr": "Yılan", "uz": "Ilon", "example": "Uzun yılan – Uzun ilon"},
        {"tr": "Kurbağa", "uz": "Qurbaqa", "example": "Yeşil kurbağa – Yashil qurbaqa"},
        {"tr": "Kartal", "uz": "Burgut", "example": "Dağ kartalı – Tog' burguti"},
        {"tr": "Papağan", "uz": "To'ti qush", "example": "Renkli papağan – Rangli to'ti"},
        {"tr": "Balık", "uz": "Baliq", "example": "Deniz balığı – Dengiz balig'i"},
        {"tr": "Yunus", "uz": "Delfin", "example": "Zeki yunus – Aqlli delfin"},
        {"tr": "Fil", "uz": "Fil", "example": "Büyük fil – Katta fil"},
        {"tr": "Zürafa", "uz": "Jirafa", "example": "Uzun boyunlu zürafa – Uzun bo'ynli jirafa"},
        {"tr": "Maymun", "uz": "Maymun", "example": "Şakacı maymun – Hazilkash maymun"},
    ],

    "jism": [
        {"tr": "Baş", "uz": "Bosh", "example": "Başım ağrıyor – Boshim og'riyapti"},
        {"tr": "Yüz", "uz": "Yuz", "example": "Güzel bir yüz – Chiroyli yuz"},
        {"tr": "Göz", "uz": "Ko'z", "example": "Mavi göz – Ko'k ko'z"},
        {"tr": "Kulak", "uz": "Quloq", "example": "Kulağım ağrıyor – Qulog'im og'riyapti"},
        {"tr": "Burun", "uz": "Burun", "example": "Uzun burun – Uzun burun"},
        {"tr": "Ağız", "uz": "Og'iz", "example": "Ağzımı açtım – Og'zimni ochdim"},
        {"tr": "Diş", "uz": "Tish", "example": "Dişim ağrıyor – Tishim og'riyapti"},
        {"tr": "Dil", "uz": "Til", "example": "Türkçe öğreniyorum – Turk tilini o'rganmoqdaman"},
        {"tr": "Boyun", "uz": "Bo'yin", "example": "Uzun boyun – Uzun bo'yin"},
        {"tr": "Omuz", "uz": "Yelka", "example": "Geniş omuzlar – Keng yelkalar"},
        {"tr": "Kol", "uz": "Qo'l (yelkadan)", "example": "Güçlü kollar – Kuchli qo'llar"},
        {"tr": "El", "uz": "Qo'l (kaft)", "example": "Yıkadım ellerimi – Qo'llarimni yuvdim"},
        {"tr": "Parmak", "uz": "Barmoq", "example": "Beş parmak – Besh barmoq"},
        {"tr": "Göğüs", "uz": "Ko'krak", "example": "Göğsüm ağrıyor – Ko'kragim og'riyapti"},
        {"tr": "Karın", "uz": "Qorin", "example": "Karnım acıktı – Qorim ochdi"},
        {"tr": "Sırt", "uz": "Orqa", "example": "Sırtım ağrıyor – Orqam og'riyapti"},
        {"tr": "Bacak", "uz": "Oyoq (son)", "example": "Uzun bacaklar – Uzun oyoqlar"},
        {"tr": "Diz", "uz": "Tizza", "example": "Dizim ağrıyor – Tizzam og'riyapti"},
        {"tr": "Ayak", "uz": "Oyoq (tovon)", "example": "Ayaklarım yoruldu – Oyoqlarim charchadi"},
        {"tr": "Saç", "uz": "Soch", "example": "Uzun saç – Uzun soch"},
        {"tr": "Kaş", "uz": "Qosh", "example": "Kalın kaşlar – Qalin qoshlar"},
        {"tr": "Kirpik", "uz": "Kiprik", "example": "Uzun kirpikler – Uzun kipriklar"},
    ],

    "oila": [
        {"tr": "Anne", "uz": "Ona", "example": "Annem evde – Onam uyda"},
        {"tr": "Baba", "uz": "Ota", "example": "Babam işte – Otam ishda"},
        {"tr": "Abla", "uz": "Opa", "example": "Ablam okuyor – Opam o'qiyapti"},
        {"tr": "Abi / Ağabey", "uz": "Aka", "example": "Ağabeyim büyük – Akam katta"},
        {"tr": "Kardeş", "uz": "Aka/uka/opa/singil", "example": "Kardeşim küçük – Ukam kichik"},
        {"tr": "Erkek kardeş", "uz": "Aka yoki uka", "example": "Erkek kardeşim var – Akam/ukam bor"},
        {"tr": "Kız kardeş", "uz": "Opa yoki singil", "example": "Kız kardeşim var – Opam/singilim bor"},
        {"tr": "Dede", "uz": "Bobo", "example": "Dedem yaşlı – Bobom keksa"},
        {"tr": "Babaanne", "uz": "Buvi (ota tomoni)", "example": "Babaannem güzel – Buvim chiroyli"},
        {"tr": "Nine / Anneanne", "uz": "Buvi (ona tomoni)", "example": "Ninem Türkiye'de – Buvim Turkiyada"},
        {"tr": "Amca", "uz": "Amaki", "example": "Amcam doktor – Amakam shifokor"},
        {"tr": "Hala", "uz": "Hola (ota tomoni)", "example": "Halam öğretmen – Holam o'qituvchi"},
        {"tr": "Dayı", "uz": "Tog'a", "example": "Dayım mühendis – Tog'am muhandis"},
        {"tr": "Teyze", "uz": "Xola (ona tomoni)", "example": "Teyzem İstanbul'da – Xolam Istanbulda"},
        {"tr": "Kuzen", "uz": "Amakivachcha/xolavachcha", "example": "Kuzenimle oynadım – Amakivachcham bilan o'yndim"},
        {"tr": "Eş / Karı-koca", "uz": "Er-xotin", "example": "Eşim çalışıyor – Erim/xotinim ishlayapti"},
        {"tr": "Koca / Erkek", "uz": "Er", "example": "Kocam evde – Erim uyda"},
        {"tr": "Karı / Hanım", "uz": "Xotin", "example": "Hanımım güzel – Xotinim chiroyli"},
        {"tr": "Çocuk", "uz": "Bola", "example": "Çocuğum okula gitti – Bolam maktabga ketdi"},
        {"tr": "Oğul / Oğlan", "uz": "O'g'il", "example": "Oğlum 5 yaşında – O'g'lim 5 yoshda"},
        {"tr": "Kız", "uz": "Qiz (farzand)", "example": "Kızım çok güzel – Qizim juda chiroyli"},
    ],

    "kasb": [
        {"tr": "Doktor", "uz": "Shifokor", "example": "O bir doktordur – U shifokor"},
        {"tr": "Öğretmen", "uz": "O'qituvchi", "example": "O öğretmendir – U o'qituvchi"},
        {"tr": "Mühendis", "uz": "Muhandis", "example": "Bilgisayar mühendisi – Kompyuter muhandisi"},
        {"tr": "Avukat", "uz": "Advokat", "example": "İyi bir avukat – Yaxshi advokat"},
        {"tr": "Hemşire", "uz": "Hamshira", "example": "Hemşire hastanede çalışıyor – Hamshira kasalxonada ishlaydi"},
        {"tr": "Polis", "uz": "Politsiya", "example": "Polis geldi – Politsiya keldi"},
        {"tr": "İtfaiyeci", "uz": "O't o'chiruvchi", "example": "İtfaiyeci yangını söndürdü – O't o'chiruvchi yong'inni o'chirdi"},
        {"tr": "Şoför", "uz": "Haydovchi", "example": "Taksi şoförü – Taksi haydovchisi"},
        {"tr": "Aşçı", "uz": "Oshpaz", "example": "Restoran aşçısı – Restoran oshpazi"},
        {"tr": "Garson", "uz": "Ofitsiant", "example": "Garson yemek getirdi – Ofitsiant taom keltirdi"},
        {"tr": "Kasap", "uz": "Qassob", "example": "Mahalle kasabı – Mahalla qassobi"},
        {"tr": "Fırıncı", "uz": "Novvoy", "example": "Sabah fırıncı – Ertalab novvoy"},
        {"tr": "Terzi", "uz": "Tikuvchi", "example": "Elbise terzisi – Ko'ylak tikuvchisi"},
        {"tr": "Berber", "uz": "Sartarosh", "example": "Berbere gittim – Sartaroshga bordim"},
        {"tr": "Mimar", "uz": "Arxitektor", "example": "Ünlü mimar – Mashhur arxitektor"},
        {"tr": "Ressam", "uz": "Rassom", "example": "Yetenekli ressam – Iqtidorli rassom"},
        {"tr": "Müzisyen", "uz": "Musiqachi", "example": "Türk müzisyen – Turk musiqachisi"},
        {"tr": "Oyuncu", "uz": "Aktyor", "example": "Türk oyuncu – Turk aktyori"},
        {"tr": "Gazeteci", "uz": "Jurnalist", "example": "Televizyon gazetecisi – Televiziya jurnalisti"},
        {"tr": "Çiftçi", "uz": "Dehqon", "example": "Köy çiftçisi – Qishloq dehqoni"},
        {"tr": "Asker", "uz": "Askar", "example": "Türk askeri – Turk askari"},
        {"tr": "Pilot", "uz": "Pilot", "example": "Uçak pilotu – Samolyot piloti"},
        {"tr": "Kaptan", "uz": "Kapitan", "example": "Gemi kaptanı – Kema kapitani"},
    ],

    "transport": [
        {"tr": "Araba", "uz": "Mashina", "example": "Yeni araba – Yangi mashina"},
        {"tr": "Otobüs", "uz": "Avtobus", "example": "Şehir otobüsü – Shahar avtobusi"},
        {"tr": "Metro", "uz": "Metro", "example": "İstanbul metrosu – Istanbul metrosi"},
        {"tr": "Tramvay", "uz": "Tramvay", "example": "Tramvaya bindim – Tramvayga chiqdim"},
        {"tr": "Tren", "uz": "Poyezd", "example": "Hızlı tren – Tez poyezd"},
        {"tr": "Uçak", "uz": "Samolyot", "example": "Uçakla gidiyorum – Samolyot bilan ketyapman"},
        {"tr": "Gemi", "uz": "Kema", "example": "Yolcu gemisi – Yo'lovchi kemasi"},
        {"tr": "Vapur", "uz": "Parom", "example": "Boğaz vapuru – Bo'g'oz paromi"},
        {"tr": "Bisiklet", "uz": "Velosiped", "example": "Kırmızı bisiklet – Qizil velosiped"},
        {"tr": "Motosiklet", "uz": "Mototsikl", "example": "Hızlı motosiklet – Tez mototsikl"},
        {"tr": "Kamyon", "uz": "Yuk mashinasi", "example": "Büyük kamyon – Katta yuk mashinasi"},
        {"tr": "Ambulans", "uz": "Tez yordam mashinasi", "example": "Ambulans geliyor – Tez yordam kelayapti"},
        {"tr": "İtfaiye", "uz": "O't o'chiruvchi", "example": "İtfaiye arabası – O't o'chiruvchi mashinasi"},
        {"tr": "Taksi", "uz": "Taksi", "example": "Sarı taksi – Sariq taksi"},
        {"tr": "Dolmuş", "uz": "Marshrutka", "example": "Dolmuşa bindim – Marshrutkaga chiqdim"},
        {"tr": "Helikopter", "uz": "Vertolyot", "example": "Askeri helikopter – Harbiy vertolyot"},
    ],

    "shahar": [
        {"tr": "Şehir", "uz": "Shahar", "example": "Büyük şehir – Katta shahar"},
        {"tr": "Köy", "uz": "Qishloq", "example": "Küçük köy – Kichik qishloq"},
        {"tr": "Mahalle", "uz": "Mahalla", "example": "Güzel mahalle – Chiroyli mahalla"},
        {"tr": "Sokak", "uz": "Ko'cha", "example": "Dar sokak – Tor ko'cha"},
        {"tr": "Cadde", "uz": "Katta ko'cha", "example": "Geniş cadde – Keng katta ko'cha"},
        {"tr": "Meydan", "uz": "Maydon", "example": "Taksim Meydanı – Taksim maydoni"},
        {"tr": "Park", "uz": "Park", "example": "Şehir parkı – Shahar parki"},
        {"tr": "Köprü", "uz": "Ko'prik", "example": "Boğaz köprüsü – Bo'g'oz ko'prigi"},
        {"tr": "Hastane", "uz": "Kasalxona", "example": "Devlet hastanesi – Davlat kasalxonasi"},
        {"tr": "Okul", "uz": "Maktab", "example": "İlkokul – Boshlang'ich maktab"},
        {"tr": "Üniversite", "uz": "Universitet", "example": "İstanbul Üniversitesi – Istanbul Universiteti"},
        {"tr": "Kütüphane", "uz": "Kutubxona", "example": "Şehir kütüphanesi – Shahar kutubxonasi"},
        {"tr": "Müze", "uz": "Muzey", "example": "Tarih müzesi – Tarix muzeyi"},
        {"tr": "Cami", "uz": "Masjid", "example": "Sultanahmet Camii – Sultanahmet masjidi"},
        {"tr": "Kilise", "uz": "Cherkov", "example": "Tarihi kilise – Tarixiy cherkov"},
        {"tr": "Market", "uz": "Do'kon/Supermarket", "example": "Büyük market – Katta supermarket"},
        {"tr": "Restoran", "uz": "Restoran", "example": "Türk restoranı – Turk restoroni"},
        {"tr": "Otel", "uz": "Mehmonxona", "example": "5 yıldızlı otel – 5 yulduzli mehmonxona"},
        {"tr": "Havalimanı", "uz": "Aeroport", "example": "İstanbul Havalimanı – Istanbul aeroporti"},
        {"tr": "Liman", "uz": "Port", "example": "Deniz limanı – Dengiz porti"},
        {"tr": "İstasyon", "uz": "Vokzal/Stansiya", "example": "Tren istasyonu – Poyezd vokzali"},
        {"tr": "Banka", "uz": "Bank", "example": "Merkez bankası – Markaziy bank"},
        {"tr": "PTT", "uz": "Pochta", "example": "PTT şubesi – Pochta bo'limi"},
        {"tr": "Eczane", "uz": "Dorixona", "example": "Nöbetçi eczane – Navbatchi dorixona"},
        {"tr": "Benzin istasyonu", "uz": "Benzin quyish", "example": "Benzin istasyonuna uğradım – Benzin quyishga kirdim"},
    ],

    "tabiat": [
        {"tr": "Dağ", "uz": "Tog'", "example": "Kar dağları – Qorli tog'lar"},
        {"tr": "Deniz", "uz": "Dengiz", "example": "Mavi deniz – Ko'k dengiz"},
        {"tr": "Göl", "uz": "Ko'l", "example": "Derin göl – Chuqur ko'l"},
        {"tr": "Nehir", "uz": "Daryo", "example": "Uzun nehir – Uzun daryo"},
        {"tr": "Orman", "uz": "O'rmon", "example": "Yeşil orman – Yashil o'rmon"},
        {"tr": "Çöl", "uz": "Cho'l", "example": "Sıcak çöl – Issiq cho'l"},
        {"tr": "Vadi", "uz": "Vodiy", "example": "Geniş vadi – Keng vodiy"},
        {"tr": "Şelale", "uz": "Sharshara", "example": "Güzel şelale – Chiroyli sharshara"},
        {"tr": "Mağara", "uz": "G'or", "example": "Derin mağara – Chuqur g'or"},
        {"tr": "Ada", "uz": "Orol", "example": "Küçük ada – Kichik orol"},
        {"tr": "Sahil", "uz": "Qirg'oq", "example": "Kumlu sahil – Qumli qirg'oq"},
        {"tr": "Kum", "uz": "Qum", "example": "Sarı kum – Sariq qum"},
        {"tr": "Taş", "uz": "Tosh", "example": "Büyük taş – Katta tosh"},
        {"tr": "Toprak", "uz": "Tuproq", "example": "Verimli toprak – Unumdor tuproq"},
        {"tr": "Ağaç", "uz": "Daraxt", "example": "Büyük ağaç – Katta daraxt"},
        {"tr": "Çiçek", "uz": "Gul", "example": "Renkli çiçekler – Rangli gullar"},
        {"tr": "Yaprak", "uz": "Barg", "example": "Yeşil yaprak – Yashil barg"},
        {"tr": "Çimen", "uz": "O't/Maysazor", "example": "Yeşil çimen – Yashil maysazor"},
        {"tr": "Güneş", "uz": "Quyosh", "example": "Parlak güneş – Yorqin quyosh"},
        {"tr": "Ay", "uz": "Oy", "example": "Dolunay – To'lin oy"},
        {"tr": "Yıldız", "uz": "Yulduz", "example": "Parlak yıldız – Yorqin yulduz"},
        {"tr": "Bulut", "uz": "Bulut", "example": "Beyaz bulut – Oq bulut"},
        {"tr": "Yağmur", "uz": "Yomg'ir", "example": "Yağmur yağıyor – Yomg'ir yog'yapti"},
        {"tr": "Kar", "uz": "Qor", "example": "Beyaz kar – Oq qor"},
        {"tr": "Rüzgar", "uz": "Shamol", "example": "Sert rüzgar – Kuchli shamol"},
        {"tr": "Fırtına", "uz": "Bo'ron", "example": "Güçlü fırtına – Kuchli bo'ron"},
        {"tr": "Şimşek", "uz": "Chaqmoq", "example": "Parlak şimşek – Yorqin chaqmoq"},
        {"tr": "Gökkuşağı", "uz": "Kamalak", "example": "Renkli gökkuşağı – Rangli kamalak"},
    ],

    "vaqt": [
        {"tr": "Şimdi", "uz": "Hozir", "example": "Şimdi gidiyorum – Hozir ketyapman"},
        {"tr": "Sonra", "uz": "Keyin", "example": "Sonra görüşürüz – Keyin ko'rishamiz"},
        {"tr": "Önce", "uz": "Avval/Oldin", "example": "Önce ye, sonra çalış – Avval ye, keyin ishlа"},
        {"tr": "Bugün", "uz": "Bugun", "example": "Bugün hava güzel – Bugun havo yaxshi"},
        {"tr": "Yarın", "uz": "Ertaga", "example": "Yarın geleceğim – Ertaga kelaman"},
        {"tr": "Dün", "uz": "Kecha", "example": "Dün geldim – Kecha keldim"},
        {"tr": "Sabah", "uz": "Ertalab", "example": "Sabah erken kalktım – Ertalab erta turдim"},
        {"tr": "Öğle", "uz": "Tush payt", "example": "Öğle yemeği – Tushlik"},
        {"tr": "Akşam", "uz": "Kechqurun", "example": "Akşam yemeği – Kechki ovqat"},
        {"tr": "Gece", "uz": "Tun", "example": "Gece geç kaldım – Tunda kech qoldim"},
        {"tr": "Hafta", "uz": "Hafta", "example": "Bu hafta – Bu hafta"},
        {"tr": "Ay", "uz": "Oy", "example": "Bu ay – Bu oy"},
        {"tr": "Yıl", "uz": "Yil", "example": "Bu yıl – Bu yil"},
        {"tr": "Saat", "uz": "Soat", "example": "Saat kaç? – Soat necha?"},
        {"tr": "Dakika", "uz": "Daqiqa", "example": "On dakika – O'n daqiqa"},
        {"tr": "Saniye", "uz": "Soniya", "example": "Birkaç saniye – Bir necha soniya"},
        {"tr": "Erken", "uz": "Erta", "example": "Erken geldim – Erta keldim"},
        {"tr": "Geç", "uz": "Kech", "example": "Geç kaldım – Kechiktim"},
        {"tr": "Hemen", "uz": "Hoziroq/Darhol", "example": "Hemen gel! – Hoziroq kel!"},
        {"tr": "Yavaş yavaş", "uz": "Asta-sekin", "example": "Yavaş yavaş öğreniyor – Asta-sekin o'rganmoqda"},
    ],

    "kunlar": [
        {"tr": "Pazartesi", "uz": "Dushanba", "example": "Pazartesi okul var – Dushanba maktab bor"},
        {"tr": "Salı", "uz": "Seshanba", "example": "Salı toplantı – Seshanba yig'ilish"},
        {"tr": "Çarşamba", "uz": "Chorshanba", "example": "Çarşamba pazarı – Chorshanba bozori"},
        {"tr": "Perşembe", "uz": "Payshanba", "example": "Perşembe dersi – Payshanba darsi"},
        {"tr": "Cuma", "uz": "Juma", "example": "Cuma namazı – Juma namozi"},
        {"tr": "Cumartesi", "uz": "Shanba", "example": "Cumartesi tatil – Shanba dam olish"},
        {"tr": "Pazar", "uz": "Yakshanba", "example": "Pazar güzel – Yakshanba yaxshi"},
        {"tr": "Ocak", "uz": "Yanvar", "example": "Ocak ayı – Yanvar oyi"},
        {"tr": "Şubat", "uz": "Fevral", "example": "Şubat soğuk – Fevral sovuq"},
        {"tr": "Mart", "uz": "Mart", "example": "Mart baharı – Mart bahori"},
        {"tr": "Nisan", "uz": "Aprel", "example": "Nisan yağmuru – Aprel yomg'iri"},
        {"tr": "Mayıs", "uz": "May", "example": "Mayıs çiçekleri – May gullari"},
        {"tr": "Haziran", "uz": "Iyun", "example": "Haziran sıcağı – Iyun issiqi"},
        {"tr": "Temmuz", "uz": "Iyul", "example": "Temmuz tatili – Iyul ta'tili"},
        {"tr": "Ağustos", "uz": "Avgust", "example": "Ağustos güneşi – Avgust quyoshi"},
        {"tr": "Eylül", "uz": "Sentabr", "example": "Eylül okul – Sentabr maktab"},
        {"tr": "Ekim", "uz": "Oktabr", "example": "Ekim yaprakları – Oktabr barglari"},
        {"tr": "Kasım", "uz": "Noyabr", "example": "Kasım yağmuru – Noyabr yomg'iri"},
        {"tr": "Aralık", "uz": "Dekabr", "example": "Aralık karı – Dekabr qori"},
        {"tr": "İlkbahar", "uz": "Bahor", "example": "Güzel ilkbahar – Chiroyli bahor"},
        {"tr": "Yaz", "uz": "Yoz", "example": "Sıcak yaz – Issiq yoz"},
        {"tr": "Sonbahar", "uz": "Kuz", "example": "Renkli sonbahar – Rangli kuz"},
        {"tr": "Kış", "uz": "Qish", "example": "Soğuk kış – Sovuq qish"},
    ],

    "hissiyot": [
        {"tr": "Mutluluk", "uz": "Baxt/Xursandlik", "example": "Büyük mutluluk – Katta baxt"},
        {"tr": "Üzüntü", "uz": "G'am/Qayg'u", "example": "Derin üzüntü – Chuqur qayg'u"},
        {"tr": "Öfke", "uz": "G'azab", "example": "Öfkemi kontrol edemedim – G'azabimni tiya olmadim"},
        {"tr": "Korku", "uz": "Qo'rquv", "example": "Büyük korku – Katta qo'rquv"},
        {"tr": "Şaşkınlık", "uz": "Hayronlik", "example": "Büyük şaşkınlık – Katta hayronlik"},
        {"tr": "Heyecan", "uz": "Hayajon", "example": "Büyük heyecan – Katta hayajon"},
        {"tr": "Sevinç", "uz": "Quvonch", "example": "Sevinç gözyaşları – Quvonch ko'z yoshlari"},
        {"tr": "Nefret", "uz": "Nafrat", "example": "Nefret duygusu – Nafrat hissi"},
        {"tr": "Sevgi", "uz": "Sevgi/Muhabbat", "example": "Sonsuz sevgi – Cheksiz sevgi"},
        {"tr": "Kıskançlık", "uz": "Hasad/Rashk", "example": "Kıskançlık duygusu – Rashk hissi"},
        {"tr": "Gurur", "uz": "Faxr/G'urur", "example": "Gurur duyuyorum – Faxrlanmoqdaman"},
        {"tr": "Utanç", "uz": "Uyat", "example": "Utanç duydum – Uyat his qildim"},
        {"tr": "Umut", "uz": "Umid", "example": "Büyük umut – Katta umid"},
        {"tr": "Hayal kırıklığı", "uz": "Umidsizlik", "example": "Büyük hayal kırıklığı – Katta umidsizlik"},
        {"tr": "Huzur", "uz": "Tinchlik/Farovonlik", "example": "İç huzuru – Ichki tinchlik"},
        {"tr": "Stres", "uz": "Stress", "example": "Çok stres – Juda stress"},
        {"tr": "Endişe", "uz": "Tashvish", "example": "Büyük endişe – Katta tashvish"},
        {"tr": "Merak", "uz": "Qiziqish", "example": "Büyük merak – Katta qiziqish"},
    ],

    "sport": [
        {"tr": "Futbol", "uz": "Futbol", "example": "Futbol oynuyorum – Futbol o'ynayapman"},
        {"tr": "Basketbol", "uz": "Basketbol", "example": "Basketbol maçı – Basketbol o'yini"},
        {"tr": "Voleybol", "uz": "Voleybol", "example": "Voleybol takımı – Voleybol jamoasi"},
        {"tr": "Yüzme", "uz": "Suzish", "example": "Yüzme havuzu – Suzish havzasi"},
        {"tr": "Koşu", "uz": "Yugurish", "example": "Sabah koşusu – Ertalab yugurish"},
        {"tr": "Bisiklet", "uz": "Velosiped", "example": "Bisiklet sürmek – Velosiped haydash"},
        {"tr": "Güreş", "uz": "Kurash", "example": "Türk güreşi – Turk kurashi"},
        {"tr": "Boks", "uz": "Boks", "example": "Boks maçı – Boks musobaqasi"},
        {"tr": "Tenis", "uz": "Tennis", "example": "Tenis oynamak – Tennis o'ynash"},
        {"tr": "Golf", "uz": "Golf", "example": "Golf sahası – Golf maydoni"},
        {"tr": "Kayak", "uz": "Chang'i", "example": "Kayak yapmak – Chang'i uchish"},
        {"tr": "Dağcılık", "uz": "Tog' tirmashish", "example": "Dağcılık sporu – Tog' tirmashish sporti"},
        {"tr": "Okçuluk", "uz": "Kamondan otish", "example": "Türk okçuluğu – Turk kamonchiligi"},
        {"tr": "Halter", "uz": "Og'ir atletika", "example": "Halter sporu – Og'ir atletika"},
        {"tr": "Jimnastik", "uz": "Gimnastika", "example": "Artistik jimnastik – Badiiy gimnastika"},
        {"tr": "Sporcu", "uz": "Sportchi", "example": "Milli sporcu – Milliy sportchi"},
        {"tr": "Antrenör", "uz": "Murabbiy", "example": "Futbol antrenörü – Futbol murabbiysi"},
        {"tr": "Şampiyon", "uz": "Chempion", "example": "Dünya şampiyonu – Jahon chempioni"},
        {"tr": "Turnuva", "uz": "Turnir", "example": "Futbol turnuvası – Futbol turniri"},
        {"tr": "Kupa", "uz": "Kubok", "example": "Dünya Kupası – Jahon kubogi"},
    ],

    "kiyim": [
        {"tr": "Gömlek", "uz": "Ko'ylak (erkak)", "example": "Beyaz gömlek – Oq ko'ylak"},
        {"tr": "Elbise", "uz": "Ko'ylak (ayol)", "example": "Güzel elbise – Chiroyli ko'ylak"},
        {"tr": "Pantolon", "uz": "Shim", "example": "Kot pantolon – Jinsi shim"},
        {"tr": "Şort", "uz": "Shim (qisqa)", "example": "Yaz şortu – Yoz shimlari"},
        {"tr": "Etek", "uz": "Yubka", "example": "Uzun etek – Uzun yubka"},
        {"tr": "Ceket", "uz": "Jeket", "example": "Spor ceket – Sport jeket"},
        {"tr": "Mont", "uz": "Palto", "example": "Kış montu – Qish palto"},
        {"tr": "Kazak", "uz": "Sviter", "example": "Yün kazak – Jun sviter"},
        {"tr": "Sweatshirt", "uz": "Tellashka/Hudi", "example": "Renkli sweatshirt – Rangli tellashka"},
        {"tr": "Ayakkabı", "uz": "Oyoq kiyim", "example": "Deri ayakkabı – Charm oyoq kiyim"},
        {"tr": "Bot", "uz": "Etik", "example": "Kış botu – Qish etigi"},
        {"tr": "Terlik", "uz": "Shippak", "example": "Ev terliği – Uy shippagi"},
        {"tr": "Çorap", "uz": "Paypoq", "example": "Beyaz çorap – Oq paypoq"},
        {"tr": "İç çamaşırı", "uz": "Ichki kiyim", "example": "Pamuklu iç çamaşırı – Paxta ichki kiyim"},
        {"tr": "Şapka", "uz": "Shapka/Qalpoq", "example": "Kış şapkası – Qish qalpoqi"},
        {"tr": "Eldiven", "uz": "Qo'lqop", "example": "Kış eldiveni – Qish qo'lqopi"},
        {"tr": "Atkı / Fular", "uz": "Ro'mol/Sharf", "example": "Yün atkı – Jun sharf"},
        {"tr": "Kravat", "uz": "Galstuk", "example": "Resmi kravat – Rasmiy galstuk"},
        {"tr": "Kemer", "uz": "Kamar bog'i", "example": "Deri kemer – Charm kamar"},
        {"tr": "Çanta", "uz": "Sumka", "example": "Deri çanta – Charm sumka"},
        {"tr": "Gözlük", "uz": "Ko'zoynak", "example": "Güneş gözlüğü – Quyosh ko'zoynagi"},
        {"tr": "Yüzük", "uz": "Uzuk", "example": "Altın yüzük – Oltin uzuk"},
        {"tr": "Kolye", "uz": "Marjon", "example": "Gümüş kolye – Kumush marjon"},
        {"tr": "Bileklik", "uz": "Bilaguzuk", "example": "Deri bileklik – Charm bilaguzuk"},
    ],

    "uy": [
        {"tr": "Ev", "uz": "Uy", "example": "Büyük ev – Katta uy"},
        {"tr": "Daire", "uz": "Kvartira", "example": "Üç odalı daire – Uch xonali kvartira"},
        {"tr": "Villa", "uz": "Villa", "example": "Deniz kenarı villası – Dengiz bo'yidagi villa"},
        {"tr": "Oda", "uz": "Xona", "example": "Büyük oda – Katta xona"},
        {"tr": "Salon", "uz": "Mehmonxona", "example": "Geniş salon – Keng mehmonxona"},
        {"tr": "Mutfak", "uz": "Oshxona", "example": "Modern mutfak – Zamonaviy oshxona"},
        {"tr": "Banyo", "uz": "Vanna xona", "example": "Temiz banyo – Toza vanna xona"},
        {"tr": "Tuvalet", "uz": "Hojatxona", "example": "Küçük tuvalet – Kichik hojatxona"},
        {"tr": "Yatak odası", "uz": "Yotoq xona", "example": "Rahat yatak odası – Qulay yotoq xona"},
        {"tr": "Balkon", "uz": "Balkon", "example": "Geniş balkon – Keng balkon"},
        {"tr": "Kapı", "uz": "Eshik", "example": "Ahşap kapı – Yog'och eshik"},
        {"tr": "Pencere", "uz": "Deraza", "example": "Büyük pencere – Katta deraza"},
        {"tr": "Merdiven", "uz": "Zinа", "example": "Ahşap merdiven – Yog'och zina"},
        {"tr": "Asansör", "uz": "Lift", "example": "Asansörle çıktım – Lift bilan chiqdim"},
        {"tr": "Kanepe", "uz": "Divan/Kreslolar", "example": "Rahat kanepe – Qulay divan"},
        {"tr": "Masa", "uz": "Stol", "example": "Ahşap masa – Yog'och stol"},
        {"tr": "Sandalye", "uz": "Stul", "example": "Ahşap sandalye – Yog'och stul"},
        {"tr": "Yatak", "uz": "Karavot", "example": "Büyük yatak – Katta karavot"},
        {"tr": "Dolap", "uz": "Shkaf", "example": "Büyük dolap – Katta shkaf"},
        {"tr": "Buzdolabı", "uz": "Muzlatgich", "example": "Büyük buzdolabı – Katta muzlatgich"},
        {"tr": "Fırın", "uz": "Pech/Duxovka", "example": "Elektrikli fırın – Elektr duxovkasi"},
        {"tr": "Çamaşır makinesi", "uz": "Kir yuvish mashinasi", "example": "Otomatik çamaşır makinesi – Avtomatik kir yuvish"},
        {"tr": "Televizyon", "uz": "Televizor", "example": "Büyük ekranlı TV – Katta ekranli TV"},
        {"tr": "Klima", "uz": "Konditsioner", "example": "Klimayı açtım – Konditsionerni yoqdim"},
    ],

    "maktab": [
        {"tr": "Okul", "uz": "Maktab", "example": "İlkokul – Boshlang'ich maktab"},
        {"tr": "Sınıf", "uz": "Sinf", "example": "5. sınıf – 5-sinf"},
        {"tr": "Öğretmen", "uz": "O'qituvchi", "example": "Matematik öğretmeni – Matematika o'qituvchisi"},
        {"tr": "Öğrenci", "uz": "O'quvchi", "example": "İyi öğrenci – Yaxshi o'quvchi"},
        {"tr": "Ders", "uz": "Dars", "example": "Türkçe dersi – Turkcha darsi"},
        {"tr": "Kitap", "uz": "Kitob", "example": "Ders kitabı – Darslik"},
        {"tr": "Defter", "uz": "Daftar", "example": "Yeni defter – Yangi daftar"},
        {"tr": "Kalem", "uz": "Qalam", "example": "Kurşun kalem – Oddiy qalam"},
        {"tr": "Silgi", "uz": "O'chirg'ich", "example": "Beyaz silgi – Oq o'chirg'ich"},
        {"tr": "Cetvel", "uz": "Chizg'ich", "example": "Plastik cetvel – Plastik chizg'ich"},
        {"tr": "Çanta", "uz": "Sumka", "example": "Okul çantası – Maktab sumkasi"},
        {"tr": "Tahta", "uz": "Doskа", "example": "Beyaz tahta – Oq doska"},
        {"tr": "Ödev", "uz": "Uy vazifasi", "example": "Ödevimi yaptım – Uy vazifamni qildim"},
        {"tr": "Sınav", "uz": "Imtihon", "example": "Zor sınav – Qiyin imtihon"},
        {"tr": "Not", "uz": "Baho", "example": "Yüksek not – Yuqori baho"},
        {"tr": "Tatil", "uz": "Ta'til", "example": "Yaz tatili – Yozgi ta'til"},
        {"tr": "Kütüphane", "uz": "Kutubxona", "example": "Okul kütüphanesi – Maktab kutubxonasi"},
        {"tr": "Kantin", "uz": "Bufet/Oshxona", "example": "Okul kantini – Maktab bufeti"},
        {"tr": "Spor salonu", "uz": "Sport zali", "example": "Okul spor salonu – Maktab sport zali"},
        {"tr": "Matematik", "uz": "Matematika", "example": "Matematik dersi – Matematika darsi"},
        {"tr": "Türkçe", "uz": "Turkcha", "example": "Türkçe öğreniyorum – Turkcha o'rganmoqdaman"},
        {"tr": "İngilizce", "uz": "Inglizcha", "example": "İngilizce biliyorum – Inglizcha bilaman"},
        {"tr": "Tarih", "uz": "Tarix", "example": "Tarih dersi – Tarix darsi"},
        {"tr": "Coğrafya", "uz": "Geografiya", "example": "Coğrafya kitabı – Geografiya kitobi"},
        {"tr": "Fen bilgisi", "uz": "Tabiatshunoslik", "example": "Fen dersi – Tabiatshunoslik darsi"},
    ],

    "salomatlik": [
        {"tr": "Hastane", "uz": "Kasalxona", "example": "Acil servis – Tez yordam"},
        {"tr": "Doktor", "uz": "Shifokor", "example": "Aile doktoru – Oilaviy shifokor"},
        {"tr": "Hemşire", "uz": "Hamshira", "example": "Hemşire iğne yaptı – Hamshira ukol qildi"},
        {"tr": "İlaç", "uz": "Dori", "example": "Ağrı kesici ilaç – Og'riq qoldiruvchi dori"},
        {"tr": "Reçete", "uz": "Retsept", "example": "Doktor reçete yazdı – Shifokor retsept yozdi"},
        {"tr": "Eczane", "uz": "Dorixona", "example": "Eczaneden ilaç aldım – Dorixonadan dori oldim"},
        {"tr": "Sağlık sigortası", "uz": "Sog'liq sug'urtasi", "example": "Sağlık sigortam var – Sog'liq sug'urtam bor"},
        {"tr": "Baş ağrısı", "uz": "Bosh og'rig'i", "example": "Baş ağrım var – Boshim og'riyapti"},
        {"tr": "Ateş", "uz": "Isitma", "example": "Ateşim çıktı – Isitmam chiqdi"},
        {"tr": "Öksürük", "uz": "Yo'tal", "example": "Çok öksürüyorum – Juda yo'talmoqdaman"},
        {"tr": "Nezle", "uz": "Shamollash", "example": "Nezle oldum – Shamolladim"},
        {"tr": "Grip", "uz": "Gripp", "example": "Grip tedavisi – Gripp davolash"},
        {"tr": "Mide ağrısı", "uz": "Qorin og'rig'i", "example": "Midem ağrıyor – Qorinim og'riyapti"},
        {"tr": "Alerji", "uz": "Allergiya", "example": "Polen alerjisi – Gulchangi allergiyasi"},
        {"tr": "Ameliyat", "uz": "Operatsiya", "example": "Ameliyat oldum – Operatsiya bo'ldim"},
        {"tr": "Röntgen", "uz": "Rentgen", "example": "Röntgen çektirdim – Rentgen oldirdim"},
        {"tr": "Kan tahlili", "uz": "Qon tahlili", "example": "Kan tahlili yaptırdım – Qon tahlili oldirdim"},
        {"tr": "Tansiyon", "uz": "Qon bosimi", "example": "Tansiyonum yüksek – Qon bosimim baland"},
        {"tr": "Şeker hastalığı", "uz": "Diabet", "example": "Şeker hastası – Diabet bемori"},
        {"tr": "Ambulans", "uz": "Tez yordam", "example": "Ambulans çağırdım – Tez yordam chaqdim"},
    ],

    "sayohat": [
        {"tr": "Havalimanı", "uz": "Aeroport", "example": "İstanbul Havalimanı – Istanbul aeroporti"},
        {"tr": "Pasaport", "uz": "Pasport", "example": "Pasaportumu unuttum – Pasportimni unutdim"},
        {"tr": "Vize", "uz": "Viza", "example": "Türkiye vizesi – Turkiya vizasi"},
        {"tr": "Bilet", "uz": "Chipta", "example": "Uçak bileti – Samolyot chiptasi"},
        {"tr": "Bagaj", "uz": "Bagaj", "example": "Büyük bagaj – Katta bagaj"},
        {"tr": "Check-in", "uz": "Ro'yxatdan o'tish", "example": "Check-in yaptım – Ro'yxatdan o'tdim"},
        {"tr": "Kapı numarası", "uz": "Darvoza raqami", "example": "Kapı numaranız 15 – Darvozangiz 15"},
        {"tr": "Kalkış", "uz": "Jo'nash", "example": "Kalkış saati 10:00 – Jo'nash vaqti 10:00"},
        {"tr": "İniş", "uz": "Qo'nish", "example": "İniş saati 14:00 – Qo'nish vaqti 14:00"},
        {"tr": "Aktarma", "uz": "Pересадка", "example": "İstanbul'da aktarma – Istanbulda o'tish"},
        {"tr": "Otel", "uz": "Mehmonxona", "example": "5 yıldızlı otel – 5 yulduzli mehmonxona"},
        {"tr": "Rezervasyon", "uz": "Bron qilish", "example": "Otel rezervasyonu – Mehmonxona bronи"},
        {"tr": "Check-out", "uz": "Chiqib ketish", "example": "Check-out saati 12:00 – Chiqish vaqti 12:00"},
        {"tr": "Tur", "uz": "Sayohat/Tur", "example": "İstanbul turu – Istanbul sayohati"},
        {"tr": "Rehber", "uz": "Gid", "example": "Turist rehberi – Turist gidi"},
        {"tr": "Harita", "uz": "Xarita", "example": "Şehir haritası – Shahar xaritasi"},
        {"tr": "Döviz", "uz": "Valyuta", "example": "Döviz bozdurdum – Valyuta almashtirdim"},
        {"tr": "Kamera", "uz": "Kamera", "example": "Fotoğraf çektim – Rasm oldim"},
        {"tr": "Hediyelik eşya", "uz": "Sovg'a", "example": "Türkiye'den hediye – Turkiyadan sovg'a"},
        {"tr": "Tatil", "uz": "Ta'til", "example": "Tatile gidiyorum – Ta'tilga ketyapman"},
    ],

    "texnologiya": [
        {"tr": "Telefon", "uz": "Telefon", "example": "Akıllı telefon – Aqlli telefon"},
        {"tr": "Bilgisayar", "uz": "Kompyuter", "example": "Dizüstü bilgisayar – Noutbuk"},
        {"tr": "Tablet", "uz": "Planshet", "example": "iPad tableti – iPad plansheti"},
        {"tr": "İnternet", "uz": "Internet", "example": "Hızlı internet – Tez internet"},
        {"tr": "Wi-Fi", "uz": "Wi-Fi", "example": "Wi-Fi şifresi – Wi-Fi paroli"},
        {"tr": "Şarj cihazı", "uz": "Zaryadlovchi", "example": "Telefon şarj cihazı – Telefon zaryadlovchisi"},
        {"tr": "Kulaklık", "uz": "Quloqchin", "example": "Kablosuz kulaklık – Simsiz quloqchin"},
        {"tr": "Kamera", "uz": "Kamera", "example": "Selfie kamerası – Selfie kamerasi"},
        {"tr": "Uygulama", "uz": "Ilova/Dastur", "example": "Türkçe öğrenme uygulaması – Turkcha o'rganish ilovasi"},
        {"tr": "Sosyal medya", "uz": "Ijtimoiy tarmoq", "example": "Sosyal medya kullanıyorum – Ijtimoiy tarmoq ishlataman"},
        {"tr": "E-posta", "uz": "Elektron pochta", "example": "E-posta gönderdim – Elektron xat yubordim"},
        {"tr": "Şifre", "uz": "Parol", "example": "Şifremi unuttum – Parolimni unutdim"},
        {"tr": "Yazılım", "uz": "Dasturiy ta'minot", "example": "Bilgisayar yazılımı – Kompyuter dasturi"},
        {"tr": "Donanım", "uz": "Qurilma", "example": "Bilgisayar donanımı – Kompyuter qurilmasi"},
        {"tr": "Ekran", "uz": "Ekran", "example": "Büyük ekran – Katta ekran"},
        {"tr": "Klavye", "uz": "Klaviatura", "example": "Kablosuz klavye – Simsiz klaviatura"},
        {"tr": "Fare", "uz": "Sichqoncha", "example": "Optik fare – Optik sichqoncha"},
        {"tr": "Yazıcı", "uz": "Printer", "example": "Renkli yazıcı – Rangli printer"},
        {"tr": "Tarayıcı", "uz": "Skaner", "example": "Belge tarayıcı – Hujjat skaneri"},
        {"tr": "Bellek", "uz": "Xotira", "example": "USB bellek – USB xotira"},
    ],

    "savdo": [
        {"tr": "Market", "uz": "Do'kon", "example": "Büyük market – Katta do'kon"},
        {"tr": "Alışveriş merkezi", "uz": "Savdo markazi", "example": "Modern AVM – Zamonaviy savdo markazi"},
        {"tr": "Fiyat", "uz": "Narx", "example": "Fiyat ne kadar? – Narxi qancha?"},
        {"tr": "İndirim", "uz": "Chegirma", "example": "50% indirim – 50% chegirma"},
        {"tr": "Kasa", "uz": "Kassa", "example": "Kasada bekledim – Kassada kutdim"},
        {"tr": "Fatura", "uz": "Hisob/Kvitansiya", "example": "Fatura aldım – Kvitansiya oldim"},
        {"tr": "Ödeme", "uz": "To'lov", "example": "Kredi kartıyla ödeme – Kredit karta bilan to'lov"},
        {"tr": "Para üstü", "uz": "Qaytim", "example": "Para üstümü aldım – Qaytimimni oldim"},
        {"tr": "Sepet", "uz": "Savat", "example": "Alışveriş sepeti – Xarid savati"},
        {"tr": "Torba", "uz": "Paket/Xalta", "example": "Plastik torba – Plastik xalta"},
        {"tr": "Ürün", "uz": "Mahsulot", "example": "Kaliteli ürün – Sifatli mahsulot"},
        {"tr": "Marka", "uz": "Brend", "example": "Türk markası – Turk brendи"},
        {"tr": "Garanti", "uz": "Kafolat", "example": "2 yıl garanti – 2 yil kafolat"},
        {"tr": "İade", "uz": "Qaytarish", "example": "Ürünü iade ettim – Mahsulotni qaytardim"},
        {"tr": "Stok", "uz": "Ombor/Zaxira", "example": "Stokta yok – Zaxirada yo'q"},
        {"tr": "Sipariş", "uz": "Buyurtma", "example": "Online sipariş – Online buyurtma"},
        {"tr": "Teslimat", "uz": "Yetkazib berish", "example": "Ücretsiz teslimat – Bepul yetkazib berish"},
        {"tr": "Kargo", "uz": "Pochta/Yuk", "example": "Hızlı kargo – Tez yetkazib berish"},
    ],

    "tarix": [
        {"tr": "Türkiye", "uz": "Turkiya", "example": "Güzel Türkiye – Chiroyli Turkiya"},
        {"tr": "İstanbul", "uz": "Istanbul", "example": "İstanbul şehri – Istanbul shahri"},
        {"tr": "Ankara", "uz": "Anqara (poytaxt)", "example": "Ankara başkent – Anqara poytaxt"},
        {"tr": "İzmir", "uz": "Izmir", "example": "İzmir denizi – Izmir dengizi"},
        {"tr": "Boğaz", "uz": "Bo'g'oz (Istanbul)", "example": "İstanbul Boğazı – Istanbul bo'g'ozi"},
        {"tr": "Osmanlı", "uz": "Usmonli imperiya", "example": "Osmanlı tarihi – Usmonli tarixi"},
        {"tr": "Atatürk", "uz": "Otaturk (Mustafa Kemal)", "example": "Atatürk Türkiye'yi kurdu – Otaturk Turkiyani barpo etdi"},
        {"tr": "Bayrak", "uz": "Bayroq", "example": "Türk bayrağı – Turk bayrog'i"},
        {"tr": "Hilal", "uz": "Hilol (yarim oy)", "example": "Türk bayrağında hilal var – Turk bayrog'ida hilol bor"},
        {"tr": "Lira", "uz": "Lira (Turk puli)", "example": "Türk lirası – Turk lirasi"},
        {"tr": "Bozkurt", "uz": "Ko'k bo'ri (ramz)", "example": "Bozkurt Türk sembolüdür – Ko'k bo'ri Turk ramzidir"},
        {"tr": "Hamam", "uz": "Turk hammomi", "example": "Türk hamamı – Turk hammomi"},
        {"tr": "Çarşı", "uz": "Bozor", "example": "Kapalıçarşı – Qopalı bozor"},
        {"tr": "Medeniyet", "uz": "Madaniyat/Sivilizatsiya", "example": "Türk medeniyeti – Turk madaniyati"},
    ],
}

# ============================================================
# TALAFFUZ QO'LLANMASI
# ============================================================
PRONUNCIATION_GUIDE = {
    "harflar": [
        {"harf": "A / a", "talaffuz": "O'zbek 'a' kabi", "misol": "araba (mashina)", "audio_hint": "ah"},
        {"harf": "B / b", "talaffuz": "O'zbek 'b' kabi", "misol": "baba (ota)", "audio_hint": "beh"},
        {"harf": "C / c", "talaffuz": "'j' kabi (English 'j')", "misol": "cadde (ko'cha)", "audio_hint": "jeh"},
        {"harf": "Ç / ç", "talaffuz": "'ch' kabi", "misol": "çay (choy)", "audio_hint": "cheh"},
        {"harf": "D / d", "talaffuz": "O'zbek 'd' kabi", "misol": "dil (til)", "audio_hint": "deh"},
        {"harf": "E / e", "talaffuz": "O'zbek 'e' kabi", "misol": "ev (uy)", "audio_hint": "eh"},
        {"harf": "F / f", "talaffuz": "O'zbek 'f' kabi", "misol": "fiyat (narx)", "audio_hint": "feh"},
        {"harf": "G / g", "talaffuz": "O'zbek 'g' kabi", "misol": "gün (kun)", "audio_hint": "geh"},
        {"harf": "Ğ / ğ", "talaffuz": "Oldingi unlini cho'zadi, deyarli eshitilmaydi", "misol": "dağ (tog')", "audio_hint": "uzatuvchi"},
        {"harf": "H / h", "talaffuz": "O'zbek 'h' kabi", "misol": "hava (havo)", "audio_hint": "heh"},
        {"harf": "I / ı", "talaffuz": "Til orqaga tortilgan 'i' (ingichka 'ı')", "misol": "kız (qiz)", "audio_hint": "uh"},
        {"harf": "İ / i", "talaffuz": "O'zbek 'i' kabi", "misol": "iyi (yaxshi)", "audio_hint": "ee"},
        {"harf": "J / j", "talaffuz": "Fransuz 'j' kabi (yumshoq)", "misol": "jilet (jilet)", "audio_hint": "jheh"},
        {"harf": "K / k", "talaffuz": "O'zbek 'k' kabi", "misol": "kitap (kitob)", "audio_hint": "keh"},
        {"harf": "L / l", "talaffuz": "O'zbek 'l' kabi", "misol": "lira (lira)", "audio_hint": "leh"},
        {"harf": "M / m", "talaffuz": "O'zbek 'm' kabi", "misol": "masa (stol)", "audio_hint": "meh"},
        {"harf": "N / n", "talaffuz": "O'zbek 'n' kabi", "misol": "ne (nima)", "audio_hint": "neh"},
        {"harf": "O / o", "talaffuz": "O'zbek 'o' kabi", "misol": "okul (maktab)", "audio_hint": "oh"},
        {"harf": "Ö / ö", "talaffuz": "'o' va 'e' orasida (lablar dumaloq, 'e' deyiladi)", "misol": "göz (ko'z)", "audio_hint": "eu"},
        {"harf": "P / p", "talaffuz": "O'zbek 'p' kabi", "misol": "para (pul)", "audio_hint": "peh"},
        {"harf": "R / r", "talaffuz": "O'zbek 'r' kabi (titrash bilan)", "misol": "renk (rang)", "audio_hint": "reh"},
        {"harf": "S / s", "talaffuz": "O'zbek 's' kabi", "misol": "su (suv)", "audio_hint": "seh"},
        {"harf": "Ş / ş", "talaffuz": "'sh' kabi", "misol": "şeker (shakar)", "audio_hint": "sheh"},
        {"harf": "T / t", "talaffuz": "O'zbek 't' kabi", "misol": "tren (poyezd)", "audio_hint": "teh"},
        {"harf": "U / u", "talaffuz": "O'zbek 'u' kabi", "misol": "uyku (uyqu)", "audio_hint": "oo"},
        {"harf": "Ü / ü", "talaffuz": "'u' va 'i' orasida (lablar dumaloq, 'i' deyiladi)", "misol": "üzüm (uzum)", "audio_hint": "uu"},
        {"harf": "V / v", "talaffuz": "O'zbek 'v' kabi (yumshoqroq)", "misol": "var (bor)", "audio_hint": "veh"},
        {"harf": "Y / y", "talaffuz": "O'zbek 'y' kabi", "misol": "yemek (ovqat)", "audio_hint": "yeh"},
        {"harf": "Z / z", "talaffuz": "O'zbek 'z' kabi", "misol": "zaman (vaqt)", "audio_hint": "zeh"},
    ],
    "qoidalar": [
        "✅ Turkchada har harf doimo bir xil o'qiladi – istisnolar yo'q!",
        "✅ Ç = CH (Çay = Choy)",
        "✅ Ş = SH (Şehir = Shahri)",
        "✅ Ğ = tovushni cho'zadi (Dağ ≈ Daag)",
        "✅ I (nqotsiz) = ingichka, orqa 'ı' tovushi",
        "✅ İ (nuqtali) = oddiy 'i' tovushi",
        "✅ Ö = lablar dumaloq holatda 'e'",
        "✅ Ü = lablar dumaloq holatda 'i'",
        "✅ Urg'u ko'pincha so'nggi bo'g'inga tushadi",
        "✅ Turkcha so'zlar odatda oxiridan o'qiladi (suffiks tili)",
    ],
    "misollar": [
        {"tr": "Merhaba", "uz": "Salom", "pronounce": "Mer-ha-BA", "tip": "Urg'u oxirga"},
        {"tr": "Teşekkür ederim", "uz": "Rahmat", "pronounce": "Te-shek-KÜR e-de-RIM", "tip": "Ş=SH, Ü=yumaloq i"},
        {"tr": "İstanbul", "uz": "Istanbul", "pronounce": "İs-tan-BUL", "tip": "İ=nuqtali i"},
        {"tr": "Türkiye", "uz": "Turkiya", "pronounce": "Tür-ki-YE", "tip": "Ü=yumaloq i"},
        {"tr": "Günaydın", "uz": "Xayrli tong", "pronounce": "Gü-nay-DIN", "tip": "Ü=yumaloq i, I=qotsiz ı"},
        {"tr": "Çok teşekkür ederim", "uz": "Ko'p rahmat", "pronounce": "CHOK te-shek-kür e-de-rim", "tip": "Ç=CH"},
        {"tr": "Nasılsınız", "uz": "Qandaysiz", "pronounce": "Na-sıl-SIniz", "tip": "I=qotsiz ı"},
    ]
}

# ============================================================
# TURK TILIDAN HELP (Yordamchi iboralar)
# ============================================================
HELP_PHRASES = {
    "tushunmadim": [
        {"tr": "Anlayamadım", "uz": "Tushunmadim", "use": "Biror narsani tushunmaganingizda"},
        {"tr": "Tekrar eder misiniz?", "uz": "Qayta aytib berasizmi?", "use": "Qayta ayttirishda"},
        {"tr": "Daha yavaş konuşur musunuz?", "uz": "Sekinroq gapira olasizmi?", "use": "Juda tez gapirsa"},
        {"tr": "Ne demek istiyorsunuz?", "uz": "Nima demoqchisiz?", "use": "Ma'nosini so'rashda"},
        {"tr": "Türkçe bilmiyorum", "uz": "Turkcha bilmayman", "use": "Bilmasligingizni aytishda"},
        {"tr": "Biraz Türkçe biliyorum", "uz": "Ozgina Turkcha bilaman", "use": "Biroz bilsangiz"},
        {"tr": "İngilizce biliyor musunuz?", "uz": "Inglizcha bilasizmi?", "use": "Boshqa til bilan murojaat"},
        {"tr": "Özbekçe biliyor musunuz?", "uz": "O'zbekcha bilasizmi?", "use": "O'zbekcha so'rashda"},
    ],
    "yozish": [
        {"tr": "Yazabilir misiniz?", "uz": "Yozib berasizmi?", "use": "Yozib berishni so'rashda"},
        {"tr": "Lütfen yazar mısınız?", "uz": "Iltimos, yozib berasizmi?", "use": "Iltimos bilan"},
        {"tr": "Nasıl yazılır?", "uz": "Qanday yoziladi?", "use": "Yozilishini so'rashda"},
        {"tr": "Bunu yazdırabilir miyim?", "uz": "Buni yozdirib olsam bo'ladimi?", "use": "Yozdirish"},
    ],
    "yordam": [
        {"tr": "Yardım edin lütfen!", "uz": "Iltimos, yordam bering!", "use": "Yordam so'rashda"},
        {"tr": "Yardımcı olabilir misiniz?", "uz": "Yordam bera olasizmi?", "use": "Muloyim so'rash"},
        {"tr": "İmdat!", "uz": "Yordam!", "use": "Favqulodda holatlarda"},
        {"tr": "Kayboldum", "uz": "Adashib qoldim", "use": "Yo'l topolmasa"},
        {"tr": "Nerede...?", "uz": "Qayerda...?", "use": "Joy so'rashda"},
        {"tr": "Nasıl giderim?", "uz": "Qanday boraman?", "use": "Yo'l so'rashda"},
        {"tr": "Ne kadar uzak?", "uz": "Qancha uzoq?", "use": "Masofa so'rashda"},
        {"tr": "Ambulans çağırın!", "uz": "Tez yordam chaqiring!", "use": "Tibbiy yordam kerak bo'lsa"},
        {"tr": "Polis çağırın!", "uz": "Politsiya chaqiring!", "use": "Xavfsizlik muammo bo'lsa"},
    ],
    "dokon": [
        {"tr": "Bu ne kadar?", "uz": "Bu qancha?", "use": "Narx so'rashda"},
        {"tr": "Pahalı", "uz": "Qimmat", "use": "Qimmat ekanini bildirishda"},
        {"tr": "İndirim var mı?", "uz": "Chegirma bormi?", "use": "Chegirma so'rashda"},
        {"tr": "Daha ucuzu var mı?", "uz": "Arzonroq bormi?", "use": "Arzon variant so'rashda"},
        {"tr": "Bunu alıyorum", "uz": "Buni olaman", "use": "Sotib olishda"},
        {"tr": "Almıyorum", "uz": "Olmayman", "use": "Rad etishda"},
        {"tr": "Başka rengi var mı?", "uz": "Boshqa rangi bormi?", "use": "Rang so'rashda"},
        {"tr": "Başka bedeni var mı?", "uz": "Boshqa o'lchami bormi?", "use": "O'lcham so'rashda"},
        {"tr": "Deneyebilir miyim?", "uz": "Kiyib ko'rsam bo'ladimi?", "use": "Kiyim kiyib ko'rishda"},
        {"tr": "Kartla ödeyebilir miyim?", "uz": "Karta bilan to'lasam bo'ladimi?", "use": "Karta bilan to'lash"},
    ],
    "restoran": [
        {"tr": "Bir masa istiyorum", "uz": "Bir stol kerak", "use": "Stol so'rashda"},
        {"tr": "Menü lütfen", "uz": "Menyu iltimos", "use": "Menyu so'rashda"},
        {"tr": "Ne tavsiye edersiniz?", "uz": "Nima maslahat berasiz?", "use": "Tavsiya so'rashda"},
        {"tr": "Vejetaryenim", "uz": "Men vegetarianman", "example": "Maxsus ovqat"},
        {"tr": "Helalmi?", "uz": "Halolmi?", "use": "Halol so'rashda"},
        {"tr": "Baharatsız lütfen", "uz": "Zarsozsiz iltimos", "use": "Zarsoz bo'lmasligini so'rashda"},
        {"tr": "Hesap lütfen!", "uz": "Hisob-kitob iltimos!", "use": "To'lash vaqti"},
        {"tr": "Çok lezzetli", "uz": "Juda mazali", "use": "Maqtashda"},
        {"tr": "Az pişmiş", "uz": "Kam pishgan", "use": "Ovqat tayyor emasligida"},
        {"tr": "Paket yapabilir misiniz?", "uz": "Paketlasam bo'ladimi?", "use": "Olib ketishda"},
    ],
}

# ============================================================
# MAVJUD FLASHCARDLAR (Oldingi + yangi)
# ============================================================
FLASHCARDS = [
    {"tr": "Merhaba", "uz": "Salom", "emoji": "👋"},
    {"tr": "Günaydın", "uz": "Xayrli tong", "emoji": "🌅"},
    {"tr": "İyi akşamlar", "uz": "Xayrli kech", "emoji": "🌆"},
    {"tr": "İyi geceler", "uz": "Xayrli tun", "emoji": "🌙"},
    {"tr": "Teşekkür ederim", "uz": "Rahmat", "emoji": "🙏"},
    {"tr": "Rica ederim", "uz": "Marhamat", "emoji": "😊"},
    {"tr": "Evet", "uz": "Ha", "emoji": "✅"},
    {"tr": "Hayır", "uz": "Yo'q", "emoji": "❌"},
    {"tr": "Lütfen", "uz": "Iltimos", "emoji": "🤲"},
    {"tr": "Özür dilerim", "uz": "Kechirasiz", "emoji": "😔"},
    {"tr": "Nasılsınız?", "uz": "Qandaysiz?", "emoji": "🤔"},
    {"tr": "İyiyim", "uz": "Yaxshiman", "emoji": "😄"},
    {"tr": "Adınız ne?", "uz": "Ismingiz nima?", "emoji": "🏷️"},
    {"tr": "Görüşürüz", "uz": "Ko'rishguncha", "emoji": "👋"},
    {"tr": "Su", "uz": "Suv", "emoji": "💧"},
    {"tr": "Ekmek", "uz": "Non", "emoji": "🍞"},
    {"tr": "Et", "uz": "Go'sht", "emoji": "🥩"},
    {"tr": "Çay", "uz": "Choy", "emoji": "🍵"},
    {"tr": "Kahve", "uz": "Qahva", "emoji": "☕"},
    {"tr": "Ev", "uz": "Uy", "emoji": "🏠"},
    {"tr": "Okul", "uz": "Maktab", "emoji": "🏫"},
    {"tr": "Hastane", "uz": "Kasalxona", "emoji": "🏥"},
    {"tr": "Market", "uz": "Do'kon", "emoji": "🛒"},
    {"tr": "Havalimanı", "uz": "Aeroport", "emoji": "✈️"},
    {"tr": "Restoran", "uz": "Restoran", "emoji": "🍽️"},
    {"tr": "Araba", "uz": "Mashina", "emoji": "🚗"},
    {"tr": "Otobüs", "uz": "Avtobus", "emoji": "🚌"},
    {"tr": "Kırmızı", "uz": "Qizil", "emoji": "🔴"},
    {"tr": "Mavi", "uz": "Ko'k", "emoji": "🔵"},
    {"tr": "Yeşil", "uz": "Yashil", "emoji": "🟢"},
    {"tr": "Sarı", "uz": "Sariq", "emoji": "🟡"},
    {"tr": "Beyaz", "uz": "Oq", "emoji": "⚪"},
    {"tr": "Siyah", "uz": "Qora", "emoji": "⚫"},
    {"tr": "Büyük", "uz": "Katta", "emoji": "🔼"},
    {"tr": "Küçük", "uz": "Kichik", "emoji": "🔽"},
    {"tr": "Güzel", "uz": "Chiroyli", "emoji": "😍"},
    {"tr": "Hızlı", "uz": "Tez", "emoji": "⚡"},
    {"tr": "Yavaş", "uz": "Sekin", "emoji": "🐢"},
    {"tr": "Yeni", "uz": "Yangi", "emoji": "✨"},
    {"tr": "Eski", "uz": "Eski", "emoji": "🏚️"},
    {"tr": "Ucuz", "uz": "Arzon", "emoji": "💚"},
    {"tr": "Pahalı", "uz": "Qimmat", "emoji": "💸"},
    {"tr": "Anne", "uz": "Ona", "emoji": "👩"},
    {"tr": "Baba", "uz": "Ota", "emoji": "👨"},
    {"tr": "Öğretmen", "uz": "O'qituvchi", "emoji": "👨‍🏫"},
    {"tr": "Bugün", "uz": "Bugun", "emoji": "📅"},
    {"tr": "Yarın", "uz": "Ertaga", "emoji": "⏭️"},
    {"tr": "Dün", "uz": "Kecha", "emoji": "⏮️"},
    {"tr": "Mutlu", "uz": "Xursand", "emoji": "😄"},
    {"tr": "Üzgün", "uz": "Xafa", "emoji": "😢"},
    {"tr": "Kızgın", "uz": "G'azablangan", "emoji": "😠"},
    {"tr": "Yorgun", "uz": "Charchagan", "emoji": "😴"},
    {"tr": "Aç", "uz": "Och", "emoji": "🍽️"},
    {"tr": "Tok", "uz": "To'q", "emoji": "😊"},
    {"tr": "Sıcak", "uz": "Issiq", "emoji": "🌡️"},
    {"tr": "Soğuk", "uz": "Sovuq", "emoji": "❄️"},
    {"tr": "Dağ", "uz": "Tog'", "emoji": "⛰️"},
    {"tr": "Deniz", "uz": "Dengiz", "emoji": "🌊"},
    {"tr": "Orman", "uz": "O'rmon", "emoji": "🌲"},
    {"tr": "Güneş", "uz": "Quyosh", "emoji": "☀️"},
    {"tr": "Yağmur", "uz": "Yomg'ir", "emoji": "🌧️"},
    {"tr": "Kar", "uz": "Qor", "emoji": "❄️"},
    {"tr": "Futbol", "uz": "Futbol", "emoji": "⚽"},
    {"tr": "Kitap", "uz": "Kitob", "emoji": "📚"},
    {"tr": "Müzik", "uz": "Musiqa", "emoji": "🎵"},
    {"tr": "Film", "uz": "Film", "emoji": "🎬"},
    {"tr": "Para", "uz": "Pul", "emoji": "💰"},
    {"tr": "Zaman", "uz": "Vaqt", "emoji": "⏰"},
    {"tr": "Dil", "uz": "Til", "emoji": "🗣️"},
    {"tr": "Ülke", "uz": "Mamlakat", "emoji": "🌍"},
    {"tr": "Şehir", "uz": "Shahar", "emoji": "🏙️"},
    {"tr": "Yol", "uz": "Yo'l", "emoji": "🛣️"},
    {"tr": "Kapı", "uz": "Eshik", "emoji": "🚪"},
    {"tr": "Pencere", "uz": "Deraza", "emoji": "🪟"},
    {"tr": "Masa", "uz": "Stol", "emoji": "🪑"},
    {"tr": "Sandalye", "uz": "Stul", "emoji": "🪑"},
    {"tr": "Yemek", "uz": "Ovqat", "emoji": "🍲"},
    {"tr": "İçmek", "uz": "Ichmoq", "emoji": "🥤"},
    {"tr": "Gitmek", "uz": "Ketmoq", "emoji": "🏃"},
    {"tr": "Gelmek", "uz": "Kelmoq", "emoji": "🚶"},
    {"tr": "Okumak", "uz": "O'qimoq", "emoji": "📖"},
    {"tr": "Yazmak", "uz": "Yozmoq", "emoji": "✍️"},
    {"tr": "Konuşmak", "uz": "Gapirmoq", "emoji": "💬"},
    {"tr": "Dinlemek", "uz": "Tinglash", "emoji": "👂"},
    {"tr": "Görmek", "uz": "Ko'rmoq", "emoji": "👀"},
    {"tr": "Sevmek", "uz": "Sevmoq", "emoji": "❤️"},
    {"tr": "Bilmek", "uz": "Bilmoq", "emoji": "🧠"},
    {"tr": "İstemek", "uz": "Xohlamoq", "emoji": "🙋"},
    {"tr": "Çalışmak", "uz": "Ishlash/O'qish", "emoji": "💪"},
    {"tr": "Uyumak", "uz": "Uxlamoq", "emoji": "😴"},
    {"tr": "Oynamak", "uz": "O'ynash", "emoji": "🎮"},
]

# ============================================================
# KUNLIK SO'ZLAR (Mavjud + yangilari)
# ============================================================
DAILY_WORDS = [
    [
        {"tr": "Merhaba", "uz": "Salom", "example": "Merhaba! Nasılsın? – Salom! Qandaysan?"},
        {"tr": "Günaydın", "uz": "Xayrli tong", "example": "Günaydın öğretmenim! – Xayrli tong, o'qituvchi!"},
        {"tr": "İyi akşamlar", "uz": "Xayrli kech", "example": "İyi akşamlar! – Xayrli kech!"},
        {"tr": "Teşekkür ederim", "uz": "Rahmat", "example": "Yardımın için teşekkür ederim – Yordaming uchun rahmat"},
        {"tr": "Evet", "uz": "Ha", "example": "Evet, anlıyorum – Ha, tushunaman"},
        {"tr": "Hayır", "uz": "Yo'q", "example": "Hayır, bilmiyorum – Yo'q, bilmayman"},
        {"tr": "Lütfen", "uz": "Iltimos", "example": "Lütfen bekleyin – Iltimos kuting"},
        {"tr": "Özür dilerim", "uz": "Kechirasiz", "example": "Özür dilerim, geç kaldım – Kechirasiz, kechiktim"},
        {"tr": "Görüşürüz", "uz": "Ko'rishguncha", "example": "Yarın görüşürüz – Ertaga ko'rishguncha"},
        {"tr": "Hoşça kalın", "uz": "Xayirli qoling", "example": "Hoşça kalın! – Xayirli qoling!"},
    ],
    [
        {"tr": "Su", "uz": "Suv", "example": "Bir bardak su lütfen – Bir stakan suv iltimos"},
        {"tr": "Ekmek", "uz": "Non", "example": "Bu ekmek çok taze – Bu non juda yangi"},
        {"tr": "Et", "uz": "Go'sht", "example": "Et yemek istiyorum – Go'sht yemoqchiman"},
        {"tr": "Sebze", "uz": "Sabzavot", "example": "Sebzeler çok sağlıklı – Sabzavotlar juda foydali"},
        {"tr": "Meyve", "uz": "Meva", "example": "Hangi meyveyi seviyorsun? – Qaysi mevani yaxshi ko'rasan?"},
        {"tr": "Çay", "uz": "Choy", "example": "Türk çayı çok lezzetli – Turk choyi juda mazali"},
        {"tr": "Kahve", "uz": "Qahva", "example": "Türk kahvesi içer misin? – Turk qahvasi ichasizmi?"},
        {"tr": "Süt", "uz": "Sut", "example": "Çocuklar süt içmeli – Bolalar sut ichishi kerak"},
        {"tr": "Yumurta", "uz": "Tuxum", "example": "Sabah yumurta yedim – Ertalab tuxum yedim"},
        {"tr": "Peynir", "uz": "Pishloq", "example": "Beyaz peynir çok güzel – Oq pishloq juda yaxshi"},
    ],
    [
        {"tr": "Ev", "uz": "Uy", "example": "Evim çok büyük – Uyim juda katta"},
        {"tr": "Okul", "uz": "Maktab", "example": "Okula gidiyorum – Maktabga ketyapman"},
        {"tr": "İş", "uz": "Ish", "example": "İşe geç kaldım – Ishga kechiktim"},
        {"tr": "Hastane", "uz": "Kasalxona", "example": "Hastaneye gitmem gerekiyor – Kasalxonaga borishim kerak"},
        {"tr": "Market", "uz": "Do'kon", "example": "Markete gidelim – Do'konga boraylik"},
        {"tr": "Havalimanı", "uz": "Aeroport", "example": "Havalimanı çok kalabalık – Aeroport juda gavjum"},
        {"tr": "Restoran", "uz": "Restoran", "example": "Bu restoran çok pahalı – Bu restoran juda qimmat"},
        {"tr": "Otel", "uz": "Mehmonxona", "example": "Otelde kalıyorum – Mehmonxonada yashamoqdaman"},
        {"tr": "Banka", "uz": "Bank", "example": "Bankaya para yatıracağım – Bankaga pul qo'yaman"},
        {"tr": "Cami", "uz": "Masjid", "example": "Camiye namaza gidiyorum – Masjidga namozga ketyapman"},
    ],
    [
        {"tr": "Büyük", "uz": "Katta", "example": "Büyük bir ev – Katta uy"},
        {"tr": "Küçük", "uz": "Kichik", "example": "Küçük bir çocuk – Kichik bola"},
        {"tr": "Güzel", "uz": "Chiroyli", "example": "Güzel bir şehir – Chiroyli shahar"},
        {"tr": "Yeni", "uz": "Yangi", "example": "Yeni bir araba – Yangi mashina"},
        {"tr": "Eski", "uz": "Eski", "example": "Eski bir kitap – Eski kitob"},
        {"tr": "İyi", "uz": "Yaxshi", "example": "İyi bir insan – Yaxshi inson"},
        {"tr": "Kötü", "uz": "Yomon", "example": "Kötü haber – Yomon xabar"},
        {"tr": "Hızlı", "uz": "Tez", "example": "Hızlı bir araba – Tez mashina"},
        {"tr": "Yavaş", "uz": "Sekin", "example": "Yavaş yavaş öğreniyor – Asta-sekin o'rganmoqda"},
        {"tr": "Pahalı", "uz": "Qimmat", "example": "Bu çok pahalı – Bu juda qimmat"},
    ],
    [
        {"tr": "Mutlu", "uz": "Xursand", "example": "Bugün çok mutluyum – Bugun juda xursandman"},
        {"tr": "Üzgün", "uz": "Xafa", "example": "Üzgün görünüyor – Xafa ko'rinadi"},
        {"tr": "Yorgun", "uz": "Charchagan", "example": "Çok yorgunum – Juda charchandim"},
        {"tr": "Aç", "uz": "Och", "example": "Çok açım – Juda ochdirman"},
        {"tr": "Tok", "uz": "To'q", "example": "Artık tokum – Endi to'qdirman"},
        {"tr": "Sıcak", "uz": "Issiq", "example": "Bugün çok sıcak – Bugun juda issiq"},
        {"tr": "Soğuk", "uz": "Sovuq", "example": "Hava çok soğuk – Havo juda sovuq"},
        {"tr": "Güçlü", "uz": "Kuchli", "example": "Güçlü bir sporcu – Kuchli sportchi"},
        {"tr": "Zayıf", "uz": "Kuchsiz/Ozg'in", "example": "Zayıf bir ses – Kuchsiz ovoz"},
        {"tr": "Cesur", "uz": "Jasur", "example": "Çok cesur bir kahraman – Juda jasur qahramon"},
    ],
    [
        {"tr": "Anne", "uz": "Ona", "example": "Annem evde – Onam uyda"},
        {"tr": "Baba", "uz": "Ota", "example": "Babam işte – Otam ishda"},
        {"tr": "Kardeş", "uz": "Aka/Singil", "example": "Kardeşimle oynadım – Akam bilan o'yndim"},
        {"tr": "Dede", "uz": "Bobo", "example": "Dedem yaşlı – Bobom keksa"},
        {"tr": "Nine", "uz": "Buvi", "example": "Ninem Türkiye'de – Buvim Turkiyada"},
        {"tr": "Öğretmen", "uz": "O'qituvchi", "example": "Öğretmenim çok iyi – O'qituvchim juda yaxshi"},
        {"tr": "Doktor", "uz": "Shifokor", "example": "Babam doktor – Otam shifokor"},
        {"tr": "Şoför", "uz": "Haydovchi", "example": "Taksi şoförü – Taksi haydovchisi"},
        {"tr": "Aşçı", "uz": "Oshpaz", "example": "Restoran aşçısı – Restoran oshpazi"},
        {"tr": "Mühendis", "uz": "Muhandis", "example": "Bilgisayar mühendisi – Kompyuter muhandisi"},
    ],
    [
        {"tr": "Bugün", "uz": "Bugun", "example": "Bugün hava güzel – Bugun havo yaxshi"},
        {"tr": "Yarın", "uz": "Ertaga", "example": "Yarın geleceğim – Ertaga kelaman"},
        {"tr": "Dün", "uz": "Kecha", "example": "Dün eve erken geldim – Kecha uyga erta keldim"},
        {"tr": "Sabah", "uz": "Ertalab", "example": "Sabah erken kalktım – Ertalab erta turдim"},
        {"tr": "Öğle", "uz": "Tush", "example": "Öğle yemeği yedim – Tushlik yedim"},
        {"tr": "Akşam", "uz": "Kechqurun", "example": "Akşam eve geldim – Kechqurun uyga keldim"},
        {"tr": "Gece", "uz": "Tun", "example": "Gece geç uyudum – Tunda kech uxladim"},
        {"tr": "Hafta", "uz": "Hafta", "example": "Bu hafta meşgulüm – Bu hafta bandman"},
        {"tr": "Ay", "uz": "Oy", "example": "Geçen ay Türkiye'ye gittim – O'tgan oy Turkiyaga bordim"},
        {"tr": "Yıl", "uz": "Yil", "example": "Bu yıl Türkçe öğrendim – Bu yil Turkcha o'rgandim"},
    ],
    [
        {"tr": "Pazartesi", "uz": "Dushanba", "example": "Pazartesi okul var – Dushanba maktab bor"},
        {"tr": "Salı", "uz": "Seshanba", "example": "Salı toplantı – Seshanba yig'ilish"},
        {"tr": "Çarşamba", "uz": "Chorshanba", "example": "Çarşamba pazarı – Chorshanba bozori"},
        {"tr": "Perşembe", "uz": "Payshanba", "example": "Perşembe dersi – Payshanba darsi"},
        {"tr": "Cuma", "uz": "Juma", "example": "Cuma namazı – Juma namozi"},
        {"tr": "Cumartesi", "uz": "Shanba", "example": "Cumartesi tatil – Shanba dam olish"},
        {"tr": "Pazar", "uz": "Yakshanba", "example": "Pazar güzel – Yakshanba yaxshi"},
        {"tr": "Hafta sonu", "uz": "Dam olish kunlari", "example": "Hafta sonu tatil – Dam olish kunlari"},
        {"tr": "İş günü", "uz": "Ish kuni", "example": "İş günlerinde çalışıyorum – Ish kunlari ishlayman"},
        {"tr": "Tatil", "uz": "Ta'til/Dam olish", "example": "Tatile gidiyorum – Ta'tilga ketyapman"},
    ],
    [
        {"tr": "Kedi", "uz": "Mushuk", "example": "Beyaz kedi – Oq mushuk"},
        {"tr": "Köpek", "uz": "It", "example": "Büyük köpek – Katta it"},
        {"tr": "At", "uz": "Ot", "example": "Hızlı at – Tez ot"},
        {"tr": "İnek", "uz": "Sigir", "example": "Sütlü inek – Sutli sigir"},
        {"tr": "Aslan", "uz": "Sher", "example": "Güçlü aslan – Kuchli sher"},
        {"tr": "Kartal", "uz": "Burgut", "example": "Dağ kartalı – Tog' burguti"},
        {"tr": "Balık", "uz": "Baliq", "example": "Deniz balığı – Dengiz balig'i"},
        {"tr": "Kurbağa", "uz": "Qurbaqa", "example": "Yeşil kurbağa – Yashil qurbaqa"},
        {"tr": "Yılan", "uz": "Ilon", "example": "Uzun yılan – Uzun ilon"},
        {"tr": "Papağan", "uz": "To'ti qush", "example": "Renkli papağan – Rangli to'ti"},
    ],
    [
        {"tr": "Araba", "uz": "Mashina", "example": "Yeni araba – Yangi mashina"},
        {"tr": "Otobüs", "uz": "Avtobus", "example": "Şehir otobüsü – Shahar avtobusi"},
        {"tr": "Metro", "uz": "Metro", "example": "İstanbul metrosu – Istanbul metrosi"},
        {"tr": "Tren", "uz": "Poyezd", "example": "Hızlı tren – Tez poyezd"},
        {"tr": "Uçak", "uz": "Samolyot", "example": "Uçakla gidiyorum – Samolyot bilan ketyapman"},
        {"tr": "Gemi", "uz": "Kema", "example": "Yolcu gemisi – Yo'lovchi kemasi"},
        {"tr": "Bisiklet", "uz": "Velosiped", "example": "Kırmızı bisiklet – Qizil velosiped"},
        {"tr": "Taksi", "uz": "Taksi", "example": "Sarı taksi – Sariq taksi"},
        {"tr": "Dolmuş", "uz": "Marshrutka", "example": "Dolmuşa bindim – Marshrutkaga chiqdim"},
        {"tr": "Ambulans", "uz": "Tez yordam", "example": "Ambulans geliyor – Tez yordam kelayapti"},
    ],
]

# ============================================================
# QUIZ SAVOLLARI (Kengaytirilgan)
# ============================================================
QUIZ_QUESTIONS = [
    {"question":"🇹🇷 'Merhaba' o'zbekcha?","options":["Rahmat","Salom","Ha","Yo'q"],"correct":1,"explanation":"✅ Merhaba = Salom. Asosiy salomlashish."},
    {"question":"🇹🇷 'Teşekkür ederim' o'zbekcha?","options":["Kechirasiz","Salom","Rahmat","Xayir"],"correct":2,"explanation":"✅ Teşekkür ederim = Rahmat."},
    {"question":"🇹🇷 'Güzel' o'zbekcha?","options":["Katta","Yaxshi","Chiroyli","Tez"],"correct":2,"explanation":"✅ Güzel = Chiroyli."},
    {"question":"🇹🇷 'Büyük' o'zbekcha?","options":["Kichik","Yaxshi","Katta","Yangi"],"correct":2,"explanation":"✅ Büyük = Katta."},
    {"question":"🇹🇷 'Mutlu' o'zbekcha?","options":["Xafa","Charchagan","Xursand","G'azablangan"],"correct":2,"explanation":"✅ Mutlu = Xursand."},
    {"question":"🇹🇷 'Üzgün' o'zbekcha?","options":["Xursand","Xafa","Charchagan","Och"],"correct":1,"explanation":"✅ Üzgün = Xafa."},
    {"question":"🇹🇷 'Yorgun' o'zbekcha?","options":["Charchagan","Och","Xursand","Yaxshi"],"correct":0,"explanation":"✅ Yorgun = Charchagan."},
    {"question":"🇹🇷 'Hızlı' o'zbekcha?","options":["Sekin","Katta","Tez","Eski"],"correct":2,"explanation":"✅ Hızlı = Tez."},
    {"question":"🇹🇷 'Pahalı' o'zbekcha?","options":["Arzon","Yangi","Qimmat","Yaxshi"],"correct":2,"explanation":"✅ Pahalı = Qimmat."},
    {"question":"🇹🇷 'Nazik' o'zbekcha?","options":["Qo'pol","Muloyim","Dangasa","Jasur"],"correct":1,"explanation":"✅ Nazik = Muloyim/Xushmuomala."},
    {"question":"🇹🇷 'Çalışkan' o'zbekcha?","options":["Dangasa","Yaxshi","Mehnatsevar","Aqlli"],"correct":2,"explanation":"✅ Çalışkan = Mehnatsevar."},
    {"question":"🇹🇷 'Akıllı' o'zbekcha?","options":["Ahmoq","Aqlli","Kuchli","Yaxshi"],"correct":1,"explanation":"✅ Akıllı = Aqlli."},
    {"question":"🇹🇷 'Sıcak' o'zbekcha?","options":["Sovuq","Issiq","Iliq","Baland"],"correct":1,"explanation":"✅ Sıcak = Issiq."},
    {"question":"🇹🇷 'Soğuk' o'zbekcha?","options":["Issiq","Iliq","Sovuq","Past"],"correct":2,"explanation":"✅ Soğuk = Sovuq."},
    {"question":"🇹🇷 'Tatlı' o'zbekcha?","options":["Achchiq","Nordon","Sho'r","Shirin"],"correct":3,"explanation":"✅ Tatlı = Shirin."},
    {"question":"🇹🇷 'Acı' o'zbekcha?","options":["Shirin","Achchiq","Nordon","Sho'r"],"correct":1,"explanation":"✅ Acı = Achchiq."},
    {"question":"🇹🇷 'Lezzetli' o'zbekcha?","options":["Mazasiz","Mazali","Yaxshi","Chiroyli"],"correct":1,"explanation":"✅ Lezzetli = Mazali."},
    {"question":"🇹🇷 'Temiz' o'zbekcha?","options":["Iflos","Toza","Yaxshi","Yangi"],"correct":1,"explanation":"✅ Temiz = Toza."},
    {"question":"🇹🇷 'Kirli' o'zbekcha?","options":["Toza","Iflos","Qoʻpolroq","Yomon"],"correct":1,"explanation":"✅ Kirli = Iflos."},
    {"question":"🇹🇷 'Güçlü' o'zbekcha?","options":["Kuchsiz","Kuchli","Katta","Tez"],"correct":1,"explanation":"✅ Güçlü = Kuchli."},
    {"question":"🇺🇿 'Yashil' turkcha?","options":["Mavi","Sarı","Yeşil","Kırmızı"],"correct":2,"explanation":"✅ Yashil = Yeşil."},
    {"question":"🇺🇿 'Sariq' turkcha?","options":["Kırmızı","Mavi","Yeşil","Sarı"],"correct":3,"explanation":"✅ Sariq = Sarı."},
    {"question":"🇺🇿 'Binafsha' turkcha?","options":["Pembe","Mor","Turuncu","Gri"],"correct":1,"explanation":"✅ Binafsha = Mor."},
    {"question":"🇺🇿 'Pushti' turkcha?","options":["Mor","Pembe","Sarı","Bej"],"correct":1,"explanation":"✅ Pushti = Pembe."},
    {"question":"🇹🇷 'Uzun' o'zbekcha?","options":["Qisqa","Katta","Uzun","Baland"],"correct":2,"explanation":"✅ Uzun = Uzun. (bir xil!)"},
    {"question":"🇹🇷 'Kısa' o'zbekcha?","options":["Uzun","Qisqa","Kichik","Past"],"correct":1,"explanation":"✅ Kısa = Qisqa."},
    {"question":"🇹🇷 'Derin' o'zbekcha?","options":["Sayoz","Katta","Chuqur","Uzun"],"correct":2,"explanation":"✅ Derin = Chuqur."},
    {"question":"🇹🇷 'Hafif' o'zbekcha?","options":["Og'ir","Yengil","Kichik","Tez"],"correct":1,"explanation":"✅ Hafif = Yengil."},
    {"question":"🇹🇷 'Ağır' o'zbekcha?","options":["Yengil","Og'ir","Katta","Kuchli"],"correct":1,"explanation":"✅ Ağır = Og'ir."},
    {"question":"🇹🇷 'Sert' o'zbekcha?","options":["Yumshoq","Qattiq","Kuchli","Baland"],"correct":1,"explanation":"✅ Sert = Qattiq."},
    {"question":"🇹🇷 'Yumuşak' o'zbekcha?","options":["Qattiq","Yengil","Yumshoq","Iliq"],"correct":2,"explanation":"✅ Yumuşak = Yumshoq."},
    {"question":"🇹🇷 'Boş' o'zbekcha?","options":["To'la","Bo'sh","Katta","Yangi"],"correct":1,"explanation":"✅ Boş = Bo'sh."},
    {"question":"🇹🇷 'Dolu' o'zbekcha?","options":["Bo'sh","To'la","Ko'p","Katta"],"correct":1,"explanation":"✅ Dolu = To'la."},
    {"question":"🇹🇷 'Çok' o'zbekcha?","options":["Kam","Ko'p","Yetarli","Juda"],"correct":1,"explanation":"✅ Çok = Ko'p (yoki Juda)."},
    {"question":"🇹🇷 'Az' o'zbekcha?","options":["Ko'p","Kam","Oz","Biroz"],"correct":1,"explanation":"✅ Az = Kam/Oz."},
    {"question":"🇹🇷 'Yeni' o'zbekcha?","options":["Eski","Yangi","Chiroyli","Yaxshi"],"correct":1,"explanation":"✅ Yeni = Yangi."},
    {"question":"🇹🇷 'Eski' o'zbekcha?","options":["Yangi","Eski","Yomon","Kichik"],"correct":1,"explanation":"✅ Eski = Eski. (bir xil!)"},
    {"question":"🇹🇷 'Sabırlı' o'zbekcha?","options":["Sabrsiz","Dangasa","Sabr-toqatli","Aqlli"],"correct":2,"explanation":"✅ Sabırlı = Sabr-toqatli."},
    {"question":"🇹🇷 'Cömert' o'zbekcha?","options":["Xasis","Saxiy","Yaxshi","Halol"],"correct":1,"explanation":"✅ Cömert = Saxiy."},
    {"question":"🇹🇷 'Meraklı' o'zbekcha?","options":["Zerikkan","Qiziquvchan","Hayajonlangan","Aqlli"],"correct":1,"explanation":"✅ Meraklı = Qiziquvchan."},
]

# ============================================================
# GRAMMATIKA DARSLARI (Kengaytirilgan)
# ============================================================
GRAMMAR_LESSONS = [
    {
        "title": "📖 1-dars: Turkcha harflar va talaffuz",
        "content": """🔤 *TURKCHA ALIFBO*

Turkcha alifbo 29 ta harfdan iborat (lotin asosida).

*Maxsus harflar:*
• *Ç* = "ch" (Çay = Choy)
• *Ğ* = tovushni cho'zadi (Dağ ≈ Daag)
• *I / ı* = orqa "ı" (nuqtasiz, ingichka)
• *İ / i* = oddiy "i" (nuqtali)
• *Ö / ö* = lablar dumaloq, "e" deyiladi
• *Ş / ş* = "sh" (Şehir = Shahri)
• *Ü / ü* = lablar dumaloq, "i" deyiladi

📌 *Muhim qoida:* Har harf doimo bir xil o'qiladi!"""
    },
    {
        "title": "📖 2-dars: Olmoshlar (Zamir)",
        "content": """👤 *TURKCHA OLMOSHLAR*

| O'zbek | Turkcha |
|--------|---------|
| Men | Ben |
| Sen | Sen |
| U | O |
| Biz | Biz |
| Sizlar | Siz |
| Ular | Onlar |

*Misollar:*
• Ben öğrenciyim – Men o'quvchiman
• Sen çok güzelsin – Sen juda chiroylisan
• O öğretmendir – U o'qituvchi
• Biz Özbekistanlıyız – Biz O'zbekistonlikmiz

📌 "Sen" – yaqin, "Siz" – hurmat bilan"""
    },
    {
        "title": "📖 3-dars: Hozirgi zamon (-ıyor)",
        "content": """⏰ *HOZIRGI ZAMON*

Fe'lga *-ıyor* qo'shiladi:

| O'zbek | Turkcha |
|--------|---------|
| Men ketmoqdaman | Ben gidiyorum |
| Sen yemoqdasan | Sen yiyorsun |
| U o'qimoqda | O okuyor |
| Biz uxlamoqdamiz | Biz uyuyoruz |

*Asosiy fe'llar:*
• git- → gidiyorum (ketmoqdaman)
• ye- → yiyorum (yemoqdaman)
• oku- → okuyorum (o'qimoqdaman)
• gel- → geliyorum (kelmoqdaman)
• iç- → içiyorum (ichmoqdaman)
• çalış- → çalışıyorum (ishlamoqdaman)

*Misollar:*
• Ben çay içiyorum – Men choy ichmoqdaman
• O kitap okuyor – U kitob o'qimoqda"""
    },
    {
        "title": "📖 4-dars: O'tgan zamon (-di)",
        "content": """⏮️ *O'TGAN ZAMON (-di)*

| O'zbek | Turkcha |
|--------|---------|
| Men keldim | Ben geldim |
| Sen ketding | Sen gittin |
| U yedi | O yedi |
| Biz ko'rdik | Biz gördük |

*Qoida:* Jarangsiz undoshdan keyin (-ti):
• İçtim – ichdim
• Gittim – ketdim
• Yaptım – qildim

*Misollar:*
• Dün eve geldim – Kecha uyga keldim
• Türkiye'ye gittim – Turkiyaga bordim
• Film seyrettim – Film tomosha qildim"""
    },
    {
        "title": "📖 5-dars: Kelasi zamon (-acak/-ecek)",
        "content": """⏭️ *KELASI ZAMON*

| O'zbek | Turkcha |
|--------|---------|
| Men kelaman | Ben geleceğim |
| Sen borasan | Sen gideceksin |
| U o'qiydi | O okuyacak |

*Qoida:*
• e, i, ö, ü → -ecek
• Boshqalarda → -acak

*Misollar:*
• Yarın geleceğim – Ertaga kelaman
• Türkçe öğreneceğim – Turkcha o'rganaman
• İstanbul'a gidecek – Istanbulga boradi"""
    },
    {
        "title": "📖 6-dars: Savol shakli (mı/mi/mu/mü)",
        "content": """❓ *SAVOL SHAKLI*

So'z so'ngiga *mı/mi/mu/mü* qo'shiladi:

| O'zbek | Turkcha |
|--------|---------|
| O'quvchimisan? | Öğrenci misin? |
| Keldi? | Geldi mi? |
| Choy ichasizmi? | Çay içer misin? |

*Qoida:*
• a, ı → mı
• e, i → mi
• o, u → mu
• ö, ü → mü

*Misollar:*
• Türkçe biliyor musun? – Turkcha bilasanmi?
• Evde misin? – Uydasanmi?
• Gelecek misin? – Kelasanmi?"""
    },
    {
        "title": "📖 7-dars: Inkor shakli (değil / -me)",
        "content": """🚫 *INKOR SHAKLI*

*1. İsm va sifat inkori: değil*
• Ben öğrenci değilim – Men o'quvchi emasman
• O yorgun değil – U charchmagan

*2. Fe'l inkori: -me/-ma*
• Gitme! – Ketma!
• Bilmiyorum – Bilmayman
• Gelmedi – Kelmadi

*Misollar:*
• Türkçe bilmiyorum – Turkcha bilmayman
• Eve gitmedim – Uyga bormadim
• O öğrenci değil – U o'quvchi emas"""
    },
    {
        "title": "📖 8-dars: Sifat qo'shimchalari",
        "content": """🎨 *SIFAT QO'SHIMCHALARI*

Turkchada sifat otdan oldin keladi:

• Büyük ev – Katta uy ✅
• Ev büyük – Uy katta ✅ (ikkalasi ham to'g'ri)

*Ko'proq / Kam daraja:*
• Daha güzel – Chiroyiliroq
• En güzel – Eng chiroyli
• Daha ucuz – Arzonroq
• En ucuz – Eng arzon

*Misollar:*
• Bu araba daha büyük – Bu mashina kattaroq
• O en güzel kız – U eng chiroyli qiz
• Bu market daha ucuz – Bu do'kon arzonroq"""
    },
    {
        "title": "📖 9-dars: Olmosh + fe'l birikmalari",
        "content": """🔗 *BEN / SEN / O + FE'L*

Hozirgi zamon to'liq:

| Olmosh | Qo'shimcha | Misol |
|--------|-----------|-------|
| Ben | -orum/-ıyorum | geliyorum |
| Sen | -orsun/-ıyorsun | geliyorsun |
| O | -or/-ıyor | geliyor |
| Biz | -oruz/-ıyoruz | geliyoruz |
| Siz | -orsunuz/-ıyorsunuz | geliyorsunuz |
| Onlar | -orlar/-ıyorlar | geliyorlar |

*Misol: Çalışmak (Ishlash)*
• Ben çalışıyorum – Men ishlamoqdaman
• Sen çalışıyorsun – Sen ishlamoqdasan
• O çalışıyor – U ishlamoqda
• Biz çalışıyoruz – Biz ishlamoqdamiz"""
    },
    {
        "title": "📖 10-dars: Egalik qo'shimchalari",
        "content": """🏷️ *EGALIK QO'SHIMCHALARI*

| O'zbek | Qo'shimcha | Misol |
|--------|-----------|-------|
| Mening | -ım/-im/-um/-üm | kitabım (kitobim) |
| Sening | -ın/-in/-un/-ün | kitabın (kitobing) |
| Uning | -ı/-i/-u/-ü | kitabı (kitobi) |
| Bizning | -ımız/-imiz | kitabımız (kitobimiz) |
| Sizning | -ınız/-iniz | kitabınız (kitobingiz) |
| Ularning | -ları/-leri | kitapları (kitoblari) |

*Misollar:*
• Evim büyük – Uyim katta
• Araban nerede? – Mashinang qayerda?
• Annesi öğretmen – Onasi o'qituvchi
• Ailemiz mutlu – Oilamiz baxtli"""
    },
    {
        "title": "📖 11-dars: Yo'nalish va joy (-de/-da, -e/-a)",
        "content": """📍 *JOY VA YO'NALISH*

*1. Qayerda? (-de/-da)*
• Evde – Uyda
• Okulda – Maktabda
• İstanbul'da – Istanbulda

*2. Qayerga? (-e/-a)*
• Eve – Uyga
• Okula – Maktabga
• İstanbul'a – Istanbulga

*3. Qayerdan? (-den/-dan)*
• Evden – Uydan
• Okuldan – Maktabdan
• İstanbul'dan – Istanbuldan

*Misollar:*
• Evdeyim – Uydaman
• Eve gidiyorum – Uyga ketyapman
• Evden geldim – Uydan keldim"""
    },
    {
        "title": "📖 12-dars: Muhim fe'llar (100 ta)",
        "content": """🔥 *ASOSIY FE'LLAR*

*Harakat:*
• gitmek – ketmoq
• gelmek – kelmoq
• koşmak – yugurmoq
• yürümek – yurmoq
• oturmak – o'tirmoq
• kalkmak – turmoq

*Idrok:*
• görmek – ko'rmoq
• duymak – eshitmoq
• bakmak – qarаmoq
• dinlemek – tinglash

*Muloqot:*
• konuşmak – gapirmoq
• söylemek – aytmoq
• sormak – so'ramoq
• cevap vermek – javob bermoq

*Yashash:*
• yemek – yemoq
• içmek – ichmoq
• uyumak – uxlamoq
• çalışmak – ishlash

*Fikr:*
• bilmek – bilmoq
• anlamak – tushunmoq
• düşünmek – o'ylamoq
• sevmek – sevmoq"""
    },
]

# ============================================================
# DIALOGLAR (Kengaytirilgan)
# ============================================================
DIALOGUES = [
    {
        "title": "🛒 Do'konda",
        "lines": [
            {"speaker": "👤 Mijoz", "tr": "Merhaba, kaç lira bu?", "uz": "Salom, bu necha lira?"},
            {"speaker": "🛍️ Sotuvchi", "tr": "Merhaba! On beş lira.", "uz": "Salom! O'n besh lira."},
            {"speaker": "👤 Mijoz", "tr": "Çok pahalı. İndirim var mı?", "uz": "Juda qimmat. Chegirma bormi?"},
            {"speaker": "🛍️ Sotuvchi", "tr": "Tamam, on liraya veriyorum.", "uz": "Mayli, o'n liraga beraman."},
            {"speaker": "👤 Mijoz", "tr": "Teşekkür ederim!", "uz": "Rahmat!"},
        ]
    },
    {
        "title": "✈️ Aeroportda",
        "lines": [
            {"speaker": "👤 Yo'lovchi", "tr": "İstanbul'a bilet istiyorum.", "uz": "Istanbulga chipta olmoqchiman."},
            {"speaker": "✈️ Xodim", "tr": "Tek mi gidiş-dönüş mü?", "uz": "Bir tomonga yoki boriş-keliş?"},
            {"speaker": "👤 Yo'lovchi", "tr": "Tek gidiş lütfen.", "uz": "Faqat bir tomonga iltimos."},
            {"speaker": "✈️ Xodim", "tr": "Pasaportunuzu verir misiniz?", "uz": "Pasportingizni bera olasizmi?"},
            {"speaker": "👤 Yo'lovchi", "tr": "Buyurun.", "uz": "Mana."},
            {"speaker": "✈️ Xodim", "tr": "Uçuşunuz saat 14:00'de.", "uz": "Parvozingiz soat 14:00 da."},
        ]
    },
    {
        "title": "🍽️ Restoranda",
        "lines": [
            {"speaker": "🍽️ Ofitsiant", "tr": "Buyurun, ne içmek istersiniz?", "uz": "Marhamat, nima ichasiz?"},
            {"speaker": "👤 Mehmon", "tr": "Bir çay ve su lütfen.", "uz": "Bir choy va suv iltimos."},
            {"speaker": "🍽️ Ofitsiant", "tr": "Yemek ne istersiniz?", "uz": "Ovqatdan nima xohlaysiz?"},
            {"speaker": "👤 Mehmon", "tr": "Kebap ve pilav lütfen.", "uz": "Kabob va palov iltimos."},
            {"speaker": "🍽️ Ofitsiant", "tr": "Tabii, hemen getiriyorum.", "uz": "Albatta, hozir olib kelaman."},
            {"speaker": "👤 Mehmon", "tr": "Hesap lütfen!", "uz": "Hisob-kitob iltimos!"},
        ]
    },
    {
        "title": "🏫 Maktabda",
        "lines": [
            {"speaker": "👤 O'quvchi", "tr": "Öğretmenim, anlayamadım.", "uz": "O'qituvchi, tushunmadim."},
            {"speaker": "👨‍🏫 O'qituvchi", "tr": "Hangi konuyu anlamadın?", "uz": "Qaysi mavzuni tushunmading?"},
            {"speaker": "👤 O'quvchi", "tr": "Şimdiki zamanı anlayamadım.", "uz": "Hozirgi zamonni tushunmadim."},
            {"speaker": "👨‍🏫 O'qituvchi", "tr": "Tamam, tekrar anlatayım.", "uz": "Yaxshi, qayta tushuntiray."},
            {"speaker": "👤 O'quvchi", "tr": "Teşekkür ederim öğretmenim.", "uz": "Rahmat, o'qituvchi."},
        ]
    },
    {
        "title": "🏨 Mehmonxonada",
        "lines": [
            {"speaker": "👤 Mehmon", "tr": "İyi günler, bir oda istiyorum.", "uz": "Xayrli kun, bitta xona kerak."},
            {"speaker": "🏨 Qabul", "tr": "Kaç kişilik?", "uz": "Necha kishilik?"},
            {"speaker": "👤 Mehmon", "tr": "İki kişilik lütfen.", "uz": "Ikki kishilik iltimos."},
            {"speaker": "🏨 Qabul", "tr": "Kaç gece kalacaksınız?", "uz": "Necha kecha qolasiz?"},
            {"speaker": "👤 Mehmon", "tr": "Üç gece.", "uz": "Uch kecha."},
            {"speaker": "🏨 Qabul", "tr": "Pasaportunuzu alabilir miyim?", "uz": "Pasportingizni olsam bo'ladimi?"},
        ]
    },
    {
        "title": "🗺️ Yo'l so'rash",
        "lines": [
            {"speaker": "👤 Yo'lovchi", "tr": "Affedersiniz, Taksim Meydanı nerede?", "uz": "Kechirasiz, Taksim maydoni qayerda?"},
            {"speaker": "🧭 Mahalliy", "tr": "Düz gidin, sonra sağa dönün.", "uz": "To'g'ri boring, keyin o'ngga buriling."},
            {"speaker": "👤 Yo'lovchi", "tr": "Yürüyerek kaç dakika?", "uz": "Piyoda necha daqiqa?"},
            {"speaker": "🧭 Mahalliy", "tr": "Yaklaşık on dakika.", "uz": "Taxminan o'n daqiqa."},
            {"speaker": "👤 Yo'lovchi", "tr": "Çok teşekkür ederim!", "uz": "Ko'p rahmat!"},
        ]
    },
    {
        "title": "🏥 Kasalxonada",
        "lines": [
            {"speaker": "👤 Bemor", "tr": "Baş ağrım var.", "uz": "Boshim og'riyapti."},
            {"speaker": "👨‍⚕️ Doktor", "tr": "Ne zamandan beri?", "uz": "Qachondan beri?"},
            {"speaker": "👤 Bemor", "tr": "Dünden beri.", "uz": "Kechadan beri."},
            {"speaker": "👨‍⚕️ Doktor", "tr": "Ateşiniz var mı?", "uz": "Isitmangiz bormi?"},
            {"speaker": "👤 Bemor", "tr": "Evet, 38 derece.", "uz": "Ha, 38 daraja."},
            {"speaker": "👨‍⚕️ Doktor", "tr": "Reçete yazıyorum.", "uz": "Retsept yozaman."},
        ]
    },
    {
        "title": "📱 Telefonda",
        "lines": [
            {"speaker": "📞 A", "tr": "Alo, merhaba!", "uz": "Alo, salom!"},
            {"speaker": "📞 B", "tr": "Merhaba! Nasılsın?", "uz": "Salom! Qandaysan?"},
            {"speaker": "📞 A", "tr": "İyiyim, teşekkürler. Sen nasılsın?", "uz": "Yaxshiman, rahmat. Sen qandaysan?"},
            {"speaker": "📞 B", "tr": "Ben de iyiyim. Ne zaman geliyorsun?", "uz": "Men ham yaxshiman. Qachon kelasan?"},
            {"speaker": "📞 A", "tr": "Yarın saat 3'te geliyorum.", "uz": "Ertaga soat 3 da kelaman."},
            {"speaker": "📞 B", "tr": "Tamam, görüşürüz!", "uz": "Yaxshi, ko'rishguncha!"},
        ]
    },
    {
        "title": "🤝 Tanishish",
        "lines": [
            {"speaker": "👤 A", "tr": "Merhaba! Adınız ne?", "uz": "Salom! Ismingiz nima?"},
            {"speaker": "👤 B", "tr": "Merhaba! Benim adım Ahmet.", "uz": "Salom! Mening ismim Ahmet."},
            {"speaker": "👤 A", "tr": "Memnun oldum. Ben Ali.", "uz": "Tanishganimdan xursandman. Men Ali."},
            {"speaker": "👤 B", "tr": "Nerelisiniz?", "uz": "Qayerdansiz?"},
            {"speaker": "👤 A", "tr": "Özbekistanlıyım. Siz?", "uz": "O'zbekistonlikmiz. Siz?"},
            {"speaker": "👤 B", "tr": "Ben Türkiyeliyim.", "uz": "Men Turkiyalikmiz."},
        ]
    },
    {
        "title": "💰 Bankada",
        "lines": [
            {"speaker": "👤 Mijoz", "tr": "Para bozdurabilir miyim?", "uz": "Pul almashtira olsam bo'ladimi?"},
            {"speaker": "🏦 Xodim", "tr": "Tabii. Hangi döviz?", "uz": "Albatta. Qaysi valyuta?"},
            {"speaker": "👤 Mijoz", "tr": "100 dolar Türk lirasına.", "uz": "100 dollar Turk lirasiga."},
            {"speaker": "🏦 Xodim", "tr": "Bugün kur 32 lira.", "uz": "Bugun kurs 32 lira."},
            {"speaker": "👤 Mijoz", "tr": "Tamam, bozduruyorum.", "uz": "Yaxshi, almashtiraman."},
            {"speaker": "🏦 Xodim", "tr": "İşte 3200 lira.", "uz": "Mana 3200 lira."},
        ]
    },
]

# ============================================================
# DARAJALAR VA YUTUQLAR
# ============================================================
LEVELS = [
    {"name": "🥚 Yangi Boshlovchi", "min_xp": 0, "max_xp": 100},
    {"name": "⭐ Boshlang'ich", "min_xp": 100, "max_xp": 300},
    {"name": "⭐⭐ O'rta", "min_xp": 300, "max_xp": 600},
    {"name": "⭐⭐⭐ Yuqori O'rta", "min_xp": 600, "max_xp": 1000},
    {"name": "🌟 Ilg'or", "min_xp": 1000, "max_xp": 1500},
    {"name": "🏆 Ustoz", "min_xp": 1500, "max_xp": 9999},
]

BADGES = [
    {"id": "first_quiz", "name": "🏅 Birinchi Test", "desc": "Birinchi testni tugating"},
    {"id": "quiz_10", "name": "🎯 10 Ta To'g'ri", "desc": "10 ta testni to'g'ri javoblang"},
    {"id": "quiz_50", "name": "🔥 50 Ta To'g'ri", "desc": "50 ta testni to'g'ri javoblang"},
    {"id": "daily_1", "name": "📅 Birinchi Kun", "desc": "Birinchi kunlik so'zlarni o'rganing"},
    {"id": "daily_7", "name": "🗓️ 7 Kun", "desc": "7 kun ketma-ket o'rganing"},
    {"id": "grammar_1", "name": "📚 Grammatika", "desc": "Birinchi grammatika darsini tugatng"},
    {"id": "flashcard_20", "name": "🃏 Kartalar", "desc": "20 ta flashcardni ko'ring"},
    {"id": "topic_1", "name": "🗂️ Mavzu", "desc": "Birinchi mavzuni tugatng"},
    {"id": "help_1", "name": "🆘 Yordam", "desc": "Help bo'limidan foydalaning"},
    {"id": "pronounce_1", "name": "🗣️ Talaffuz", "desc": "Talaffuz darsini tugatng"},
    {"id": "adjective_1", "name": "🎨 Sifatlar", "desc": "Sifatlar bo'limini tugatng"},
    {"id": "xp_500", "name": "⚡ 500 XP", "desc": "500 XP to'plang"},
    {"id": "xp_1000", "name": "💫 1000 XP", "desc": "1000 XP to'plang"},
]
