# coding: utf-8

import re, os, time, datetime, traceback, urllib, cookielib
import urllib2
import httplib, mimetypes
import shutil
import sys
import json
import hashlib
import VirtualKeyBoardRUS
import plugin
import jsontools
import scrapertools
import httptools
import base64
import urllib
import urlparse
from enigma import eTimer

RUTAPLUGIN = "/usr/lib/enigma2/python/Plugins/Extensions/archivostv/"
RUTACOOKIE = "/usr/lib/enigma2/python/Plugins/Extensions/archivostv/cookies.dat"
RutaTMP = "/tmp/archivostv/"
user_agent_default = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

ARPORDEDE = RUTAPLUGIN+"hdfull.py"
ARPORDEDEO = RUTAPLUGIN+"hdfull.pyo"

TKN = ""
USR = ""
PSW = ""
Mediaitem = ""
Sesion = ""

OTRO = 0
host = 'https://hdfull.io'

cj = cookielib.MozillaCookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
OP = opener.open

LogeadoDD = False

cookiepath = RutaTMP

def load_cookies():
    if os.path.isfile(RUTACOOKIE):
        
        try:
            print "Cargando cookies"
            cj.load(RUTACOOKIE, ignore_discard=True)
        except:
            print "No cargamos cookies, error"
            pass
    else:
        print RUTACOOKIE
        print "No existe el fichero de cookies megadede"
        
def save_cookies():
    cj.save(RUTACOOKIE, ignore_discard=True)
    print "Guardando las cookies"

def Version():
    V = 100
    return V

def CompruebaLoginHD(self):
    load_cookies()
    url = 'https://hdfull.io/'
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent_default)
    Abrir = OP(req, timeout=20)
    data = Abrir.read()
    Abrir.close()
    
    if data.find('<a href="https://hdfull.io/user/plugine2" class="tour-join2 join">Bienvenido plugine2</a>') != -1:
        #Lo encuentra, entonces estamos logeados.
        return True
    else:
        #print data
        #No lo encuentra, asi que estamos deslogeados.
        return False

def Logear(self, usuario, contra):
    try:
        global USR
        global PSW
        global TKN
        global Mediaitem
        global Sesion
        
        load_cookies()
        Sesion = self.session

        
        LOGIN = usuario
        PASSWORD = contra
        
        USR = LOGIN
        PSW = PASSWORD
        
        url_origen = 'https://hdfull.io/'
        req = urllib2.Request(url_origen)
        req.add_header('User-Agent', user_agent_default)
        Abrir = OP(req, timeout=20)
        data = Abrir.read()
        Abrir.close()
        
        GetName = re.findall(r'login_form"><.+name=\'(.*?)\'', data)
        GetToken = re.findall(r'login_form">.+value="(.*?)"', data)

        
        NameToken = GetName[0]
        Token = GetToken[0]
        
        print "Este es el nombre: " + str(NameToken)
        print "Este es el Token: " + str(Token)
        
        url = 'https://hdfull.io/'
        post = str(NameToken) + '=' + str(Token) + '&username=' + USR + '&password=' + PSW + '&action=login'
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent_default)
        #req.add_header('Accept', '*/*')
        req.add_header('Referer', 'https://hdfull.io/')
        #req.add_header('X-Requested-With', 'XMLHttpRequest')
        #req.add_header('X-CSRF-TOKEN', TKN)
        Abrir = OP(req, data=post)
        data = Abrir.read()
        Abrir.close()
        
        save_cookies()
        
        XXX = CompruebaLoginHD(self)
        
        return XXX
    except Exception as er:
        print "Error: "+ str(er) + " En Logear"
        print "Error: "+ str(er) + " En Logear"
        print "Error: "+ str(er) + " En Logear"
        return [1, er]
        
