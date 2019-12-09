# -*- coding: utf-8 -*-
from turnstile import Turnstile
from unlocked import Unlocked

def test_turnstile_is_locked_after_creation():
    turnstile = Turnstile()
    assert turnstile.current_state() == "locked"

def test_pushing_locked_turnstile_remains_locked():
    turnstile = Turnstile()
    turnstile.push()
    assert turnstile.current_state() == "locked"
    
def test_insert_insufficient_coins_keeps_turnstile_locked():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(5)
    assert turnstile.current_state() == "locked"
    
def test_insert_just_sufficient_coins_opens_turnstile():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(10)
    assert turnstile.current_state() == "unlocked"

def test_inserting_half_the_required_amount_twice_unlocks_turnstile():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(5)
    assert turnstile.current_state() == "locked"
    turnstile.insert_coin(5)
    assert turnstile.current_state() == "unlocked"

def test_insert_more_than_sufficient_coins_opens_turnstile():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(15)
    assert turnstile.current_state() == "unlocked"

def test_insert_coins_keeps_unlocked_turnstile_unlocked():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.change_state(Unlocked(turnstile))
    turnstile.insert_coin(5)
    assert turnstile.current_state() == "unlocked"

def test_push_locks_previously_unlocked_turnstile():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.change_state(Unlocked(turnstile))
    turnstile.push()
    assert turnstile.current_state() == "locked"

def test_amount_in_turnstile_is_reset_after_unlocking():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(15)
    assert turnstile.current_amount() == 0

def test_amount_increases_when_inserting_coin():
    turnstile = Turnstile(amount_for_passing=10)
    turnstile.insert_coin(5)
    assert turnstile.current_amount() == 5

