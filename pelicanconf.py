#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Brecht Machiels'
#SITENAME = 'MOS6581'
SITENAME = "<span style=\'color:black;\'>mos</span><span style=\'color:#AA1032;\'>6581</span>"
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'en'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']  # , 'liquid_tags.img'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

TYPOGRIFY = True
THEME = 'pelican-elegant'
CUSTOM_CSS = 'customization'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

#MENUITEMS = (('About', 'http://about.me/brechtmachiels'),
#)

LANDING_PAGE_ABOUT = {
    'title': 'Brecht Machiels, tech addict',
    'details': """<p>I've always been intrigued by technology. My dad's <a href="http://en.wikipedia.org/wiki/Commodore_64" title="Wikipedia: Commodore 64">Commodore 64</a> grabbed my attention at an early age and computers and technology have never stopped fascinating me. I even went to the trouble of completing a <a href="/distributed-amplification-in-cmos" title="Distributed Amplification in CMOS">Ph.D. degree in micro-electronics</a>. Additionally, I am self-taught in computer programming, with over 10 years of hands-on experience. Over the years, I have developed a number of open-source applications. My most ambitious project so far, <a href="http://github.com/brechtm/rinoh" title="RinohType">RinohType</a>, is a modern alternative to <a href="http://en.wikipedia.org/wiki/LaTeX" title="Wikipedia: LaTeX">LaTeX</a> written in <a href="http://www.python.org/" title="Python Programming Language - Official Website">Python</a>, my favorite programming language. Four years into its development, it is now quickly approaching a state where it offers most of the features you would expect from such an application.</p>

<p>I'm very inquisitive; I want to know exactly how things work. I'm also perfectionist to the point where it aggravates even myself at times. I believe these two qualities help me be a good engineer; I'm only satisfied when I fully understand a problem and have devised an elegant solution. Otherwise, I can be summarized as an <a href="http://www.41q.com/type.41q?p=23582594&n=Brecht+Machiels" title="Brecht's personality type">individualistic doer</a> a.k.a. <a href="http://www.123test.com/ISTP-personality-type/" title="ISTP Personality Type">ISTP</a> (<a href="http://www.ted.com/talks/susan_cain_the_power_of_introverts.html" title="Susan Cain, The Power of Introverts">Introversion</a>, Sensing, Thinking, Perception), which has its advantages and, of course, disadvantages.</p>""",
}

PROJECTS = [
    {'name': 'RinohType',
     'url': 'http://github.com/brechtm/rinoh',
     'description': 'Elegant document preparation system written in pure Python'},
    {'name': 'citeproc-py',
     'url': 'http://github.com/brechtm/citeproc-py',
     'description': 'A <a href="http://citationstyles.org" title="Citation Style Language">CSL</a> processor for Python'},
    {'name': 'python-substratestack',
     'url': 'https://substratestack.appspot.com',
     'description': 'Python module to simplify substrate stackups and export '
                    'them for use in Momentum and Sonnet'},
    {'name': 'python-nport',
     'url': 'https://github.com/bmachiel/python-nport',
     'description': 'Python package for handling n-port data (Touchstone, CITI)'},
]

# Blogroll
LINKS = None
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
GITHUB_URL = 'http://github.com/brechtm/'
SOCIAL = (('twitter', 'http://twitter.com/brechtmachiels'),
          ('github', 'http://github.com/brechtm'),
)

EMAIL = 'brecht@mos6581.org'
TWITTER_USERNAME = 'brechtmachiels'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'theme/images',
    'files',
    'extra/CNAME',
    'extra/customization.css',
]

EXTRA_PATH_METADATA = {
    os.path.join('extra', 'CNAME'): {'path': 'CNAME'},
    os.path.join('extra', 'customization.css'): {'path': 'theme/css/customization.css'},
}

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

