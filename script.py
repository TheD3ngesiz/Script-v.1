import os as dsa
from urllib2 import*

dsa.system('clear' if dsa.name == 'nt' else 'reset')
print("""\033[1;36m
			+----------------------------------------------+	
			|                                              |
			|           User = [ DSAdmin ]                 |
			|         Password = [ ******* ]               |
			|                                              |
			|            Darksecarmy.com                   |
			|              PcDunyasi.tv                    |
			|              	                               |
			|                                              |
			+----------------------------------------------+

			1) Http Header                  2) TCP Port Scan

	""")
ra = raw_input("\033[1;31mdsa\033[1;32m> \033[1;36m")
if ra == "1":
	ip = raw_input("\033[1;34mEnter Domain: \033[1;36m")
	site = "http://api.hackertarget.com/httpheaders/?q=" + ip
	zone = urlopen(site).read()
	dsa.system('clear' if dsa.name == 'nt' else 'reset')
	print (zone)
	quit()

elif ra == "2":
	ipd = raw_input("\033[1;34mEnter Ip Adress: \033[1;36m")
	system = "http://api.hackertarget.com/nmap/?q=" + ipd
	namp = urlopen(system).read()
	dsa.system('clear' if dsa.name == 'nt' else 'reset')
	print (namp)
	quit()
