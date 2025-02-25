import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def masks_card() -> str:
    return "7000792289606361"


def test_masks_card(masks_card: str) -> None:
    assert get_mask_card_number(masks_card) == "7000 79** **** 6361"


def test_masks_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
