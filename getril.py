#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import readitlater
import test_configs as configs

client = readitlater.API(configs.RIL_APIKEY,
                         configs.RIL_USERNAME,
                         #"wyatt",
                         configs.RIL_PASSWORD)
try:
    client.auth()
except readitlater.AuthError, e:
    print "认证失败：%s" % e
    sys.exit(1)


items = client.get()

lists = items['list']

for values in lists.values():
    for k, v in values.items():
        print "%s == > %s" % (k, v)


