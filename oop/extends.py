# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print("animal is runing")


class Dog(Animal):
    def dog_speak(self):
        print("wolf wolf ...")

class Cat(Animal):
    def cat_speak(self):
        print("maw maw ...")

d = Dog()
d.run()
d.dog_speak()

m = Cat()
m.run()
m.cat_speak()