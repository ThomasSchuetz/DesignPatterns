# -*- coding: utf-8 -*-

import unittest
from turnstile import Turnstile
from locked import Locked
from unlocked import Unlocked

class TestTurnstileEvents(unittest.TestCase):

    def test_turnstile_is_locked_after_creation(self):
        turnstile = Turnstile()
        self.assertEqual(turnstile.current_state(), "locked")
    
    def test_pushing_locked_turnstile_remains_locked(self):
        turnstile = Turnstile()
        turnstile.push()
        self.assertEqual(turnstile.current_state(), "locked")
        
    def test_insert_insufficient_coins_keeps_turnstile_locked(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(5)
        self.assertEqual(turnstile.current_state(), "locked")
        
    def test_insert_just_sufficient_coins_opens_turnstile(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(10)
        self.assertEqual(turnstile.current_state(), "unlocked")
    
    def test_inserting_half_the_required_amount_twice_unlocks_turnstile(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(5)
        self.assertEqual(turnstile.current_state(), "locked")
        turnstile.insert_coin(5)
        self.assertEqual(turnstile.current_state(), "unlocked")
    
    def test_insert_more_than_sufficient_coins_opens_turnstile(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(15)
        self.assertEqual(turnstile.current_state(), "unlocked")

    def test_insert_coins_keeps_unlocked_turnstile_unlocked(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.change_state(Unlocked(turnstile))
        turnstile.insert_coin(5)
        self.assertEqual(turnstile.current_state(), "unlocked")
    
    def test_push_locks_previously_unlocked_turnstile(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.change_state(Unlocked(turnstile))
        turnstile.push()
        self.assertEqual(turnstile.current_state(), "locked")
    
    def test_amount_in_turnstile_is_reset_after_unlocking(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(15)
        self.assertEqual(turnstile.current_amount(), 0)
    
    def test_amount_increases_when_inserting_coin(self):
        turnstile = Turnstile(amount_for_passing=10)
        turnstile.insert_coin(5)
        self.assertEqual(turnstile.current_amount(), 5)

if __name__ == '__main__':
    unittest.main()
    