def NavegarEstrenos(self, Nam, Pagina):
    try:
        global opener
        global OTRO
        
        NN = Nam
        NN = NN.replace("¡","")
        NN = NN.replace("¿","")
        NN = NN.replace("?","")
        NN = NN.replace(":","")
        NN = NN.replace("º","")
        NN = NN.replace("ª","")
        NN = NN.replace("\"","")
        NN = NN.replace("\'","")
        NN = NN.replace("(","")
        NN = NN.replace(")","")
        NN = NN.replace("á","a")
        NN = NN.replace("Á","A")
        NN = NN.replace("é","e")
        NN = NN.replace("É","E")
        NN = NN.replace("í","i")
        NN = NN.replace("Í","I")
        NN = NN.replace("ó","o")
        NN = NN.replace("Ó","O")
        NN = NN.replace("ú","u")
        NN = NN.replace("Ú","U")
        NN = NN.replace("ñ","n")
        NN = NN.replace("Ñ","N")
        NN = NN.replace("&ntilde;","n")
        NN = NN.replace("&quot;","")
        NN = NN.replace("'","")
        NN = NN.replace("&#039;","")
        PAG = Pagina
        PG = PAG
        
        Categ = RutaTMP + NN + str(PG) + ".xml"
        
        url = 'https://hdfull.io/peliculas-estreno'
        PAG = int(PAG)
        
        req = urllib2.Request(url)
        req.add_header('User-Agent',user_agent_default)
        req.add_header('Referer','https://www.megadede.com/pelis')
        Abrir = OP(req)
        data = Abrir.read()
        Abrir.close()
        
        Recopila = re.findall(r'href="(.*?)".+\s+.+src="(.*?)"\s.+title="(.*?)"\sst', data)
        IDS = re.findall(r'data-seen="(.*?)"', data)
        
        if PAG == 0:
            i = 1
        else:
            i = PAG+1
            
        FF = open(Categ, 'w')
        FF.write('<?xml version="1.0" encoding="iso-8859-1"?>\n<items>\n<playlist_name><![CDATA[' + NN + ']]></playlist_name>\n\n')
        
        Conteo = 0
        
        if Recopila == []:
            Mensaje = "Error","No hay mas resultados aqui."
            FF.close()
            return [1, Mensaje]
        else:
            for enlace,imagen,titulo in Recopila:
                ID = IDS[Conteo]
                Conteo = Conteo + 1
                ENLA = enlace
                if '/serie' in ENLA or "/tags-tv" in ENLA:
                    ENLA += "###" + ID + ";1"
                else:
                    ENLA += "###" + ID + ";2"
                NN = titulo
                NN = NN.replace("¡","")
                NN = NN.replace("¿","")
                NN = NN.replace("?","")
                NN = NN.replace(":","")
                NN = NN.replace("º","")
                NN = NN.replace("ª","")
                NN = NN.replace("\"","")
                NN = NN.replace("\'","")
                NN = NN.replace("(","")
                NN = NN.replace(")","")
                NN = NN.replace("á","a")
                NN = NN.replace("Á","A")
                NN = NN.replace("é","e")
                NN = NN.replace("É","E")
                NN = NN.replace("í","i")
                NN = NN.replace("Í","I")
                NN = NN.replace("ó","o")
                NN = NN.replace("Ó","O")
                NN = NN.replace("ú","u")
                NN = NN.replace("Ú","U")
                NN = NN.replace("&ntilde;","n")
                NN = NN.replace("&quot;","")
                NN = NN.replace("'","")
                NN = NN.replace("&#039;","")
                IMAG = imagen
                
                ImgDefinitiva = ObtenImagenes(self, IMAG)
                
                #FF.write("type=poraa\nname=" + NN.encode('utf8') +"\nthumb=" + IMAG + "\nURL=" + ENLA + "\ndescription=./description\n\n")
                FF.write("<channel>\n")
                FF.write("    <title><![CDATA[" + NN.encode('utf8') + "]]></title>\n")
                FF.write('    <description><![CDATA[<img src="' + IMAG + '">]]></description>\n')
                FF.write('    <playlist_url><![CDATA[' + ENLA + ']]></playlist_url>\n')
                FF.write('    <img_src><![CDATA[' + ImgDefinitiva + ']]></img_src>\n')
                FF.write('    <tipo><![CDATA[hdfullEnlaces]]></tipo>\n')
                FF.write('    <historial><![CDATA[' + Categ +']]></historial>\n')
                FF.write('</channel>\n\n')
                
            
            if Conteo < 58:
                pass
            else:
                FF.write("<channel>\n")
                FF.write("    <title><![CDATA[Pagina Siguiente]]></title>\n")
                FF.write('    <description><![CDATA[<img src="http://ps3plusteam.ddns.net/ps3plus/images/letras/siguiente.png">]]>Avanza a la pagina siguiente para ver mas peliculas!</description>\n')
                FF.write('    <img_src><![CDATA[http://ps3plusteam.ddns.net/ps3plus/images/letras/siguiente.png]]></img_src>\n')
                FF.write('    <ts_stream><![CDATA[' + str(i) + ']]></ts_stream>\n')
                FF.write('    <tipo><![CDATA[hdfullEstrenos]]></tipo>\n')
                FF.write('    <historial><![CDATA[' + Categ +']]></historial>\n')
                FF.write('</channel>\n\n')
                
            
            if i == 1:
                FF.write('<prev_page_url text="CH- ATRAS"><![CDATA[hdfull.xml]]></prev_page_url>\n</items>')
            if i == 2:
                FF.write('<prev_page_url text="CH- ATRAS"><![CDATA[/tmp/archivostv/Navegar en Estrenos0.xml]]></prev_page_url>\n</items>')
            if i > 2:
                i = i - 1
                FF.write('<prev_page_url text="CH- ATRAS"><![CDATA[/tmp/archivostv/Pagina Siguiente' + str(i - 1) + '.xml]]></prev_page_url>\n</items>')
            
            
            FF.close()
            
            return Categ
            
    except Exception as er:
        print "Error: "+ str(er) + " En NavegarEstrenos HDFULL"
        print "Error: "+ str(er) + " En NavegarEstrenos HDFULL"
        print "Error: "+ str(er) + " En NavegarEstrenos HDFULL"
        return [1, er]
        
