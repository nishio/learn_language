# -*- coding: utf-8 -*-
"""
PythonでPerl風の「値を持つHashと関数を持つパッケージ」をやったもの
"""
def push(values):
    values["count"] += 1
    print "%(name)s: %(count)s匹" % values

def reset(values):
    values["count"] = 0
    print "%(name)s: リセット" % values

c1 = {"name": "スズメ", "count": 0}
c2 = {"name": "カラス", "count": 0}

push(c1) #-> スズメ: 1匹
push(c1) #-> スズメ: 2匹
push(c2) #-> カラス: 1匹
push(c1) #-> スズメ: 3匹

