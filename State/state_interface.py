# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class StateInterface(ABC):
    
    def __init__(self, turnstile):
        self._turnstile = turnstile
    
    @abstractmethod
    def get_current_state(self):
        pass
    
    @abstractmethod
    def insert_coin(self, amount):
        pass
    
    @abstractmethod
    def push(self):
        pass
