/*Gramatyka "Automatyczny Saper" */

/*Przyk³ady wykorzystania

rozkaz(A,B,[chwyæ,bombê],[]).
rozkaz(A,B,C,[podnieœ,bombê,o,20,m],[]).

Nie zadzia³aja, je¿eli nie zgadza siê A,B,C.
Poprawi jednoliterowe zmiany, np. Podnieœ na podnieœ. Komunikat to ostatnia linia wyjœcia: Podnieœ = podnieœ.

*/


/* SK£ADNIA */

?-rozkaz(A,B,C,[nazwafunkcji,obiekt,parametr],[]).
?-rozkaz(A,B,[nazwafunkcji,obiekt],[]).




/* Oznaczenia

rodzaj czynnoœci:

liftna - przemieszczanie w górê bomby na okreœlon¹ wysokoœæ
lifto - przemieszczanie w górê bomby o okreœlony odcinek
move - poruszanie siê B (przód, ty³) o okreœlon¹ d³ugoœæ
rotate - obrócenie (prawo,lewo)siê w prawo o zadany k¹t
takebomb - chwycenie bomby
dropbomb - upuszczenie bomby
set_danger - ustalenie poziomu zagro¿enia
detonate - detonacja ³adunku


typ obiektu:
ciê¿ar /przyk³ady:skrzynia, paczka, bomba/
sk is ciê¿ar  /skrzynia jest ciê¿arem/
bmb is ciê¿ar /bomba jest ciê¿arem/
rm is element /ramiê jest elementem/
ko is element /ko³o jest elementem/
jd is poziom /jeden jest poziomem/
dw is poziom /dwa jest poziomem/
sp is element 
tr is poziom /trzy jest poziomem/
*/



/*S³ownik */
/*funkcje, czasowniki 
s(<rodzaj_czynnoœci>,<typ_obiektu>,<parametr>)*/


s(liftna,ciê¿ar,wysokoœæ(na),['podnieœ'|X],X).
s(lifto,ciê¿ar,wysokoœæ(o),['podnieœ'|X],X).
s(move,kierunek,d³ugoœæ(o),['pojedŸ'|X],X).
s(rotate,rotatekierunek,k¹t(o),['obróæ'|X],X).
s(takebomb,ciê¿ar,['chwyæ'|X],X).
s(dropbomb,ciê¿ar,['upuœæ'|X],X).
s(set_danger,poziom(na),['ustaw'|X],X).
s(detonate,ciê¿ar,['zdetonuj'|X],X).



/*rzeczownik*/

s(sk,['skrzyniê'|X],X).
s(pk,['paczkê'|X],X).
s(rm,['ramiê'|X],X).
s(bmb,['bombê'|X],X).
s(bmb,['bomba'|X],X).
s(bmb,['bombie'|X],X).
s(jd,['jeden'|X],X).
s(dw,['dwa'|X],X).
s(tr,['trzy'|X],X).
s(sp,['sapera'|X],X).
s(przód,['przód'|X],X).
s(ty³,['ty³'|X],X).
s(ty³,['ty³u'|X],X).
s(przód,['przodu'|X],X).
s(przód,['do','przodu'|X],X).
s(ty³,['do','ty³u'|X],X).
s(lewo,['lewo'|X],X).
s(prawo,['prawo'|X],X).

jest(sk,ciê¿ar). /*skrzynia jest ciê¿arem*/
jest(pk,ciê¿ar). /*paczka jest ciê¿arem*/
jest(rm,element).
jest(bmb,ciê¿ar).
jest(jd,poziom).
jest(dw,poziom).
jest(tr,poziom).
jest(sp,element).
jest(przód,kierunek).
jest(ty³,kierunek).
jest(lewo,rotatekierunek).
jest(prawo,rotatekierunek).

s(j_miary(metry),['m'|X],X).
s(j_miary(metry),['metr'|X],X).
s(j_miary(metry),['metra'|X],X).
s(j_miary(metry),['metry'|X],X).
s(j_miary(metry),['metrów'|X],X).
s(j_miary(stopnie),['st'|X],X).
s(j_miary(stopnie),['stopieñ'|X],X).
s(j_miary(stopnie),['stopnia'|X],X).
s(j_miary(stopnie),['stopnie'|X],X).
s(j_miary(stopnie),['stopni'|X],X).

miara(M,X0,X1) :- s(j_miary(M),X0,X1).

s(liczba(L),[L|X],X) :- number(L).
/* number rozpoznaje liczby ca³kowite oraz dziesiêtne dodatnie i ujemne */

/*ROZKAZ z parametrami funkcja,obiekt/kierunek,parametr*/

rozkaz(A,B,C,Polecenie,[]) :-
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

akcja(A,B,C,X0,X1) :-
    X0=['podnieœ'|X1],
    s(A,B,C,X0,X1).
	
akcja(A,B,C,X0,X1) :-
    X0=['pojedŸ'|X1],
    s(A,B,C,X0,X1).
		
	akcja(A,B,C,X0,X1) :-
	X0=['obróæ'|X1],
    s(A,B,C,X0,X1).
	

obiekt(B1,B,X0,X1):-
    X0=['skrzyniê'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bombê'|X1],
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
    X0=['ty³'|X1],
    s(B,X0,X1),
    jest(B,B1).
	

	obiekt(B1,B,X0,X1):-
    X0=['do','przodu'|X1],
    s(B,X0,X1),
    jest(B,B1)
	

	obiekt(B1,B,X0,X1):-
    X0=['do','ty³u'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['do'|X1],
    s(B,X0,X1),
    jest(B,B1).
	


parametry_akcji(wysokoœæ(na),wys(W,M),['na','wysokoœæ',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(wysokoœæ(na),wys(W,M),['na',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
miara(M,X1,X2).
parametry_akcji(wysokoœæ(o),wys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(k¹t(o),k¹t_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).

parametry_akcji(k¹t(o),k¹t_wzgl(W,M),['o','k¹t',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	
parametry_akcji(d³ugoœæ(o),dys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	



	/*ROZKAZ funkcja,obiekt*/
	
	rozkaz(A,B,Polecenie,[]) :-
    akcja(A,B1,Polecenie,X1),
    obiekt(B1,B,X1,X2).
	
	akcja(A,B,X0,X1) :-
    X0=['chwyæ'|X1],
    s(A,B,X0,X1).
	
	akcja(A,B,X0,X1) :-
    X0=['upuœæ'|X1],
    s(A,B,X0,X1).
	
	obiekt(B1,B,X0,X1):-
    X0=['skrzyniê'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bombê'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
 
	
	

	