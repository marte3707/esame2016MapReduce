#!/usr/bin/python
# -*- coding: utf-8 -*-

#------UTILIZZO------#
#echo data.txt | ./mapper.py | sort -k1,1 | ./reducer.py
#--------------------#

import sys

#l'input proviene dallo Standard Input (STDIN)
for line in sys.stdin:
    #per ogni nuova riga rimuovo spazi e tabulazioni
    line = line.strip()
    #splitto le righe in modo tale da poterle leggere una ad una
    parole = line.split()
    #per ogni parola (quindi per ogni riga) estraggo data e importo
    for parola in parole:
        #scrivo l'output su STDOUT che sarà l'input per il reducer.py
        #divido le "parole" ogni volta incontro un ";" (punto e virgola)
        #inoltre creo una variabile che mi permetta di poter estrarre solo l'anno e non la data completa
        s = line.split(';')
        anno = (s[0].split('-'))
        #stampo solo la prima parte della stringa (l'anno) e l'ultima parte (che contiene l'importo)
        print '%s\t%s' % (anno[0].strip(),s[6].strip())
        #come risultato finale del mapping avremo per ogni riga questo formato: [ANNO]  [IMPORTO]   es: 2016    100 (divisi da una tabulazione)
