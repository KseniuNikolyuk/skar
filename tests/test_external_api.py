from unittest.mock import Mock, patch
from src.external_api import amount_transaction, get_convert_rub


@patch("requests.get")
def test_get_convert_rub_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 123.45}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "1"}}

    result = get_convert_rub(transaction)
    assert result == 123.45


def test_get_convert_rub_key_error():
    transaction = {"invalid": {}}
    assert get_convert_rub(transaction) is None


def test_amount_transaction_rub_only():
    transactions = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.50"}}]
    assert amount_transaction(transactions) == 100.50


# Тест для amount_transaction с одной валютной транзакцией
@patch("src.external_api.get_convert_rub")
def test_amount_transaction_with_conversion(mock_convert):
    mock_convert.return_value = 80.0

    transactions = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "1"}}]
    assert amount_transaction(transactions) == 80.0


@patch("src.external_api.get_convert_rub")
def test_amount_transaction_with_invalid(mock_convert):
    def side_effect(transaction):
        if transaction["operationAmount"]["amount"] == "1":
            return 100.0
        return None  # bad_amount должен возвращать None

    mock_convert.side_effect = side_effect

    transactions = [
        None,
        {},
        {"operationAmount": {"currency": {"code": "USD"}, "amount": "bad_amount"}},
        {"operationAmount": {"currency": {"code": "USD"}, "amount": "1"}},
    ]

    assert amount_transaction(transactions) == 100.0
