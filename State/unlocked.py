# -*- coding: utf-8 -*-

from state_interface import StateInterface
import locked

class Unlocked(StateInterface):
    
    def get_current_state(self):
        return "unlocked"
    
    def insert_coin(self, amount):
        pass
        
    def push(self):
        self._turnstile.change_state(new_state=locked.Locked(self._turnstile))
