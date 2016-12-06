# KCK-saper
email naglowek:
KCK-sr-SAPER-Data

Wymagania/Requirements:

 - Środowisko/Enviroment: python 2.7
 - Biblioteka/Library: pygame
 - Opcjonalnie/Optional: pycharm
 - Opcjonalnie biblioteka/Optional library: cx_freeze 
===== 
Założenia:
- Poł-automatyczne poruszanie się do celu, który został wyznaczony
- Automatyczne znajdowanie celu
- Rozpoznanie celu, rozbrojenie celu lub zdetonowanie w bezpiecznym miejscu(w razie niebezpiecznego miejsca, przewieść w bezpieczną lokalizację)
- okienko z wynikiem 
- lokalizacje z danymi właściwościami typu "bezpieczne", "miejsce z możliwością detonacji", 

=====
Raporty przyrostowe
opis postępu w danym tygodniu
zamierzenia na najbliższy okres
cel uzasadnić argumentem
w razie nieukończenia jakiegoś postępu uzasadnić dlaczego

=====
Lista umiejętności sapera:

poruszanie się
obracanie się 
przenoszenie
rozpoznawanie bomb wg zagrożenia
przyjmowanie poleceń
przetwarzanie poleceń
rozpoznawanie cech otoczenia

=====
Propozycja przetwarzania języka

1. Wyszukiwanie typu akcji wykorzystując słownik np. podnieś, bierze

2. Znalezienie szablonu do danej akcji (wyszukanie wymaganych informacji typu odległość, czas)

3. Dodanie do kolejki znalezioną akcję wraz ze szczegółami, aby zachować kolejność wykonania polecenia np. jedź do przodu a potem skręć w prawo

Albo inaczej:

Szukasz w zdaniu słowa czasownika, jest np. podnieś, masz napisane że podnieś bierze obiekt i odległość, szukasz w zdaniu obiekt i odległość?

=====
Inne 

Będą znajdowały się tam różne przeszkody typu krzesła, stół, szafki itd.
Saper będzie napotykał przeszkody i je rozpoznawał poprzez pewne właściwości typu kolor
Możliwość obrotu i poruszania w pewnym kierunku przez określony czas

