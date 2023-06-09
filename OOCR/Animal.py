#######################################################
# 
# Animal.py
# Python implementation of the Class Animal
# Generated by Enterprise Architect
# Created on:      03-03-2023 8:55:16
# Original author: liu dongliang
# 
#######################################################
from abc import ABC, abstractmethod

from Water import Water
from Oxygen import Oxygen


class Animal(ABC):

    @abstractmethod
    def metabolize(self, o, w):
        print("Animal depends on Oxygen Water: parameter of metabolize");

    @abstractmethod
    def propagate(self):
        print("Animal depends on Oxygen Water: local variable of propagate");
        o = Oxygen();
        w = Water();
