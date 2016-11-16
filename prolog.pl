
/*Gramatyka "DWIG" */
/*ZV, 2016-10-08*/

/*PRZYK£ADY TESTOWE*/
/*Podnieœ skrzyniê na 10 m*/
/*Podnieœ skrzyniê na wysokoœæ 10 metrów*/
/*Podnieœ skrzyniê o 10.5 metra*/
/*Zegnij ramiê o 90 stopni */
/*Rozprostuj ramiê o 30 stopni*/

?-rozkaz(A,B,C,[qwertyuio,fghjk,fgggg],[]).

/* OZNACZENIA */
/*
rodzaj czynnoœci:
pd1 - przemieszczanie w górê ciê¿aru na okreœlon¹ wysokoœæ
pd2 - przemieszczanie w górê ciê¿aru o okreœlony odcinek
zg - zmniejszenie k¹ta rozwarcia o okreœlon¹ wielkoœæ
rzw - zwiêkszenie k¹ta rozwarcia o okreœlon¹ wielkoœæ
typ obiektu:
ciê¿ar /przyk³ady:skrzynia, paczka/
sk is ciê¿ar  /skrzynia jest ciê¿arem/
pk is ciê¿ar /paczka jest ciê¿arem/
rm is element /ramiê jest elementem/
*/

/*S£OWNIK*/
/*czasownik*/
/*s(<rodzaj_czynnoœci>,<typ_obiektu>,*/
s(pd1,ciê¿ar,wysokoœæ(na),['podnieœ'|X],X).
s(pd2,ciê¿ar,wysokoœæ(o),['podnieœ'|X],X).
s(zg,element,k¹t(o),['zegnij'|X],X).
s(wypr,element,k¹t(o),['rozprostuj'|X],X).

/*rzeczownik*/
s(sk,['skrzyniê'|X],X).
s(pk,['paczkê'|X],X).
s(rm,['ramiê'|X],X).
jest(sk,ciê¿ar). /*skrzynia jest ciê¿arem*/
jest(pk,ciê¿ar). /*paczka jest ciê¿arem*/
jest(rm,element).

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

/*ROZKAZ*/

rozkaz(A,B,C,Polecenie,[]) :- 
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

/* ELEMENTY ROZKAZU */
akcja(A,B,C,X0,X1) :-
    X0=['podnieœ'|X1],
    s(A,B,C,X0,X1).
akcja(A,B,C,X0,X1) :-
    X0=['zegnij'|X1],
    s(A,B,C,X0,X1).
akcja(A,B,C,X0,X1) :-
    X0=['rozprostuj'|X1],
    s(A,B,C,X0,X1).

obiekt(B1,B,X0,X1):-
    X0=['skrzyniê'|X1],
    s(B,X0,X1),
    jest(B,B1).
obiekt(B1,B,X0,X1):-
    X0=['ramiê'|X1],
    s(B,X0,X1),
    jest(B,B1).

/*na wysokoœæ 10 m */
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