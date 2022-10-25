# Insertion Sort Projesi

'Insertion Sort' bir sıralama yöntemidir. Bu yöntemde 0. indexten başlayarak herbir index kendinden sonra gelen en küçük sayı ile yerdeğiştirerek sıralanır.

[22,27,16,2,18,6] dizisini insertion sort'a göre sıralayalım.
1. Adımda 0. index(22) en küçük sayı ile yer değiştirir. En küçük sayı 2dir. Sıralama şöyledir: [2,27,16,22,18,6]. 0. indexe en küçük sayı taşınmış olup 0. index sıralanmıştır. Bu adımda "n" tane işlem yapılmıştır.
2. Adımda 1. index(27) sıralanır. İkinci en küçük değer 6dır. Sıralama şöyle olur: [2,6,16,22,18,27]. 1. indexe ikinci en küçük sayı taşınmış olup 1. index sıralanmıştır. Bu adımda (n-1) tane işlem yapılmıştır.
3. Adımda 2. index(16) sıralanır. Bu değer dizideki en küçük değer olduğu için yeri değişmeyip sıralanmış olur. Bu adımda (n-2) tane işlem yapılmıştır.
4. Adımda 3. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-3) tane işlem yapılmıştır.
5. Adımda 4. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-4) tane işlem yapılmıştır.
6. Adımda 5. index sıralanır. [2,6,16,18,22,27]. Bu adımda (n-5) tane yani 1 tane işlem yapılmıştır.

Yukarıdaki örnekte de görüldüğü gibi işlem sayısı n'den başlayarak 1'e kadar olan sayıların toplamı kadardır. Toplam İşlem sayısı `n*(n-1)/2` kadardır. Buradan da O(n^2) olur.

"18" değeri sıralı dizide ortada bulunduğundan dolayı case'i **average**dır.

[7,3,5,8,2,9,4,15,6] bu dizinin ilk dört adımdaki sıralanışına bakalım.
1. Adımda 2 ile 7 yer değiştirir. [2,3,5,8,7,9,4,15,6]
2. Aadımda sıralama değişmez çünkü 3 en küçük ikinci değerdir.
3. Adımda 4 ile 5 yer değiştirir. [2,3,4,8,7,9,5,15,6]
4. Adımda ise 8 ile 5 yerdeğiştirir. [2,3,4,5,7,9,8,15,6]