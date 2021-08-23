import os
author="Red White Shadow"
print("""
  Coded by Red White Shadow
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1- Nmap İle Hafif Port Tara
2- Nmap İle Servis Versiyon Bilgisini Al
3- Sqlmap İle Dbs Çek
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
""")
vur=input("Lütfen yapacagınız işlemi seçiniz =>")
if vur == "1" :
  vur2 =input("ip veya link girin => ")
  os.system("nmap " + vur2)
if vur == "2" :
   vur3 = input("ip adresi => ")
   os.system("sudo nmap -sS -sV " +vur3)
if vur == "3":
   vur4 = input("açıklı url => ")
   os.system("sqlmap "+vur4 + "--dbs")
else :
  ("hatalı fonksiyon knk ")
