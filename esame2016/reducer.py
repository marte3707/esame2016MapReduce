#!/usr/bin/python
# -*- coding: utf-8 -*-

#------UTILIZZO------#
#echo data.txt | ./mapper.py | sort -k1,1 | ./reducer.py
#------        ------#


from operator import itemgetter
import sys

#creo delle variabili temporanee che mi serviranno per il reducer e altre che faranno da contatori
parola_corrente = None
counter = 0
parola = None

#l'input proviene sempre da STDIN
for line in sys.stdin:
    #per ogni nuova riga rimuovo spazi e tabulazioni
    line = line.strip()
    #parse dell'input proveniente da mapper.py
    #indichiamo che c'è una tabulazione
    parola, count = line.split('\t', 1)
    #dobbiamo convertire il count in un intero perché al momento è un dato tipo String
    try:
        count = int(count)
    except ValueError:
        #se count non è un numero quindi ignora questo elemento
        continue

    #il primo giro parola_corrente è None quindi passo all'else
    if parola_corrente == parola:
        counter += count
    else:
        #al primo giro è ancora None quindi passo sotto
        #mi assicuro che l'anno sia 2016, confronto la stringa contenuta in parola_corrente con 2016
        if parola_corrente and parola_corrente == '2016':
            #scrivi risultato su STDOUT
            print '%s\t%s' % (parola_corrente, counter)
        #memorizzo dentro le variabili create in precedenza i nuovi valori e passo all'if iniziale
        #che controllerà se esiste già un'occorrenza uguale e in quel caso incremento il count precedente
        counter = count
        parola_corrente = parola
        #es. 2016   2450

#non dimentichiamo di stampare anche l'ultimo risultato
#come sopra, verifico che l'anno sia 2016 altrimenti non printo nulla
if parola_corrente == parola and parola_corrente == '2016':
    print '%s\t%s' % (parola_corrente, counter)
