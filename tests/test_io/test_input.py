import pytest
from app.io.input import read_text_from_file_builtin, read_text_from_file_pandas


def test_read_file_builtin(tmp_path):
    """Тест зчитування з файлу"""
    content = read_text_from_file_builtin("../../data/test_file_builtin.txt")
    assert content == "Test for builtin\n"

def test_read_empty_file_builtin():
    """Тест зчитування з порожнього файлу"""
    content = read_text_from_file_builtin("../../data/empty_file.txt")
    assert content == ""

def test_read_file_pandas():
    """Тест зчитування з файлу за допомогою pandas"""
    content = read_text_from_file_pandas("../../data/test_file_pandas.csv")
    assert content == "Test for pandas"

def test_read_empty_file_pandas():
    """Тест зчитування з порожнього файлу за допомогою pandas"""
    content = read_text_from_file_pandas("../../data/empty_file_pandas.cvs")
    assert content == ""
