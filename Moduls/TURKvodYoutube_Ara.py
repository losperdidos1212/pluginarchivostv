# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TURKvod/Moduls/TURKvodYoutube_Ara.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2
import urllib as ul
import os, re
from datetime import datetime
from time import time

def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    url = 'http://' + url
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 TURKvod 2.01',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_youtube_ara:

    def __init__(self):
        self.video_liste = []
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = ''
        self.active_site_url = ''
        self.playlistname = ''
        self.playlist_cat_name = ''
        self.kino_title = ''
        self.category_back_url = ''
        self.error = ''

    def get_list(self, url):
        debug(url, 'youtube')
        parts = url.split('@')
        video_list_temp = []
        url = parts[0]
        page = parts[1]
        name = parts[2].encode('utf-8')
        self.search_text = 'ARA TEXT TUSU'
        self.search_on = 'search'
        chan_counter = 0
        if len(parts) == 3:
            self.playlistname = 'YOUTUBE ARAMA'
            new = (1, 'ARAMA ICIN LUTFEN ( TEXT ) TUSUNA BASINIZ', None, None, None, '', None, '', '', None, None)
            video_list_temp.append(new)
        if len(parts) == 4:
            param = parts[3].encode('cp1251')
            param = param.replace(' ', '%20')
            url = 'gdata.youtube.com/feeds/api/videos?max-results=50&q=' + param
            page = mod_request(url)
            results = re.findall("<media:player url='(.*?)&amp;feature=youtube_gdata_player'/><media:thumbnail url='(.*?)' height='360' width='480'.*?\\/><media:thumbnail url.*?\\/><media:thumbnail url=.*?\\/><media:thumbnail url=.*?\\/><media:title type='plain'>(.*?)<\\/media:title><yt:duration seconds='(.*?)'/>", page)
            self.playlistname = '%s    %i ADET SONUC BULUNMUSTUR' % (parts[3], len(results))
            for text in results:
                img = text[1]
                title = text[2].upper()
                descr = self.playlistname + '\n' + 'YOUTUBE ARAMA MOTORU \n TEKRAR ARAMA ICIN TEXT TUSUNA BASINIZ \n' + 'Sure: ' + text[3] + '  Saniye' + '\n' + title
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 descr,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = ''
        self.prev_page_text = 'BACK'
        self.video_liste = video_list_temp
        return