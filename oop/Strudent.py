# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printInfo(self):
        print("name:"+self.name+";score:"+str(self.score))


demo = Student("jj",23)
demo.age = 12
demo.printInfo()
print(demo.age)
print(demo.name)
print(demo.score)
print(demo)
