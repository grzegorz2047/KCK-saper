/*Gramatyka "Automatyczny Saper" */
/*MIKOLAJ, 2016-10-22*/

/*PRZYKŁADY TESTOWE*/
/*Podnieś skrzynię na 10 m*/
/*Podnieś skrzynię na wysokość 10 metrów*/
/*Podnieś skrzynię o 10.5 metra*/
/*Zegnij ramię o 90 stopni */
/*Rozprostuj ramię o 30 stopni*/

?-rozkaz(A,B,C,[qwertyuio,fghjk,fgggg],[]).
?-rozkaz2(A,B,[qwertyuioadsa,asdaafghjk],[]).

/* OZNACZENIA */
/*
rodzaj czynności:
pd1 - przemieszczanie w górę bomby na określoną wysokość
pd2 - przemieszczanie w górę bomby o określony odcinek
mvf - poruszenie się prosto o określony odcinek
mvb - poruszenie się tył o określony odcinek
obr - obrócenie się w prawo o zadany kąt
obl - obrócenie się w lewo o zadany kąt
tkb - chwycenie bomby
dpb - upuszczenie bomby
set - ustalenie poziomu zagrożenia
det - detonacja ładunku
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

/*SŁOWNIK*/
/*czasownik*/
/*s(<rodzaj_czynności>,<typ_obiektu>,*/
s(pd1,ciężar,wysokość(na),['podnieś'|X],X).
s(pd2,ciężar,wysokość(o),['podnieś'|X],X).
s(mvf,element,długość(o),['pojedźdoprzodu'|X],X).
s(mvb,element,długość(o),['pojedźdotyłu'|X],X).
s(obr,element,kąt(o),['obróćwprawo'|X],X).
s(obl,element,kąt(o),['obróćwlewo'|X],X).
s(tkb,ciężar,['chwyć'|X],X).
s(dpb,ciężar,['upuść'|X],X).
s(set,poziom(na),['ustaw'|X],X).
s(det,ciężar,['zdetonuj'|X],X).



/*rzeczownik*/
s(sk,['skrzynię'|X],X).
s(pk,['paczkę'|X],X).
s(rm,['ramię'|X],X).
s(bmb,['bombę'|X],X).
s(jd,['jeden'|X],X).
s(dw,['dwa'|X],X).
s(tr,['trzy'|X],X).
s(sp,['sapera'|X],X).

jest(sk,ciężar). /*skrzynia jest ciężarem*/
jest(pk,ciężar). /*paczka jest ciężarem*/
jest(rm,element).
jest(bmb,ciężar).
jest(jd,poziom).
jest(dw,poziom).
jest(tr,poziom).
jest(sp,element).

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

/*ROZKAZ*/

rozkaz(A,B,C,Polecenie,[]) :-
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

/* ELEMENTY ROZKAZU */
akcja(A,B,C,X0,X1) :-
    X0=['podnieś'|X1],
    s(A,B,C,X0,X1).

akcja(A,B,C,X0,X1) :-
    X0=['obróćwprawo'|X1],
    s(A,B,C,X0,X1).

akcja(A,B,C,X0,X1) :-
    X0=['obróćwlewo'|X1],
    s(A,B,C,X0,X1).

akcja(A,B,C,X0,X1) :-
    X0=['pojedźdoprzodu'|X1],
    s(A,B,C,X0,X1).

akcja(A,B,C,X0,X1) :-
    X0=['pojedźdotyłu'|X1],
    s(A,B,C,X0,X1).


akcja(A,B,C,X0,X1) :-
    X0=['ustaw'|X1],
    s(A,B,C,X0,X1).

akcja(A,B,C,X0,X1) :-
    X0=['zdetonuj'|X1],
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
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).

/*na wysokość 10 m */
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

/*na długość 10 m */
	parametry_akcji(długość(na),dys(W,M),['na','długość',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(długość(na),dys(W,M),['na',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
miara(M,X1,X2).
parametry_akcji(długość(o),dys_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	
/*parametry_akcji(kąt(o),kąt_wzgl(W,M),['o',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
parametry_akcji(kąt(o),kąt_wzgl(W,M),['o','kąt',W|X1],X2) :-
    s(liczba(W),[W|X1],X1),
    miara(M,X1,X2).
	*/

	/*ROZKAZ2*/
	
	rozkaz2(A,B,Polecenie,[]) :-
    akcja(A,B1,Polecenie,X1),
    obiekt(B1,B,X1,X2).
	
	/* ELEMENTY ROZKAZU */
	
	akcja(A,B,X0,X1) :-
    X0=['chwyć'|X1],
    s(A,B,X0,X1).
	
	obiekt(B1,B,X0,X1):-
    X0=['bombę'|X1],
    s(B,X0,X1),
    jest(B,B1).
	
	
akcja(A,B,X0,X1) :-
    X0=['upuść'|X1],
    s(A,B,X0,X1).
	
	
	obiekt(B1,B,X0,X1):-
    X0=['sapera'|X1],
    s(B,X0,X1),
    jest(B,B1).
