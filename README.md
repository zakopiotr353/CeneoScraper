# CeneoScraper
# CeneoScraper
## Selektory CSS składowych opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

| Składowa | Nazwa | Selektor |
| --- | --- | --- |
| opinia | opinion/single\_opinion | div.js\_product-review |
| identyfikator opinii | opinion\_id | [data-entry-id] |
| autor | author | span.user-post\_\_author-name |
| rekomendacja | recommendation | span.user-post\_\_author-recomendation \> em |
| liczba gwiazdek | stars | span.user-post\_\_score-countspan.score-marker[style] |
| czy opinia jest potwierdzona zakupem | purchased | div.review-pz |
| data wystawienia opinii | opinion\_date | span.user-post\_\_published \> time:nth\_child(1)[datetime] |
| data zakupu produktu | purchase\_date | span.user-post\_\_published \> time:nth\_child(2)[datetime] |
| ile osób uznało opinię za przydatną | usefull\_count | button.vote-yes[data-total-vote]button.vote-yes \> span |
| ile osób uznało opinię za nieprzydatną | unusefull\_count | button.vote-no[data-total-vote]button.vote-no \> span |
| treść opinii | content | div.user-post\_\_text |
| listę zalet | pros | div.review-feature\_\_title--positives ~ div.review-feature\_\_item |
| listę wad | cons | div.review-feature\_\_title--negatives ~ div.review-feature\_\_item |