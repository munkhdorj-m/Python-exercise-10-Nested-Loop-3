import pytest
import inspect
from assignment import print_pattern_1, print_pattern_2

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source
    
@pytest.mark.parametrize("n, expected1, expected2, expected3", [
    (3, (
        "1 2 3 \n"
        "4 5 6 \n"
        "7 8 9 \n"
    ),(
        "1  2  3 \n"
        "4  5  6 \n"
        "7  8  9 \n"
    )
    (
        "1 2 3\n"
        "4 5 6\n"
        "7 8 9\n"
    )),
    (5, (
        "1 2 3 4 5 \n"
        "6 7 8 9 10 \n"
        "11 12 13 14 15 \n"
        "16 17 18 19 20 \n"
        "21 22 23 24 25 \n"
    ),(
        "1  2  3  4  5 \n"
        "6  7  8  9  10 \n"
        "11 12 13 14 15 \n"
        "16 17 18 19 20 \n"
        "21 22 23 24 25 \n"
    ),(
        "1 2 3 4 5\n"
        "6 7 8 9 10\n"
        "11 12 13 14 15\n"
        "16 17 18 19 20\n"
        "21 22 23 24 25\n"
    )),
])
def test1(capsys,n, expected1,expected2,expected3):
    print_pattern_1(n)
    captured = capsys.readouterr()
    assert captured.out == expected1 or captured.out == expected2 or captured.out == expected3 

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

