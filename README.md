# Insertion Sort Projesi

*Insertion Sort* bir sıralama yöntemidir. Bu yöntemde 0. indexten başlayarak herbir index kendinden sonra gelen en küçük sayı ile yerdeğiştirerek sıralanır.

[22,27,16,2,18,6] dizisini insertion sort'a göre sıralayalım.
1. Adımda 0. index(22) en küçük sayı ile yer değiştirir. En küçük sayı 2dir. Sıralama şöyledir: [2,27,16,22,18,6]. 0. indexe en küçük sayı taşınmış olup 0. index sıralanmıştır. Bu adımda "n" tane işlem yapılmıştır.
2. Adımda 1. index(27) sıralanır. İkinci en küçük değer 6dır. Sıralama şöyle olur: [2,6,16,22,18,27]. 1. indexe ikinci en küçük sayı taşınmış olup 1. index sıralanmıştır. Bu adımda (n-1) tane işlem yapılmıştır.
3. Adımda 2. index(16) sıralanır. Bu değer dizideki en küçük değer olduğu için yeri değişmeyip sıralanmış olur. Bu adımda (n-2) tane işlem yapılmıştır.
4. Adımda 3. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-3) tane işlem yapılmıştır.
5. Adımda 4. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-4) tane işlem yapılmıştır.
6. Adımda 5. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-5) tane yani 1 tane işlem yapılmıştır.

Yukarıdaki örnekte de görüldüğü gibi işlem sayısı n'den başlayarak 1'e kadar olan sayıların toplamı kadardır. Toplam İşlem sayısı `n*(n-1)/2` kadardır. Buradan da **O(n^2)** olur.

"18" değeri sıralı dizide ortada bulunduğundan dolayı case'i **average**dır.

[7,3,5,8,2,9,4,15,6] bu dizinin ilk dört adımdaki sıralanışına bakalım.
1. Adımda 2 ile 7 yer değiştirir. [2,3,5,8,7,9,4,15,6]
2. Aadımda sıralama değişmez çünkü 3 en küçük ikinci değerdir.
3. Adımda 4 ile 5 yer değiştirir. [2,3,4,8,7,9,5,15,6]
4. Adımda ise 8 ile 5 yerdeğiştirir. [2,3,4,5,7,9,8,15,6]

# Merge Sort Projesi

*Merge Sort* bir sıralama yöntemidir. Bu yöntemde her bir adımda diziyi iki parçaya bölerek diziyi küçük parçalara ayırırız. En sonda iki veya daha az sayıda eleman kaldıktan sonra herbir parçayı sıralayarak birleştiririz. En sonunda sıralı bir dizi elde etmiş oluruz.

[16,21,11,8,12,22] dizisini merge sort ile sıralayalım.
1. Adımda dizi iki eşit parçaya bölünür. [16,21,11] [8,12,22]
2. Adımda dizi tekrardan iki parçaya bölünür. [16,21] [11] [8,12] [22]
3. Adımda diziler tekrardan bölünür. [16] [21] [11] [8] [12] [22]
4. Adımda sıralama işlemine geçilir ve sıralama eleman bazında karşılaştırmalı olarak gerçekleştirilir. Yani bir dizinin ilk elemanı ile diğer dizinin ilk elemanından hangisi küçükse önce küçük olan yazılır daha sonra ilk karşılaştırmada diğerinden büyük olan eleman ile diğer dizideki ikinci küçük eleman karşılaştırılır. [16,21] [11] [8,12] [22]
5. Adımda birleştirme işlemine devam edilir. [11,16,21] [8,12,22]
6. Adımda *8 mi küçük 11 mi?* *8 küçüktür. İlk olarak 8 yazılır.*12 mi küçük 11 mi?* *11 küçük önce 11 yazılır.* son birleştirme işlemi de gerçekleştirilir. [8,11,12,16,21,22]

Bölme işlemi esnasında 2^x=ndir. İşlem sayısı x=logn olur. Birleştirme işleminde n tane işlem yapılır. **O(nlogn)** olur.

# Binary Search Tree

*Binary Search Tree* ile hem sıralama hem de arama yapmanız mümkündür. Ayrıca eleman eklemek, çıkarmak ve bulmak oldukça kolaydır.

[7,5,1,8,3,6,0,9,4,2] dizisini ele alalım.
1. Adımda bir kök belirlemeliyiz. Bu kökümüz 5 olsun. Kökün sağında bulunan değer 5ten büyük solunda bulunan değerler 5ten küçük olacaktır. 5in şağında bulunan bubblemız 7 solunda bulunan bubblemız 3 olsun.
2. Adımda seviye ikideki kökleri ele alacağız. 3ün sağında bulunan değer 4 solunda bulunan değer 1dir. 7nin sağında 9 solunda 6 vardır.
3. Adımda seviye üçteki kökleri ele alacağız. 1in sağında 2 solunda 0 vardır. 9uz solunda 8 vardır. Ağaç şu şekildedir.
                    5
            3               7
        1       4       6       9
    0       2               8

Time complexity *average case*de **O(logn)**dir.