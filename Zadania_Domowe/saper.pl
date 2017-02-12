/*Gramatyka "Automatyczny Saper" */
/* Rozszerzenie przykładu z ćwiczeń - Mikołaj Balcerek */
/*Przykłady wykorzystania

rozkaz(A,B,[chwyć,bombę],[]).
rozkaz(A,B,C,[podnieś,bombę,o,20,m],[]).

Nie zadziałaja, jeżeli nie zgadza się A,B,C.
Poprawi jednoliterowe zmiany, np. Podnieś na podnieś. Komunikat to ostatnia linia wyjścia: Podnieś = podnieś.

*/


/* SKŁADNIA */

?-rozkaz(A,B,C,[nazwafunkcji,obiekt,parametr],[]).
?-rozkaz(A,B,[nazwafunkcji,obiekt],[]).




/* Oznaczenia

rodzaj czynności:

liftna - przemieszczanie w górę bomby na określoną wysokość
lifto - przemieszczanie w górę bomby o określony odcinek
move - poruszanie się B (przód, tył) o określoną długość
rotate - obrócenie (prawo,lewo)się w prawo o zadany kąt
takebomb - chwycenie bomby
dropbomb - upuszczenie bomby
set_danger - ustalenie poziomu zagrożenia
detonate - detonacja ładunku


typ obiektu:
ciężar /przykłady:skrzynia, paczka, bomba/
sk is ciężar  /skrzynia jest ciężarem/
bmb is ciężar /bomba jest ciężarem/
rm is element /ramię jest elementem/
ko is element /koło jest elementem/
jd is poziom /jeden jest poziomem/
dw is poziom /dwa jest poziomem/
sp is element 
tr is poziom /trzy jest poziomem/
*/



/*Słownik */
/*funkcje, czasowniki 
s(<rodzaj_czynności>,<typ_obiektu>,<parametr>)*/


s(liftna,ciężar,wysokość(na),['podnieś'|X],X).
s(lifto,ciężar,wysokość(o),['podnieś'|X],X).
s(move,kierunek,długość(o),['pojedź'|X],X).
s(rotate,rotatekierunek,kąt(o),['obróć'|X],X).
s(takebomb,ciężar,['chwyć'|X],X).
s(dropbomb,ciężar,['upuść'|X],X).
s(set_danger,poziom(na),['ustaw'|X],X).
s(detonate,ciężar,['zdetonuj'|X],X).



/*rzeczownik*/

s(sk,['skrzynię'|X],X).
s(pk,['paczkę'|X],X).
s(rm,['ramię'|X],X).
s(bmb,['bombę'|X],X).
s(bmb,['bomba'|X],X).
s(bmb,['bombie'|X],X).
s(jd,['jeden'|X],X).
s(dw,['dwa'|X],X).
s(tr,['trzy'|X],X).
s(sp,['sapera'|X],X).
s(przód,['przód'|X],X).
s(tył,['tył'|X],X).
s(tył,['tyłu'|X],X).
s(przód,['przodu'|X],X).
s(przód,['do','przodu'|X],X).
s(tył,['do','tyłu'|X],X).
s(lewo,['lewo'|X],X).
s(prawo,['prawo'|X],X).

jest(sk,ciężar). /*skrzynia jest ciężarem*/
jest(pk,ciężar). /*paczka jest ciężarem*/
jest(rm,element).
jest(bmb,ciężar).
jest(jd,poziom).
jest(dw,poziom).
jest(tr,poziom).
jest(sp,element).
jest(przód,kierunek).
jest(tył,kierunek).
jest(lewo,rotatekierunek).
jest(prawo,rotatekierunek).

s(j_miary(metry),['m'|X],X).
s(j_miary(metry),['metr'|X],X).
s(j_miary(metry),['metra'|X],X).
s(j_miary(metry),['metry'|X],X).
s(j_miary(metry),['metrów'|X],X).
s(j_miary(stopnie),['st'|X],X).
s(j_miary(stopnie),['stopień'|X],X).
s(j_miary(stopnie),['stopnia'|X],X).
s(j_miary(stopnie),['stopnie'|X],X).
s(j_miary(stopnie),['stopni'|X],X).

miara(M,X0,X1) :- s(j_miary(M),X0,X1).

s(liczba(L),[L|X],X) :- number(L).
/* number rozpoznaje liczby całkowite oraz dziesiętne dodatnie i ujemne */

/*ROZKAZ z parametrami funkcja,obiekt/kierunek,parametr*/

rozkaz(A,B,C,Polecenie,[]) :-
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

akcja(A,B,C,X0,X1) :-
    X0=['podnieś'|X1],
    s(A,B,C,X0,X1).
	
akcja(A,B,C,X0,X1) :-
    X0=['pojedź'|X1],
    s(A,B,C,X0,X1).
		
	akcja(A,B,C,X0,X1) :-
	X0=['obróć'|X1],
    s(A,B,C,X0,X1).
	

obiekt(B1,B,X0,X1):-
    X0=['skrzynię'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bombę'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['bomba'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	
	obiekt(B1,B,X0,X1):-
    X0=['bombie'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
obiekt(B1,B,X0,X1):-
    X0=['przód'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['prawo'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['lewo'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	
obiekt(B1,B,X0,X1):-
    X0=['tył'|X1],
    s(B,X0,X1),
    jest(B,B1).
	

	obiekt(B1,B,X0,X1):-
    X0=['do','przodu'|X1],
    s(B,X0,X1),
    jest(B,B1)
	

	obiekt(B1,B,X0,X1):-
    X0=['do','tyłu'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['do'|X1],
    s(B,X0,X1),
    jest(B,B1).
	


parametry_akcji(wysokość(na),wys(W,M),['na','wysokość',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(wysokość(na),wys(W,M),['na',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
miara(M,X1,X2).
parametry_akcji(wysokość(o),wys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(kąt(o),kąt_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).

parametry_akcji(kąt(o),kąt_wzgl(W,M),['o','kąt',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	
parametry_akcji(długość(o),dys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	



	/*ROZKAZ funkcja,obiekt*/
	
	rozkaz(A,B,Polecenie,[]) :-
    akcja(A,B1,Polecenie,X1),
    obiekt(B1,B,X1,X2).
	
	akcja(A,B,X0,X1) :-
    X0=['chwyć'|X1],
    s(A,B,X0,X1).
	
	akcja(A,B,X0,X1) :-
    X0=['upuść'|X1],
    s(A,B,X0,X1).
	
	obiekt(B1,B,X0,X1):-
    X0=['skrzynię'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bombę'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
 
	
	

	
