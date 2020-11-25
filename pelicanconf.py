#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import re
import shutil
import logging
import matplotlib
import qrcode

# to embed videos https://pyembed.github.io/usage/rst/
# from pyembed.rst import PyEmbedRst
# PyEmbedRst().register()



AUTHOR = 'nick'
SITENAME = 'fob.monster'
SITESUBTITLE = 'some things for FOBs'
SITEURL = 'https://fob.monster'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('Pelican', 'http://getpelican.com/'),
            ('Python.org', 'http://python.org/'),
            )
SOCIAL = (
            ('github', 'https://github.com/babyvampire'),
            )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# M_SITE_LOGO_TEXT = 'fobsite'
M_SITE_LOGO = 'images/flyingFrankiesaurus.jpg'

## text on the bottom of the page
M_LINKS_FOOTER1 = []
M_LINKS_FOOTER2 = []
M_LINKS_FOOTER3 = []
M_LINKS_FOOTER4 = []
M_FINE_PRINT = SITENAME + """. Put together with `Pelican <https://docs.getpelican.com/en/stable/>`_ and `m.css <https://mcss.mosra.cz>`_.
Here's my `GitHub <https://github.com/babyvampire>`_."""

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'media',
    'text',
    ]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    }

PLUGIN_PATHS = ['m.css/plugins',
                'pelican-plugins']
PLUGINS = ['m.abbr',
           'm.alias',
           'm.code',
           'm.components',
           'm.dox',
           'm.dot',
           'm.filesize',
           'm.gl',
           'm.gh',
           'm.htmlsanity',
           'm.images',
           'm.link',
           'm.math',
           'm.metadata',
           'm.plots',
           'm.sphinx',
           'm.qr',
           'm.vk',
           'better_figures_and_images'
           ]

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_THEME_COLOR = '#22272e'
M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Code+Pro:400,400i,600%7CSource+Sans+Pro:400,400i,600,600i&subset=latin-ext',
               'static/m-dark.css',
               # enable so we see the problems right away (not present for
               # publish)
               'static/m-debug.css'
              ]
#M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               #'static/m-light.css']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

if not shutil.which('latex'):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

# Used by the m.code plugin docs

_css_colors_src = re.compile(r"""<span class="mh">#(?P<hex>[0-9a-f]{6})</span>""")
_css_colors_dst = r"""<span class="mh">#\g<hex><span class="m-code-color" style="background-color: #\g<hex>;"></span></span>"""

M_CODE_FILTERS_PRE = {
    ('C++', 'codename'): lambda code: code.replace('DirtyMess', 'P300::V1'),
    ('C++', 'fix_typography'): lambda code: code.replace(' :', ':'),
}
M_CODE_FILTERS_POST = {
    'CSS': lambda code: _css_colors_src.sub(_css_colors_dst, code)
}

DIRECT_TEMPLATES = ['archives']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'examples/'
ARCHIVES_SAVE_AS = 'examples/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHORS_SAVE_AS = None # Not used
CATEGORIES_SAVE_AS = None # Not used
TAGS_SAVE_AS = None # Not used

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

LOAD_CONTENT_CACHE = False

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True