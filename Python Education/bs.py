from bs4 import BeautifulSoup

kod="""""<!doctype html>
<html>
<head>
<meta charset="utf-8">
    <title>Liste Örnekleri-1</title>
</head>
    <body>
    <ol>
        <li>
            SICAK İÇECEKLER
            <ol type="I">
                <li>ÇAY</li>
                <li>KAHVE</li>
                    <ol type="a">
                        <li>TÜRK KAHVESİ</li>
                        <li>NESCAFE</li>
                    </ol>
                <li>SICAK ÇİKOLATA</li>
            </ol>
        </li>
        
        <li>
            SOĞUK İÇECEKLER
            <ol>
                <li>MEYVE SULARI
                    <ul>
                        <li>Vişne</li>
                        <li>Şeftali</li>
                        <li>Kayısı</li>
                        <li>Elma</li>
                    </ul>
                </li>
                
                <li>
                    LİMONATA
                </li>
            </ol>
        </li>
    </ol>
    
    </body>
</html>"""""

parset=BeautifulSoup(kod,"html.parser") #analiz

yaz=parset.prettify() #karmaşık kodları düzenler.

#print(yaz)

yaz2=parset.title

#print(yaz2)

#sadece etiket ismini istiyorsak #52.satırdaki kodun yanına .name yazılır

yaz3=parset.ol.findParent

print(yaz3)

#eğerki name i değile içineki bilgiler almak istiyorsak(alt)

yaz4=parset.title.string

#print(yaz4)

yaz5=parset.find_all("li") #parset.li yaparsak sadece sıcaklar çıkıyor
#liste yapar
#print(yaz5)

yaz6=parset.find_all("li")[0].ol.li #li alanından li'nin sıfırıncı indeksinden ilk yakaladığın ol etiketini getir
# print(yaz6)


