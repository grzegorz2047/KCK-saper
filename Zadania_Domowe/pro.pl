/*Gramatyka "Automatyczny Saper" */
/* Rozszerzenie slownika  z cwiczen - Mikolaj Balcerek */

/*Przyk�ady wykorzystania

rozkaz(A,B,[chwy�,bomb�],[]).
rozkaz(A,B,C,[podnie�,bomb�,o,20,m],[]).

Nie zadzia�aja, je�eli nie zgadza si� A,B,C.
Poprawi jednoliterowe zmiany, np. Podnie� na podnie�. Komunikat to ostatnia linia wyj�cia: Podnie� = podnie�.

*/


/* SK�ADNIA */

?-rozkaz(A,B,C,[nazwafunkcji,obiekt,parametr],[]).
?-rozkaz(A,B,[nazwafunkcji,obiekt],[]).




/* Oznaczenia

rodzaj czynno�ci:

liftna - przemieszczanie w g�r� bomby na okre�lon� wysoko��
lifto - przemieszczanie w g�r� bomby o okre�lony odcinek
move - poruszanie si� B (prz�d, ty�) o okre�lon� d�ugo��
rotate - obr�cenie (prawo,lewo)si� w prawo o zadany k�t
takebomb - chwycenie bomby
dropbomb - upuszczenie bomby
set_danger - ustalenie poziomu zagro�enia
detonate - detonacja �adunku


typ obiektu:
ci�ar /przyk�ady:skrzynia, paczka, bomba/
sk is ci�ar  /skrzynia jest ci�arem/
bmb is ci�ar /bomba jest ci�arem/
rm is element /rami� jest elementem/
ko is element /ko�o jest elementem/
jd is poziom /jeden jest poziomem/
dw is poziom /dwa jest poziomem/
sp is element 
tr is poziom /trzy jest poziomem/
*/



/*S�ownik */
/*funkcje, czasowniki 
s(<rodzaj_czynno�ci>,<typ_obiektu>,<parametr>)*/


s(liftna,ci�ar,wysoko��(na),['podnie�'|X],X).
s(lifto,ci�ar,wysoko��(o),['podnie�'|X],X).
s(move,kierunek,d�ugo��(o),['pojed�'|X],X).
s(rotate,rotatekierunek,k�t(o),['obr��'|X],X).
s(takebomb,ci�ar,['chwy�'|X],X).
s(dropbomb,ci�ar,['upu��'|X],X).
s(set_danger,poziom(na),['ustaw'|X],X).
s(detonate,ci�ar,['zdetonuj'|X],X).



/*rzeczownik*/

s(sk,['skrzyni�'|X],X).
s(pk,['paczk�'|X],X).
s(rm,['rami�'|X],X).
s(bmb,['bomb�'|X],X).
s(bmb,['bomba'|X],X).
s(bmb,['bombie'|X],X).
s(jd,['jeden'|X],X).
s(dw,['dwa'|X],X).
s(tr,['trzy'|X],X).
s(sp,['sapera'|X],X).
s(prz�d,['prz�d'|X],X).
s(ty�,['ty�'|X],X).
s(ty�,['ty�u'|X],X).
s(prz�d,['przodu'|X],X).
s(prz�d,['do','przodu'|X],X).
s(ty�,['do','ty�u'|X],X).
s(lewo,['lewo'|X],X).
s(prawo,['prawo'|X],X).

jest(sk,ci�ar). /*skrzynia jest ci�arem*/
jest(pk,ci�ar). /*paczka jest ci�arem*/
jest(rm,element).
jest(bmb,ci�ar).
jest(jd,poziom).
jest(dw,poziom).
jest(tr,poziom).
jest(sp,element).
jest(prz�d,kierunek).
jest(ty�,kierunek).
jest(lewo,rotatekierunek).
jest(prawo,rotatekierunek).

s(j_miary(metry),['m'|X],X).
s(j_miary(metry),['metr'|X],X).
s(j_miary(metry),['metra'|X],X).
s(j_miary(metry),['metry'|X],X).
s(j_miary(metry),['metr�w'|X],X).
s(j_miary(stopnie),['st'|X],X).
s(j_miary(stopnie),['stopie�'|X],X).
s(j_miary(stopnie),['stopnia'|X],X).
s(j_miary(stopnie),['stopnie'|X],X).
s(j_miary(stopnie),['stopni'|X],X).

miara(M,X0,X1) :- s(j_miary(M),X0,X1).

s(liczba(L),[L|X],X) :- number(L).
/* number rozpoznaje liczby ca�kowite oraz dziesi�tne dodatnie i ujemne */

/*ROZKAZ z parametrami funkcja,obiekt/kierunek,parametr*/

rozkaz(A,B,C,Polecenie,[]) :-
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

akcja(A,B,C,X0,X1) :-
    X0=['podnie�'|X1],
    s(A,B,C,X0,X1).
	
akcja(A,B,C,X0,X1) :-
    X0=['pojed�'|X1],
    s(A,B,C,X0,X1).
		
	akcja(A,B,C,X0,X1) :-
	X0=['obr��'|X1],
    s(A,B,C,X0,X1).
	

obiekt(B1,B,X0,X1):-
    X0=['skrzyni�'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bomb�'|X1],
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
    X0=['prz�d'|X1],
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
    X0=['ty�'|X1],
    s(B,X0,X1),
    jest(B,B1).
	

	obiekt(B1,B,X0,X1):-
    X0=['do','przodu'|X1],
    s(B,X0,X1),
    jest(B,B1)
	

	obiekt(B1,B,X0,X1):-
    X0=['do','ty�u'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['do'|X1],
    s(B,X0,X1),
    jest(B,B1).
	


parametry_akcji(wysoko��(na),wys(W,M),['na','wysoko��',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(wysoko��(na),wys(W,M),['na',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
miara(M,X1,X2).
parametry_akcji(wysoko��(o),wys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(k�t(o),k�t_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).

parametry_akcji(k�t(o),k�t_wzgl(W,M),['o','k�t',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	
parametry_akcji(d�ugo��(o),dys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	



	/*ROZKAZ funkcja,obiekt*/
	
	rozkaz(A,B,Polecenie,[]) :-
    akcja(A,B1,Polecenie,X1),
    obiekt(B1,B,X1,X2).
	
	akcja(A,B,X0,X1) :-
    X0=['chwy�'|X1],
    s(A,B,X0,X1).
	
	akcja(A,B,X0,X1) :-
    X0=['upu��'|X1],
    s(A,B,X0,X1).
	
	obiekt(B1,B,X0,X1):-
    X0=['skrzyni�'|X1],
    s(B,X0,X1),
    jest(B,B1).

	obiekt(B1,B,X0,X1):-
    X0=['bomb�'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	obiekt(B1,B,X0,X1):-
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
 
	
	

	