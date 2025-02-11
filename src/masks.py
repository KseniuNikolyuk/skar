def get_mask_card_number(card_number: str) -> str:
    """функция для скрытия номера"""
    # card_number = str(card_number)
    block1 = card_number[:4]
    block2 = card_number[4:6]
    block3 = "**"
    block4 = "****"
    block5 = card_number[-4:]
    mask_card = f"{block1} {block2}{block3} {block4} {block5}"
    return mask_card


def get_mask_account(account_number: str) -> str:
    """функция для скрытия номера"""
    block6 = account_number[-4:]
    mask_number = f"**{block6}"
    return mask_number
