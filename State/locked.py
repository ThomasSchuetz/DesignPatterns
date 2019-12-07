# -*- coding: utf-8 -*-

from state_interface import StateInterface
from unlocked import Unlocked

class Locked(StateInterface):
    
    def get_current_state(self):
        return "locked"
    
    def insert_coin(self, amount):
        # insert abbreviation to improve readability
        turnstile = self._turnstile
        
        turnstile.increase_current_amount(amount)
        
        if turnstile.current_amount() >= turnstile.required_amount():
            turnstile.change_state(new_state=Unlocked(turnstile))
    
    def push(self):
        pass