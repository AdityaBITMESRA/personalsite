#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime



AUTHOR = "Aditya Pandey"
SITEURL = "https://adityabitmesra.github.io/personalsite"
SITENAME = """Aditya's Blog"""
SITETITLE = AUTHOR
SITESUBTITLE = "<pre>$ cd /Engineering && Neuroscience</pre>"
SITEDESCRIPTION = "programming, python, CS, AWS, Django"
BROWSER_COLOR = "#333333"
PATH = "content"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 5

# Theme Settings
SITELOGO = "/images/logo.svg"
FAVICON = "/images/favicon.png"
THEME = "themes/Flex"
PYGMENTS_STYLE = "default"

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives"),
    ("Categories", "/categories"),
    ("Tags", "/tags"),
)



# Social widget


# Plugins
# See: http://docs.getpelican.com/en/latest/plugins.html
PLUGINS = ["pelican.plugins.sitemap"]

# Sitemap Settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.6,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    },
}

STATIC_PATHS = ["images", "extras/CNAME", "extras/robots.txt", "extras/keybase.txt"]
EXTRA_PATH_METADATA = {
    "extras/custom.css": {"path": "static/custom.css"},
    "extras/CNAME": {"path": "CNAME"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/keybase.txt": {"path": "keybase.txt"},
}

CUSTOM_CSS = "static/custom.css"
HOME_HIDE_TAGS = True
USE_LESS = False
FEED_USE_SUMMARY = True



# Formatting for URLS
ARTICLE_URL = "{slug}"
PAGE_URL = "pages/{slug}"
CATEGORY_URL = "category/{slug}"
TAG_URL = "tag/{slug}"
AUTHOR_SAVE_AS = "author/{slug}.html"
AUTHORS_SAVE_AS = False

FLAIR = True

READERS = {"html": None}

# DEFAULT_CONFIG["MD_EXTENSIONS"] =

# MD_EXTENSIONS = []
# MARKDOWN = [CodeHiliteExtension(css_class="highlight", linenums=True), "extra"]