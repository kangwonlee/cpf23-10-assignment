import pathlib
import sys

import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import ex10


@pytest.fixture
def coin_holder_empty():
    return ex10.Class10()


def test_balance_empty(coin_holder_empty):
    assert 0 == coin_holder_empty.balance()


def test_push_one_balance(coin_holder_empty):
    coin_holder_empty.push(10)
    assert 10 == coin_holder_empty.balance()


def test_push_two_balance(coin_holder_empty):
    coin_holder_empty.push(10)
    coin_holder_empty.push(500)
    assert 510 == coin_holder_empty.balance()


def test_push_two_pop_one_balance(coin_holder_empty):
    coin_holder_empty.push(10)
    coin_holder_empty.push(500)
    r = coin_holder_empty.pop()
    assert 500 == r
    assert 10 == coin_holder_empty.balance()


def test_push_three_pop_one_balance(coin_holder_empty):
    coin_holder_empty.push(10)
    coin_holder_empty.push(500)
    r = coin_holder_empty.pop()
    assert 500 == r
    assert 10 == coin_holder_empty.balance()


if "__main__" == __name__:
    pytest.main([__file__])