def Enlaces(self, Nam, URLL = "", THUMB = "", historial = ""):

    NN = Nam
    NN = NN.replace("¡","")
    NN = NN.replace("¿","")
    NN = NN.replace("?","")
    NN = NN.replace(":","")
    NN = NN.replace("º","")
    NN = NN.replace("ª","")
    NN = NN.replace("\"","")
    NN = NN.replace("\'","")
    NN = NN.replace("(","")
    NN = NN.replace(")","")
    NN = NN.replace("á","a")
    NN = NN.replace("Á","A")
    NN = NN.replace("é","e")
    NN = NN.replace("É","E")
    NN = NN.replace("í","i")
    NN = NN.replace("Í","I")
    NN = NN.replace("ó","o")
    NN = NN.replace("Ó","O")
    NN = NN.replace("ú","u")
    NN = NN.replace("Ú","U")
    NN = NN.replace("ñ","n")
    NN = NN.replace("Ñ","N")
    NN = NN.replace("&ntilde;","n")
    NN = NN.replace("&quot;","")
    NN = NN.replace("'","")
    NN = NN.replace("&#039;","")
    ENN = URLL
    IMG = THUMB

    Categ = RutaTMP + NN + ".xml"
    
    if "###" in ENN:
        id = ENN.split("###")[1].split(";")[0]
        type = ENN.split("###")[1].split(";")[1]
        ENN = ENN.split("###")[0]
        
    
    itemlist = []
    it1 = []
    it2 = []
    
    url_targets = ENN

    data_js = httptools.downloadpage("http://ps3plusteam.ddns.net/hdfull/jquery.hdfull.view.min.js", headers={'referer': 'http://ps3plusteam.ddns.net/'}).data
    key = scrapertools.find_single_match(data_js, 'JSON.parse\(atob.*?substrings\((.*?)\)')

    data_js = httptools.downloadpage("http://ps3plusteam.ddns.net/hdfull/providers.js", headers={'referer': 'http://ps3plusteam.ddns.net/'}).data

    decoded = jhexdecode(data_js).replace("'", '"')
    providers_pattern = 'p\[(\d+)\]= {"t":"([^"]+)","d":".*?","e":.function.*?,"l":.function.*?return "([^"]+)".*?};'
    providers = scrapertools.find_multiple_matches (decoded, providers_pattern)
    provs = {}
    for provider, e, l in providers:
        provs[provider]=[e,l]

    data = agrupa_datos(ENN)
    data_obf = scrapertools.find_single_match(data, "var ad\s*=\s*'([^']+)'")

    data_decrypt = jsontools.load(obfs(base64.b64decode(data_obf), 126 - int(key)))
    
    FF = open(Categ, 'w')
    FF.write('<?xml version="1.0" encoding="iso-8859-1"?>\n<items>\n<playlist_name><![CDATA[' + NN + ']]></playlist_name>\n\n')
    
    Conteo = 0
    matches = []
    for match in data_decrypt:
        if match['provider'] in provs:
            try:
                embed = provs[match['provider']][0]
                url = provs[match['provider']][1]+match['code']
                matches.append([match['lang'], match['quality'], url, embed])
            except:
                pass
    
    for idioma, calidad, url, embed in matches:
        if embed == 'd':
            option = "Descargar"
            option1 = 2
        else:
            option = "Ver"
            option1 = 1
            
            if idioma == "ESP":
                Conteo = Conteo + 1
                if url.find('vidoza') != -1:
                    FF.write("<channel>\n")
                    FF.write("    <title><![CDATA[Ver en vidoza " + NN.encode('utf8') + " " + calidad + "]]></title>\n")
                    FF.write('    <description><![CDATA[' + IMG + ']]></description>\n')
                    FF.write('    <playlist_url><![CDATA[' + url + ']]></playlist_url>\n')
                    FF.write('    <stream_url><![CDATA[http://ps3plusteam.ddns.net/teamps3plus/pro/vidoza.txt]]></stream_url>\n')
                    FF.write('    <img_src><![CDATA[http://ps3plusteam.ddns.net/ps3plus/images/letras/vidoza.png]]></img_src>\n')
                    FF.write('    <tipo><![CDATA[hdfullLinks]]></tipo>\n')
                    FF.write('</channel>\n\n')                
                if url.find('gamovideo') != -1:
                    Conteo = Conteo + 1
                    buscaID = re.findall(r'com/(.*)', url)
                    buscaID = buscaID[0]
                    FF.write("<channel>\n")
                    FF.write("    <title><![CDATA[Ver en gamovideo " + NN.encode('utf8') + " " + calidad + "]]></title>\n")
                    FF.write('    <description><![CDATA[' + IMG + ']]></description>\n')
                    FF.write('    <playlist_url><![CDATA[http://gamovideo.com/embed-' + buscaID + '-640x360.html]]></playlist_url>\n')
                    FF.write('    <stream_url><![CDATA[http://ps3plusteam.ddns.net/teamps3plus/props3/gamo.txt]]></stream_url>\n')
                    FF.write('    <img_src><![CDATA[http://ps3plusteam.ddns.net/ps3plus/images/letras/gamovideo.png]]></img_src>\n')
                    FF.write('    <tipo><![CDATA[hdfullLinks]]></tipo>\n')
                    FF.write('</channel>\n\n') 
                     
    FF.write('<prev_page_url text="CH- ATRAS"><![CDATA[' + historial + ']]></prev_page_url>\n</items>')
    
    if Conteo == 0:
        return None
    
    return Categ

