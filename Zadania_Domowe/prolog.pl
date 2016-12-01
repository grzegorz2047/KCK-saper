
/*Gramatyka "D�WIG" */
/*ZV, 2016-10-08*/

/*PRZYK�ADY TESTOWE*/
/*Podnie� skrzyni� na 10 m*/
/*Podnie� skrzyni� na wysoko�� 10 metr�w*/
/*Podnie� skrzyni� o 10.5 metra*/
/*Zegnij rami� o 90 stopni */
/*Rozprostuj rami� o 30 stopni*/

?-rozkaz(A,B,C,[qwertyuio,fghjk,fgggg],[]).

/* OZNACZENIA */
/*
rodzaj czynno�ci:
pd1 - przemieszczanie w g�r� ci�aru na okre�lon� wysoko��
pd2 - przemieszczanie w g�r� ci�aru o okre�lony odcinek
zg - zmniejszenie k�ta rozwarcia o okre�lon� wielko��
rzw - zwi�kszenie k�ta rozwarcia o okre�lon� wielko��
typ obiektu:
ci�ar /przyk�ady:skrzynia, paczka/
sk is ci�ar  /skrzynia jest ci�arem/
pk is ci�ar /paczka jest ci�arem/
rm is element /rami� jest elementem/
*/

/*S�OWNIK*/
/*czasownik*/
/*s(<rodzaj_czynno�ci>,<typ_obiektu>,*/
s(pd1,ci�ar,wysoko��(na),['podnie�'|X],X).
s(pd2,ci�ar,wysoko��(o),['podnie�'|X],X).
s(zg,element,k�t(o),['zegnij'|X],X).
s(wypr,element,k�t(o),['rozprostuj'|X],X).

/*rzeczownik*/
s(sk,['skrzyni�'|X],X).
s(pk,['paczk�'|X],X).
s(rm,['rami�'|X],X).
jest(sk,ci�ar). /*skrzynia jest ci�arem*/
jest(pk,ci�ar). /*paczka jest ci�arem*/
jest(rm,element).

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

/*ROZKAZ*/

rozkaz(A,B,C,Polecenie,[]) :- 
    akcja(A,B1,C1,Polecenie,X1),
    obiekt(B1,B,X1,X2),
    parametry_akcji(C1,C,X2,[]).

/* ELEMENTY ROZKAZU */
akcja(A,B,C,X0,X1) :-
    X0=['podnie�'|X1],
    s(A,B,C,X0,X1).
akcja(A,B,C,X0,X1) :-
    X0=['zegnij'|X1],
    s(A,B,C,X0,X1).
akcja(A,B,C,X0,X1) :-
    X0=['rozprostuj'|X1],
    s(A,B,C,X0,X1).

obiekt(B1,B,X0,X1):-
    X0=['skrzyni�'|X1],
    s(B,X0,X1),
    jest(B,B1).
obiekt(B1,B,X0,X1):-
    X0=['rami�'|X1],
    s(B,X0,X1),
    jest(B,B1).

/*na wysoko�� 10 m */
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