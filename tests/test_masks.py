import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    input_card = "7189237812348121"
    expected = "7189 23** **** 8121"
    assert get_mask_card_number(input_card) == expected

def test_get_mask_account():
    input_account = "12874624812964718260471"
    expected = "**0471"
    assert get_mask_account(input_account) == expected

def test_short_card_number():
    input_card = "12345678"
    expected = "1234 56** **** 5678"
    assert get_mask_card_number(input_card) == expected
