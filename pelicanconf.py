#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CDS Team'
SITENAME = 'Coding Dojo Silesia'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'Europe/Warsaw'
PAGE_ORDER_BY = 'date'

DEFAULT_LANG = 'pl'

SITELOGO = '/images/logo.png'
FAVICON = '/images/favicon.ico'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{slug}-{lang}/'
PAGE_LANG_SAVE_AS = '{slug}-{lang}/index.html'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_LANG_URL = '{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}/index.html'

COPYRIGHT_NAME = 'CDS team 2019'
HOME_HIDE_TAGS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#PLUGINS = ['jinja2content']
#JINJA2CONTENT_TEMPLATES = ['../templates']
STATIC_PATHS = ['extra', 'images']

LINKS = (
)

SOCIAL = (
    ('facebook', 'https://pl-pl.facebook.com/codingdojosilesia/'),
    ('github', 'https://github.com/coding-dojo-silesia'),
    ('envelope', 'mailto:sensei@coding-dojo-silesia.pl'),
)

DEFAULT_PAGINATION = False

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {},
    'markdown.extensions.admonition': {},
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
}
