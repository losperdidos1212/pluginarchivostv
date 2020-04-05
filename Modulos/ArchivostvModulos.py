# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/archivostv/ArchivostvModulos.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2
import urllib as ul
import os, re
from datetime import datetime
from time import time

def debug(obj, text=''):
	print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
	print '%s' % text +  ' %s\n' % obj

def mod_request(url):
	url = 'http://' + url
	html = ''
	try:
		debug(url, 'MODUL REQUEST URL')
		req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 Archivostv 0.1', 'Connection': 'Close'})
		html = urllib2.urlopen(req).read() 
		#print html
	except Exception, ex:
		print ex
		print 'REQUEST Exception'
	return html
	    
class html_parser_moduls:
	
	def __init__(self):
		self.video_list = []
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

	def reset_buttons(self):
		self.kino_title = ''
		self.next_page_url = None
		self.next_page_text = ''
		self.prev_page_url = None
		self.prev_page_text = ''
		self.search_text = ''
		self.search_on = None

	def get_list(self, url):
		debug(url, 'MODUL URL: ')
		self.reset_buttons() 