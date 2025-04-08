from unittest.mock import mock_open, patch
from src.utils import load_transactions


# Тест: файл не существует
@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_exists(mock_exists):
    result = load_transactions("nonexistent.json")
    assert result == []


# Тест: невалидный JSON
@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_load_transactions_invalid_json(mock_file, mock_exists):
    result = load_transactions("invalid.json")
    assert result == []


# Тест: JSON не список
@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_load_transactions_not_a_list(mock_file, mock_exists):
    result = load_transactions("notalist.json")
    assert result == []


# Тест: корректный список транзакций
@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}, {"id": 2}]')
def test_load_transactions_success(mock_file, mock_exists):
    result = load_transactions("transactions.json")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2
