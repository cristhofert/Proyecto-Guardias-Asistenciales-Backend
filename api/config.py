#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
mariadb = {
         'user': 'app_user',
         'passwd': 'app0987user',
         'host': 'localhost',	
         'db': 'sggdb',
         'port': '3306'}

mariadbConfig =  "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(mariadb['user'], mariadb['passwd'], mariadb['host'], mariadb['port'], mariadb['db'])