# coding:utf-8
"""
old-classとnew-classのメソッド解決順序に関する実験
"""

class Base:
    x = "base"

class D1(Base):
    pass

class D2(Base):
    x = "D2"

class D3(D1, D2):
    pass

print D3.x #-> base



class Base(object):
    x = "base"

class D1(Base):
    pass

class D2(Base):
    x = "D2"

class D3(D1, D2):
    pass

print D3.x #-> D2




class Base(object):
    x = "base"

class D1(Base):
    pass

class D2(object):
    x = "D2"

class D3(D1, D2):
    pass

print D3.x #-> base
