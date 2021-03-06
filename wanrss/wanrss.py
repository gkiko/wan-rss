# -*- coding: utf-8 -*-
import os

from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import requests
import datetime

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    base = 'http://www.interpressnews.ge/ge/'
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; JHR Build/98234) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.95 Mobile Safari/537.36'}
    r = requests.get(base, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    a_list = []

    items = soup.find(id='mobile_topnews').find_all(class_='topnews_content')
    for item in items:
        a = my_item(item, base)
        a_list.append(a)

    fg = FeedGenerator()
    fg.id('http://lernfunk.de/media/654321')
    fg.title('Some Testfeed')
    fg.author( {'name':'John Doe','email':'john@example.de'} )
    fg.link( href='http://goo.gl/OzZCmm', rel='alternate' )
    fg.icon('https://goo.gl/vsNdil')
    fg.subtitle('This is a cool feed!')
    fg.link( href='http://larskiesow.de/test.atom', rel='self' )
    fg.language('ge')

    for a in a_list:
        fe = fg.add_entry()
        fe.id(str(hash(a.get('title', ''))))
        fe.title(a.get('title', 'EMPTY'))
        fe.content('COMING SOON', type='text')
        fe.summary('COMING SOON')
        fe.link(href=a.get('link', ''), type='text/html')
        fe.author( {'name':'John Doe','email':'john@example.de'} )
        fe.updated(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%dT%H:%M:%SZ'))

    atomfeed = fg.atom_str(pretty=True)
    return atomfeed

def my_item(item, base):
    top_img = item.find_all(class_='topnews_img')
    top_title = item.find_all(class_='topnews_title')

    a = {}
    if top_img:
        a['img'] = top_img[0].img['src']
    if top_title:
        a['link'] = urljoin(base, top_title[0].a['href'])
        a['title'] = top_title[0].a.string
    return a

if __name__ == "__main__":
    debug_mode = 'True' == os.environ.get('DEBUG','True')
    print(debug_mode)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
