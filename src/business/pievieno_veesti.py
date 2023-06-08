def pievieno_veesti(lietotaajs):
 import pandas as pd
 from datetime import datetime

 izveelne_pv1={
  1:'Publisks vēstījums',
  2:'Visiem draugiem',
  3:'Vienam cilvēkam',
  4:'Atpakaļ pie darbībām'
  }
 print()
 print('Izvēlieties sava vēstījuma saņēmējus:')
 for i in sorted(izveelne_pv1.keys()):
  print(i,'-',izveelne_pv1[i]) 
 atb = input('Izvēlieties: ') 
 if atb == '1':
  virziens='publiski'
 elif atb == '2':
  virziens='draugiem'
 elif atb == '3':
  virziens = input("Kam sūtīsiet vēsti? Ievadiet saņēmēja lietotājvārdu: ") 
  pf_file=r"..\data\profili.csv"
  profili = pd.read_csv(pf_file) 
  if not virziens in profili["Lietotāja vārds"].values:
   return([1,"Vēstījuma saņēmējs '"+virziens+"' nav pieejams!"])
 else:
  return([1,'Kļūme izvēlē!'])
 print(virziens,"\n")


 def csv_naakamais(csv_datne):
  import glob, os
  csv_un_skaitlis=glob.glob(csv_datne+'.*')[0]
  sk_saakums=int(csv_un_skaitlis.rfind('.'))+1
  skaitlis=int(csv_un_skaitlis[sk_saakums:])
  naakamais_sk=skaitlis+1
  os.rename(csv_un_skaitlis,csv_datne+'.'+str(naakamais_sk))
  return(naakamais_sk)
 
 csv_datne=r'..\data\veestis.csv'
 
 naakamaa_vst=csv_naakamais(csv_datne)
 
 # import pytz
 # tz_Riga = pytz.timezone('Europe/Riga')
 # laiks=datetime.now(tz_Riga).strftime("%Y.%m.%d_%H:%M:%S")
 laiks=datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
 
 veests=input('Ievadiet savu vēstījumu: ')
 atbildot_uz=None
 
 dati={
  'npk':[naakamaa_vst],
  'laiks':[laiks],
  'lietotaajs':[lietotaajs],
  'virziens':[virziens],
  'atbildot_uz':[atbildot_uz],
  'veests':[veests]
 }
 pd_dataframe=pd.DataFrame(dati)
 pd_dataframe.to_csv(csv_datne, mode='a', index=False, header=False)
 return([0,lietotaajs + ' vēsts ierakstīta virzienā ' + virziens]) 
