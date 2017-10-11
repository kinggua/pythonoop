# !/usr/bin/env python
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.age = age

    def printInfo(self):
        print("name:"+self.__name+",age:"+str(self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

s = Student("junjun",12)
#print(s.__age)
print(s.age)