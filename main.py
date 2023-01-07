import re
import time
import os
import pystyle
from pystyle import Colors, Colorate, Center
import webbrowser
import pymetasploit3
from pymetasploit3.msfrpc import MsfRpcClient

os.system("title HellXsploit - Website Vulnerability Scanner and Exploiter")
os.system("color 4")

banner = """     ( (  ) )     (       (     .      (   
    )\)\(\( ( (  )\   (  ))\ (   (  ( )\  
    (_)(_))(|)\)\((_)__)\(((_))\  )\ )\(_) 
    | || |()\| | | \/ /(_) '_ \ |((_)_) |_ 
    | __ | -_) | |>  <(_-/ .__/ | _ \ |  _|
    |_||_|___|_|_|_/\_\__/_|  |_|___/_|\__|
===============================================
   Auto website vuln scanner & exploiter
   Made with ❤ by XiraS3c
===============================================

 [1] XSS ScannerXExploiter   [2] SQLi Scanner
 
 [3] 2020-5902 CVE           [4] All CVE Check
 
 [5] NMap                    [6] Pages Scanner

 [7] Wordlist Maker (HARD)   [8] Payload Maker 
                                 (linux only)

 [9] Subdomain Finder        [10] Version

 [11] Credits
"""

print(Center.Center(banner))
print()
print()
print()
choice = input("[root@hellxsploit] $: ")
if choice == "1":
    os.system("python xss.py")
    input()
if choice == "2":
    domain = input("Targetted domain name: ")
    port = input("Targtetted port (80 if you dont' know): ")
    os.system("cls")
    os.system("color a")
    os.system(f'python sql.py -u {domain} -p {port}')
    input()
if choice == "3":
    ipstart = input("IP Start: ")
    ipend = input("IP End: ")
    os.system("cls")
    os.system("color a")
    os.system(f'cve2020.py {ipstart} {ipend}')
    input()
if choice == "4":
    target = input("Target: ")
    webbrowser.open(f'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={target}')
    input()
if choice == "5":
    os.system("cls")
    os.system("color a")
    os.system("python nmap.py")
    input()
if choice == "6":
    os.system("cls")
    os.system("color a")
    os.system("python pagescanner.py")
    input()
if choice == "7":
    os.system("cls")
    os.system("color a")
    print("[!] Very Strong, be carrefull, close the programm to, stop this!")
    os.system("python wrdlm.py")
    input()
if choice == "8":
    os.system("cls")
    os.system("color a")
    os.system("python ezsploit.py")
    input()
if choice == "9":
    os.system("cls")
    os.system("color a")
    os.system("python subd.py")
    input()
if choice == "10":
    print("The current version is 0.0.1")
    input()
if choice == "11":
    print("""
HellXSploit: XiraS3c, Snoyxo, Hashkiller, ZRX, SCP-079, MaKarov
""")
    input()
