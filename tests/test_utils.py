import pytest
import json
import os
from tempfile import NamedTemporaryFile
from src.utils import load_transactions



def test_load_transactions_valid():
    data = [{"amount": 100}, {"amount": 200}]
    with NamedTemporaryFile(mode="w", delete=False, suffix=".json", encoding="utf-8") as temp_file:
        json.dump(data, temp_file)
        temp_file_path = temp_file.name

    try:
        result = load_transactions(temp_file_path)
        assert result == data
    finally:
        os.remove(temp_file_path)


def test_load_transactions_file_not_exists():
    result = load_transactions("non_existent_file.json")
    assert result == []


def test_load_transactions_invalid_json():
    with NamedTemporaryFile(mode="w", delete=False, suffix=".json", encoding="utf-8") as temp_file:
        temp_file.write("невалидный json")  # специально портили JSON
        temp_file_path = temp_file.name

    try:
        result = load_transactions(temp_file_path)
        assert result == []
    finally:
        os.remove(temp_file_path)


def test_load_transactions_not_a_list():
    data = {"amount": 100}
    with NamedTemporaryFile(mode="w", delete=False, suffix=".json", encoding="utf-8") as temp_file:
        json.dump(data, temp_file)
        temp_file_path = temp_file.name

    try:
        result = load_transactions(temp_file_path)
        assert result == []
    finally:
        os.remove(temp_file_path)
