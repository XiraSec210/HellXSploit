import requests
import time

print ("                 ------------------------------------")
print ("                 --         Sub Domain Finder      --")
print ("                 --                 By             --")
print ("                 --           @Mr_Amir_Typer       --")
print ("                 --                                --")
print ("                 ------------------------------------")
print ()


td = input("[*] Site = ")
    
a = requests.get ("https://api.hackertarget.com/hostsearch/?q="+td)

if td:
    

    
    print('''
[*] SubDomains:
    ''')
    print(a.text)
    time.sleep(8)
    print("""
[Bye Friend <3 | Script By @Mr_Amir_Typer]
    """)
else:
    print('''
[*] Something Happend!! [ Error ] '''

          )
    print("""
[Bye Friend <3 | Script By @Mr_Amir_Typer]""")
