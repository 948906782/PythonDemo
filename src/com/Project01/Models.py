# -*- coding:utf-8 -*-
import time,uuid
from src.com.Project01.orms import Model,StringField,BooleanField,FloatField,TextField,IntegerField

def next_id():
    return int(time.time() * 1000)

class User(Model):
    __table__='te'
    id=IntegerField(primary_key=True,default=next_id())
    name=StringField(ddl='varchar(128)')

