__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import random

dict = {}
print(dict)

dict["en"]=1
dict["to"]=2
dict["tre"]=3

dict2 = {"fire":4,"fem":5}

dict.update(dict2)
print(dict)


for key,value in dict.items():
    print(key,value)
    dict[key]=value+1

print(dict)


dict["to tall"]=random.randint(1,5)
print(dict)

dict["to tall"]=[dict["to tall"],random.randint(1,5)]
print(dict)


mitt_sett=set()
print(mitt_sett)

for i in range(10):
    mitt_sett.add(random.randint(1,10))
print(mitt_sett)