def jhexdecode(t):
    r = re.sub(r'_\d+x\w+x(\d+)', 'var_' + r'\1', t)
    r = re.sub(r'_\d+x\w+', 'var_0', r)
    def to_hx(c):
        h = int("%s" % c.groups(0), 16)
        if 19 < h < 160:
            return chr(h)
        else:
            return ""
    r = re.sub(r'(?:\\|)x(\w{2})', to_hx, r).replace('var ', '')
    f = eval(scrapertools.find_single_match(r, '\s*var_0\s*=\s*([^;]+);'))
    for i, v in enumerate(f):
        r = r.replace('[[var_0[%s]]' % i, "." + f[i])
        r = r.replace(':var_0[%s]' % i, ":\"" + f[i] + "\"")
        r = r.replace(' var_0[%s]' % i, " \"" + f[i] + "\"")
        r = r.replace('(var_0[%s]' % i, "(\"" + f[i] + "\"")
        r = r.replace('[var_0[%s]]' % i, "." + f[i])
        if v == "": r = r.replace('var_0[%s]' % i, '""')
    r = re.sub(r':(function.*?\})', r":'\g<1>'", r)
    r = re.sub(r':(var[^,]+),', r":'\g<1>',", r)
    return r
    
def obfs(data, key, n=126):
    #if PY3: data = "".join(chr(x) for x in bytes(data))
    chars = list(data)
    for i in range(0, len(chars)):
        c = ord(chars[i])
        if c <= n:
            number = (ord(chars[i]) + key) % n
            chars[i] = chr(number)
    return "".join(chars)
    
def agrupa_datos(url, post=None):
    req = urllib2.Request(url)
    req.add_header('User-Agent',user_agent_default)
    req.add_header('Referer','https://hdfull.io/')
    Abrir = OP(req)
    data = Abrir.read()
    Abrir.close()
    
    ## Agrupa los datos
    data = re.sub(r'\n|\r|\t|&nbsp;|<br>|<!--.*?-->', '', data)
    data = re.sub(r'\s+', ' ', data)
    data = re.sub(r'>\s<', '><', data)
    return data
        
def ObtenImagenes(self, enlace):
    try:
        m = hashlib.md5()
        m.update(enlace)
        cover_md5 = m.hexdigest()
        
        req = urllib2.Request(enlace)
        req.add_header('User-Agent',user_agent_default)
        Abrir = OP(req, timeout=8)
        data = Abrir.read()
        Abrir.close()
        
        self.picfile = '%s%s.jpg' % (RutaTMP, cover_md5)
        FF = open(self.picfile, 'w')
        FF.write(data)
        FF.close()
        
        return self.picfile
        
    except Exception as err:
        print err
        print err
        print err
        if os.path.isfile(self.picfile):
            try:
                os.remove(self.picfile)
            except:
                pass