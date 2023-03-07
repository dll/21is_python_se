#######################################################
# 
# WildGoose.py
# Python implementation of the Class WildGoose
# Generated by Enterprise Architect
# Created on:      03-03-2023 8:55:17
# Original author: liu dongliang
# 
#######################################################
from Fly import Fly
from Bird import Bird


class WildGoose(Bird, Fly):
    def fly(self):
        print("Flying in herringbone formation!\n");

    def propagate(self):
        print("WildGoose egg 150g\n");

    def WildGoose(self):
        print("my is a WildGoose\n");