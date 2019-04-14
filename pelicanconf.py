#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Team89'
SITENAME = 'SeaminglyAccurate'
SITEURL = 'http://aimondo.github.io'
FAVICON = "/images/favicon.png"

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = './plugins'
PLUGINS = ['ipynb.markup']

THEME = '../pelican-themes/attila'

AUTHORS_BIO = {
  "Team89": {
    "name": "Team89",
    "cover": "https://upload.wikimedia.org/wikipedia/en/1/1e/Baseball_%28crop%29.jpg",
    "image": "https://upload.wikimedia.org/wikipedia/en/1/1e/Baseball_%28crop%29.jpg",
    "website": "http://aimondo.github.io",
    "location": "OMSCS",
    "bio": "We are a group of CSE6242 students who are trying to Beat the Streak"
  }
}

HOME_COVER = '/assets/images/baseball-math.png'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

IGNORE_FILES = ['.ipynb_checkpoints']
