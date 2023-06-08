def izveidot_profilu():
 import hashlib, getpass, pandas as pd
 pf_file=r"..\data\profili.csv"
 
 print("Jauna lietotāja veidošana. (Lai pārtrauktu, ievadiet 'q'!)")
 
 gadu_skaits = input("Ievadiet pilnu nodzīvoto gadu skaitu: ")
 try:
  if int(gadu_skaits) < 12:
   print("Vecums neatbilst vismaz 12 gadu dalībnieka ierobežojumam.") 
   return('')
 except ValueError:
  return('')
 
 while True:
  lietotaja_vards = input("Ievadiet vēlamo lietotāja vārdu: ")
  if lietotaja_vards == 'q':
   return('')
  profili = pd.read_csv(pf_file)
  if not lietotaja_vards in profili["Lietotāja vārds"].values:
   break
  print("Profils jau eksistē. Lūdzu, izvēlieties citu lietotāja vārdu.")
  return('')
 
 while True:
  parole = getpass.getpass("Ievadiet paroli: ")
  if parole == 'q':
   return('')
  parole_atkartoti = getpass.getpass("Atkārtoti ievadiet paroli: ")
  if parole == parole_atkartoti:
   break
  print("Atkārtotā parole nesakrīt ar atkārtojamo!")
  print("Veidojam paroli no jauna.")

 vards = input("Ievadiet savu vārdu: ")
 if vards == 'q':
  return('')
 uzvards = input("Ievadiet savu uzvārdu: ")
 if uzvards == 'q':
  return('')
 
 jauns_profils = pd.DataFrame({
  "Lietotāja vārds": [lietotaja_vards],
  "Parole": [hashlib.sha256((lietotaja_vards+parole).encode('utf-8')).hexdigest()], 
  "Vārds": [vards],
  "Uzvārds": [uzvards]})

 #profili = profili.append(jauns_profils, ignore_index=True)

 jauns_profils.to_csv(pf_file, mode='a', index=False, header=False)

 print("Lietotāja",vards,uzvards,"profils '"+lietotaja_vards+"' veiksmīgi izveidots.")
 return(lietotaja_vards)

