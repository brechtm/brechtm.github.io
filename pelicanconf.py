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
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'share_post']  # , 'liquid_tags.img'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

TYPOGRIFY = True
THEME = 'pelican-elegant'

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
    'title': 'Brecht Machiels <small>Tech Addict</small>',
    'details': """<p>I've always been intrigued by technology. My dad's <a href="http://en.wikipedia.org/wiki/Commodore_64" title="Wikipedia: Commodore 64">Commodore 64</a> grabbed my attention at an early age and computers and technology have never stopped fascinating me. I even went to the trouble of completing a <a href="/distributed-amplification-in-cmos" title="Distributed Amplification in CMOS">Ph.D. degree in micro-electronics</a>. Additionally, I am self-taught in computer programming, with over 10 years of hands-on experience. Over the years, I have developed a number of open-source applications. My most ambitious project so far, <a href="http://github.com/brechtm/rinohtype" title="RinohType on GitHub">RinohType</a>, is a modern alternative to <a href="http://en.wikipedia.org/wiki/LaTeX" title="Wikipedia: LaTeX">LaTeX</a> written in <a href="http://www.python.org/" title="Python Programming Language - Official Website">Python</a>, my favorite programming language. Four years into its development, it is now quickly approaching a state where it offers most of the features you would expect from such an application.</p>

<p>I'm very inquisitive; I want to know exactly how things work. I'm also perfectionist to the point where it aggravates even myself at times. I believe these two qualities help me be a good engineer; I'm only satisfied when I fully understand a problem and have devised an elegant solution. Otherwise, I can be summarized as an <a href="http://www.41q.com/type.41q?p=23582594&n=Brecht+Machiels" title="Brecht's personality type">individualistic doer</a> a.k.a. <a href="http://www.123test.com/ISTP-personality-type/" title="ISTP Personality Type">ISTP</a> (<a href="http://www.ted.com/talks/susan_cain_the_power_of_introverts.html" title="Susan Cain, The Power of Introverts">Introversion</a>, Sensing, Thinking, Perception), which has its advantages and, of course, disadvantages.</p>

<p>After obtaining my Ph.D. and working as a C++ developer for 18 months, I'm now starting out as a freelance engineering consultant. In particular, I'm looking to apply my analytical and software development skills to solve problems in engineering. See my <a href="http://be.linkedin.com/pub/brecht-machiels/4/444/581/" title="Brecht Machiels on LinkedIn">LinkedIn profile</a> for details.</p>

<!-- p><script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
<script type="IN/MemberProfile" data-id="http://www.linkedin.com/pub/brecht-machiels/4/444/581" data-format="hover" data-text="Brecht Machiels" data-related="false"></script></p -->

<p><a href="https://twitter.com/brechtmachiels" class="twitter-follow-button" data-show-count="true">Follow @brechtmachiels</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
<iframe src="http://ghbtns.com/github-btn.html?user=brechtm&type=follow&count=true" allowtransparency="true" frameborder="0" scrolling="0" width="165" height="20"></iframe></p>

<!-- p><a href='https://www.ohloh.net/accounts/61830?ref=Tiny' target='_blank'>
<img alt='Ohloh profile for Brecht Machiels' border='0' height='15' src='https://www.ohloh.net/accounts/61830/widgets/account_tiny.gif' width='80' /></a></p -->""",
}

PROJECTS = [
    {'name': 'RinohType',
     'url': 'http://github.com/brechtm/rinohtype',
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
          ('email', 'mailto:brecht@mos6581.org'),
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
    'extra/custom.css',
    'extra/google9ddc49a50caff71e.html'
]

EXTRA_PATH_METADATA = {
    os.path.join('extra', 'CNAME'): {'path': 'CNAME'},
    os.path.join('extra', 'custom.css'): {'path': 'theme/css/custom.css'},
    os.path.join('extra', 'google9ddc49a50caff71e.html'): {'path': 'google9ddc49a50caff71e.html'},
}

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

