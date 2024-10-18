import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2, print_pattern_3

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

def test1(capsys):
    expected_output = (
        "1 \n"
        "2 2 \n"
        "3 3 3 \n"
        "4 4 4 4 \n"
        "5 5 5 5 5 \n"
    )
    print_pattern_1(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test2(capsys):
    expected_output = (
        "    1 \n"
        "   2 2 \n"
        "  3 3 3 \n"
        " 4 4 4 4 \n"
        "5 5 5 5 5 \n"
    )
    print_pattern_2(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test3(capsys):
    expected_output = (
        "1 \n"
        "0 1 \n"
        "1 0 1 \n"
        "0 1 0 1 \n"
        "1 0 1 0 1 \n"
    )
    print_pattern_3(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output
