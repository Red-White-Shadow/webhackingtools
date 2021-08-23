import os
author="Red White Shadow"
print("""
  Coded by Red White Shadow
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1- Nmap İle Hafif Port Tara
2- Nmap İle Servis Versiyon Bilgisini Al
3- Sqlmap İle Dbs Çek
4- Md5 Ouştur &  Kır 
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
if vur == "4" :
   import hashlib
import os
import json
import subprocess
import urllib3
import requests
os.system("clear")
print ("""
_______________________________
|        hacktivizm.org       |
_______________________________
+         Red White Shadow    +
+         MD5 - CRACKER       +
+++++++++++++++++++++++++++++++
+       1. MD5 OLUŞTUR        +
+++++++++++++++++++++++++++++++
+       2. MD5 KIR            +
+          (BRUTE FORCE)      +
+++++++++++++++++++++++++++++++
+       3. MD5 KIR (APİ)      +
+++++++++++++++++++++++++++++++
""")
veri = input("Islem Numarasini Girin : ")
if veri =="1" :

    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()
    print(h2)

if veri =="2":

    wlist = input("wordlist: ")
    hash2crack = input("hash: ")
    wlistlines = open(wlist, "r").readlines()


    for i in range(0, len(wlistlines)):

        hash2comp = hashlib.md5(wlistlines[i].replace(
                "\n", "").encode()).hexdigest()

        if hash2crack == hash2comp:
            print("Cracklendi: "+wlistlines[i].replace("\n", ""))
            exit()
            print("Cracklenemedi....")
if veri == "3" :
    dat2 = input("Kırılacak MD5 Hash ==> ")
    print ("")
    print ("_______________________________")
    print ("")
    response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
    print ("crack sonucu => " , response)
    print ("")
    print ("cracklenen hash => " ,dat2)
    print ("")
    print ("_______________________________")

else :
  input ("hatalı fonksiyon")
