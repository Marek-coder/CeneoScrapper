# CeneoScrapper
## Etap 1 - Analiza struktury opinii w serwisie [Ceneo.pl] (https://www.ceneo.pl/)
|Składowa                |Selektor                                        |Nazwa zmiennej|
|------------------------|------------------------------------------------|--------------|
|opinia                  |li.js_product-review                            |opinion	 |
|identyfikator opinii    |["data-entry-id"]                               |opinion_id    |
|autor                   |div.reviewer-name-line                          |author	 |
|rekomendacja            |div.product-review-summary > em                 |recommendation|
|ocena                   |span.review-score-count                         |stars  	 |
|treść opinii            |p.product-review-body                           |content	 |
|lista wad               |div.cons-cell > ul                              |cons	 	 |
|lista zalet             |div.pros-cell > ul                              |pros		 |
|przydatna               |button.vote-yes > span                          |useful	 |
|nieprzydatna            |button.vote-no > span                           |useless	 |
|data wystawienia opinii |span.review-time > time:first-child["datetime"] |opinion_date	 |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"]|purchase_date |

## Etap2 - pobranie składowych pojedynczej opinii biblioteka() http request)
## pobranie kodu jednej strony z opiniami o  konkretnym produkcie
## wyciągnięcie z kodu strony fragmentów odpowiadających poszczególnym opiniom(beautyfull)
## zapisanie do pojedynczych zmiennych wartosci poszczegolnych skladowych opinii(date frame pandas)
## parametr -a dziala tylko przy zmieniancyh plikach nie nowych
## etap3 pobranie wszystkich opini o pojedynczym produkcie
## przechodzenie po kolejnych stronach z opiniami
## zapis wszystkich opinii o pojedynczym produkcie do pliku
## etap 4
#	Wyczyszczenie danych i transformacja
#    refaktorin kodu(usuniecie powtarzajacego sie kodu)
#	przerobic to by pobierac opinie dla dowolnego produktu
	