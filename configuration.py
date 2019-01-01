#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu
# maintainer: Fad
from __future__ import (unicode_literals, absolute_import, division,
                        print_function)
import os
from Common.cstatic import CConstants

ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))


class Config(CConstants):
    """ docstring for Config """
    DATEFORMAT = u'%d-%m-%Y'

    def __init__(self):
        CConstants.__init__(self)

    # ------------------------- Organisation --------------------------#
    LSE = False
    DEBUG = False
    PEEWEE_V = 224
    ORG_LOGO = None

    AUTOR = u"IBS Mali"

    # -------- Application -----------#
    NAME_MAIN = "main.py"
    APP_NAME = "R_coop_desktop"
    APP_VERSION = 1
    APP_DATE = u"10/2018"
    img_media = os.path.join(os.path.join(ROOT_DIR, "static"), "img/")
    APP_LOGO = os.path.join(img_media, "logo.png")
    IBS_LOGO = os.path.join(img_media, "ibs.jpg")
    APP_LOGO_ICO = os.path.join(img_media, "logo.ico")

    BASE_URL = "http://192.168.6.6:9009/"
    BASE_URL = "http://192.168.1.15:9009/"
    BASE_URL = "http://172.20.10.2:9009/"
    # BASE_URL = "https://msah.ml/"
    SERV = True
    EXCLUDE_MENU_ADMIN = ["del_all", "theme"]
