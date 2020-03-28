# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/nStreamVOD/Moduls/TURKvodModuls.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2, urllib
import urllib as ul
import os, re, cookielib
from datetime import datetime
from time import time
import string
import base64
from urllib import urlencode
from jsunpacker import cJsUnpacker
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
from TURKvodModul_vkontakte import html_parser_vkontakte
from TURKvodModul_vizor_tv import html_parser_vizor_tv
from TURKvodModul_bicaps import html_parser_bicaps
from TURKvodModul_youtube import html_parser_youtube
from TURKvodYoutube_Ara import html_youtube_ara

def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    url = 'http://' + url.replace('http://', '')
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_moduls:

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

    def reset_buttons(self):
        self.kino_title = ''
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
        return

    def get_list(self, url):
        debug(url, 'MODUL URL: ')
        self.reset_buttons()
        if url.find('youtubesearch') > -1:
            YOUTUBESEARCH = html_parser_youtube()
            YOUTUBESEARCH.get_list(url)
            self.video_liste = YOUTUBESEARCH.video_liste
            self.next_page_url = YOUTUBESEARCH.next_page_url
            self.next_page_text = YOUTUBESEARCH.next_page_text
            self.prev_page_url = YOUTUBESEARCH.prev_page_url
            self.prev_page_text = YOUTUBESEARCH.prev_page_text
            self.search_text = YOUTUBESEARCH.search_text
            self.search_on = YOUTUBESEARCH.search_on
            self.active_site_url = YOUTUBESEARCH.active_site_url
            self.playlistname = YOUTUBESEARCH.playlistname
            self.playlist_cat_name = YOUTUBESEARCH.playlist_cat_name
            self.kino_title = YOUTUBESEARCH.kino_title
            self.category_back_url = YOUTUBESEARCH.category_back_url
            self.error = YOUTUBESEARCH.error
        if url.find('bicapssearch') > -1:
            BICAPSSEARCH = html_parser_bicaps()
            BICAPSSEARCH.get_list(url)
            self.video_liste = BICAPSSEARCH.video_liste
            self.next_page_url = BICAPSSEARCH.next_page_url
            self.next_page_text = BICAPSSEARCH.next_page_text
            self.prev_page_url = BICAPSSEARCH.prev_page_url
            self.prev_page_text = BICAPSSEARCH.prev_page_text
            self.search_text = BICAPSSEARCH.search_text
            self.search_on = BICAPSSEARCH.search_on
            self.active_site_url = BICAPSSEARCH.active_site_url
            self.playlistname = BICAPSSEARCH.playlistname
            self.playlist_cat_name = BICAPSSEARCH.playlist_cat_name
            self.kino_title = BICAPSSEARCH.kino_title
            self.category_back_url = BICAPSSEARCH.category_back_url
            self.error = BICAPSSEARCH.error
        if url.find('vkontaktesearch') > -1:
            VKONTAKTESEARCH = html_parser_vkontakte()
            VKONTAKTESEARCH.get_list(url)
            self.video_liste = VKONTAKTESEARCH.video_liste
            self.next_page_url = VKONTAKTESEARCH.next_page_url
            self.next_page_text = VKONTAKTESEARCH.next_page_text
            self.prev_page_url = VKONTAKTESEARCH.prev_page_url
            self.prev_page_text = VKONTAKTESEARCH.prev_page_text
            self.search_text = VKONTAKTESEARCH.search_text
            self.search_on = VKONTAKTESEARCH.search_on
            self.active_site_url = VKONTAKTESEARCH.active_site_url
            self.playlistname = VKONTAKTESEARCH.playlistname
            self.playlist_cat_name = VKONTAKTESEARCH.playlist_cat_name
            self.kino_title = VKONTAKTESEARCH.kino_title
            self.category_back_url = VKONTAKTESEARCH.category_back_url
            self.error = VKONTAKTESEARCH.error
        if url.find('vizor.tv') > -1:
            VIZORTV = html_parser_vizor_tv()
            VIZORTV.get_list(url)
            self.video_liste = VIZORTV.video_liste
            self.next_page_url = VIZORTV.next_page_url
            self.next_page_text = VIZORTV.next_page_text
            self.prev_page_url = VIZORTV.prev_page_url
            self.prev_page_text = VIZORTV.prev_page_text
            self.search_text = VIZORTV.search_text
            self.search_on = VIZORTV.search_on
            self.active_site_url = VIZORTV.active_site_url
            self.playlistname = VIZORTV.playlistname
            self.playlist_cat_name = VIZORTV.playlist_cat_name
            self.kino_title = VIZORTV.kino_title
            self.category_back_url = VIZORTV.category_back_url
            self.error = VIZORTV.error
        if url.find('youtubeara') > -1:
            YOUTUBEARA = html_youtube_ara()
            YOUTUBEARA.get_list(url)
            self.video_liste = YOUTUBEARA.video_liste
            self.next_page_url = YOUTUBEARA.next_page_url
            self.next_page_text = YOUTUBEARA.next_page_text
            self.prev_page_url = YOUTUBEARA.prev_page_url
            self.prev_page_text = YOUTUBEARA.prev_page_text
            self.search_text = YOUTUBEARA.search_text
            self.search_on = YOUTUBEARA.search_on
            self.active_site_url = YOUTUBEARA.active_site_url
            self.playlistname = YOUTUBEARA.playlistname
            self.playlist_cat_name = YOUTUBEARA.playlist_cat_name
            self.kino_title = YOUTUBEARA.kino_title
            self.category_back_url = YOUTUBEARA.category_back_url
            self.error = YOUTUBEARA.error
        if url.find('m3u') > -1:
            parts = url.split('@')
            filename = parts[0]
            name = parts[2].encode('utf-8')
            self.playlistname = name
            ts = None
            if url.find('TS') > -1:
                ts = 'True'
            try:
                video_list_temp = []
                chan_counter = 0
                if filename.find('http') > -1:
                    url = filename.replace('http://', '')
                    myfile = mod_request(url)
                else:
                    myfile = open('/usr/lib/enigma2/python/Plugins/Extensions/nStreamVOD/%s' % filename, 'r').read()
                regex = re.findall('#EXTINF.*,(.*\\s)\\s*(.*)', myfile)
                if not len(regex) > 0:
                    regex = re.findall('((.*.+)(.*))', myfile)
                for text in regex:
                    title = text[0].strip()
                    url = text[1].strip()
                    chan_counter += 1
                    chan_tulpe = (chan_counter,
                     title,
                     '',
                     'xxx.png',
                     url,
                     None,
                     None,
                     '',
                     '',
                     None,
                     ts)
                    video_list_temp.append(chan_tulpe)
                    if len(video_list_temp) < 1:
                        print 'ERROR m3u CAT LIST_LEN = %s' % len(video_list_temp)

            except:
                print 'ERROR m3u'

            return video_list_temp
        else:
            if url.find('hdfilmsehri.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.hdfilmsehri.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hdfilmsehri_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hdfilmsehri.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_hdfilmsehri_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdfilmsehri_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdfilmsehri_film(url)
            if url.find('unutulmazfilmler.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.unutulmazfilmler.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_unutulmazfilmler_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'unutulmazfilmler.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_unutulmazfilmler_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_unutulmazfilmler_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_unutulmazfilmler_film(url)
            if url.find('divxclub.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.divxclub.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_divxclub_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'divxclub.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_divxclub_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_divxclub_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_divxclub_film(url)
            if url.find('onlinefilmizle.tv') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.onlinefilmizle.tv'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_onlinefilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'onlinefilmizle.tv : ' + self.playlist_cat_name
                    self.video_liste = self.get_onlinefilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_onlinefilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_onlinefilmizle_film(url)
            if url.find('onlinefilmiizlet.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.onlinefilmiizlet.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_onlinefilmiizlet_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'onlinefilmiizlet.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_onlinefilmiizlet_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_onlinefilmiizlet_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_onlinefilmiizlet_film(url)
            if url.find('filmifullizle.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.filmifullizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmifullizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmifullizle.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmifullizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmifullizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmifullizle_film(url)
            if url.find('birfilmizle.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.birfilmizle.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_birfilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'birfilmizle.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_birfilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_birfilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_birfilmizle_film(url)
            if url.find('hdfilmsiten.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.hdfilmsiten.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hdfilmsiten_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hdfilmsiten.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_hdfilmsiten_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdfilmsiten_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdfilmsiten_film(url)
            if url.find('gunlukfilm.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'gunlukfilm.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_gunlukfilm_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'gunlukfilm.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_gunlukfilm_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_gunlukfilm_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_gunlukfilm_film(url)
            if url.find('direkizle.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'direkizle.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_direkizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'direkizle.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_direkizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_direkizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_direkizle_film(url)
            if url.find('cinemaizle.org') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.cinemaizle.org'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_cinemaizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'cinemaizle.org : ' + self.playlist_cat_name
                    self.video_liste = self.get_cinemaizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_cinemaizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_cinemaizle_film(url)
            if url.find('filmtekpart.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.filmtekpart.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmtekpart_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmtekpart.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmtekpart_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmtekpart_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmtekpart_film(url)
            if url.find('divxfilmizle.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.divxfilmizle.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_divxfilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'divxfilmizle.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_divxfilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_divxfilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_divxfilmizle_film(url)
            if url.find('hdfilmtube.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.hdfilmtube.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hdfilmtube_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hdfilmtube.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_hdfilmtube_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdfilmtube_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdfilmtube_film(url)
            if url.find('filmizlehep.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'filmizlehep.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmizlehep_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmizlehep.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmizlehep_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmizlehep_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmizlehep_film(url)
            if url.find('seyretogren.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.seyretogren.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_seyretogren_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'seyretogren.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_seyretogren_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_seyretogren_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_seyretogren_film(url)
            if url.find('vkfilmizle.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.vkfilmizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_vkfilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'vkfilmizle.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_vkfilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_vkfilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_vkfilmizle_film(url)
            if url.find('movietr.org') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.movietr.org'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_movietr_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'movietr.org : ' + self.playlist_cat_name
                    self.video_liste = self.get_movietr_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_movietr_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_movietr_film(url)
            if url.find('filmodam.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.filmodam.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmodam_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmodam.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmodam_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmodam_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmodam_film(url)
            if url.find('gercekfilmler.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.gercekfilmler.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_gercekfilmler_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'gercekfilmler.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_gercekfilmler_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_gercekfilmler_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_gercekfilmler_film(url)
            if url.find('tamseyret.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.tamseyret.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_tamseyret_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'tamseyret.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_tamseyret_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_tamseyret_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_tamseyret_film(url)
            if url.find('sinesalon.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.sinesalon.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_sinesalon_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'sinesalon.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_sinesalon_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_sinesalon_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_sinesalon_film(url)
            if url.find('cinestream.cc') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'cinestream.cc'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_cinestream_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'cinestream.cc : ' + self.playlist_cat_name
                    self.video_liste = self.get_cinestream_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_cinestream_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_cinestream_film(url)
            if url.find('zaplat.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.zaplat.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_zaplat_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'zaplat.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_zaplat_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_zaplat_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_zaplat_film(url)
            if url.find('hbyfilm.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.hbyfilm.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hbyfilm_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hbyfilm.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_hbyfilm_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hbyfilm_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hbyfilm_film(url)
            if url.find('belgeseltv.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.belgeseltv.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_belgeseltvnet_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_belgeseltvnet_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_belgeseltvnet_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_belgeseltvnet_film(url)
            if url.find('trfullfilmizle.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.trfullfilmizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_trfullfilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'trfullfilmizle.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_trfullfilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_trfullfilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_trfullfilmizle_film(url)
            if url.find('trdiziizle.org') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.trdiziizle.org'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_trdiziizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'trdiziizle.org : ' + self.playlist_cat_name
                    self.video_liste = self.get_trdiziizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_trdiziizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_trdiziizle_film(url)
            if url.find('hdivx.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.hdivx.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hdivx_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hdivx.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_hdivx_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdivx_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdivx_film(url)
            if url.find('720pfilmizle.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.720pfilmizle.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_720pfilmizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = '720pfilmizle.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_720pfilmizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_720pfilmizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_720pfilmizle_film(url)
            if url.find('herdizi.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.herdizi.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_herdizi_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'herdizi.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_herdizi_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_herdizi_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_herdizi_film(url)
            if url.find('filmcok.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.filmcok.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmcok_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmcok.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmcok_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmcok_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmcok_film(url)
            if url.find('sporxtv.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.sporxtv.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_sporxtv_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'sporxtv.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_sporxtv_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_sporxtv_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_sporxtv_film(url)
            if url.find('diziwu.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.diziwu.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_diziwu_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'diziwu.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_diziwu_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_diziwu_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_diziwu_film(url)
            if url.find('dizi-mag.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.dizi-mag.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_dizimag_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'dizi-mag.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_dizimag_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_dizimag_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_dizimag_film(url)
            if url.find('ddizi.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'ddizi.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_ddizi_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'ddizi.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_ddizi_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_ddizi_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_ddizi_film(url)
            if url.find('fullhdfilmizlet.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.fullhdfilmizlet.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_fullhdfilmizlet_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'fullhdfilmizlet.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_fullhdfilmizlet_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_fullhdfilmizlet_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_fullhdfilmizlet_film(url)
            if url.find('dizihdtv') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'dizihdtv.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_dizihdtv_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_dizihdtv_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_dizihdtv_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_dizihdtv_film(url)
            if url.find('pornetto') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.pornetto.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_pornetto_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_pornetto_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_pornetto_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_pornetto_film(url)
            if url.find('webteizle') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'webteizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_webteizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'webteizle.com: ' + self.playlist_cat_name
                    self.video_liste = self.get_webteizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_webteizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_webteizle_film(url)
            if url.find('hdbelgeselizle.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.hdbelgeselizle.com'
                if page == 'start':
                    url = 'www.hdbelgeselizle.com'
                    self.playlistname = name
                    self.video_liste = self.get_hdbelgeselizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'KATEGORILER: ' + self.playlist_cat_name
                    self.video_liste = self.get_hdbelgeselizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdbelgeselizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdbelgeselizle_film(url)
            if url.find('annemmutfakta.tv') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.annemmutfakta.tv'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_annemmutfakta_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'annemmutfakta.tv : ' + self.playlist_cat_name
                    self.video_liste = self.get_annemmutfakta_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_annemmutfakta_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_annemmutfakta_film(url)
            if url.find('webtv.hurriyet') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'webtv.hurriyet.com.tr'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hurriyet_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_hurriyet_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hurriyet_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hurriyet_film(url)
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hurriyetyazar_film(url)
            if url.find('trdizi.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.trdizi.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_trdizi_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_trdizi_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_trdizi_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = name
                    self.video_liste = self.get_trdizi_film(url)
            if url.find('xvideos.com') > -1:
                debug('#SWITCH xvideos.com #')
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.xvideos.com'
                video_list_temp = []
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_xvideos_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'XVIDEOS CAT: ' + self.playlist_cat_name
                    self.video_liste = self.get_xvideos_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    print '++++++++++++'
                    print page
                    print len(page)
                    if int(len(page) - 2) > 0:
                        page_nr = ' PAGE ' + page[len(page) - 2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_xvideos_category_films(url)
                    self.category_back_url = url
            if url.find('bicaps.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'bicaps.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_bicaps_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'bicaps.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_bicaps_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_bicaps_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_bicaps_film(url)
            if url.find('eroguru') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'eroguru.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_eroguru_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_eroguru_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_eroguru_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_eroguru_film(url)
            if url.find('evrenselfilm') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.evrenselfilm.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_evrenselfilm_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_evrenselfilm_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_evrenselfilm_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_evrenselfilm_film(url)
            if url.find('fragg') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'fragg.me'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_fragg_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_fragg_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_fragg_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_fragg_film(url)
            if url.find('filmizlese') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.filmizlese.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmizlese_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_filmizlese_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmizlese_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmizlese_film(url)
            if url.find('myvideo') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.myvideo.de'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_myvideo_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_myvideo_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_myvideo_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = name
                    self.video_liste = self.get_myvideo_film(url)
            if url.find('megasinema.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'megasinema.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_megasinema_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'megasinema.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_megasinema_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_megasinema_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_megasinema_film(url)
            if url.find('filmizleturkcedublaj.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'filmizleturkcedublaj.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_filmizleturkcedublaj_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'filmizleturkcedublaj.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_filmizleturkcedublaj_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_filmizleturkcedublaj_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_filmizleturkcedublaj_film(url)
            if url.find('hdfilmport.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'hdfilmport.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_hdfilmport_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'hdfilmport.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_hdfilmport_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_hdfilmport_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_hdfilmport_film(url)
            if url.find('macozetizle') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'macozetizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_macozetizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'macozetizle.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_macozetizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_macozetizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_macozetizle_film(url)
            if url.find('megasinema.net') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'megasinema.net'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_megasinema_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'megasinema.net : ' + self.playlist_cat_name
                    self.video_liste = self.get_megasinema_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 5 and page[3] == 'page':
                        page_nr = ' PAGE ' + page[4]
                    if len(page) == 3 and page[1] == 'page':
                        page_nr = ' PAGE ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_megasinema_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_megasinema_film(url)
            if url.find('vizyonfilmi.org') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'vizyonfilmi.org'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_vizyonfilmi_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'vizyonfilmi.org : ' + self.playlist_cat_name
                    self.video_liste = self.get_vizyonfilmi_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_vizyonfilmi_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_vizyonfilmi_film(url)
            if url.find('yabancidiziizle') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2].encode('utf-8')
                self.active_site_url = 'www.yabancidiziizle.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_yabancidiziizle_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = self.playlist_cat_name
                    self.video_liste = self.get_yabancidiziizle_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_yabancidiziizle_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_yabancidiziizle_film(url)
            if url.find('kemalsunalfilm.com') > -1:
                parts = url.split('@')
                url = parts[0]
                page = parts[1]
                name = parts[2]
                self.active_site_url = 'www.kemalsunalfilm.com'
                if page == 'start':
                    self.playlistname = name
                    self.video_liste = self.get_kemalsunalfilm_categories(url)
                if page == 'category':
                    self.playlist_cat_name = name
                    self.playlistname = 'kemalsunalfilm.com : ' + self.playlist_cat_name
                    self.video_liste = self.get_kemalsunalfilm_category_films(url)
                    self.category_back_url = url
                    self.category_title = name
                if page == 'category_page':
                    page_nr = ''
                    page = url.split('/')
                    if len(page) == 6 and page[3] == 'page':
                        page_nr = ' SAYFA ' + page[4]
                    if len(page) == 4 and page[1] == 'page':
                        page_nr = ' SAYFA ' + page[2]
                    self.playlistname = self.playlist_cat_name + page_nr
                    self.video_liste = self.get_kemalsunalfilm_category_films(url)
                    self.category_back_url = url
                if page == 'film':
                    self.kino_title = name
                    self.playlistname = self.playlist_cat_name + ' ' + name
                    self.video_liste = self.get_kemalsunalfilm_film(url)
            return self.video_liste

    def get_hdfilmsehri_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.hdfilmsehri.com/wp-content/uploads/2012/04/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.hdfilmsehri.com/wp-content/uploads/2012/04/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li><a href="http:\\/\\/(www.hdfilmsehri.com\\/category.*?)">(.*?)<\\/a><\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.hdfilmsehri.com/wp-content/uploads/2012/08/logoo1.jpg',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.hdfilmsehri.com/wp-content/uploads/2012/08/logoo1.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hdfilmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmsehri_category'

        return video_list_temp

    def get_hdfilmsehri_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h2> <a href="(.*?)">(.*?)<\\/a> <\\/h2>', page)
            for text in regex:
                url = text[0]
                title = text[1].replace('&#8211; ', '')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hdfilmsehri.com@start@hdfilmsehri KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hdfilmsehri CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmsehri_category_films'

        return video_list_temp

    def get_hdfilmsehri_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(http:\\/\\/vk.com.*?)".*?><\\/iframe>', page)
        descr = re.findall('<div class="konuozet">\\W+<p><p>(.*?)<\\/p>', page)
        img = re.findall('<img.*? src="(.*?)" class=".*?wp-post-image"', page)
        url22 = re.findall('<a href="http:\\/\\/(\\b[^>]*)"><span>.*?<\\/span>', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<p><iframe.*?src="(.*?)".*?><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '').replace('amp;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('<iframe.*?src="http:\\/\\/www.youtube.com\\/embed\\/(.*?)".*?><\\/iframe>', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Fragman : ' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_unutulmazfilmler_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://unutulmazfilmler.com/images/logo.gif',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://unutulmazfilmler.com/images/logo.gif',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<a href="(http:\\/\\/unutulmazfilmler.com\\/kategori\\/.*?)">\\W+<img src=".*?" alt="(.*?)" \\/>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://unutulmazfilmler.com/images/logo.gif',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://unutulmazfilmler.com/images/logo.gif',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR unutulmazfilmler CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_unutulmazfilmler_category'

        return video_list_temp

    def get_unutulmazfilmler_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="(.*?)"><img src="(.*?)" width="134" height="194" alt="(.*?)" \\/><\\/a>', page)
            for text in regex:
                url = text[0]
                img_url = text[1]
                title = text[2].replace('&#8211; ', '')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<\\/span> <a href="(.*?)">', page)
            prev = re.findall('<\\/a> <a href="(.*?)">\\d+<\\/a> <span>\\d+<\\/span>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@unutulmazfilmler.com@start@unutulmazfilmler KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR unutulmazfilmler CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_unutulmazfilmler_category_films'

        return video_list_temp

    def get_unutulmazfilmler_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        match = re.compile('webscripti\\("(.*?)","(.*?)"\\);').findall(page)
        for a, b in match:
            bilgiler = urllib.urlencode({'vid': a,
             'kisim': b})

        vk = mod_request('http://unutulmazfilmler.com/playerayar.php', bilgiler)
        vk = re.compile('src="(http://vk.com/.*?)"').findall(vk)
        img = re.compile('<div class="leftflmbg_left2">\\W+<a.*?><img src="(.*?)"').findall(page)
        descr = re.findall('<div class="leftflmbg_right_content">\\W+(.*?)<\\/div>', page)
        url22 = re.findall('<a href="(.*?)">Part \\d+', page)
        for link in url22:
            page2 = mod_request(link)
            match = re.compile('webscripti\\("(.*?)","(.*?)"\\);').findall(page2)
            for a, b in match:
                bilgiler = urllib.urlencode({'vid': a,
                 'kisim': b})

            vk2 = mod_request('http://unutulmazfilmler.com/playerayar.php', bilgiler)
            vk2 = re.compile('src="(http://vk.com/.*?)"').findall(vk2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for url in vk:
                text = url
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_divxclub_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.divxclub.net/wp-content/themes/keremiya/logo/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.divxclub.net/wp-content/themes/keremiya/logo/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="(http:\\/\\/.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.divxclub.net/wp-content/themes/keremiya/logo/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.divxclub.net/wp-content/themes/keremiya/logo/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR divxclub CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_divxclub_category'

        return video_list_temp

    def get_divxclub_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a href="(.*?)">\\W+.*?<img src="(.*?)" alt="(.*?)".*?\\/>', page)
            for text in regex:
                url = text[0]
                img_url = text[1]
                title = text[2].replace('&#8211; ', '')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("<span class=.current.>\\d+<\\/span><a href=\\'(http:\\/\\/\\b[^>]*)\\' class=\\'page larger\\'>", page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@divxclub.net@start@divxclub KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR divxclub CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_divxclub_category_films'

        return video_list_temp

    def get_divxclub_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        pl_link = re.findall('<iframe src="(http:\\/\\/www.putlocker.com.*?)"', page, re.S)
        data = mod_request(pl_link[0])
        url_id = re.findall('<a href="/file/(.*?)"', data, re.S)
        url = 'http://www.putlocker.com/embed/%s' % url_id[0]
        enter = re.findall('<input type="hidden" value="(.*?)" name="fuck_you">', data)
        post_data = urlencode({'fuck_you': enter[0],
         'confirm': 'Close Ad and Watch as Free User'})
        values = {'fuck_you': enter[0],
         'confirm': 'Close+Ad+and+Watch+as+Free+User'}
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        cookiejar = cookielib.LWPCookieJar()
        cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
        opener = urllib2.build_opener(cookiejar)
        urllib2.install_opener(opener)
        data = urlencode(values)
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        link = response.read()
        embed = re.findall("get_file.php.stream=(.*?)'\\,", link, re.S)
        req = urllib2.Request('http://www.putlocker.com/get_file.php?stream=%s' % embed[0])
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        link = response.read()
        stream_url = re.findall('<media:content url="(.*?)"', link, re.S)
        medialink = stream_url[1].replace('&amp;', '&').replace("'", '')
        descr = re.findall('<div class="konuozet">\\W+<p><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img src="(.*?)"', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(medialink) > 0:
            text = medialink
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + ' Parca :' + str(chan_counter),
             aciklama,
             img[0],
             text,
             None,
             None,
             img[0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_onlinefilmizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://onlinefilmizle.tv/wp-content/uploads/2012/06/online_film_izle.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://onlinefilmizle.tv/wp-content/uploads/2012/06/online_film_izle.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://onlinefilmizle.tv/wp-content/uploads/2012/06/online_film_izle.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://onlinefilmizle.tv/wp-content/uploads/2012/06/online_film_izle.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_onlinefilmizle_category_films(self, url):
        print 'get_onlinefilmizle_category_films'
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\n<a.*?href="http:\\/\\/(.*?)">\\n<img src="(http:\\/\\/.*?)" alt="(.*?)" height=".*?".*?width=".*?".*?\\/>.*?<\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('#8211;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("<span class='current'>\\d+<\\/span><a href='(http:\\/\\/.*?)' class='page larger'>", page)
            prev = re.findall("<a.*?href='(.*?)'.*?class='previouspostslink'>", page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@onlinefilmizle.tv@start@ONLINEFILMIZLE KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_onlinefilmizle_film(self, url):
        print 'get_sinemaizle_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="konuozet">\\n.*?<p><p>(.*?)<\\/p>', page)
        img = re.findall('<img.*?src="(.*?)".*?alt=".*?".*?height=".*?" width=".*?".*?\\/>', page)
        url2 = re.findall('Part.*?<\\/span>.*?<a.*?href="http:\\/\\/(.*?)">.*?<span>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<p><iframe.*?src="(.*?)".*?width=".*?".*?height=".*?".*?frameborder=".*?"><\\/iframe><\\/p>', page2)
            for ll in vk2:
                vk.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_onlinefilmiizlet_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.onlinefilmiizlet.com/wp-content/themes/tahamata-v2/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.onlinefilmiizlet.com/wp-content/themes/tahamata-v2/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_onlinefilmiizlet_category_films(self, url):
        print 'get_onlinefilmiizlet_category_films'
        try:
            page = mod_request(url)
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="imdb.*?".*?><\\/div>\\n.*?\\n.*?<a.*?href="http:\\/\\/(.*?)" title="(.*?)">\\n.*?\\n<img src="(http:\\/\\/.*?)".*?<\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("<span class='page-numbers current'>\\d+<\\/span>\\n<a class='page-numbers' href='(http:\\/\\/.*?)'>\\d+<\\/a>", page)
            prev = re.findall("<a class='page-numbers' href='(.*?\\d+)'>\\d+<\\/a>\\n<span class='page-numbers current'>\\d+<\\/span>", page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@onlinefilmiizlet.com@start@ONLINEFILMIIZLET KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_onlinefilmiizlet_film(self, url):
        print 'get_hdfilmsiten_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="filmdetayx_aciklama">.*?<\\/div>\\n<p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmdetayx_resimimg">\\n<img src="(http:\\/\\/.*?)" class="img" alt="" \\/><\\/div>', page)
        url2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmifullizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://resim.filmifullizle.com/resimler/logo.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://resim.filmifullizle.com/resimler/logo.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://resim.filmifullizle.com/resimler/logo.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://resim.filmifullizle.com/resimler/logo.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmifullizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmifullizle_category'

        return video_list_temp

    def get_filmifullizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="http:\\/\\/(.*?)"><img.*?src="(.*?)".*?alt="(.*?)" class="captify".*?><\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('#8211;', '', title)
                title = re.sub('&#038;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active_page"><a href=".*?">.*?<\\/a><\\/li>\\n<li><a href="(.*?)">.*?<\\/a><\\/li>', page)
            prev = re.findall('<li><a href="(.*?)">\\d+<\\/a><\\/li>\\n<li class="active_page">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmifullizle.com@start@filmifullizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmifullizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmifullizle_category_films'

        return video_list_temp

    def get_filmifullizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="solmeta"><b>A..klama<\\/b><\\/div>.*?\\n(.*?)<br \\/>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title,
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_hdfilmsiten_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.hdfilmsiten.com/wp-content/themes/temahd/c/dizifilm/webtv/c/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.hdfilmsiten.com/wp-content/themes/temahd/c/dizifilm/webtv/c/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.hdfilmsiten.com/wp-content/themes/temahd/c/dizifilm/webtv/c/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.hdfilmsiten.com/wp-content/themes/temahd/c/dizifilm/webtv/c/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hdfilmsiten CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmsiten_category'

        return video_list_temp

    def get_hdfilmsiten_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="filmresim">\\n.*?\\n.*?<a.*?href="http:\\/\\/(.*?)" title="(.*?)"><img src="(http:\\/\\/.*?)".*?<\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('span class=.current.>\\d+<\\/span><a  href="(http:\\/\\/.*?)" class="page larger">', page)
            prev = re.findall('<\\/a><a\\s+href="(.*?\\d+)" class="previouspostslink">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hdfilmsiten.com@start@hdfilmsiten KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hdfilmsiten CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmsiten_category_films'

        return video_list_temp

    def get_hdfilmsiten_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<p><iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe><\\/p>', page)
        descr = re.findall('<em>(.*?)<\\/em>', page)
        img = re.findall('<link rel="image_src" href="(http:\\/\\/.*?)"\\/>', page)
        url2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Part : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_gunlukfilm_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://gunlukfilm.com/wp-content/themes/gunluk/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://gunlukfilm.com/wp-content/themes/gunluk/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1].replace('&#8211;', '')
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://gunlukfilm.com/wp-content/themes/gunluk/images/logo.png',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://gunlukfilm.com/wp-content/themes/gunluk/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR gunlukfilm CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_gunlukfilm_category'

        return video_list_temp

    def get_gunlukfilm_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="film-baslik"><a href="http:\\/\\/(.*?)" title="(.*?)">.*?<\\/a><\\/div>', page)
            img = re.findall('<p><img.*?src="(http:\\/\\/.*?)".*?" \\/><\\/p>', page)
            for text in regex:
                url = text[0]
                img_url = img[0]
                title = text[1].replace('&#8211;', ' ')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active_page"><a href=".*?">.*?<\\/a><\\/li>\\n<li><a href="(http:\\/\\/.*?)">.*?<\\/a><\\/li>', page)
            prev = re.findall('<li><a href="(http:\\/\\/.*?)">\\d+<\\/a><\\/li>\\n<li class="active_page">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@gunlukfilm.com@start@GUNLUKFILM KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR gunlukfilm CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_gunlukfilm_category_films'

        return video_list_temp

    def get_gunlukfilm_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(http:\\/\\/vk.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe><\\/p>', page)
        descr = re.findall('<div.*?class="konuozet">\\s*<p><\\/p>\\s*(.*?)\\s*<\\/div>', page)
        img = re.findall('<img src="(.*?)" alt=".*?" title=".*?" width="\\d+" height="\\d+".*?\\/>', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_direkizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://direkizle.net/wp-content/themes/sorunsuztema/images/direkizle-11.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://direkizle.net/wp-content/themes/sorunsuztema/images/direkizle-11.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1].replace('&#8211;', '')
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://direkizle.net/wp-content/themes/sorunsuztema/images/direkizle-11.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://direkizle.net/wp-content/themes/sorunsuztema/images/direkizle-11.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_direkizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="filmbaslik"><h2><a.*?href="http:\\/\\/(.*?)" rel=".*?" title="(.*?)">.*?<\\/a><\\/h2><\\/div>', page)
            img = re.findall('<p><img.*?src="(http:\\/\\/.*?)".*? width="\\d+" height="\\d+" .*?/>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = img[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active_page"><a href=".*?">.*?<\\/a><\\/li>\\n<li><a href="(.*?)">.*?<\\/a><\\/li>', page)
            prev = re.findall('<\\/li>\\s?<li><a href="(http:\\/\\/.*?)">\\d+<\\/a><\\/li>\\n<li class="active_page">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@direkizle.net@start@DIREKIZLE KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_direkizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div.*?class="konuozet">\\s*<p><\\/p>\\s*(.*?)\\s*<\\/div>', page)
        img = re.findall('<p><img.*?src="(http://.*?)".*? width="\\d+" height="\\d+" .*?/>', page)
        url2 = re.findall('Part.*?<\\/span>.*?<a.*?href="http:\\/\\/(.*?)">.*?<span>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<p><iframe.*?src="(.*?)".*?width=".*?".*?height=".*?".*?frameborder=".*?"><\\/iframe><\\/p>', page2)
            for ll in vk2:
                vk.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_birfilmizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.birfilmizle.net/wp-content/themes/CineMovie/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.birfilmizle.net/wp-content/themes/CineMovie/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1].replace('&#8211;', '')
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.birfilmizle.net/wp-content/themes/CineMovie/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.birfilmizle.net/wp-content/themes/CineMovie/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_birfilmizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="soneklenen-orta">\\n<a href="http:\\/\\/(.*?)" title="(.*?)">\\n*<img src=".*?\\?src=(http:\\/\\/.*?)&.*?<\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("<span class='current'>\\d+<\\/span><a href='(.*?)' class.*?>", page)
            prev = re.findall("<a href='(http://www.birfilmizle.net/page/\\d+)' class='page smaller'>\\d+</a><span class='current'>\\d+</span>", page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@birfilmizle.net@start@BIRFILMIZLE KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_birfilmizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="detaylaricc">Konusu : <span><p>(.*?)</p>', page)
        img = re.findall('<div class="vizyon-film-orta">\\n<a href=".*?" title=".*?"><img src=".*?src=(.*?jpg)&.*?" alt=".*?"\\/><\\/a>', page)
        url2 = re.findall('Part.*?<\\/span>.*?<a.*?href="http:\\/\\/(.*?)">.*?<span>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<p><iframe.*?src="(.*?)".*?width=".*?".*?height=".*?".*?frameborder=".*?"><\\/iframe><\\/p>', page2)
            for ll in vk2:
                vk.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_cinemaizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://cinemaizle.org/wp-content//themes/zadev2/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://cinemaizle.org/wp-content//themes/zadev2/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a href="(http:\\/\\/.*?)" title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://cinemaizle.org/wp-content//themes/zadev2/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://cinemaizle.org/wp-content//themes/zadev2/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR cinemaizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_cinemaizle_category'

        return video_list_temp

    def get_cinemaizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="ana-resim"><a href="http:\\/\\/(.*?)" ><img src=".*?src=(http:\\/\\/.*?)&.*? alt="(.*?)" \\/><\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('#8211;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@cinemaizle.org@start@cinemaizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR cinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_cinemaizle_category_films'

        return video_list_temp

    def get_cinemaizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<h1>.*?</h1>\\n<p>(.*?)<br \\/>', page)
        img = re.findall('<div class="aciklamaresim">\\n<img src=".*?src=(http:\\/\\/.*?)&.*?<\\/div>', page)
        url22 = re.findall('<a href="http:\\/\\/(.*?)">K.*?m \\d+<\\/a>', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('<iframe width="\\d+".?height="\\d+" src="http:\\/\\/www.youtube.com\\/embed\\/(\\S{11}).*?frameborder="\\d+".*?><\\/iframe>', page)
        isim = re.findall('<h2 class="baslik"><a href=".*?" rel="bookmark" title="(.*?)">.*?<\\/a><\\/h2>', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                title = isim[0]
                chan_tulpe = (chan_counter,
                 title + ' Parca : ' + str(chan_counter),
                 '',
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmtekpart_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.filmtekpart.com/wp-content/themes/tahamata-V2/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.filmtekpart.com/wp-content/themes/tahamata-V2/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li\\W+class="cat-item cat-item-\\d+"><a\\nhref="http:\\/\\/(.*?)" title=".*?">(.*)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.filmtekpart.com/wp-content/themes/tahamata-V2/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.filmtekpart.com/wp-content/themes/tahamata-V2/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmtekpart CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmtekpart_category'

        return video_list_temp

    def get_filmtekpart_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a\\Whref="http:\\/\\/(.*?)" title="(.*?)"><img\\Wsrc="(.*?)" class="img" alt="" \\/><\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('&#8211;', '', title)
                title = re.sub('&#038;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("<span class='current'>\\d+</span><a href='(http://.*?)' class='page larger'>", page)
            prev = re.findall("class='page-numbers' href='(http://.*?)'>\\d+<\\/a> <span\\nclass='page-numbers current'>\\d+</span>", page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmtekpart.com@start@filmtekpart KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmtekpart CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmtekpart_category_films'

        return video_list_temp

    def get_filmtekpart_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('class="filmdetayx_aciklama"><p>(.*)<a', page)
        img = re.findall('<div\\nclass="filmdetayx_resimimg"> <img\\nsrc="(http:\\/\\/.*?)" class="img" alt="" /></div>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 descr[0],
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_divxfilmizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.divxfilmizle.net/wp-content/themes/inove/img/header.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.divxfilmizle.net/wp-content/themes/inove/img/header.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a href="http:\\/\\/(.*?)" title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.divxfilmizle.net/wp-content/themes/inove/img/header.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.divxfilmizle.net/wp-content/themes/inove/img/header.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR divxfilmizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_divxfilmizle_category'

        return video_list_temp

    def get_divxfilmizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a href="(.*?)">\\W+<img src="(.*?)" alt="(.*?)".*?\\/><\\/a>', page)
            descr = re.findall('<strong>Film Konusu:<\\/strong><\\/span>(.*?)<br \\/>', page)
            if len(descr):
                aciklama = descr[0]
            else:
                aciklama = 'Konu mevcut degil'
            for text in regex:
                img_url = text[1]
                url = text[0]
                title = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active"><a href=".*?">\\d+<\\/a><\\/li><li><a href="(.*?)">', page)
            prev = re.findall('(http:\\/\\/\\b[^<]*)">&laquo; Geri', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@divxfilmizle.net@start@DIVXFILMIZLE KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR divxfilmizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_divxfilmizle_category_films'

        return video_list_temp

    def get_divxfilmizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="(http:\\/\\/vk.com\\b[^"]*)', page)
        descr = re.findall('<strong>Film Konusu:<\\/strong><\\/span>(.*?)<br \\/>', page)
        img = re.findall('<p><img src="(.*?)" alt="" title=".*?"', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('amp;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('<iframe width="\\d+".?height="\\d+" src="http:\\/\\/www.youtube.com\\/embed\\/(\\S{11}).*?frameborder="\\d+".*?><\\/iframe>', page)
        isim = re.findall('<p><img class="alignleft size-full wp-image-\\d+" title="(.*?)"', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                title = isim[0]
                chan_tulpe = (chan_counter,
                 title + ' Parca : ' + str(chan_counter),
                 '',
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_hdfilmtube_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.hdfilmtube.com/wp-content/themes/blackman/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.hdfilmtube.com/wp-content/themes/blackman/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.hdfilmtube.com/wp-content/themes/blackman/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.hdfilmtube.com/wp-content/themes/blackman/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hdfilmtube CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmtube_category'

        return video_list_temp

    def get_hdfilmtube_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('class="durumdil2"><\\/div><a href="http:\\/\\/(.*?)" title="(.*?)"><img src="(.*?)" \\/><\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('&#8211;', '', title)
                title = re.sub('&#038;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+<\\/span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hdfilmtube.com@start@hdfilmtube KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hdfilmtube CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdfilmtube_category_films'

        return video_list_temp

    def get_hdfilmtube_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<span class="pas">Konusu: </span>(.*?)\\n', page)
        img = re.findall('<a href="(.*?)" rel="lightbox"><img id="afisimdostumm" src="http:\\/\\/.*?" alt=".*?"\\/><\\/a>', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmizlehep_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://filmizlehep.com/wp-content/themes/filmizlehep/images/header_zemin.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://filmizlehep.com/wp-content/themes/filmizlehep/images/header_zemin.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://filmizlehep.com/wp-content/themes/filmizlehep/images/header_zemin.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://filmizlehep.com/wp-content/themes/filmizlehep/images/header_zemin.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmizlehep CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmizlehep_category'

        return video_list_temp

    def get_filmizlehep_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="cover">\\W+<.*?\\W*.*?a  href="(.*?)" rel="bookmark"><img src="(.*?)".*?alt="(.*?)"', page)
            for text in regex:
                url = text[0]
                img_url = text[1]
                title = text[2].replace('&#8211; ', '')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+<\\/span><a\\s+href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a\\s+href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmizlehep.net@start@filmizlehep KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmizlehep CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmizlehep_category_films'

        return video_list_temp

    def get_filmizlehep_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="(http:\\/\\/vk.com\\/.*?)"', page)
        img = re.findall('<a  href="http:\\/\\/.*?" rel="bookmark"><img src="(.*?)" alt=".*?" class="afis" \\/><\\/a>', page)
        url22 = re.findall('<li class="pagelink"><center><a  href="(.*?)">', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe src="(http:\\/\\/vk.com\\/.*?)"', page2)
            for jj in vk2:
                vk.append(jj)

        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 None,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_belgeseltvnet_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             '',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li id="menu-item-.*?" class=".*?"><a href="http:\\/\\/(www.belgeseltv.net/kategori.*?)">(.*?)<\\/a><\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 '',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR belgeseltvnet CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_belgeseltvnet_category'

        return video_list_temp

    def get_belgeseltvnet_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="cover"><a href="http:\\/\\/(.*?)" rel="bookmark" title="(.*?)"><img src=".*?src=(http:\\/\\/.*?)&.*?width=".*?" height=".*?" alt=".*?" \\/><\\/a><\\/div>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<p><a href="http:\\/\\/(.*?)" >.*?nceki Sayfalar<\\/a><a href=".*" >Sonraki Sayfalar &raquo;</a></p>', page)
            prev = re.findall('<p><a href="http:\\/\\/.*?" >.*?nceki Sayfalar<\\/a><a href="(.*)" >Sonraki Sayfalar &raquo;</a></p>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@belgeseltv.net@start@belgeseltvnet KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR belgeseltvnet CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_belgeseltvnet_category_films'

        return video_list_temp

    def get_belgeseltvnet_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="(.*?)" frameborder="\\d+" width="\\d+" height="\\d+"><\\/iframe><\\/p>', page)
        descr = re.findall('<div.*?class="konuozet">\\s*<p><\\/p>\\s*(.*?)\\s*<\\/div>', page)
        img = re.findall('<img.*?src="(.*?)".*?alt=".*?".*?height=".*?" width=".*?".*?\\/>', page)
        url2 = re.findall('Part.*?<\\/span>.*?<a.*?href="http:\\/\\/(.*?)">.*?<span>', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<p><iframe.*?src="(.*?)".*?width=".*?".*?height=".*?".*?frameborder=".*?"><\\/iframe><\\/p>', page2)
            for ll in vk2:
                vk.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('<param name="movie" value="http:\\/\\/www.youtube.com\\/v\\/(\\S{11}).*? \\/><param name=".*?" value=".*?" \\/>', page)
        isim = re.findall('<h1><a href="http:\\/\\/.*?" rel="bookmark" title=".*?">(.*?)<\\/a><\\/h1>', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                title = isim[0]
                chan_tulpe = (chan_counter,
                 title + ' Parca : ' + str(chan_counter),
                 '',
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_seyretogren_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex2 = re.findall('<a href="(.*?)">.*?<\\/a> \\x7C', page)
            for text in regex2:
                title = text
                url = 'www.seyretogren.com/' + text
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.seyretogren.com/templates/ja_lead/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.seyretogren.com/templates/ja_lead/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR seyretogren CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_seyretogren_category'

        return video_list_temp

    def get_seyretogren_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h4><a href="\\/(.*?)" title="(.*?)">.*?<\\/a><\\/h4>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + 'www.seyretogren.com/' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active_page"><a href=".*?">.*?<\\/a><\\/li>\\n<li><a href="(.*?)">.*?<\\/a><\\/li>', page)
            prev = re.findall('<li><a href="(.*?)">\\d+<\\/a><\\/li>\\n<li class="active_page">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@seyretogren.com@start@seyretogren KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR seyretogren CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_seyretogren_category_films'

        return video_list_temp

    def get_seyretogren_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<div class="videotitleinmodule" ><a href=http:\\/\\/(.*?)>.*?<\\/a>', page)
        url22 = re.findall('<div class="videotitleinmodule"><a href=http:\\/\\/(.*?)>.*?<\\/a>', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<param name="flashvars" value="file=(.*?)&amp;autostart=true">', page2)
            for jj in vk2:
                vk.append(jj)

        if len(vk) > 0:
            for text in vk:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_vkfilmizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.vkfilmizle.com/wp-content/themes/tahamata/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.vkfilmizle.com/wp-content/themes/tahamata/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li\\Wclass="cat-item cat-item-\\d+"><a  href="(http:\\/\\/.*?)" title=".*?">(.*)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.vkfilmizle.com/wp-content/themes/tahamata/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.vkfilmizle.com/wp-content/themes/tahamata/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR vkfilmizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_vkfilmizle_category'

        return video_list_temp

    def get_vkfilmizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a  href="(http:\\/\\/.*?)" title="(.*?)"><img src="(http:\\/\\/.*?)" alt=".*?" class="thumbnail"', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = title.replace('&#8211;', '')
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.page-numbers current.>\\d+<\\/span>\\n<a  class="page-numbers" href=.(http:\\/\\/\\b[^>]*)', page)
            prev = re.findall('<a  class="page-numbers" href=.(http:\\/\\/\\b[^>]*).>\\d+<\\/a>\\n<span class=.page-numbers current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@vkfilmizle.com@start@vkfilmizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR vkfilmizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_vkfilmizle_category_films'

        return video_list_temp

    def get_vkfilmizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('src="(http:\\/\\/vk.com.*?)"', page)
        descr = re.findall('<div class="filmdetayx_aciklama"><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmdetayx_resim">\\W+<img src="(.*?)" alt=".*?" class="resimboyut" \\/>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 descr[0],
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_movietr_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://d1206.hizliresim.com/y/d/7tv7z.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://d1206.hizliresim.com/y/d/7tv7z.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a href="(http:\\/\\/.*?)" title=".*?">(.*)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://d1206.hizliresim.com/y/d/7tv7z.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://d1206.hizliresim.com/y/d/7tv7z.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR movietr CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_movietr_category'

        return video_list_temp

    def get_movietr_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="(http:\\/\\/.*?)" rel="bookmark" title="(.*?)"><img src="(.*?)".*?alt=""', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.page-numbers current.>\\d+<\\/span>\\n<a  class="page-numbers" href=.(http:\\/\\/\\b[^>]*)', page)
            prev = re.findall('<a  class="page-numbers" href=.(http:\\/\\/\\b[^>]*).>\\d+<\\/a>\\n<span class=.page-numbers current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@movietr.org@start@movietr KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR movietr CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_movietr_category_films'

        return video_list_temp

    def get_movietr_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(http:\\/\\/vk.com.*?)"', page)
        descr = re.findall('<p><span>Konu<\\/span>: (.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img.*?src="(.*?)".*?alt=".*?".*?height=".*?" width=".*?".*?\\/>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 None,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmodam_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.filmodam.com/wp-content/uploads/2012/06/FILMODAM1.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.filmodam.com/wp-content/uploads/2012/06/FILMODAM1.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a  href="http:\\/\\/(.*?)" title=".*?">(.*)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.filmodam.com/wp-content/uploads/2012/06/FILMODAM1.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.filmodam.com/wp-content/uploads/2012/06/FILMODAM1.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmodam CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmodam_category'

        return video_list_temp

    def get_filmodam_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div id="moviefilm">\\W+<a  href="(.*?)" rel="bookmark" title="(.*?)"><img src=".*?"', page)
            for text in regex:
                url = text[0]
                title = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a  href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmodam.com@start@filmodam KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmodam CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmodam_category_films'

        return video_list_temp

    def get_filmodam_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="(http:\\/\\/vk.com.*?)"', page)
        descr = re.findall('<p><span>Konu<\\/span>:(.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img src="(http:\\/\\/.*?)"', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '').replace('amp;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_gercekfilmler_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.gercekfilmler.com/wp-content/themes/filmizle/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.gercekfilmler.com/wp-content/themes/filmizle/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a href="http:\\/\\/(.*?)" title=".*?">(.*)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.gercekfilmler.com/wp-content/themes/filmizle/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.gercekfilmler.com/wp-content/themes/filmizle/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR gercekfilmler CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_gercekfilmler_category'

        return video_list_temp

    def get_gercekfilmler_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="entry">\\W+<a href="http:\\/\\/(.*?)" rel="bookmark" title="(.*?)">', page)
            img = re.findall('<img src="(http:\\/\\/.*?)" alt=".*?" class="post_thumbnail" \\/>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                img_url = img[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.page current.>\\d+<\\/span><\\/li><li><a href=.(http:\\/\\/\\b[^>]*). title=.\\d+. class=.page.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page.>\\d+<\\/a><\\/li><li><span class=.page current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@gercekfilmler.com@start@gercekfilmler KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR gercekfilmler CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_gercekfilmler_category_films'

        return video_list_temp

    def get_gercekfilmler_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        img = re.findall('<p><img src="(.*?)" alt="" title=".*?" width="\\d+" height="\\d+" class=".*?" \\/><\\/p>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 None,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_tamseyret_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.tamseyret.com/lib/images/background/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.tamseyret.com/lib/images/background/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<a href="(.*?)" title=".*?"><span>(.*?)<\\/span><\\/a>', page)
            for text in regex2:
                title = text[1]
                url = 'www.tamseyret.com/' + text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.tamseyret.com/lib/images/background/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.tamseyret.com/lib/images/background/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR tamseyret CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_tamseyret_category'

        return video_list_temp

    def get_tamseyret_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="(Film-izle\\/.*?)" title="(.*?)" class="listpan"><li>', page)
            img_url = re.findall('<span class="afis left"><img src="(.*?)" alt=".*?" width="\\d+" height="\\d+"\\/>', page)
            for text in regex:
                url = 'www.tamseyret.com/' + text[0]
                title = text[1]
                img_url = 'http://www.tamseyret.com/' + img_url[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<a href=".*?&page=\\d+" class=.active.>\\d+<\\/a>\\W+<a href="(.*?&page=\\d+)" >\\d+<\\/a>', page)
            prev = re.findall('<a href="(.*?&page=\\d+)" >\\d+</a>\\W+<a href=".*?&page=\\d+" class=.active.>\\d+<\\/a>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@tamseyret.com@start@tamseyret KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR tamseyret CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_tamseyret_category_films'

        return video_list_temp

    def get_tamseyret_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        img = re.findall('<div class="left afis">\\W+<img src="(.*?)" alt=".*?" width="\\d+" \\/>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 None,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_sinesalon_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://sinesalon.net/templates/onarcade/images/header.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://sinesalon.net/templates/onarcade/images/header.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<a href="http:\\/\\/(.*?)" target="_self" class="header-link">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1].upper()
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://sinesalon.net/templates/onarcade/images/header.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://sinesalon.net/templates/onarcade/images/header.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR sinesalon CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinesalon_category'

        return video_list_temp

    def get_sinesalon_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="http:\\/\\/(.*?)" target="_self"><img src="(.*?)" width="\\d+" height="\\d+" title="(.*?)" alt=".*?" border="0"><\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[2].upper()
                title = re.sub('#8211;', '', title)
                title = re.sub('&#038;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<\\/tr><tr><td colspan=.\\d+. class=.pagenumbers..*?<b>\\d+<\\/b> <a href="http:\\/\\/(.*?)">\\d+<\\/a>', page)
            prev = re.findall('a href="([^<]*)">\\d+<\\/a> <b>\\d+<\\/b>.*?\\W+<table class="browsegamesbox">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@sinesalon.net@start@sinesalon KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinesalon CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinesalon_category_films'

        return video_list_temp

    def get_sinesalon_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe\\Wsrc="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        if len(vk) > 0:
            for text in vk:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' parca :' + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_ddizi_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://ddizi.com/img/ustarka.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://ddizi.com/img/ustarka.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li><a href="(http:\\/\\/ddizi.com\\/diziler/\\d+\\/.+?)">(.+?)<\\/a>', page)
            for url, title in regex2:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://ddizi.com/img/ustarka.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://ddizi.com/img/ustarka.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR ddizi CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_ddizi_category'

        return video_list_temp

    def get_ddizi_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a.+?href="(.+?)".+?img src="(.+?)".+?\\W*<.+?">.+?>(.+?)<\\/a>', page)
            for url, img, title in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('class="active">.+?\\W+<li ><a href="(.+?)"', page)
            prev = re.findall('<a href="(.+?)">\\d+</a></li\\W+<li  class="active">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@ddizi.com@start@ddizi KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR ddizi CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_ddizi_category_films'

        return video_list_temp

    def get_ddizi_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        film = re.findall('file.,encodeURIComponent..(.+?)...;', page)
        url22 = re.findall('<li ><a href="(.+?)">.+?Par.+?a</a><\\/li>', page)
        print url22
        for link in url22:
            link = 'ddizi.com' + str(link)
            print link
            page2 = mod_request(link)
            film2 = re.findall('file.,encodeURIComponent..(.+?)...;', page2)
            if len(film2) < 1:
                film2 = re.findall('src="(http://vk.com/.+?)"', page2)
                for jj in film2:
                    film.append(jj)

        if len(film) > 0:
            for text in film:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_cinestream_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://cinestream.cc/templates/SoftEye/images/logotype.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://cinestream.cc/templates/SoftEye/images/logotype.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li><a href="(\\/news\\/.+?/)">(.+?)<\\/a><\\/li>', page)
            for text in regex2:
                title = text[1]
                url = 'cinestream.cc' + text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://cinestream.cc/templates/SoftEye/images/logotype.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://cinestream.cc/templates/SoftEye/images/logotype.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR cinestream CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_cinestream_category'

        return video_list_temp

    def get_cinestream_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h2 class="newsTitle"><a href="(.+?)">(.+?)<\\/a><\\/h2>', page)
            img = re.findall('<div align="center"><span style="font-size: 18pt;"><\\/span><br\\/><img src="(.+?)"', page)
            descr = re.findall('<br\\/><img src=".+?\\/><br\\/>(.+?)\\n', page)
            if len(descr):
                aciklama = descr[chan_counter].replace('&ldquo;', '').replace('&rdquo;', '')
            else:
                aciklama = 'Konu mevcut degil'
            for text in regex:
                url = text[0]
                title = text[1]
                img_url = img[chan_counter]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 aciklama,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span>\\d+</span> <a href="(.+?)">', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*)>\\d+<\\/a> <span>\\d+<\\/span>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@cinestream.cc@start@cinestream KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR cinestream CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_cinestream_category_films'

        return video_list_temp

    def get_cinestream_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        img = re.findall('<\\/span><br\\/><img src="(.+?)"', page)
        descr = re.findall('alt="" width="256" height="340" border="0"\\/><br\\/><br\\/>(.+?)<br\\/>', page)
        if len(descr):
            aciklama = descr[0].replace('&ldquo;', '').replace('&rdquo;', '')
        else:
            aciklama = 'Konu mevcut degil'
        pl_link = re.findall('<iframe src="(http://www.putlocker.com/.+?)"', page)
        if len(pl_link):
            try:
                data = mod_request(pl_link[0])
                url_id = re.findall('<a href="/file/(.*?)"', data, re.S)
                url = 'http://www.putlocker.com/embed/%s' % url_id[0]
                enter = re.findall('<input type="hidden" value="(.*?)" name="fuck_you">', data)
                post_data = urlencode({'fuck_you': enter[0],
                 'confirm': 'Close Ad and Watch as Free User'})
                values = {'fuck_you': enter[0],
                 'confirm': 'Close+Ad+and+Watch+as+Free+User'}
                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                headers = {'User-Agent': user_agent}
                cookiejar = cookielib.LWPCookieJar()
                cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
                opener = urllib2.build_opener(cookiejar)
                urllib2.install_opener(opener)
                data = urlencode(values)
                req = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(req)
                link = response.read()
                embed = re.findall("get_file.php.stream=(.*?)'\\,", link, re.S)
                req = urllib2.Request('http://www.putlocker.com/get_file.php?stream=%s' % embed[0])
                req.add_header('User-Agent', user_agent)
                response = urllib2.urlopen(req)
                link = response.read()
                stream_url = re.findall('<media:content url="(.*?)"', link, re.S)
                medialink = stream_url[1].replace('&amp;', '&').replace("'", '')
                if len(medialink) > 0:
                    for url in medialink:
                        chan_counter = chan_counter + 1
                        chan_tulpe = (chan_counter,
                         self.kino_title + ' *putlocker*',
                         aciklama,
                         None,
                         url,
                         None,
                         None,
                         None,
                         '',
                         None,
                         None)
                        video_list_temp.append(chan_tulpe)

            except:
                pass

        vixden_url = re.findall('<a href="(http:\\/\\/www.vidxden.com/.+?)"', page)
        if len(vixden_url):
            try:
                data = mod_request(vixden_url[0])
                ids = re.findall('<input name="id" type="hidden" value="(.*?)">', data)
                fname = re.findall('<input name="fname" type="hidden" value="(.*?)">', data)
                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                headers = {'User-Agent': user_agent,
                 'Content-Type': 'application/x-www-form-urlencoded'}
                post_data = urllib.urlencode({'op': 'download1',
                 'usr_login': '',
                 'id': ids[0],
                 'fname': fname[0],
                 'method_free': 'Continue+to+Video',
                 'referer': ''})
                f = urllib2.urlopen(vixden_url[0], post_data)
                data = f.read()
                f.close()
                get_packedjava = re.findall('<script type=.text.javascript.>eval.function(.*?)\\W</script>', data, re.S)
                sJavascript = get_packedjava[0]
                sUnpacked = cJsUnpacker().unpackByString(sJavascript)
                vidxden_link = re.findall("file','(.+?)'", sUnpacked)
                for url in vidxden_link:
                    text = url
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' *vidxden*',
                     aciklama,
                     img[0],
                     text,
                     None,
                     None,
                     img[0],
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            except:
                pass

        flashx = re.findall('<a href="http:\\/\\/flashx.tv/video/(.+?)/.+?"', page)
        if len(flashx):
            try:
                for link in flashx:
                    url = 'http://play.flashx.tv/nuevo/player/cst.php?hash=' + link
                    data = mod_request(url)
                    media_link = re.compile('<file>(.+?)</file>').findall(data)
                    text = media_link[0]
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' *flashx.tv*',
                     aciklama,
                     img[0],
                     text,
                     None,
                     None,
                     img[0],
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            except:
                pass

        movshare = re.findall('src="(http://embed.movshare.net.+?)&', page)
        if len(movshare):
            try:
                for link in movshare:
                    data = mod_request(link)
                    match = re.compile('flashvars.file="(.*?)";\\W+flashvars.filekey="(.*?)"').findall(data)
                    for fil, key in match:
                        url = 'http://www.movshare.net/api/player.api.php?file=' + fil + '&key=' + key
                        'http://www.movshare.net/api/player.api.php?key=' + key + '&user=undefined&codes=undefined&pass=undefined&file' + fil

                    link = mod_request(url)
                    match = re.compile('url=(.*?)&title').findall(link)
                    text = match[0]
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' *movshare.net*',
                     aciklama,
                     img[0],
                     text,
                     None,
                     None,
                     img[0],
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            except:
                pass

        BillionUploads = re.findall('"(http://BillionUploads.com/.+?)"', page)
        if len(BillionUploads):
            try:
                for link in BillionUploads:
                    print link
                    data = mod_request(link)
                    match = re.compile("value='file=(http://BillionUploads.com/.*?)&").findall(data)
                    for url in match:
                        chan_counter = chan_counter + 1
                        chan_tulpe = (chan_counter,
                         self.kino_title + ' *BillionUploads.com*',
                         aciklama,
                         img[0],
                         url,
                         None,
                         None,
                         img[0],
                         '',
                         None,
                         None)
                        video_list_temp.append(chan_tulpe)

            except:
                pass

        ysupload = re.findall('"(http://180upload.com/.+?)"', page)
        if len(ysupload):
            try:
                for link in ysupload:
                    data = mod_request(link)
                    down_direct = re.findall('<input type="hidden" name="down_direct" value="(.+)">', data)
                    ids = re.findall('<input type="hidden" name="id" value="(.+)">', data)
                    op = re.findall('<input type="hidden" name="op" value="(.+)">', data)
                    rand = re.findall('<input type="hidden" name="rand" value="(.+)">', data)
                    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                    headers = {'User-Agent': user_agent,
                     'Content-Type': 'application/x-www-form-urlencoded'}
                    post_data = urllib.urlencode({'op': op[0],
                     'id': ids[0],
                     'rand': rand[0],
                     'method_free': '',
                     'method_premium': '',
                     'down_direct': down_direct[0]})
                    f = urllib2.urlopen(link, post_data)
                    data = f.read()
                    f.close()
                    match = re.findall('<B><a href="(.+?)" target="_parent"><span class="', data)
                    for url in match:
                        chan_counter = chan_counter + 1
                        chan_tulpe = (chan_counter,
                         self.kino_title + ' *180upload.com*',
                         aciklama,
                         img[0],
                         url,
                         None,
                         None,
                         img[0],
                         '',
                         None,
                         None)
                        video_list_temp.append(chan_tulpe)

            except:
                pass

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_zaplat_categories(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex2 = re.findall('<div class="RBCategoryItem"><a class="grey3" href="(.*?)">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = 'www.zaplat.com' + text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.zaplat.com/static/i/g/zaplat_logo200.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.zaplat.com/static/i/g/zaplat_logo200.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR zaplat CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_zaplat_category'

        return video_list_temp

    def get_zaplat_category_films(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('src="(.*?)".*?><\\/div><div class="VBLF_Data"><div class="VBLF_Title"><a class="blue" href="(.*?)" title="(.*?)">.*?<\\/a>', page)
            for text in regex:
                url = 'www.zaplat.com' + text[1]
                title = text[2]
                img_url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<div class="vlPagerItem vlPagerActive">.*?<div .*?><a href="([^>]*)"', page)
            prev = re.findall('<a href="([^<]*)">\\d+<\\/a><\\/div><div class="vlPagerItem vlPagerActive">', page)
            if len(next):
                self.next_page_url = 'nStreamModul@www.zaplat.com' + next[0] + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = 'nStreamModul@www.zaplat.com' + prev[0] + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@zaplat.com@start@zaplat KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR zaplat CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_zaplat_category_films'

        return video_list_temp

    def get_zaplat_film(self, url):
        page = mod_request(url).decode('windows-1254').encode('utf-8')
        chan_counter = 0
        video_list_temp = []
        film = re.findall('title=".file:.(http:\\/\\/.*?)..title:.(.*?)..showSuggestions.*?screenshot:.(.*?).."><\\/div>', page)
        if len(film) > 0:
            for text in film:
                url = text[0]
                title = text[1]
                img_url = text[2]
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 None,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_hbyfilm_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.hbyfilm.com/wp-content/themes/keremiyav4/logo/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.hbyfilm.com/wp-content/themes/keremiyav4/logo/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.hbyfilm.com/wp-content/themes/keremiyav4/logo/logo.png',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.hbyfilm.com/wp-content/themes/keremiyav4/logo/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hbyfilm CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hbyfilm_category'

        return video_list_temp

    def get_hbyfilm_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a href="http:\\/\\/(.*?)">\\W+.*?<img src="(.*?)" alt="(.*?)".*?<\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('#8211;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hbyfilm.com@start@hbyfilm KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hbyfilm CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hbyfilm_category_films'

        return video_list_temp

    def get_hbyfilm_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        yt = re.findall('src="http:\\/\\/www.youtube.com\\/embed\\/(\\S{11}).*?><\\/iframe>', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Fragman : ' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="konuozet">\\W+<p><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img src="(http:\\/\\/.*?)"', page)
        url22 = re.findall('<a href="http:\\/\\/(.*?)"><span>.*?</span>', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_trfullfilmizle_categories(self, url):
        print 'get_trfullfilmizle_categories'
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.trfullfilmizle.com/wp-content/themes/trfullfilmizle/logo/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.trfullfilmizle.com/wp-content/themes/trfullfilmizle/logo/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.trfullfilmizle.com/wp-content/themes/keremiyav4/logo/logo.png',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.trfullfilmizle.com/wp-content/themes/keremiyav4/logo/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR trfullfilmizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_trfullfilmizle_category'

        return video_list_temp

    def get_trfullfilmizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a href="http:\\/\\/(.*?)">\\W+.*?<img src="(.*?)" alt="(.*?)".*?\\/><\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[2]
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@trfullfilmizle.com@start@trfullfilmizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR trfullfilmizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_trfullfilmizle_category_films'

        return video_list_temp

    def get_trfullfilmizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="konuozet">\\W+<p><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img src="(http:\\/\\/.*?)"', page)
        url22 = re.findall('a href="http:\\/\\/(.*?)"><span>Part \\d+', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('<iframe width="\\d+".?height="\\d+" src="http:\\/\\/www.youtube.com\\/embed\\/(\\S{11}).*?frameborder="\\d+".*?><\\/iframe>', page)
        isim = re.findall('<title>(.*?)</title><link rel="pingback"', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                title = isim[0]
                chan_tulpe = (chan_counter,
                 title + ' Parca : ' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_trdiziizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.trdiziizle.org/wp-content/themes/dizi/resimler/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.trdiziizle.org/wp-content/themes/dizi/resimler/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="(http:\\/\\/.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for url, title in regex2:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.trdiziizle.org/wp-content/themes/dizi/resimler/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.trdiziizle.org/wp-content/themes/dizi/resimler/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR trdiziizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_trdiziizle_category'

        return video_list_temp

    def get_trdiziizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="kutu-resim">\\W*<a href="(.+?)" title="(.+?)"><img.+?src="(.+?)"', page)
            for url, title, img in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@trdiziizle.org@start@trdiziizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR trdiziizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_trdiziizle_category_films'

        return video_list_temp

    def get_trdiziizle_film(self, url):
        page = mod_request(url).decode('utf-8')
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="konuozet">\\W+<p><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmaltiimg">\\W+<img src="(http:\\/\\/.*?)"', page)
        url22 = re.findall('a href="http:\\/\\/(.*?)">.*?Par.a<\\/a>', page)
        for link in url22:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for jj in vk2:
                vk.append(jj)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' **vk.com ** ' + str(chan_counter),
                 aciklama,
                 img,
                 text,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        yt = re.findall('src="(http://www.youtube.com/embed/.+?)"', page)
        if len(yt) > 0:
            for film in yt:
                url = film.replace('embed/', 'watch?v=')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' **yt** ' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_hdivx_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://3.bp.blogspot.com/-AkUw-l_aPew/T1N0X_0ucrI/AAAAAAAACfk/Ms-zpHvifa4/s400/imagesCA707VQZ.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://3.bp.blogspot.com/-AkUw-l_aPew/T1N0X_0ucrI/AAAAAAAACfk/Ms-zpHvifa4/s400/imagesCA707VQZ.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li><a href=.http:\\/\\/(.*?=\\d+). title=..*?.>(.*?)<\\/a>\\n<\\/li>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://3.bp.blogspot.com/-AkUw-l_aPew/T1N0X_0ucrI/AAAAAAAACfk/Ms-zpHvifa4/s400/imagesCA707VQZ.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://3.bp.blogspot.com/-AkUw-l_aPew/T1N0X_0ucrI/AAAAAAAACfk/Ms-zpHvifa4/s400/imagesCA707VQZ.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hdivx CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdivx_category'

        return video_list_temp

    def get_hdivx_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h3 class=.post-title entry-title.>\\W+<a href=.(http:\\/\\/.*?).>(.*?)<\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = title.replace('&#8211;', '')
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<a class=.blog-pager-older-link. href=.(.*?). id=.Blog1_blog-pager-older-link.', page)
            prev = re.findall('<a class=.blog-pager-newer-link. href=.(.*?). id=.Blog1_blog-pager-newer-link.', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hdivx.com@start@hdivx KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hdivx CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hdivx_category_films'

        return video_list_temp

    def get_hdivx_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        match = re.findall('src="(http://stagevu.com\\/embed.*?;uid=.*?)"', page)
        print match
        match = match[0].replace('amp;', '')
        linkpg = mod_request(match)
        filmlink = re.compile('<embed type="video\\/divx" src="(.*?)"').findall(linkpg)
        print filmlink
        if len(filmlink) > 0:
            for text in filmlink:
                link = text
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' (stagevu.com) :' + str(chan_counter),
                 None,
                 None,
                 link,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_720pfilmizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.720pfilmizle.net/wp-content/uploads/2012/08/logoo1.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.720pfilmizle.net/wp-content/uploads/2012/08/logoo1.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="(http:\\/\\/.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.720pfilmizle.net/wp-content/uploads/2012/08/logoo1.jpg',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.720pfilmizle.net/wp-content/uploads/2012/08/logoo1.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR 720pfilmizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_720pfilmizle_category'

        return video_list_temp

    def get_720pfilmizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a href="(http:\\/\\/.*?)">\\W+.*?<img src="(.*?)" alt="(.*?)".*?<\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('#8211;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@720pfilmizle.net@start@720pfilmizle KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR 720pfilmizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_720pfilmizle_category_films'

        return video_list_temp

    def get_720pfilmizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        links = []
        links.append(url)
        url22 = re.findall('<a href="(.+?)"><span>.+?<\\/span><\\/a>', page)
        if len(url22) > 0:
            for link in url22:
                links.append(link)

        for flink in links:
            page = mod_request(flink)
            img = re.findall('<div class="filmaltiimg">\\W+<img src="(http:\\/\\/.*?)"', page)
            yt = re.findall('src="(http://www.youtube.com/embed/.+?)"', page)
            if len(yt) > 0:
                for film in yt:
                    url = film.replace('embed/', 'watch?v=')
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **yt(Fragman)** ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            vk = re.findall('src="(http://vk.com/.+?)"', page)
            if len(vk) > 0:
                for url in vk:
                    url = url.replace('#038;', '').replace('amp;', '')
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **vk.com** ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            movshare = re.findall("src='(http://embed.movshare.net.+?)&", page)
            if len(movshare):
                try:
                    for link in movshare:
                        data = mod_request(link)
                        match = re.compile('flashvars.file="(.*?)";\\W+flashvars.filekey="(.*?)"').findall(data)
                        for fil, key in match:
                            url = 'http://www.movshare.net/api/player.api.php?file=' + fil + '&key=' + key
                            'http://www.movshare.net/api/player.api.php?key=' + key + '&user=undefined&codes=undefined&pass=undefined&file' + fil

                        link = mod_request(url)
                        match = re.compile('url=(.*?)&title').findall(link)
                        text = match[0]
                        chan_counter = chan_counter + 1
                        chan_tulpe = (chan_counter,
                         self.kino_title + ' **movshare.net** ' + str(chan_counter),
                         None,
                         None,
                         text,
                         None,
                         None,
                         None,
                         '',
                         None,
                         None)
                        video_list_temp.append(chan_tulpe)

                except:
                    pass

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_herdizi_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'dizi_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.herdizi.com/wp-content/themes/ogdizi/images/logo.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.herdizi.com/wp-content/themes/ogdizi/images/logo.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li><a href="(http:\\/\\/.*?)">(.*?)<\\/a><\\/li>', page)
            for url, title in regex2:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.herdizi.com/wp-content/themes/ogdizi/images/logo.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.herdizi.com/wp-content/themes/ogdizi/images/logo.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_herdizi_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="thumbnail"> <a href="(http:\\/\\/.*?)">\\W+<img src="(.*?)" alt="(.*?)" \\/>', page)
            for url, img, title in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@herdizi.com@start@herdizi KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_herdizi_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        embedsrc = re.compile("<iframe.*?src='(.*?)'").findall(page)
        embed = embedsrc[0].replace('#038;', '')
        page = mod_request(embed)
        params = re.compile('flashvars.file="(.*?)"\\W+flashvars.filekey="(.*?)"').findall(page)
        for param in params:
            fullurl = 'http://www.nowvideo.eu/api/player.api.php?file=' + param[0] + '&key=' + param[1]

        link = mod_request(fullurl)
        mediaurl = re.compile('url=(.*?)&title').findall(link)
        if len(mediaurl) > 0:
            for text in mediaurl:
                link = text
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' (nowvideo.eu) :' + str(chan_counter),
                 None,
                 None,
                 link,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmcok_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.filmcok.net/wp-content/themes/basizlev4/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.filmcok.net/wp-content/themes/basizlev4/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.filmcok.net/wp-content/themes/basizlev4/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.filmcok.net/wp-content/themes/basizlev4/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_filmcok_category_films(self, url):
        try:
            page = mod_request(url)
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a  href="http:\\/\\/(.*?)" rel="bookmark"><img src="(.*?)" alt="(.*?)" class="afisfoto" \\/>', page)
            for text in regex:
                url = text[0]
                title = text[2]
                title = re.sub('&#8211;', '', title)
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a  href="(http:\\/\\/\\b[^>]*)" class=.page larger.>', page)
            prev = re.findall('<a  href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmcok.net@start@filmcok KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_filmcok_film(self, url):
        print 'get_sinemaizle_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<h3>Film Hakk.nda<\\/h3><p>(.*?)\\.', page)
        img = re.findall('<img src="(.*?)".*?class="info-resim" \\/>', page)
        url2 = re.findall('<li class="pagelink"><center><a  href="(.*?)">.. Part', page)
        for link in url2:
            page2 = mod_request(link)
            vk2 = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page2)
            for ll in vk2:
                vk.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_sporxtv_categories(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.sporxtv.com/_img/sporxtv_logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.sporxtv.com/_img/sporxtv_logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<a href="\\/(.*?)" class="ansktg">(.*?)<\\/a><br \\/>\\W', page)
            for text in regex2:
                title = text[1]
                url = 'www.sporxtv.com/' + text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.sporxtv.com/_img/sporxtv_logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.sporxtv.com/_img/sporxtv_logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR sporxtv CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sporxtv_category'

        return video_list_temp

    def get_sporxtv_category_films(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="(.+?)".+?class=.(lislnk|ynvdt).>(.+?)</a>', page)
            for url, bos, title in regex:
                url = 'www.sporxtv.com' + url
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<div class="paging_sagsol_on" onclick="parent.location=.([^>]*).;">ileri<\\/div>', page)
            prev = re.findall('<div class="paging_sagsol_on" onclick="parent.location=.([^>]*).;">geri<\\/div>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@www.sporxtv.com') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@www.sporxtv.com') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@sporxtv.com@start@sporxtv KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sporxtv CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sporxtv_category_films'

        return video_list_temp

    def get_sporxtv_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        film = re.findall('file: .(.*?).,', page)
        if len(film) > 0:
            for text in film:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'parca :' + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_diziwu_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.diziwu.com/wp-content/themes/fds/img/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.diziwu.com/wp-content/themes/fds/img/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<li class="cat-item cat-item.+?"><a href="(.+?)" title=".+?">(.+?)<\\/a>\\W+<ul class=.children.>', page)
            for url, title in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR diziwu CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_diziwu_category'

        return video_list_temp

    def get_diziwu_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="http:\\/\\/(.*?)" target="_self"><img src="(.*?)" width="\\d+" height="\\d+" title="(.*?)" alt=".*?" border="0"><\\/a>', page)
            regex = re.findall('<a href="(.+?)" title="(.+?)">.+?src="(.+?)"', page)
            for url, title, img in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<li class="active_page"><a href=".+?">\\d+<\\/a><\\/li>\\W<li><a href="(.+?)">', page)
            prev = re.findall('<li><a href="(.+?)">\\d+<\\/a><\\/li>\\W<li class="active_page">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@diziwu.com@start@diziwu KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR diziwu CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_diziwu_category_films'

        return video_list_temp

    def get_diziwu_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('"(http://vk.com/video_ext.+?)"', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' parca :' + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_kemalsunalfilm_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex2 = re.findall('<a href="http://adf.ly/2856200(\\/.*?)" target="_blank" onmouseover="x5engine.imTip.Show\\(this, \\{text: \\\'&lt;img src=&quot;(.*?)&quot; alt=&quot;&quot; /&gt;&lt;br /&gt;(.*?)\\\', width: 180\\}', page)
            for url, img, title in regex2:
                url = 'http://www.kemalsunalfilm.com' + url + '.html'
                img = 'http://www.kemalsunalfilm.com/' + img
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR kemalsunalfilm CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_kemalsunalfilm_category'

        return video_list_temp

    def get_kemalsunalfilm_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        film = re.findall('<embed src="http://www.youtube.com/v/(.+?)\\?version', page)
        descr = re.findall('<span class="ff0 fs20.*?"><br />(.+?)<\\/span>', page)
        img = re.findall('id="imObjectImage.*?" src="(.+?)"', page)
        if len(descr):
            konu = descr[0].replace('\xf6', 'o').replace('\xd6', 'O').replace('\xfc', 'u').replace('\xdd', 'I').replace('\xfd', 'i').replace('\xe7', 'c').replace('\xde', 's').replace('\xfe', 's').replace('\xc7', 'c').replace('\xf0', 'g')
        else:
            konu = 'Konu mevcut degil'
        if len(film) > 0:
            for text in film:
                url = 'http://www.youtube.com/watch?v=' + text
                img = 'http://www.kemalsunalfilm.com/' + str(img[0])
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title,
                 konu,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@www.kemalsunalfilm.com@start@Kemalsunal KATEGORILER'
        self.prev_page_text = 'Film Listesi'
        return video_list_temp

    def get_hdbelgeselizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex:
                title = text[1].upper()
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_kinomaxpro_category'

        return video_list_temp

    def get_hdbelgeselizle_category_films(self, url):
        page = mod_request(url)
        video_list_temp = []
        chan_counter = 0
        regex = re.findall('<a href="http:\\/\\/(.*?)" title="(.*?)" class="play">izle<\\/a>', page)
        img = re.findall('<img src="(.*?)" alt=".*?" width="\\d+" height="\\d+" \\/><br \\/>', page)
        for text in regex:
            chan_counter += 1
            url = text[0]
            title = text[1].replace('&#8211;', ':').upper()
            chan_tulpe = (chan_counter,
             title,
             None,
             img[chan_counter - 1],
             None,
             'nStreamModul@' + url + '@film@' + title,
             None,
             img[chan_counter - 1],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)

        next = re.findall("<\\/a><a href='(.*?)'.*?class='nextpostslink'>", page)
        prev = re.findall("<\\/span><a href='(.*?)'.*?class='previouspostslink'>", page)
        if len(next):
            self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
            self.next_page_text = 'SONRAKI'
        if len(prev):
            self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
            self.prev_page_text = 'ONCEKI'
        else:
            self.prev_page_url = 'nStreamModul@www.hdbelgeselizle.com@start@KATEGORILER'
            self.prev_page_text = 'KATEGORILER'
        if len(video_list_temp) < 1:
            print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        return video_list_temp

    def get_hdbelgeselizle_film(self, url):
        page = mod_request(url).encode('utf-8')
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<p><iframe .*?src="http:\\/\\/vk(.*?)".*?frameborder="\\d+".*?width="\\d+".*?height="\\d+"><\\/iframe><\\/p>', page)
        vkresis = re.findall('<img.*?src="(.*?)".*?alt=".*?"\\/>', page)
        isim = re.findall('<h1>(.*?)</h1>', page)
        if len(vk) > 0:
            url = 'http://vk' + vk[0].replace('&amp;', '&')
            chan_counter = chan_counter + 1
            title = isim[0].replace('&#8211;', '-').upper()
            chan_tulpe = (chan_counter,
             title + ' (turanemeksiz)',
             '',
             vkresis[0][0],
             url,
             None,
             None,
             vkresis[0][0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        yt = re.findall('<iframe.*?src="http:\\/\\/www.youtube.com\\/embed\\/(\\S{11}).*?frameborder="\\d+".*?width="\\d+".?height="\\d+"><\\/iframe>', page)
        isim = re.findall('<h1>(.*?)</h1>', page)
        if len(yt) > 0:
            for film in yt:
                url = 'http://www.youtube.com/watch?v=' + film
                chan_counter = chan_counter + 1
                title = isim[0].upper()
                chan_tulpe = (chan_counter,
                 title + ' (turanemeksiz)',
                 '',
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_trdizi_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'dizi_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<li class="item \\d+"><a href="(.*?)" title="">(.*?)<\\/a><\\/li>', page)
            for text in regex:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsevenler_category'

        return video_list_temp

    def get_trdizi_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="thumb"><img src="(.*?)" alt="(.*?)".+?<\\/div>\\W+<h3><a href="(http:\\/\\/.*?)"', page)
            for img, title, url in regex:
                title = title
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=\'rightok\'><a href=\\"(.*?)\\" class=\\"nextpostslink\\"><\\/a><\\/span><\\/div>', page)
            prev = re.findall('<span class=\'leftok\'><a href=\\"(.*?)\\" class=\\"previouspostslink\\"><\\/a><\\/span>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@www.trdizi.com@start@trdizi.com KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsevenler_category_films'

        return video_list_temp

    def get_trdizi_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        links = []
        links.append(url)
        url22 = re.findall('<a href="(.+?)" rel="nofollow">.+?<\\/a>', page)
        if len(url22) > 0:
            for link in url22:
                links.append(link)

        for flink in links:
            page = mod_request(flink)
            film = re.findall("file\\',encodeURIComponent\\(\\'(.+?)\\'", page)
            img = re.findall('<img src="(.+?)".*?class="aciklamaresim"\\/>', page)
            if len(film) > 0:
                for text in film:
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **jw** ' + str(chan_counter),
                     None,
                     img,
                     text,
                     None,
                     None,
                     img,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            yt = re.findall('<embed src="(http://www.youtube.com/v/.+?)\\?version=3', page)
            if len(yt) > 0:
                for film in yt:
                    url = film.replace('v/', 'watch?v=')
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **yt** ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            vk = re.findall('src="(http://vk.com/.+?)"', page)
            if len(vk) > 0:
                for url in vk:
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **vk** ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_xvideos_categories(self, url):
        video_list_temp = []
        chan_counter = 0
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'LAST',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com@category@XVIDEOS LAST VIDEOS',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'HITS',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com/hits@category@XVIDEOS HITS',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'Best Of Today',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com/best/day/@category@XVIDEOS Best Of Today',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'Best Of 7 Days',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com/best/week/@category@XVIDEOS Best Of 7 Days',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'Best Of 30 Days',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com/best/month/@category@XVIDEOS Best Of 30 Days',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        chan_counter = chan_counter + 1
        new = (chan_counter,
         'Best Of All Time',
         None,
         None,
         None,
         'nStreamModul@www.xvideos.com/best@category@XVIDEOS Best Of All Time',
         None,
         '',
         '',
         None,
         None)
        video_list_temp.append(new)
        return video_list_temp

    def get_xvideos_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            print page
            regex = re.findall(' <a href="(.*?)"><img src="(.*?)" id=".*?" \\/><\\/a>\\s*<\\/div>\\s*<p><a href=".*?">(.*?)<\\/a><\\/p>', page)
            for text in regex:
                url = 'http://www.xvideos.com' + text[0]
                img_url = text[1]
                title = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 None,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('nP" href="([^<"]*)">Next', page)
            prev = re.findall('<a href="([^<"]*)" class="nP">Prev', page)
            if next:
                slash = ''
                if next[0][0:1] != '/':
                    slash = '/'
                self.next_page_url = 'nStreamModul@www.xvideos.com' + slash + next[0] + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'NEXT'
            if prev:
                slash = ''
                if prev[0][0:1] != '/':
                    slash = '/'
                self.prev_page_url = 'nStreamModul@www.xvideos.com' + slash + prev[0] + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'PREV'
            else:
                self.prev_page_url = 'nStreamModul@www.xvideos.com@start@XVIDEOS ALL CATEGORIES'
                self.prev_page_text = 'Categories'
            if len(video_list_temp) < 1:
                print 'ERROR xvideos CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_xvideos_category_films'

        return video_list_temp

    def get_bicaps_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://bicaps.com/bicapslogo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://bicaps.com/bicapslogo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://bicaps.com/bicapslogo.png',
                 url,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://bicaps.com/bicapslogo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_bicaps_category_films(self, url):
        print 'get_sinemaizle_category_films'
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="moviefilm">\\W+<a  href="(.*?)">\\W+<span class=".*?"><\\/span>\\W+<img src="(.*?)" alt="(.*?)"', page)
            for text in regex:
                url = text[0]
                title = text[2]
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 url,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+</span><a  href="(http:\\/\\/\\b[^>]*)" class="page larger">', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@bicaps.com@start@BICAPS KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_bicaps_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        links = []
        links.append(url)
        url22 = re.findall('<a  href="(.*?)"><span>', page)
        if len(url22) > 0:
            for link in url22:
                links.append(link)

        for f in links:
            page1 = mod_request(f)
            yt = re.findall('src="(http://www.youtube.com/embed/.+?)"', page1)
            if len(yt):
                url = yt[0].replace('embed/', 'watch?v=')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' **youtube**' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
            vk = re.findall('<iframe src="(http:\\/\\/vk.com\\/.*?)"', page1)
            if len(vk) > 0:
                for text in vk:
                    text = text.replace('#038;', '')
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' **vk** : ' + str(chan_counter),
                     None,
                     None,
                     text,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            divxstage = re.findall('src=.(http://embed.divxstage.eu/.+?)&', page1)
            if len(divxstage) > 0:
                for dslink in divxstage:
                    link = mod_request(dslink)
                    match = re.compile('domain="http://www.divxstage.eu";\n\t\t\tflashvars.file="(.*?)";\n\t\t\tflashvars\\.filekey="(.*?)"').findall(link)
                    for fil, key in match:
                        url = 'http://www.divxstage.eu/api/player.api.php?file=' + fil + '&key=' + key

                    link1 = mod_request(url)
                    match = re.compile('url=(.*?)&title').findall(link1)
                    if len(match) > 0:
                        for text in match:
                            chan_counter = chan_counter + 1
                            chan_tulpe = (chan_counter,
                             self.kino_title + '**divxstage**' + str(chan_counter),
                             None,
                             None,
                             text,
                             None,
                             None,
                             None,
                             '',
                             None,
                             None)
                            video_list_temp.append(chan_tulpe)

                self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = self.playlist_cat_name

        return video_list_temp

    def get_hurriyet_categories(self, url):
        print 'get_hurriyet_categories'
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex1 = re.findall('<a href="http:\\/\\/(.*?)".*?title="(.*?)".*?class=".*?CategoryHeader">', page)
            for url, title in regex1:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://webtv.hurriyet.com.tr/images2011/hurriyet_logo_k.gif',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://webtv.hurriyet.com.tr/images2011/hurriyet_logo_k.gif',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR hurriyet CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hurriyet_category'

        return video_list_temp

    def get_hurriyet_category_films(self, url):
        print 'get_hurriyet_category_films'
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href=\'(.+?)\'>\\W+<.+?longdesc=\'(.+?)\'.+?\\W+alt=\\"(.+?)\\" \\/>', page)
            for url, img, title in regex:
                title = title
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<div class="WebtvBackButton FL">\\s*<a href="(.*?)">\\s*<img src="', page)
            prev = re.findall('<div class="WebtvNextButton FL">\\s*<a href="(.*?)">', page)
            if not len(next):
                next = re.findall('<div class="PagerRightLogo FL">\\s*<a href="(.*?)">', page)
            if not len(prev):
                prev = re.findall('<div class="PagerLeftLogo FL">\\s*<a href="(.*?)">', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hurriyet.com.tr@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR hurriyet CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_hurriyet_category_films'

        return video_list_temp

    def get_hurriyet_film(self, url):
        page = mod_request(url).decode('iso-8859-9').encode('utf-8')
        chan_counter = 0
        video_list_temp = []
        film = re.findall('"VideoUrl": "(.+?)"', page)
        descr = re.findall('<span id="ctl04_Label_Desc">(.+?)</span>', page)
        title = re.findall('<meta property="og:title" content="(.+?)" \\/>', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(film) > 0:
            for url in film:
                title = str(title[0]).capitalize()
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 title,
                 aciklama,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_webteizle_categories(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://webteizle.com/images/WebteizleLogo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://webteizle.com/images/WebteizleLogo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?><a\\s*href="\\/(.*?)"\\s*title="(.*?)">', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://webteizle.com/images/WebteizleLogo.png',
                 None,
                 'nStreamModul@' + self.active_site_url + '/' + url + '@category@' + title,
                 None,
                 'http://webteizle.com/images/WebteizleLogo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_webteizle_category_films(self, url):
        try:
            page = mod_request(url).decode('windows-1254').encode('utf-8')
            if url != 'webteizle.com':
                url_nav = url.split('/')
                url_navi = url_nav[0] + '/' + url_nav[1] + '/'
            else:
                url_nav = ''
                url_navi = ''
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div.*?>.*?<a.*?href="(.*?)".*?class="red-link".*?title="(.*?)".*?><img.*?src="(.*?)".*?alt=".*?"', page)
            descrip = re.findall('Konu:<\\/font>.*?<strong>(.*?)<\\w', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 descrip[chan_counter - 1],
                 img_url,
                 None,
                 'nStreamModul@' + 'webteizle.com' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            prev = re.findall('<a href="(.*?)">\\d+</a>\\s*\\s*<b>\\d+<\\/b>', page)
            next = re.findall('<b>\\d+<\\/b>\\s*\\s*<a href="(.*?)">\\d+</a>', page)
            if len(next):
                self.next_page_url = 'nStreamModul@' + url_navi + next[0] + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = 'nStreamModul@' + url_navi + prev[0] + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@webteizle.com@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_webteizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('Konu:.*?<\\/strong>(.*?)\\s*<\\w+', page)
        img = re.findall('<link.*?rel="image_src".*?href="(.*?)".*?\\/>', page)
        if len(vk) > 0:
            for text in vk:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title,
                 descr[0],
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_dizihdtv_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'dizi_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://dizihdtv.com/player/images/onezel.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://dizihdtv.com/player/images/onezel.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li class="cat-item cat-item-\\d+"><a href="(http:\\/\\/.*?)".*?title="(.*?)">.*?<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://dizihdtv.com/player/images/onezel.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://dizihdtv.com/player/images/onezel.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR dizihdtv CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_dizihdtv_category'

        return video_list_temp

    def get_dizihdtv_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="(http:\\/\\/.+?)"><img src="(.+?)" ><\\/a>\\W+<h2><a href=".+?">(.+?)<\\/a><\\/h2>', page)
            for text in regex:
                url = text[0]
                title = text[2]
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class="current">&.+?;\\d+&.+?;<\\/span><a href="(.+?)"', page)
            prev = re.findall('<a href="(http://dizihdtv.com/.+?/\\b[^<]*)".+?<\\/a><span class="current">', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@dizihdtv.com@start@dizihdtv KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR dizihdtv CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_dizihd_category_films'

        return video_list_temp

    def get_dizihdtv_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        yt = re.findall('src="(http://www.youtube.+?)"', page)
        if len(yt) > 0:
            for url in yt:
                url = url.replace('embed/', 'watch?v=').replace('?rel=0', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '* Youtube *',
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        vk = re.findall('<iframe src="(http://vk.com/.+?)"', page)
        if len(vk) > 0:
            for film in vk:
                url = film
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '* vk.com *',
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        mailru = re.findall("file': '(.+?video.+?mail.ru.+?)'", page)
        if len(mailru) > 0:
            for film in mailru:
                url = film
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '* mailru *',
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        xmlpag = re.findall("var xmlAddress.*?'(http:\\/\\/.*?)'", page)
        if len(xmlpag) > 0:
            xmlpage = mod_request(xmlpag[0])
            parts = re.findall('<videoPath value="(.*?)"\\/>\\s*<previewImage.*?\\/>\\s*<thumbImage value="(.*?)"\\/>', xmlpage)
            if len(parts) > 0:
                for text in parts:
                    url = text[0]
                    img = text[1]
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' Parca : ' + str(chan_counter),
                     None,
                     img,
                     url,
                     None,
                     None,
                     img,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmizlese_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.filmizlese.net/logo.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.filmizlese.net/logo.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<a class="filmkate" href="(.*?)" title=".*?">(.*?)</a>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.filmizlese.net/logo.jpg',
                 None,
                 'nStreamModul@' + self.active_site_url + url + '@category@' + title,
                 None,
                 'http://www.filmizlese.net/logo.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_filmizlese_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="filml"><div style="float: left;"><a href="(.*?)" title="(.*?)"><img src="(.*?)" alt=".*?"', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = 'http://www.filmizlese.net' + text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + self.active_site_url + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('class="selected">\\d+<\\/a><a href="(.*?)"', page)
            if len(next):
                self.next_page_url = 'nStreamModul@' + self.active_site_url + next[0] + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            else:
                self.prev_page_url = 'nStreamModul@' + self.active_site_url + '@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_filmizlese_film(self, url):
        print 'get_sinemaizle_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        mailru = re.findall('><embed src="\\/filmplayer.swf\\?file=(.*?)" quality', page)
        descr = re.findall('<div.*?class="konuozet">\\s*<p><\\/p>\\s*(.*?)\\s*<\\/div>', page)
        img = ''
        url22 = re.findall('m.*?<\\/li><li><a href="(.*?)">.*?K', page)
        for link in url22:
            page2 = mod_request(self.active_site_url + link)
            mailru2 = re.findall('><embed src="\\/filmplayer.swf\\?file=(.*?)" quality', page2)
            for ll in mailru2:
                mailru.append(ll)

        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(mailru) > 0:
            for text in mailru:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter),
                 aciklama,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_evrenselfilm_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni EKlenenler',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<li class="cat-item cat-item-\\d*"><a href="http:\\/\\/(.*?)" title=".*?">(.*?)<\\/a>', page)
            for text in regex:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_evrenselfilm_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            data = re.findall('<div class="solust"><a href="http:\\/\\/(.*?)" rel="bookmark" title=".*?">(.*?)<\\/a>', page)
            data1 = re.findall('<p><img src="(.*?)" alt="" title=".*?\\/><br.*?\\/>\\s*(.*?)<\\/p>', page)
            for text in data:
                url = text[0]
                img_url = data1[chan_counter][0]
                title = text[1].replace('&#8211;', '-')
                descr = data1[chan_counter][1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 descr,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<\\/a><a href="(.*?)" class="nextpostslink', page)
            prev = re.findall('class="previouspostslink">.*?<\\/a><a href=\\\'(.*?)\\\' class', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@evrenselfilm.com@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category_films'

        return video_list_temp

    def get_evrenselfilm_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        yt = re.findall('"(http://www.youtube.com/.+?)"', page)
        image = re.findall('<p><img src="(.*?)" alt="" title=".*?\\/><br.*?\\/>\\s*.*?<\\/p>', page)
        img = image[0] if image else None
        aciklama = re.findall('<p><img src=".*?" alt="" title=".*?\\/><br.*?\\/>\\s*(.*?)<\\/p>', page)
        desc = aciklama[0] if aciklama else None
        if len(yt):
            try:
                url = yt[0].replace('?rel=0', '').replace('v/', '/watch?v=').replace('embed/', 'watch?v=')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' **youtube ** ' + str(chan_counter),
                 desc,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
            except:
                pass

        vk = re.findall('"(http://vk.com/.+?)"', page)
        if len(vk) > 0:
            for url in vk:
                url = url.replace('#038;', '').replace('&sd', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '**vk.part ** ' + str(chan_counter),
                 desc,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        pl_link = re.findall('"(http://www.putlocker.com/.+?)"', page)
        if len(pl_link):
            try:
                data = mod_request(pl_link[0])
                url_id = re.findall('<a href="/file/(.*?)"', data, re.S)
                url = 'http://www.putlocker.com/embed/%s' % url_id[0]
                enter = re.findall('<input type="hidden" value="(.*?)" name="fuck_you">', data)
                values = {'fuck_you': enter[0],
                 'confirm': 'Close+Ad+and+Watch+as+Free+User'}
                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                headers = {'User-Agent': user_agent}
                cookiejar = cookielib.LWPCookieJar()
                cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
                opener = urllib2.build_opener(cookiejar)
                urllib2.install_opener(opener)
                data = urlencode(values)
                req = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(req)
                link = response.read()
                embed = re.findall("get_file.php.stream=(.*?)'\\,", link, re.S)
                req = urllib2.Request('http://www.putlocker.com/get_file.php?stream=%s' % embed[0])
                req.add_header('User-Agent', user_agent)
                response = urllib2.urlopen(req)
                link = response.read()
                stream_url = re.findall('<media:content url="(.*?)"', link, re.S)
                url = stream_url[1].replace('&amp;', '&').replace("'", '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '**putlocker ** ' + str(chan_counter),
                 desc,
                 img,
                 None,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
            except:
                pass

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_eroguru_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            new = (1,
             'Yeni Eklenenler',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/@category@YENI EKLENENLER',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (2,
             'EROTIK - LESBIYEN',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/video-erotika/lesbi-vidyeo-hd/@category@EROTIK - LESBIYEN',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (3,
             'WEBCAM',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/video-erotika/webcam/@category@WEBCAM',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (4,
             'MASAJ',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/video-erotika/eroticheskiy-massazh/@category@MASAJ',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (5,
             'SEXY VIDEO KLIP',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/video-erotika/music-video-sexy/@category@SEXY VIDEO KLIP',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (6,
             'ANAL',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/porno-video-hd/analnyi-seks/@category@ANAL',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (7,
             'GRUP SEX',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/porno-video-hd/gruppovoe-porno/@category@GRUP SEX',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (8,
             'MASTURBASYON',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/porno-video-hd/masturbatsiya/@category@MASTURBASYON',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            new = (9,
             'BLOWJOB',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/porno-video-hd/minet-hd/@category@BLOWJOB',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_eroguru_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            data = re.findall('<a href="http:\\/\\/(.*?)" ><div align="center"><.*?:(.*?)jpg', page)
            for text in data:
                url11 = text[0]
                page1 = mod_request(url11)
                preurl = re.findall('<iframe src="(.*?)" width="\\d+" height="\\d+"', page1)
                url = preurl[0].replace('&amp;', '&')
                img_url = text[1] + 'jpg'
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 'Video' + str(chan_counter),
                 None,
                 img_url,
                 url,
                 None,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            prev = re.findall('<a href="(.*?)"><span class="thide pprev">.*?<\\/span><\\/a>', page)
            next = re.findall('<a href="(.*?)"><span class="thide pnext">.*?<\\/span><\\/a>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@eroguru.com@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category_films'

        return video_list_temp

    def get_annemmutfakta_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.annemmutfakta.tv/wp-content/themes/anneMutfakta/resim/logo_.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.annemmutfakta.tv/wp-content/themes/anneMutfakta/resim/logo_.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('href="(.+?)".*?><span>(.+?)</span></a></li><li', page)
            for url, title in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.annemmutfakta.tv/wp-content/themes/anneMutfakta/resim/logo_.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.annemmutfakta.tv/wp-content/themes/anneMutfakta/resim/logo_.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR annemmutfakta CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_annemmutfakta_category'

        return video_list_temp

    def get_annemmutfakta_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('href="(.+?)" class="post-info-title" title=".+?"> <img\\W+src=".+?src=(.+?)&.+?alt="(.+?)"', page)
            for url, img, title in regex:
                title = re.sub('&#8211;', '', title)
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("href='(.+?)' class='nextpostslink'>", page).replace('#038;', '')
            prev = re.findall("href='(.+?)' class='previouspostslink'>", page).replace('#038;', '')
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@www.annemmutfakta.tv@start@annemmutfakta KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR annemmutfakta CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_annemmutfakta_category_films'

        return video_list_temp

    def get_annemmutfakta_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        regex = re.findall("value='file=(.+?)&image=(.+?)&", page)
        if len(regex) > 0:
            for url, img in regex:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title,
                 None,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_fullhdfilmizlet_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.fullhdfilmizlet.com/wp-content/themes/basizlev1/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.fullhdfilmizlet.com/wp-content/themes/basizlev1/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex2 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*? title=".*?">(.*?)<\\/a>', page)
            for text in regex2:
                title = text[1]
                url = text[0]
                print url, title
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.fullhdfilmizlet.com/wp-content/themes/basizlev1/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.fullhdfilmizlet.com/wp-content/themes/basizlev1/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR fullhdfilmizlet CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_fullhdfilmizlet_category'

        return video_list_temp

    def get_fullhdfilmizlet_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="http:\\/\\/(.*?)" .*?><img src=".*?" alt="(.*?)" class="captify" \\/><\\/a>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<span class=.current.>\\d+<\\/span><a href=.(http:\\/\\/\\b[^>]*). class=.page larger.>', page)
            prev = re.findall('<a href=.(http:\\/\\/\\b[^>]*). class=.page smaller.>\\d+<\\/a><span class=.current.>', page)
            if len(next):
                self.next_page_url = next[-1].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@fullhdfilmizlet.com@start@fullhdfilmizlet KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR fullhdfilmizlet CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_fullhdfilmizlet_category_films'

        return video_list_temp

    def get_fullhdfilmizlet_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('amp;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca :' + str(chan_counter),
                 None,
                 None,
                 text,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
                self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name

        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_megasinema_categories(self, url):
        print 'get_sinemaizle_categories'
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.megasinema.net/wp-content/themes/tahamata/images/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.megasinema.net/wp-content/themes/tahamata/images/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.megasinema.net/wp-content/themes/tahamata/images/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.megasinema.net/wp-content/themes/tahamata/images/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_megasinema_category_films(self, url):
        print 'get_sinemaizle_category_films'
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a href="http:\\/\\/(.*?)" title=".*?">\\s*<img width="\\d+" height="\\d+" src="(.*?)" class=".*?" alt="(.*?)" title=".*?" \\/><\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[2]
                img_url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<a class="next page-numbers" href="(.*?)">.*?<\\/a><\\/div>', page)
            prev = re.findall('<a class="prev page-numbers" href="(.*?)">.*?<\\/a>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@megasinema.net@start@MEGASINEMA KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_megasinema_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        descr = re.findall('<div class="filmdetayx_aciklama">\\s*<p><p>(.*?)<\\/p>', page)
        img = re.findall('<img width="\\d+" height="\\d+" src="(.*?)" class=".*?" alt=".*?" title=".*?" \\/><\\/div>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter) + 'candost',
                 descr[0],
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_filmizleturkcedublaj_categories(self, url):
        print 'get_sinemaizle_categories'
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.filmizleturkcedublaj.com/wp-content/uploads/2012/05/filmiizle.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.filmizleturkcedublaj.com/wp-content/uploads/2012/05/filmiizle.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)</a>\\s*<\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.filmizleturkcedublaj.com/wp-content/uploads/2012/05/filmiizle.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.filmizleturkcedublaj.com/wp-content/uploads/2012/05/filmiizle.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_filmizleturkcedublaj_category_films(self, url):
        print 'get_sinemaizle_category_films'
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h2><a.*?class="title".*?href="http:\\/\\/(.*?)".*?rel="bookmark">(.*?)<\\/a><\\/h2>', page)
            img = re.findall('<p><img src="(.*?)" alt=".*?" title=".*?" width="\\d+" height="\\d+" class=".*?" \\/><\\/p>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                img = img[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("class=\\'current\\'>.*?<\\/span><a href=\\'(.*?)\\'", page)
            prev = re.findall("class=\\'previouspostslink\\'>.*?<\\/a><a href=\\'(.*?)\\'", page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@filmizleturkcedublaj.com@start@filmizleturkcedublaj KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_filmizleturkcedublaj_film(self, url):
        print 'get_sinemaizle_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        yt = re.findall('<p><iframe width="\\d+" height="\\d+" src="http:\\/\\/(.*?)" frameborder="\\d+" allowfullscreen><\\/iframe><\\/p>', page)
        descr = re.findall('<p>(.*?)<\\/p>', page)
        img = re.findall('src="(.*?)" alt=".*?" title=".*?" width="\\d+" height="\\d+" class="alignleft size-medium wp-image-\\d+" \\/><\\/p>', page)
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter) + 'candost',
                 descr[0],
                 img,
                 text,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        if len(yt):
            url = yt[0].replace('embed/', '/watch?v=')
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + ' (FRAGMAN)',
             descr[0],
             img[0],
             url,
             None,
             None,
             img[0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_hdfilmport_categories(self, url):
        print 'get_sinemaizle_categories'
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.hdfilmport.net/wp-content/themes/tahamata/images/logox.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.hdfilmport.net/wp-content/themes/tahamata/images/logox.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>\\s*<\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.hdfilmport.net/wp-content/themes/tahamata/images/logox.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.hdfilmport.net/wp-content/themes/tahamata/images/logox.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_hdfilmport_category_films(self, url):
        print 'get_sinemaizle_category_films'
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<a.*?href="http:\\/\\/(.*?)".*?title="(.*?)"><img.*?src="(.*?)".*?alt=".*?".*?class=".*?".*?width="\\d+".*?height="\\d+"\\/><\\/a>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('#8211;', '', title)
                img_url = text[2]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('<a.*?class=\\"next page-numbers\\".*?href=\\"(.*?)\\">.*?</a><\\/div>', page)
            prev = re.findall('<a.*?class=\\"prev page-numbers\\".*?href=\\"(.*?)\\">.*?<\\/a>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@hdfilmport.net@start@HDFILMPORT KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR sinemaizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_sinemaizle_category_films'

        return video_list_temp

    def get_hdfilmport_film(self, url):
        print 'get_sinemaizle_film'
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe.*?src="(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe>', page)
        yt = re.findall('<iframe width="\\d+" height="\\d+" src="http:\\/\\/(.*?)" frameborder="\\d+" allowfullscreen><\\/iframe>', page)
        descr = re.findall('<div class="filmdetayx_aciklama"><p>(.*?)<\\/p>', page)
        img = re.findall('<div class="filmdetayx_resim">.*?<img.*?src="(.*?)".*?alt=".*?".*?class=".*?".*?\\/>', page)
        if len(vk) > 0:
            for text in vk:
                text = text
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter) + 'candost',
                 descr[0],
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        if len(yt):
            url = yt[0].replace('embed/', '/watch?v=')
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + ' (FRAGMAN)',
             descr[0],
             img[0],
             url,
             None,
             None,
             img[0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_macozetizle_categories(self, url):
        print 'get_sinemaizle_categories'
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.macozetizle.com/wp-content/uploads/Untitled-13.jpg',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.macozetizle.com/wp-content/uploads/Untitled-13.jpg',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('li class="cat-item cat-item-\\d+"><a href="http:\\/\\/(.*?)" title=".*?">(.*?)<\\/a>\\s*<\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.macozetizle.com/wp-content/uploads/Untitled-13.jpg',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.macozetizle.com/wp-content/uploads/Untitled-13.jpg',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR filmsehri CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_filmsehri_category'

        return video_list_temp

    def get_macozetizle_category_films(self, url):
        print 'get_sinemaizle_category_films'
        try:
            page = mod_request(url).encode('utf-8')
            print page
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<h3><a href="http:\\/\\/(.*?)" title="(.*?)">.*?<\\/a><\\/h3>', page)
            print regex
            for text in regex:
                url = text[0]
                title = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall('class="current">.*?<\\/span><a href="(.*?)"', page)
            prev = re.findall('<a href="(.*?)" >.*?<\\/a>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@macozetizle.com@start@MACOZETI KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR macozetizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_macozetizle_category_films'

        return video_list_temp

    def get_macozetizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        dail = re.findall('<iframe.*?frameborder="\\d+".*?width="\\d+".*?height="\\d+".*?src="http:\\/\\/(.*?)"><\\/iframe><\\/p>', page)
        if len(dail):
            url = dail[0]
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + 'candost',
             None,
             None,
             url,
             None,
             None,
             None,
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        yt = re.findall('<iframe width="\\d+" height="\\d+" src="http:\\/\\/(.*?)" frameborder="\\d+" allowfullscreen><\\/iframe>', page)
        if len(yt):
            url = yt[0].replace('embed/', '/watch?v=')
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + 'candost',
             None,
             None,
             url,
             None,
             None,
             None,
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_vizyonfilmi_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni Eklenenler',
             None,
             'http://www.vizyonfilmi.org/wp-content/themes/keremiya/logo/logo.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://www.vizyonfilmi.org/wp-content/themes/keremiya/logo/logo.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex1 = re.findall('<li.*?class="cat-item.*?cat-item-\\d+"><a.*?href="http:\\/\\/(.*?)".*?title=".*?">(.*?)<\\/a>\\s*<\\/li>', page)
            for text in regex1:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://www.vizyonfilmi.org/wp-content/themes/keremiya/logo/logo.png',
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 'http://www.vizyonfilmi.org/wp-content/themes/keremiya/logo/logo.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR vizyonfilmi CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_vizyonfilmi_category'

        return video_list_temp

    def get_vizyonfilmi_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<div class="movief"><a href="http:\\/\\/(.*?)">(.*?)</a><\\/div>', page)
            for text in regex:
                url = text[0]
                title = text[1]
                title = re.sub('&#038;', '', title)
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            next = re.findall("class='current'>\\d+<\\/span><a href='(.*?)'", page)
            prev = re.findall("class='extend'>.*?</span><a href='(.*?)' class='page smaller'>\\d+<\\/a><span", page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@vizyonfilmi.org@start@VIZYONFILM KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR vizyonfilmi CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_vizyonfilmi_category_films'

        return video_list_temp

    def get_vizyonfilmi_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        vk = re.findall('<iframe src="http:\\/\\/(.*?)" width="\\d+" height="\\d+" frameborder="\\d+"><\\/iframe><\\/p>', page)
        descr = re.findall('<p>(.*?)<\\/p>', page)
        img = re.findall('<p><img src="(.*?)" alt=".*?" title=".*?" width="\\d+" height="\\d+" class=".*?" \\/><\\/p>', page)
        if len(descr):
            aciklama = descr[0]
        else:
            aciklama = 'Konu mevcut degil'
        if len(vk) > 0:
            for text in vk:
                text = text.replace('#038;', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + ' Parca : ' + str(chan_counter) + 'candost',
                 aciklama,
                 img[0],
                 text,
                 None,
                 None,
                 img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_yabancidiziizle_categories(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'dizi_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'YENI EKLENENLER',
             None,
             'http://yabancidiziizle.gen.tr/resim/logo2.png',
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             'http://yabancidiziizle.gen.tr/resim/logo2.png',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<li><a href="(/dizi.*?)" title=.*?>(.*?)</a></li>', page)
            for text in regex:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://yabancidiziizle.gen.tr/resim/logo2.png',
                 None,
                 'nStreamModul@' + 'http://www.yabancidiziizle.com' + url + '@category@' + title,
                 None,
                 'http://yabancidiziizle.gen.tr/resim/logo2.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR yabancidiziizle CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_yabancidiziizle_category'

        return video_list_temp

    def get_yabancidiziizle_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            linklist = []
            regex = re.findall('<div class="diziler-kat">\\W+<a href="(.+?)" title=".+?" class="img"><img src=".+?" alt=".+?"', page)
            if len(regex) > 0:
                for text in regex:
                    page1 = mod_request(text)
                    print page1
                    filmler = re.findall('<a href="(.+?)".*?title="(.+?)" class="img"><img src="(.+?)"', page1)
                    for link in filmler:
                        url = link[0]
                        url = url if url.startswith('http') else 'http://www.yabancidiziizle.com' + url
                        title = link[1]
                        img_url = link[2]
                        chan_counter += 1
                        chan_tulpe = (chan_counter,
                         title,
                         None,
                         img_url,
                         None,
                         'nStreamModul@' + url + '@film@' + title,
                         None,
                         img_url,
                         '',
                         None,
                         None)
                        video_list_temp.append(chan_tulpe)

            filmler = re.findall('\\t<h3><a href="(.+?)".*?title="(.+?)">.+?<\\/a><\\/h3>', page)
            if len(filmler) > 0:
                for link in filmler:
                    url = link[0]
                    url = url if url.startswith('http') else 'http://www.yabancidiziizle.com' + url
                    title = link[1]
                    chan_counter += 1
                    chan_tulpe = (chan_counter,
                     title,
                     None,
                     None,
                     None,
                     'nStreamModul@' + url + '@film@' + title,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            self.prev_page_url = 'nStreamModul@yabancidiziizle.com@start@KATEGORILER'
            self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR yabancidiziizle CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_yabancidiziizle_category_films'

        return video_list_temp

    def get_yabancidiziizle_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        linkler = []
        bolumler = re.findall('<a id="part_\\d+" href=\'(.+?)\' class=\'.+?\'>(Part.+?)<\\/a>', page)
        if len(bolumler) > 0:
            for burl, btitle in bolumler:
                bolum = 'http://www.yabancidiziizle.com/' + burl
                linkler.append([bolum, btitle])

        alt = re.findall('<li.*?><a href="(\\/.+?)" title=".+?">(.+?)<\\/a></li>\\t', page)
        if len(alt) > 0:
            for altlnk, alttitle in alt:
                url1 = 'http://www.yabancidiziizle.com' + altlnk
                title = alttitle
                page = mod_request(url1).decode('utf-8')
                altalt = re.findall('<a id="part_\\d+" href=\'\\/(.+?)\'', page)
                if len(altalt) > 0:
                    for a in altalt:
                        alink = 'http://www.yabancidiziizle.com/' + a
                        linkler.append([alink, alttitle])

                else:
                    linkler.append([url1, title])

        fragman = re.findall('strSource: "(.+?)"', page)
        if len(fragman):
            try:
                for url in fragman:
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     '** fragman **',
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            except:
                pass

        for ll in linkler:
            title = ll[1]
            page1 = mod_request(ll[0])
            print ll
            vk = re.findall('<iframe src="(http://vk.com/.+?)"', page1)
            if len(vk):
                url = vk[0].replace('autoplay=1&', '')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 title + '** vk.com **' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
            yt = re.findall("(http://www.youtube.com/watch\\?v=.+?)'", page1)
            if len(yt):
                url = yt[0]
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 title + ' ** youtube **' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
            jw = re.findall('file: "(.+?)",\\W+streamer: "(.+?)"', page1)
            if len(jw):
                for ii in jw:
                    url = ii[1] + '&' + ii[0] + '&start=0'
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     title + ' ** jwplayer **' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            fbcdn = re.findall('file: "(http:\\/\\/video.+?)"', page1)
            if len(fbcdn):
                for fb in fbcdn:
                    url = fb
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     title + ' ** fbcdn.net ** part : ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            attru = re.findall('file: "(http://download.+?)"', page1)
            if len(attru):
                for aru in attru:
                    url = aru
                    url = re.sub('\\%.+?.flv', '.flv?nc=1', url)
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     title + ' ** attachmail.ru ** part : ' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_dizimag_categories(self, url):
        try:
            burl = 'http://www.dizi-mag.com/service/?ser=liste'
            page = mod_request(burl)
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            regex = re.findall('<a href="(\\/[a-zA-Z0-9-]*?)" *?class="tdiz yabanci">(.*?)<\\/a>', page)
            for url, title in regex:
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 'http://i.dizi-mag.com/i/yeni_arama.png',
                 None,
                 'nStreamModul@' + 'www.dizi-mag.com' + url + '@category@' + title,
                 None,
                 'http://i.dizi-mag.com/i/yeni_arama.png',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR dizimag CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_dizimag_category'

        return video_list_temp

    def get_dizimag_category_films(self, url):
        try:
            page = mod_request(url)
            video_list_temp = []
            chan_counter = 0
            filmlist = []
            regex = re.findall('<a href="(\\/\\b[^<]*)" id=sezongetirr', page)
            if len(regex) > 0:
                for text in regex:
                    filmlist.append('http://www.dizi-mag.com' + text)

            else:
                filmlist.append(url)
            for url in filmlist:
                page1 = mod_request(url)
                filmler = re.findall('class=fp><a href="(.+?)"><img src=(.+?) .+?size:12px>(.+?)  B.l.m<', page1)
                for url, img, title in filmler:
                    url = 'http://www.dizi-mag.com' + url
                    title = title + 'Bolum'
                    chan_counter += 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + title,
                     None,
                     img,
                     None,
                     'nStreamModul@' + url + '@film@' + title,
                     None,
                     img,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

            next = re.findall('<a.*?class=\\"next page-numbers\\".*?href=\\"(.*?)\\">.*?</a><\\/div>', page)
            prev = re.findall('<a.*?class=\\"prev page-numbers\\".*?href=\\"(.*?)\\">.*?<\\/a>', page)
            if len(next):
                self.next_page_url = next[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = prev[0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@dizi-mag.com@start@HDFILMPORT KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR dizimag CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_dizimag_category_films'

        return video_list_temp

    def get_dizimag_film(self, url):
        page = mod_request(url)
        video_list_temp = []
        chan_counter = 0
        altlinks = []
        altlinks.append(url)
        alt = re.findall('<a href="(.+?)"><img class="tlb_b tlb_isik"', page)
        if len(alt):
            for i in alt:
                i = 'http://www.dizi-mag.com' + i
                altlinks.append(i)

        def decode_base64(substring, encoded):
            std_base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
            my_base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef%slmnopqrstuvwxyz0123456789+/'
            encoded = encoded.translate(string.maketrans(my_base64chars % substring, std_base64chars))
            return base64.b64decode(encoded)

        for link in altlinks:
            page = mod_request(link)
            duyuruid = re.findall('duyuruid="(.+?)";', page)
            duyuruid = duyuruid[0]
            duyuruid = ''.join(re.findall('[ghijk]', duyuruid))
            encoded_parts = re.findall("jQuery\\....\\.d\\('(.*?)'\\)", page)
            parts = [ decode_base64(duyuruid, x) for x in encoded_parts ]
            if len(parts):
                for url in parts:
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     'Part :' + str(chan_counter),
                     None,
                     None,
                     url,
                     None,
                     None,
                     None,
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

        vk = re.findall('<iframe src="(http://vk.com/.+?)"', page)
        if len(vk):
            url = vk[0].replace('autoplay=1&', '')
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             '** vk.com **' + str(chan_counter),
             None,
             None,
             url,
             None,
             None,
             None,
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp

    def get_fragg_categories(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            ne = (chan_counter,
             'Modul Listesi',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             None,
             'film_modul.xml',
             None,
             'http://img15.imageshack.us/img15/5597/arrowleftyellow.png',
             '',
             None,
             None)
            video_list_temp.append(ne)
            new = (chan_counter,
             'Yeni EKlenenler',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '@category@YENI EKLENENLER',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<li><a href="(\\/.+?\\/)".+?>(.+?)<\\/a><\\/li>', page)
            for url, title in regex:
                url = 'http://fragg.me' + url
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + url + '@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR fragg CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_fragg_category'

        return video_list_temp

    def get_fragg_category_films(self, url):
        try:
            page = mod_request(url).encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex = re.findall('<td valign="top"><a href="(.+?)"><.+?src="(.+?)" alt=".+?" title="(.+?)"', page)
            for url, img, title in regex:
                url = 'http://fragg.me' + url
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 img,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            prev = re.findall('Previous<\\/a>.*?<a.*?href="(.*?)">', page)
            next = re.findall('<\\/a>.*?<a.*?href="(.*?)".*?<\\/a>.*?<span>', page)
            if len(next):
                self.next_page_url = 'nStreamModul@' + self.active_site_url + next[-1] + '@category_page@' + self.playlist_cat_name
                self.next_page_text = 'SONRAKI'
            if len(prev):
                self.prev_page_url = 'nStreamModul@' + self.active_site_url + prev[0] + '@category_page@' + self.playlist_cat_name
                self.prev_page_text = 'ONCEKI'
            else:
                self.prev_page_url = 'nStreamModul@' + self.active_site_url + '@start@KATEGORILER'
                self.prev_page_text = 'KATEGORILER'
            if len(video_list_temp) < 1:
                print 'ERROR fragg CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_fragg_category_films'

        return video_list_temp

    def get_fragg_film(self, url):
        page = mod_request(url)
        chan_counter = 0
        video_list_temp = []
        film = re.findall('file: "(.+?)",.+?}', page)
        if len(film) > 0:
            for url in film:
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + 'Parca :' + str(chan_counter),
                 None,
                 None,
                 url,
                 None,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@' + self.category_back_url + '@category_page@' + self.playlist_cat_name
        self.prev_page_text = self.playlist_cat_name
        return video_list_temp
