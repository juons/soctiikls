import glob, os, getpass, pandas as pd
from datetime import datetime
import business.izveidot_profilu as p
import business.autentificeeties as a
import business.pievieno_veesti as v


lietotaajs=''
izveelne0={
 1:'Autentificēties',
 2:'Reģistrēties',
 3:'Labot profilu',
 4:'Lasīt vēstījumus',
 5:'Sūtīt vēstījumu',
 6:'Beigt darbu'
 }

while True:
 print('Lietotājs:', lietotaajs)
 print('Izvēlieties darbību:')
 for i in sorted(izveelne0.keys()):
  print(i,'-',izveelne0[i]) 
 atb=input('Izvēlieties: ')
 if atb == '1':
  #lietotaajs = input('Ievadiet savu lietotājvārdu: ') 
  lietotaajs = a.autentificeeties()
 elif atb == '2':
  lietotaajs=p.izveidot_profilu()
 elif atb == '3':
  print(izveelne0[int(atb)],'- nav izstrādāts')
 elif atb == '4':
  print(izveelne0[int(atb)],'- nav izstrādāts')
 elif atb == '5':
  if lietotaajs is None or lietotaajs == '':
   print('Jūs neesat pieslēdzies!')
   continue
  print(v.pievieno_veesti(lietotaajs)[1])
 elif atb == '6':
  print('Atā!')
  break
 else:
  print('Neatpazīstama izvēle:',atb)
 print()
 


