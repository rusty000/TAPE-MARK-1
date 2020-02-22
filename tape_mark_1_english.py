#!/usr/bin/env python

import random
import sys

 
versi = \
[[" the blinding   /  globe  /  of fire  ", "1/4", "2/3", "1"],\
[" expands   /  rapidly  ", "1/2", "3/4", "1"],\
[" 30 times  /  brighter  /  than the sun ", "2/3", "2/4", "1"],\
[" when it reaches / the stratosphere  ", "3/4", "1/2", "1"],\
[" the summit  /  of the cloud ", "1/3", "2/3", "1"],\
[" assumes   /  the well-known form  /  of mushrooms", "2/4", "3/4", "1"], \

[" the head /  pressed  /  on the shoulder  ", "1/4", "2/4", "2"],\
[" the hair   /  between the lips ", "1/4", "2/4", "2"],\
[" they lay  /   motionless  /  without speaking ", "2/3", "2/3", "2"],\
[" until he moved  /  his fingers  / slowly   ", "3/4", "1/3", "2"],\
[" trying  /  to grasp  ", "3/4", "1/2", "2"],\

[" while the multitude  /  of things  /   comes   ", "1/2", "1/2", "3"],\
[" into being  /  I see their return    ", "2/3", "3/4", "3"],\
[" although /  things  /  flourish    ", "1/2", "2/3", "3"],\
[" they all   / return    /  to their roots   ", "2/3", "1/4", "3"]]

#~ gruppo "1", 0-5: Diario di Hiroshima, di Michihito Hachiya
#~ gruppo "2", 6-10: Il Mistero dell'ascensore, di Paul Goldwin
#~ gruppo "3", 11-14: Tao te King, di Lao Tse

random.shuffle(versi)
strofa_uno = [None] * 10
strofa_uno[0] = versi[0]
versi.remove(strofa_uno[0])


try:
    i = 0 ; j = 0
    while j < 9:
        if (versi[i][1][0] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][2]) \
        and versi[i][3] != strofa_uno[j][3]:
            # se le strofe "stanno bene insieme"
            # e non appartengono allo stesso gruppo
            strofa_uno[j+1] = versi[i]
            versi.remove(versi[i])
            i = 0
            j += 1
        # altrimenti, esamina l'elemento successivo
        else:
            i += 1
            continue

# se la combinazione in esame non soddisfa le condizioni, viene scartata
except: sys.exit()


strofa = []
for k in xrange(len(strofa_uno)):
	strofa.append(strofa_uno[k][0])

s = '/'.join(strofa).split("/")

print ""

for k in xrange(len(s)):
	
	if k == (len(s) - 1): sys.stdout.write(s[k].upper())
	else: sys.stdout.write(s[k].upper())

    # senza la seguente istruzione l'output di una strofa
    # viene formattato come nel tabulato originale, senza 'a capo'
    
	# if k > 0 and (k+1)%4 == 0: print ""
	
print ""



