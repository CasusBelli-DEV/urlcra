import whois
import random

fin = open('CHANGEME.txt', 'r+') # Source Dictionaries like Cities etc

import sys
sys.stdout=open("cache.txt","w")
for zeile in fin:
    wort = zeile.strip()
    domains = ('CHANGEME-' + wort + '.de') # Set Prefix (Branche like "lawyer", "taxi", "pizza" etc)
    print(domains)
sys.stdout.close()

import os

domains = open('cache.txt')
sys.stdout=open("CHANGEME.txt","w") # Set Output Filename
for line in domains:
    hostname = line.strip()
    response = os.system("ping -c 3 " + hostname)
    if response == 0:
      print(hostname, 'is up!')
    else:
      print(hostname, 'is down!')
sys.stdout.close()
