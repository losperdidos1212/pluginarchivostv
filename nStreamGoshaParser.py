# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/nStreamVOD/nStreamGoshaParser.py
import re
import urllib2

class gosha_parsers:

    def __init__(self):
        self.quality = ''

    def get_parsed_link(self, url):
        try:
            if url.find('//kino-v-online.ru/kino/md5') > -1 or url.find('//kino-v-online.ru/serial/md5') > -1:
                url1 = 'http://kino-v-online.ru/2796-materik-online-film.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    hash_list = re.findall('/kino/(.*?)/', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = url.replace('md5hash', hash)
                except Exception as ex:
                    print ex

            if url.find('kinoprosmotr.net/') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall(';file=(.*?)\\.flv', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = hash + '.flv'
                except Exception as ex:
                    print ex

            if url.find('allserials.tv/s/md5') > -1:
                url1 = 'http://allserials.tv/serial-2166-osennie-cvety-1-sezon.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall('.tv\\/pl\\/(.*?)\\/', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = url.replace('md5hash', hash)
                except Exception as ex:
                    print ex

            if url.find('kinopod.org/get/md5') > -1:
                url1 = 'http://kinopod.ru/video.html?id=22110'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall('\\/get\\/(.*?)\\/', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = url.replace('md5hash', hash)
                except Exception as ex:
                    print ex

            if url.find('kino-dom.tv/s/md5') > -1:
                url1 = 'http://kino-dom.tv/drama/1110-taynyy-krug-the-sesret-sirsle-1-sezon-1-seriya-eng-onlayn.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall('file=http:\\/\\/kino-dom\\.tv\\/(.*?)\\/play\\/', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = url.replace('md5hash', hash)
                except Exception as ex:
                    print ex

            if url.find('linecinema.org/s/md5') > -1:
                url1 = 'http://www.linecinema.org/newsz/boevyk-online/508954-bliznecy-drakony-twin-dragons-1992-dvdrip-onlayn.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall('linecinema\\.org\\/s\\/(.*?)\\/', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = url.replace('md5hash', hash)
                except Exception as ex:
                    print ex

            if url.find('//figvam.ru/') > -1:
                url = url.replace('figvam.ru', 'go2load.com')
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('\n', '')
                    hash_list = re.findall('ftp\\:\\/\\/(.*?)"', page)
                    if len(hash_list) > 0:
                        hash = hash_list[0]
                        url = 'http://' + hash
                    print url
                except Exception as ex:
                    print ex

            if url.find('allinspace.com/') > -1:
                url_row = re.findall('&(.*?)&&', url)
                url_row = url_row[0]
                request = urllib2.Request(url_row, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    url1 = re.findall('ttp://(.*?)&', url)
                    url1 = url1[0]
                    url = 'http://' + url1
                except Exception as ex:
                    print ex

            if url.find('.igru-film.net/') > -1:
                url_row = re.findall('xyss(.*?)xys', url)
                url_row = url_row[0]
                url_film = 'http://fepcom.net/' + url_row
                film = re.findall('ssa(.*?)xyss', url)
                film = film[0]
                request = urllib2.Request(url_film, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    film_row = re.findall(';file=([^&]*)', page)
                    if len(film_row) > 0:
                        film_row = film_row[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/fepcom/code.php?code_url=' + film_row
                        request = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        code = urllib2.urlopen(request).read()
                        url = film.replace('md5hash', code)
                except Exception as ex:
                    print ex

            if url.find('kinoylei.ru/') > -1:
                url1 = 'http://server1.kinoylei.ru/player/pl.php?id=2902-3142'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code = re.findall('video/(.*?)/supervideo', page)
                    if len(code) > 0:
                        md5hash = code[0]
                        url = url.replace('md5hash', md5hash)
                except Exception as ex:
                    print ex

            if url.find('//77.120.114') > -1 or url.find('nowfilms.ru/') > -1:
                url_row = re.findall('xyss(.*?)xys', url)
                url_row = url_row[0]
                url_film = 'http://' + url_row
                film = re.findall('ssa(.*?)xyss', url)
                film = film[0]
                film_end = re.findall('/md5hash/(.*?)xys', url)
                film_end = film_end[0]
                request = urllib2.Request(url_film, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    link = urllib2.urlopen(request).read()
                    film_row = re.findall(';pl=([^"]*)', link)
                    if len(film_row) > 0:
                        film_row = film_row[0]
                        if film_row.find('/tmp/') > 0:
                            request2 = urllib2.Request(film_row, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                             'Connection': 'Close'})
                            link = urllib2.urlopen(request2).read()
                            indexer = link.find(film_end)
                        if indexer > 0:
                            md5hash = link[indexer - 23:indexer - 1]
                            url = film.replace('md5hash', md5hash)
                    else:
                        url = re.findall(';file=([^"]*)', link)
                        url = url[0]
                except Exception as ex:
                    print ex

            if url.find('//kinostok.tv/video/') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code = re.findall('file: "(.*?)"', page)
                    code = code[0]
                    if len(code) > 0:
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/kinostok/code.php?code_url=' + code
                        request3 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        url = urllib2.urlopen(request3).read()
                except Exception as ex:
                    print ex

            if url.find('/streaming.video.') > -1:
                try:
                    id_list = re.findall('get-location/(.*)/m', url)
                    id = id_list[0]
                    url1 = 'http://static.video.yandex.ru/get-token/' + id + '?nc=0.50940609164536'
                    request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                     'Connection': 'Close'})
                    page = urllib2.urlopen(request).read()
                    hash_list = re.findall('token>(.*)</token>', page)
                    hash = hash_list[0]
                    link1 = url.replace('md5hash', hash)
                    request2 = urllib2.Request(link1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                     'Connection': 'Close'})
                    page2 = urllib2.urlopen(request2).read()
                    film_list = re.findall('video-location>(.*)</video-location>', page2)
                    film = film_list[0]
                    url = film.replace('&amp;', '&')
                except Exception as ex:
                    print ex

            if url.find('/video.sibnet.ru') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    page = page.replace('&amp;', '&')
                    url_list = re.findall('<file>(.*?)<\\/file>', page)
                    if len(url_list) > 0:
                        url = url_list[0]
                        print 'sibnet'
                        print url
                except Exception as ex:
                    print ex

            if url.find('filmix.net/s/md5hash') > -1 or url.find('filevideosvc.org/s/md5hash') > -1:
                url1 = 'http://filmix.net/semejnyj/36974-tor-legenda-vikingov-legends-of-valhalla-thor-2011.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall(';file=(.*?)&', page)
                    if len(code_list) > 0:
                        code = code_list[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/filmix/code.php?code_url=' + code
                        request2 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        hash = urllib2.urlopen(request2).read()
                        url = url.replace('md5hash', hash)
                        print 'filmix'
                        print url
                except Exception as ex:
                    print ex

            if url.find('bigcinema.tv') > -1:
                url1 = 'http://bigcinema.tv/movie/prometey---prometheus.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall('file:"(.*?)"', page)
                    if len(code_list) > 0:
                        code = code_list[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/bigcinema/code.php?code_url=' + code
                        request2 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        hash = urllib2.urlopen(request2).read()
                        url = url.replace('md5hash', hash)
                        print 'filmix'
                        print url
                except Exception as ex:
                    print ex

            if url.find('.datalock.ru/') > -1:
                url1 = 'http://newseriya.ru/serial-3151-Kak_ya_vstretil_vashu_mamu-7-season.html'
                request = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall('\\/playlist\\/(.*?)\\/', page)
                    if len(code_list) > 0:
                        hash = code_list[0]
                        url = url.replace('md5hash', hash)
                        print 'seasonvar'
                        print url
                except Exception as ex:
                    print ex

            if url.find('//77.120.119') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall('file":"(.*?)"', page)
                    if len(code_list) > 0:
                        code = code_list[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/liveonline/code.php?code_url=' + code
                        request2 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        url = urllib2.urlopen(request2).read()
                        print 'filmix'
                        print url
                except Exception as ex:
                    print ex

            if url.find('uletfilm.net/') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall('file":"(.*?)"', page)
                    if len(code_list) > 0:
                        code = code_list[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/uletno/code.php?code_url=' + code
                        request2 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        url = urllib2.urlopen(request2).read()
                        print 'filmix'
                        print url
                except Exception as ex:
                    print ex

            if url.find('//vtraxe.com/') > -1:
                request = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                 'Connection': 'Close'})
                try:
                    page = urllib2.urlopen(request).read()
                    code_list = re.findall('3Fv=(.*?)&', page)
                    if len(code_list) > 0:
                        code = code_list[0]
                        code_url = 'http://gegen-abzocke.com/xml/nstrim/uletno/code.php?code_url=' + code
                        request2 = urllib2.Request(code_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                         'Connection': 'Close'})
                        url = urllib2.urlopen(request2).read()
                        print 'filmix'
                        print url
                except Exception as ex:
                    print ex

        except Exception as ex:
            print ex
            print 'goshparsed_link'

        return url