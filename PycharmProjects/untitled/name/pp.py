#!/usr/bin/python
#-*- coding:utf-8 -*-
import yaml
with open(file='1.yaml',mode='r',encoding='utf-8') as fb:
    data=yaml.load(fb,Loader=yaml.FullLoader)
    print(data)
