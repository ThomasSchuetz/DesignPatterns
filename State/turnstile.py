# -*- coding: utf-8 -*-

from locked import Locked

class Turnstile(object):
    
    def __init__(self, amount_for_passing=10):
        self.state = Locked(self)
        self._amount_for_passing = amount_for_passing
        self._current_amount = 0
    
    def required_amount(self):
        return self._amount_for_passing
    
    def increase_current_amount(self, amount):
        self._current_amount += amount
    
    def current_amount(self):
        return self._current_amount
    
    def insert_coin(self, amount):
        self.state.insert_coin(amount)
    
    def push(self):
        self.state.push()
    
    def current_state(self):
        return self.state.get_current_state()

    def change_state(self, new_state):
        self.state = new_state
    
    def reset_amount(self):
        self._current_amount = 0