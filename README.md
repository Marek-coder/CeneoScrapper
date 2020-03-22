# CeneoScrapper
## Etap 1 - Analiza struktury opinii w serwisie [Ceneo.pl] (https://www.ceneo.pl/)
|Składowa                |Selektor                                        |Nazwa zmiennej|
|------------------------|------------------------------------------------|--------------|
|opinia                  |li.js_product-review                            |
|identyfikator opinii    |["data-entry-id"]                               |
|autor                   |div.reviewer-name-line                          |
|rekomendacja            |div.product-review-summary > em                 |
|ocena                   |span.review-score-count                         |
|treść opinii            |p.product-review-body                           |
|lista wad               |div.cons-cell > ul                              |
|lista zalet             |div.pros-cell > ul                              |
|przydatna               |button.vote-yes > span                          |
|nieprzydatna            |button.vote-no > span                           |
|data wystawienia opinii |span.review-time > time:first-child["datetime"] |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"]|

## Etap2 - pobranie składowych pojedynczej opinii biblioteka() http request)
## pobranie kodu jednej strony z opiniami o  konkretnym produkcie
## wyciągnięcie z kodu strony fragmentów odpowiadających poszczególnym opiniom(beautyfull)
## zapisanie do pojedynczych zmiennych wartosci poszczegolnych skladowych opinii(date frame pandas)
## parametr -a dziala tylko przy zmieniancyh plikach nie nowych