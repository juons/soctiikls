def autentificeeties():
 import hashlib, getpass, pandas as pd
 pf_file=r"..\data\profili.csv"

 lietotaja_vards = input('Ievadiet savu lietotājvārdu: ') 
 parole = getpass.getpass('Ievadiet paroli: ')

 profili = pd.read_csv(pf_file)
 a1=hashlib.sha256((lietotaja_vards+parole).encode('utf-8')).hexdigest()
 a2=profili.loc[profili['Lietotāja vārds']==lietotaja_vards]["Parole"].values[0]
 if a1 != a2:
  print('Neatpazīstams lietotājs.')
  return('')
 return(lietotaja_vards)

