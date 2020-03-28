# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/nStreamVOD/Moduls/TURKvodModul_vkontakte.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2
import urllib as ul
import os, re
from datetime import datetime
from time import time
from xml.dom.minidom import parseString

def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    url = 'http://' + url
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 TURKvod 3.5',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_vkontakte:

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
        debug(url, 'MODUL URL: ')
        parts = url.split('@')
        video_list_temp = []
        url = parts[0]
        page = parts[1]
        name = parts[2].encode('utf-8')
        self.search_text = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
        self.search_on = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
        chan_counter = 0
        if len(parts) == 3:
            self.playlistname = '   VK \xd0\xbf\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
            new = (1, '\xd0\x9d\xd0\xb0\xd0\xb6\xd0\xbc\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xbd\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5 \xd0\xba\xd0\xbd\xd0\xbe\xd0\xbf\xd0\xba\xd1\x83 STOP', None, None, None, '', None, '', '', None, None)
            video_list_temp.append(new)
        if len(parts) == 4:
            site_url = 'http://nstream.hostei.com/portal/vk/'
            regex_ms = '<div class="thumb"><img src="(.*?)" alt="(.*?)" width="\\d+" height="\\d+" \\/><\\/div>\\s*<h3><a href="http:\\/\\/(.*?)" title=".*?<\\/a><\\/h3>'
            regex3 = '<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>t<!\\><!\\[CDATA\\[(.+?)\\]\\]>://<img src=\'(http://.+?)><(http://.+?)\'\\/.+?\\W+.+?(http://.+?)><!\\>/<!\\>r</title>\\W+.*?\\W+.*?>v<(\'\\/.+?\\W+.+?)><(http://.+?)><(\'\\/.+?\\W+.+?)>.net/<(http://.+?)>.</title><img src=\'(http:/\\/\\.+?)>v<(http:\\/\\/.+?)><(\'\\/.+?\\W+.+?)><(.+?)\\]\\]>'
            a = regex3.replace('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', 'h').replace('<!\\[CDATA\\[(.+?)\\]\\]>', 'p').replace("<img src='(http://.+?)>", 't').replace("<(http://.+?)'\\/.+?\\W+.+?(http://.+?)><!\\>/<!\\>", 'u').replace('</title>\\W+.*?\\W+.*?>', 'k').replace('<!\\>', 't').replace('<(.+?)\\]\\]>', 'l').replace("<img src='(http:/\\/\\.+?)>v<(http:\\/\\/.+?)><('\\/.+?\\W+.+?)>", 'm').replace('</title>', 'x').replace("<(http://.+?)><('\\/.+?\\W+.+?)>", 'd').replace('<(http://.+?)>', 'vk').replace("<('\\/.+?\\W+.+?)>", 'o')
            req = urllib2.Request(a, None, {'User-agent': 'Mozilla/5.0 TURKvod 3.5',
             'Connection': 'Close'})
            file = urllib2.urlopen(req)
            data = file.read()
            file.close()
            dom = parseString(data)
            url_pat = dom.getElementsByTagName('url')[0].toxml()
            code_pat = dom.getElementsByTagName('a_code')[0].toxml()
            add_pat = dom.getElementsByTagName('add')[0].toxml()
            pat_url = url_pat.replace('<url><![CDATA[', '').replace(']]></url>', '')
            pat_code = code_pat.replace('<a_code><![CDATA[', '').replace(']]></a_code>', '')
            pat_add = add_pat.replace('<add><![CDATA[', '').replace(']]></add>', '')
            url = pat_url
            param = ul.quote(parts[3].encode('cp1251'))
            debug(param, 'param')
            param = pat_add % param
            page = mod_request(url, param)
            results = re.findall(pat_code + '\\W+.+?".+?"><.+?">(.+?)<\\/div><.+?">(.+?)</div></div>\\W+.+?\\W+.+?\\W<.+?url..(.+?)\'', page)
            self.playlistname = '%s  %i \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba\xd0\xb0.' % (parts[3], len(results))
            for url, title, time, img in results:
                title = title.decode('1251').encode('utf-8') + '(  ' + str(time) + '  ) '
                descr = self.playlistname + '\n' + '  \n' + '\n' + title
                url = url
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
