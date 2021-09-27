#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
mariadb = {
         'user': 'DB00004808',#   'user': 'app_user',
         'passwd': 'OL^MCjrdqGiDKk|7dnZK1eku',#       'passwd': 'app0987user',
         'host': 'guardias-asistenciales.mdb0002298.db.skysql.net',#localhost
         'db': 'sggdb',
         'port': '5001'}#3306

mariadbConfig =  "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(mariadb['user'], mariadb['passwd'], mariadb['host'], mariadb['port'], mariadb['db'])